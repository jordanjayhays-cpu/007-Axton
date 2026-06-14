# Niah × South Summit — Setup Guide
## How to Get Everything Running
**Created:** May 10, 2026 | **Event:** June 4, 2026 | **Scale:** 50-150 people

---

## What You Have

| File | What It Is |
|------|-----------|
| `niah-south-summit-n8n-workflow.json` | Import into n8n — the full automation workflow |
| `niah-south-summit-tool-research.md` | Deep research on all tools |
| `niah-south-summit-proposal.md` | The pitch deck / proposal for South Summit |
| `niah-south-summit-leads.md` | Outreach tracker for South Summit contacts |

---

## Step 1: Import the n8n Workflow

1. Go to your n8n instance
2. → Workflows → Import → Paste the JSON or upload the file
3. Click **Save**

The workflow has **17 nodes** across **5 stages:**
- RSVP → Tally trigger → parse → add to Sheets + Mailchimp + WhatsApp confirm
- Daily (June 1-4) → check pending → send reminder emails
- Match confirmed → decision: WhatsApp (FREE) vs Mailchimp (email)
- Post-event (June 5) → send satisfaction survey → update dashboard

---

## Step 2: Create the Tally Survey

Go to [tally.so](https://tally.so), create a form with these fields:

### Survey Fields

| # | Field Name | Type | Required | Notes |
|---|-----------|------|----------|-------|
| 1 | name | Short text | Yes | |
| 2 | email | Email | Yes | |
| 3 | phone | Phone (ES) | No | WhatsApp number — enables free notifications |
| 4 | role | Multiple choice | Yes | Options: Investor / Founder / Corporate / Startup / Media / Other |
| 5 | company | Short text | Yes | |
| 6 | what_brings_you | Short text | No | Why you're at South Summit |
| 7 | who_to_meet | Long text | Yes | Who you want to meet + why |
| 8 | what_can_you_help | Long text | No | What you can offer others |
| 9 | preferences | Long text | No | Preferences / things to avoid |

**Form title:** "Before the Social Summit — 60 seconds to get matched"
**Redirect after submit:** `https://niah.io/south-summit/thank-you`

### Tally → n8n Webhook Setup
In Tally: → Form → Integrations → Webhooks → Add webhook:
- URL: `https://YOUR-N8N-URL/webhook/niah-south-summit-rsvp`
- Events: "On new submission"

In n8n: Activate the workflow → copy the webhook URL → paste into Tally.

---

## Step 3: Set Up Google Sheets

1. Create a new Google Sheet called **"Niah South Summit – Matching DB"**
2. Sheet 1 name: `Sheet1`
3. Copy the headers from the workflow into Row 6:

```
name | email | phone | role | company | what_brings_you | who_to_meet | what_can_you_help | preferences | status | submitted_at | match_name | match_email | match_reason | match_link | notified_at
```

4. Column J (status) will be updated by the matching team:
   - **Pending Match** = Yellow (waiting to be matched)
   - **Matched** = Blue (matching team has assigned a pair)
   - **Notified** = Orange (notification sent)

5. Create Sheet 2 called `Lookup` — this is the scoring reference table

6. Share the sheet with n8n service account (or use OAuth)

**Matching formula** (Column J, Sheet1):
```
=IF(A7="","",IF(COUNTIF(D7,"Investor")>0,3,0)+IF(COUNTIF(D7,"Founder")>0,3,0)+IF(COUNTIF(G7,"AI")>0,2,0))
```
Adjust based on your matching logic.

---

## Step 4: Set Up Mailchimp

1. Create audience: "South Summit Afterparty 2026"
2. Add these tags when contacts are added:
   - `south-summit` (all)
   - `[their role]` (e.g. `Founder`, `Investor`)
   - `afterparty`

3. Create email templates:
   - **Survey Invite** — "Before the Social Summit — 60 seconds to get matched"
   - **Reminder 1** — "Still time to get matched"
   - **Reminder 2** — "Final reminder — Social Summit is tomorrow"
   - **Match Notification** — "Your South Summit Match is ready"

4. In n8n: Add Mailchimp credential (API key from Mailchimp → Account → API keys)

---

## Step 5: Set Up WhatsApp Business API

### Prerequisites
- WhatsApp Business API access (via Meta for Developers)
- A phone number registered with WhatsApp Business
- A verified Meta Business account

### Setup
1. Go to [developers.facebook.com](https://developers.facebook.com)
2. Create an app → WhatsApp Business → Get API credentials
3. Note these values for n8n environment variables:

| Environment Variable | Where to Find |
|---------------------|---------------|
| `WHATSAPP_TOKEN` | Meta Business → WhatsApp → API Setup → Permanent Token |
| `WHATSAPP_PHONE_NUMBER_ID` | Same page — your phone number ID |
| `WHATSAPP_API_URL` | `https://graph.facebook.com/v18.0` |

4. In n8n: Add WhatsApp credential (OAuth2)
5. **Create WhatsApp template** in Meta Business Suite:
   - Template name: `confirmation`
   - Category: Utility
   - Body: "Hi {{1}}, you're registered for Niah at South Summit. We'll send your match before the event!"

### The Free Window Trick (IMPORTANT)
- Every time someone messages Niah on WhatsApp → 24h free window opens
- In that window, ALL messages are free (even marketing templates)
- Encourage people to message Niah on WhatsApp after filling the survey

---

## Step 6: Set Up n8n Environment Variables

In n8n → Settings → Variables, add:

```bash
WHATSAPP_TOKEN=your_permanent_meta_token
WHATSAPP_PHONE_NUMBER_ID=your_phone_number_id
WHATSAPP_API_URL=https://graph.facebook.com/v18.0
TALLY_FORMS_URL=https://api.tally.so
TALLY_SATISFACTION_FORM_ID=your_form_id
```

---

## Step 7: Connect Credentials in n8n

For each credential, go to n8n → Settings → Credentials → Add:

| Credential | What to Enter |
|-----------|---------------|
| **Google Sheets** | OAuth2 — connect your Google account |
| **Mailchimp** | API Key — from Mailchimp dashboard |
| **WhatsApp Business** | OAuth2 — from Meta Business app |
| **Airtable** | API Key + Base ID — from Airtable |

---

## Step 8: Connect Tally to n8n

1. In n8n: Open the "Tally Form Trigger" node → Click **Listen for test event**
2. Copy the webhook URL (looks like `https://your-n8n.io/webhook/niah-south-summit-rsvp`)
3. In Tally: → Your form → Integrations → Webhooks → Add
4. Paste the URL → Save
5. Submit a test entry in Tally
6. n8n should receive it → click **Save** to confirm

---

## Step 9: Matching Process (Manual)

The n8n workflow triggers when YOU update Google Sheets. The matching team does this:

### For each row with Status = "Pending Match":
1. Read the "who_to_meet" and "what_can_you_help" fields
2. Find the best complementary match (Founder + Investor = ideal)
3. In the matched row:
   - Enter `match_name` — the other person's name
   - Enter `match_email` — their email
   - Enter `match_reason` — "You're both interested in AI,互补"
   - Enter `match_link` — optional: LinkedIn or calendar link
   - Change `status` to **Matched**

4. n8n detects the update → triggers the notification flow

---

## Step 10: Pre-Event Email Sequence (June 1-4)

| Date | Time | Action |
|------|------|--------|
| June 1 | 9:00 AM | Send Survey Invite (Mailchimp broadcast) |
| June 2 | 9:00 AM | n8n sends reminders to Pending Match people |
| June 3 | 9:00 AM | Final reminder email |
| June 4 | 9:00 AM | Last reminder + matching team updates sheet |
| June 4 | 10:00 AM | n8n sends match notifications |

**Manual task June 4 morning:**
Matching team should finish all matches by 10:00 AM so n8n can notify before the 7:30 PM event.

---

## Step 11: Day-Of Setup (June 4, La Nave)

- **Niah table** at the after-party venue
- QR code on table linking to Tally survey (for late sign-ups)
- Tablet showing live sheet (read-only) — matches being notified in real-time
- Someone monitoring WhatsApp to reply to incoming messages (opens 24h windows)

---

## Step 12: Post-Event (June 5)

n8n runs automatically at 10:00 AM:
1. Reads all "Notified" contacts from Google Sheets
2. Sends satisfaction survey via Tally
3. Updates Airtable dashboard with metrics:
   - Total RSVPs
   - Total matches sent
   - Survey response rate
   - Satisfaction score
   - WhatsApp vs email notification rate

---

## KPI Targets

| KPI | Target | Alert If |
|-----|--------|----------|
| Survey completion rate | >40% | <25% |
| Match rate | >80% of completers | <60% |
| WhatsApp notification rate | >60% of notifications | <30% |
| Email open rate | >50% | <30% |
| Satisfaction score | >70% "useful connection" | <50% |

---

## Cost Summary

| Tool | Cost | Notes |
|------|------|-------|
| Tally | $0 | Free tier — unlimited |
| Mailchimp Standard | $59/mo | 1 month |
| n8n Cloud | $59/mo (Pro) | For 150 contacts |
| WhatsApp Business API | $0 | Free in 24h window |
| Google Sheets | $0 | Free |
| Airtable | $0 | Free tier |
| **TOTAL** | **~$59** | |

---

## Quick Reference — n8n Workflow Nodes

```
STAGE 1: RSVP
Tally Form Trigger → Parse Tally Data → Add to Google Sheets
                                             → Add to Mailchimp
                                             → WhatsApp Confirmation

STAGE 2: DAILY REMINDERS (June 1-4)
Daily Schedule → Get Pending Matches → Has Pending Status?
                                            → Send Reminder Email (Mailchimp)

STAGE 3: MATCHING + NOTIFICATION
Google Sheets (Status=Matched) → WhatsApp 24h Window Open?
                                   ↓ YES         ↓ NO
                              WhatsApp Match   Mailchimp Match
                                   ↓
                          Update Status to Notified

STAGE 4: POST-EVENT (June 5)
Post-Event Schedule → Get Notified Contacts → Send Satisfaction Survey
                                                   → Update Niah Dashboard
```

---

*Setup guide created: May 10, 2026*
*For questions: Jordan Hays — Telegram @6463127078*