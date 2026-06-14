# Niah × South Summit Social Summit After Party
## Partnership Proposal

**Date:** May 11, 2026
**Event:** South Summit Madrid · Social Summit After Party
**When:** Wednesday, June 4th, 2026 · 7:30 PM · La Nave, Madrid
**Goal:** AI matchmaking demo as an embedded after-party experience for 100 South Summit attendees

---

## 1. What Is Niah

AI-driven networking tool for conference after-parties. Instead of random mingling, Niah matches attendees based on:
- Role / industry / goals
- Who they want to meet and why
- What they can offer others

**The metaphor:** Like a skilled host who introduces the right people at a dinner party — but at scale.

Niah works via:
- **Email survey** (9 questions, 60 seconds to complete — via Tally)
- **Pre-event match notifications** (WhatsApp FREE within 24h window, email fallback via Mailchimp)
- **No app download required**

---

## 2. Why South Summit After Party

South Summit Social Summit is the highest-leverage networking moment of the entire event:
- 7:30 PM · after a full day of pitches and panels
- People are relaxed, drinks in hand, open to meeting new people
- 20,000+ attendees from 134 countries — investors, startups, corporates, media
- Already happening at La Nave — no extra venue cost needed

**The pitch to South Summit:**
> "Give your Social Summit after-party attendees a curated networking experience powered by Niah. We match the right people before they walk in the door. No app download. 60 seconds of profiling. Real connections, faster."

---

## 3. The Problem Niah Solves

At South Summit-scale events, networking is broken:
- **Information overload** — who should you talk to? Everyone looks equally interesting
- **Random collisions** — you meet people but not the *right* people
- **After-party chaos** — 500+ people in one room, no structure, same 5 conversations
- **Introverts lose** — the loudest networkers dominate; the best connections never happen

Niah's after-party matchmaking addresses all of these.

---

## 4. The Stack — What We're Actually Using

| Tool | Purpose | Cost |
|------|---------|------|
| **Tally** | Survey form (9 questions) | $0 |
| **n8n** | Automation workflow (18 nodes) | $59/mo |
| **Mailchimp** | Email list + email sends | $59/mo |
| **WhatsApp Business API** | Match notifications (FREE in 24h window) | $0 |
| **Google Sheets** | Matching database + metrics | $0 |
| | | |
| **Total** | | **~$59–$118** |

That's it. No Vercel, no Twilio, no Brevo, no Airtable.

---

## 5. How It Works — Operational Flow

### Stage 1: RSVP Submission
Attendee submits the Tally form → n8n receives the webhook → parses the data → adds to Google Sheets + Mailchimp + WhatsApp confirmation.

**Status: Pending Match** (Yellow)

### Stage 2: Automation Trigger
n8n workflow processes the submission in real-time:
- Adds row to Google Sheets with all profile data
- Adds contact to Mailchimp (tagged: south-summit, [role], afterparty)
- Sends WhatsApp confirmation message → opens 24h free window

**Status: Confirmed** (Green)

### Stage 3: Match Confirmed
Matching team reviews Google Sheets → finds the best complement for each person → fills in `match_name`, `match_email`, `match_reason` → changes status to **Matched**.

### Stage 4: Send Matches
n8n detects the status change → runs the decision:
- **WhatsApp 24h window open?** → Send WhatsApp match notification (FREE)
- **Window closed?** → Send Mailchimp match email (fallback)

**Status: Notified** (Orange)

### Stage 5: Post-Event
June 5 at 10am → n8n sends satisfaction survey via Tally → updates metrics in Google Sheets.

---

## 6. Daily Schedule (June 1–4)

| Date | Time | Action |
|------|------|--------|
| June 1 | 9:00 AM | Send Survey Invite via Mailchimp |
| June 1 | 9:00 AM | n8n reminder workflow activates (daily June 1–4) |
| June 2 | 9:00 AM | Reminder to Pending Match people via Mailchimp |
| June 3 | 9:00 AM | Final reminder email |
| June 4 | 9:00 AM | Last reminder + matching team finishes matches |
| June 4 | 10:00 AM | n8n sends match notifications (WhatsApp FREE or Email) |
| June 4 | 7:30 PM | Social Summit After-Party at La Nave |

---

## 7. The WhatsApp Free Window Strategy

**The key insight:** Every WhatsApp message costs $0.12–0.15 if sent cold. But there's a free window.

**How it works:**
1. After someone submits the Tally form → Niah WhatsApp sends: "Thanks! Message us to confirm your match"
2. They reply to WhatsApp → 24h free window opens
3. n8n sends the match notification within that window → **completely free**
4. If they don't WhatsApp in 48h → Mailchimp email as fallback

**For 100 attendees:**
- ~60–80 will WhatsApp (60–80% engagement for a tech crowd)
- WhatsApp notification cost: **$0** (all 100 covered in free window)
- Email fallback cost: covered by Mailchimp Standard

---

## 8. Tool Setup Status

| Tool | Status | Action Needed |
|------|--------|--------------|
| Tally Survey | ⏳ Needs setup | Create form with 9 fields |
| n8n Workflow | ✅ JSON ready to import | Import + add credentials |
| Google Sheets | ⏳ Needs credentials | Create sheet + share with n8n |
| Mailchimp | ⏳ Needs API key | Create audience + templates |
| WhatsApp Business API | ⚠️ Needs Meta credentials | Set up in Meta Business Suite |
| Google Sheets Matching DB | ⏳ Needs headers | Copy column headers |

---

## 9. What South Summit Gets

For South Summit, this is a:
- **Innovation differentiator** — "AI-powered networking at the Social Summit" is a press line
- **Attendee satisfaction driver** — people remember the event that actually helped them meet useful people
- **Investor-facing proof** — "We embedded Niah's matchmaking" = ROI story for future sponsors
- **Case study** — South Summit's name in Niah's deck = credibility for next events

**What we ask from South Summit:**
- Email promotion to their registered attendees (they already have the list)
- Physical space at the after-party (a corner, a table)
- South Summit branding on Niah match notifications
- Permission to use South Summit logo on Niah's website

**What Niah delivers:**
- Full matchmaking service (survey + matching + notifications + on-site support)
- Pre-event email campaign (3 touches)
- Day-of match notifications (WhatsApp + email)
- Post-event data report (matches made, satisfaction rate)

---

## 10. KPI Targets

| KPI | Target | Alert If |
|-----|--------|----------|
| Survey completion rate | >40% | <25% |
| Match rate | >80% of completers | <60% |
| WhatsApp notification rate | >60% of notifications | <30% |
| Email open rate | >50% | <30% |
| Satisfaction score | >70% "useful connection" | <50% |

---

## 11. Cost Breakdown — 100 Attendees

**This is the all-in number South Summit sees.**

| Tool | Plan | Monthly | 100 People — Usage | Cost |
|------|------|---------|--------------------|------|
| Tally | Free | $0 | ~100 survey submissions | **$0** |
| n8n Cloud | Pro | $59 | ~700 tasks (see below) | **$59** |
| Mailchimp | Standard | $59 | 100 contacts (well under 5K limit) | **$59** |
| WhatsApp Business API | — | $0 | 100 notifications in free window | **$0** |
| Google Sheets | Free | $0 | Matching database | **$0** |
| | | | | |
| **Total** | | | | **~$118/mo** |

**n8n task breakdown for 100 attendees (~700 total tasks):**
- 1 RSVP submission → 1 webhook trigger
- 1 submission → Google Sheets write (1 task)
- 1 submission → Mailchimp add (1 task)
- 1 submission → WhatsApp confirmation (1 task)
- 4 reminder emails (1 per person × 4 rounds) → 400 tasks
- Match notification (per person) → 100 tasks
- Post-event survey trigger → 100 tasks
- **Total: ~700 tasks/month** — well under n8n Pro's 10K limit

**Mailchimp for 100 contacts:** Standard plan ($59/mo) covers this easily. Free tier (500 contacts) would also work for $0, but Standard gives us better templates and automation features worth paying for.

**Event duration note:** The $118 is a monthly subscription. If the event runs June 1–4 only, that's 1 month of cost. If you want to pause/cancel after the event, n8n and Mailchimp both allow billing cycle cancellation.

---

## 12. Risk Mitigation

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| South Summit doesn't respond | Medium | Use LinkedIn to find specific partnership contact |
| Low survey completion rate | High | South Summit must promote via their channels |
| WhatsApp window closes before notification | Medium | Mailchimp email fallback covers all cases |
| WhatsApp setup takes too long | Medium | Email-only version works fine as backup |

---

## 13. Next Steps

1. **This week:** Send partnership email to South Summit
2. **If interested:** Share this proposal, confirm scope
3. **If confirmed:** Start setup May 27
4. **June 4:** Execute Niah matchmaking at Social Summit after-party

---

*Proposal prepared for Jordan Hays — Niah*
*Last updated: May 11, 2026*