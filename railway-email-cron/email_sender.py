#!/usr/bin/env python3
"""
Neuro Email Outreach System
- Sends one personalized cold email per day to neuro company leads
- Tracks emails sent, responses, and follow-ups
- Auto-follows up on day 3 and day 7
- Logs all activity
"""

import json
import smtplib
import os
import logging
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

# Configuration
GMAIL_USER = os.getenv("GMAIL_USER", "jordanjayhays@gmail.com")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD", "")
SENDER_NAME = os.getenv("SENDER_NAME", "Jordan")
LOG_FILE = "/tmp/neuro-email-cron/campaign_log.json"
LEADS_FILE = "/tmp/neuro-email-cron/leads.json"
SENT_FILE = "/tmp/neuro-email-cron/sent_log.json"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_json(filepath):
    """Load JSON file, return empty dict/list on failure."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.warning(f"Could not load {filepath}: {e}")
        return []


def save_json(filepath, data):
    """Save data to JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, default=str)


def load_leads():
    """Load leads from leads.json."""
    return load_json(LEADS_FILE)


def load_sent_log():
    """Load sent log or create empty structure."""
    data = load_json(SENT_FILE)
    if isinstance(data, list):
        return {"emails": data, "stats": {"total_sent": len(data), "responses": 0, "revenue": 0}}
    return data


def save_sent_log(data):
    """Save sent log to file."""
    save_json(SENT_FILE, data)


def get_next_lead(leads, sent_log):
    """Get the next lead that hasn't been emailed yet."""
    sent_emails = {entry.get("email") for entry in sent_log.get("emails", [])}
    for lead in leads:
        if lead["email"] not in sent_emails:
            return lead
    return None


def get_followup_leads(leads, sent_log, days_ago):
    """Get leads that need follow-up (emailed exactly `days_ago` days ago)."""
    target_date = datetime.now().date() - timedelta(days=days_ago)
    followup_leads = []
    
    for entry in sent_log.get("emails", []):
        if entry.get("followup_sent"):
            continue  # Already sent follow-up for this day
        
        sent_date = entry.get("sent_date", "")
        if isinstance(sent_date, str) and sent_date:
            try:
                sent_date_obj = datetime.strptime(sent_date, "%Y-%m-%d").date()
                if sent_date_obj == target_date:
                    # Find the lead info
                    for lead in leads:
                        if lead["email"] == entry["email"]:
                            followup_leads.append({
                                **lead,
                                "original_sent_date": sent_date,
                                "followup_number": days_ago
                            })
                            break
            except ValueError:
                continue
    
    return followup_leads


def build_email_content(lead, email_type="initial"):
    """Build personalized email content."""
    
    if email_type == "initial":
        subject = f"Partnership Opportunity: {lead['company']} + Our Neuro Platform"
        body = f"""Hi {lead['contact'].split()[0]},

I noticed {lead['company']}'s work in {lead['personalization']} — impressive stuff.

We're building a platform that helps neuro companies streamline their clinical trial data and accelerate FDA submissions. Given {lead['company']}'s focus on {lead['personalization']}, I think there could be a great fit.

Would love to share how we're helping similar companies cut their submission timeline by 40%.

Got 15 minutes this week for a quick chat?

Best,
Jordan
"""
    elif email_type == "followup_3":
        subject = f"Re: Partnership Opportunity: {lead['company']} + Our Neuro Platform"
        body = f"""Hi {lead['contact'].split()[0]},

Just following up on my note from earlier this week — wanted to make sure it didn't get buried.

If {lead['personalization']} is keeping your team busy, I completely understand. But if you're ever looking for ways to streamline neuro data management, we're here to help.

Let me know if you'd like to chat briefly — happy to work around your schedule.

Best,
Jordan
"""
    else:  # followup_7
        subject = f"One more thing: {lead['company']}"
        body = f"""Hi {lead['contact'].split()[0]},

I've reached out a few times now, so I'll leave you alone after this!

If you ever need help with neuro data management or FDA submissions, we're here.

Best of luck with {lead['personalization']} — sounds like meaningful work.

Jordan
"""

    return subject, body


def send_email(subject, body, to_email):
    """Send email via Gmail SMTP."""
    if not GMAIL_APP_PASSWORD:
        logger.error("GMAIL_APP_PASSWORD not set!")
        return False
    
    msg = MIMEMultipart()
    msg['From'] = f"{SENDER_NAME} <{GMAIL_USER}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.send_message(msg)
        logger.info(f"Email sent successfully to {to_email}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email to {to_email}: {e}")
        return False


def record_sent_email(lead, sent_log, followup_number=None):
    """Record that an email was sent."""
    if "emails" not in sent_log:
        sent_log["emails"] = []
    if "stats" not in sent_log:
        sent_log["stats"] = {"total_sent": 0, "responses": 0, "revenue": 0}
    
    entry = {
        "email": lead["email"],
        "company": lead["company"],
        "contact": lead["contact"],
        "sent_date": datetime.now().strftime("%Y-%m-%d"),
        "sent_datetime": datetime.now().isoformat(),
        "personalization": lead.get("personalization", ""),
        "revenue_attributed": 0,
        "responded": False,
        "followup_3_sent": False,
        "followup_7_sent": False,
    }
    
    if followup_number:
        entry["followup_number"] = followup_number
        entry["followup_sent"] = True
    
    sent_log["emails"].append(entry)
    sent_log["stats"]["total_sent"] += 1
    save_sent_log(sent_log)


def mark_response(sent_log, email, revenue=0):
    """Mark an email as responded and attribute revenue."""
    for entry in sent_log.get("emails", []):
        if entry["email"] == email:
            entry["responded"] = True
            entry["revenue_attributed"] = revenue
            sent_log["stats"]["responses"] += 1
            sent_log["stats"]["revenue"] += revenue
            save_sent_log(sent_log)
            logger.info(f"Marked response from {email}, revenue: ${revenue}")
            return


def run_campaign():
    """Main campaign logic - runs daily via Railway cron."""
    logger.info("=== Starting Neuro Email Campaign ===")
    
    # Load data
    leads = load_leads()
    sent_log = load_sent_log()
    
    if not leads:
        logger.error("No leads found!")
        return
    
    if not GMAIL_APP_PASSWORD:
        logger.error("GMAIL_APP_PASSWORD environment variable not set!")
        logger.error("Set it with: railway variable set GMAIL_APP_PASSWORD your_app_password")
        return
    
    # Check for follow-ups (day 3 and day 7)
    followup_3_leads = get_followup_leads(leads, sent_log, days_ago=3)
    followup_7_leads = get_followup_leads(leads, sent_log, days_ago=7)
    
    # Send day-3 follow-ups
    for lead in followup_3_leads:
        subject, body = build_email_content(lead, email_type="followup_3")
        if send_email(subject, body, lead["email"]):
            record_sent_email(lead, sent_log, followup_number=3)
            logger.info(f"Day-3 follow-up sent to {lead['company']}")
    
    # Send day-7 follow-ups
    for lead in followup_7_leads:
        subject, body = build_email_content(lead, email_type="followup_7")
        if send_email(subject, body, lead["email"]):
            record_sent_email(lead, sent_log, followup_number=7)
            logger.info(f"Day-7 follow-up sent to {lead['company']}")
    
    # Send new email if leads remaining
    next_lead = get_next_lead(leads, sent_log)
    
    if next_lead:
        subject, body = build_email_content(next_lead, email_type="initial")
        if send_email(subject, body, next_lead["email"]):
            record_sent_email(next_lead, sent_log)
            logger.info(f"Initial email sent to {next_lead['company']}")
    else:
        logger.info("All leads have been contacted! Campaign complete for this cycle.")
    
    # Log stats
    stats = sent_log.get("stats", {})
    logger.info(f"=== Campaign Stats ===")
    logger.info(f"Total Sent: {stats.get('total_sent', 0)}")
    logger.info(f"Responses: {stats.get('responses', 0)}")
    logger.info(f"Revenue: ${stats.get('revenue', 0)}")
    logger.info("=== Campaign Complete ===")


if __name__ == "__main__":
    run_campaign()