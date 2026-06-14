# Neuro Email Cron - Railway Deployment

## Setup Instructions

### 1. Generate Gmail App Password
1. Go to https://myaccount.google.com/security
2. Enable **2-Factor Authentication** (required for app passwords)
3. Search for "App Passwords" in the search bar
4. Create a new app password:
   - Select app: "Mail"
   - Select device: "Other (Custom name)" → type "Railway"
5. Copy the 16-character password (format: `xxxx xxxx xxxx xxxx`)

### 2. Deploy to Railway
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
cd neuro-email-cron
railway init

# Set environment variables
railway variables set GMAIL_USER jordanjayhays@gmail.com
railway variables set GMAIL_APP_PASSWORD your_app_password_here
railway variables set SENDER_NAME Jordan

# Upload leads.json and email_sender.py
railway up

# Or use GitHub integration for automatic deployments
```

### 3. Configure Cron Schedule (optional)
Edit `railway.json` to adjust the cron schedule:
```json
"schedule": "0 9 * * *"  // Runs daily at 9 AM UTC
```
Cron format: `minute hour day month weekday`

### 4. Upload Lead Data
Upload your `leads.json` file to Railway:
```bash
railway run --upload /tmp/neuro-email-cron/leads.json ./leads.json
```

Or mount a volume for persistent storage.

## Campaign Flow

1. **Day 0**: Initial personalized cold email sent to next uncontacted lead
2. **Day 3**: Auto follow-up if no response
3. **Day 7**: Final follow-up if still no response
4. **Day 10+**: Lead marked as "exhausted" (no more auto outreach)

## Tracking

Logs are stored in `sent_log.json`:
- `total_sent`: Count of all emails sent
- `responses`: Number of leads who responded
- `revenue`: Attributed revenue (update manually or via webhook)
- `emails[]`: Detailed log per lead with timestamps

## Marking Responses

When a lead responds, manually update the log:
```bash
railway run python -c "
import json
with open('sent_log.json', 'r') as f:
    log = json.load(f)
for e in log['emails']:
    if 'neurotech' in e['company'].lower():
        e['responded'] = True
        e['revenue_attributed'] = 50000
        log['stats']['responses'] += 1
        log['stats']['revenue'] += 50000
with open('sent_log.json', 'w') as f:
    json.dump(log, f, indent=2)
print('Marked response!')
"
```

## Files

- `email_sender.py` - Main script (cron runs this daily)
- `leads.json` - 10 neuro companies with contact info
- `sent_log.json` - Campaign tracking (created on first run)
- `railway.json` - Railway cron configuration
- `requirements.txt` - Python dependencies