# Niah × South Summit Social Summit — Deep Tool Research
## All Platform Options Across Every Category
**Research date:** May 10, 2026
**Goal:** Find the best tool combinations for Niah's South Summit matchmaking execution — with real pricing, real trade-offs, and real alternatives at every level.

---

## Context: What We're Building

Niah needs to:
1. **Collect** attendee profiles (survey)
2. **Match** attendees based on role + industry + goals
3. **Notify** matched pairs via email and SMS before the event
4. **Host** a simple matching interface on the web
5. **Automate** the entire sequence without manual sending
6. **Follow up** post-event with contact exchange

The event is June 4th, 2026. We have ~3 weeks to set up. Budget is basic costs only (no profit margin on the proposal to South Summit).

---

## Category 1: Survey / Profiling Form

**What it does:** Collects 3 questions from each attendee — role type, industry, goal, who they want to meet.

### Option A: Google Forms (FREE)
| Factor | Detail |
|--------|--------|
| **Cost** | $0 — free forever |
| **Responses** | Unlimited |
| **Forms** | Unlimited |
| **Integrations** | Google Sheets natively, Zapier, Make |
| **Branding** | Limited — Google branding, no custom theme |
| **Logic** | Basic skip logic, no conditional branching |
| **Mobile UX** | Basic, functional |
| **Embed** | Yes — inline embed in any page |
| **Export** | CSV, Google Sheets |
| **Email collect** | No — responses go to sheet only |

**Best for:** Maximum budget savings, no branding needed
**Key limitation:** No native email sending, no beautiful UX, limited brand presentation
**Setup time:** 30 minutes

---

### Option B: Tally Forms (FREE TIER)
| Factor | Detail |
|--------|--------|
| **Cost** | $0 free (fair usage), $29/mo Pro for custom domain + no branding |
| **Responses** | Unlimited on free |
| **Forms** | Unlimited on free |
| **Branding** | Remove Tally branding on Pro ($29/mo) |
| **Logic** | Yes — conditional logic, hidden fields |
| **Mobile UX** | Beautiful — modern, minimal, conversational |
| **Embed** | Yes — inline or popup |
| **Export** | CSV, Google Sheets, Zapier, Make |
| **Email notifications** | Yes — built-in notification to email on submission |
| **Custom domain** | Pro ($29/mo) only |

**Best for:** Beautiful forms without paying. Free tier is very generous.
**Key limitation:** Free tier has Tally branding on the form — attendees see it
**Setup time:** 45 minutes

---

### Option C: Typeform (STARTER — $25/mo billed annually)
| Factor | Detail |
|--------|--------|
| **Cost** | $25/mo annual (100 responses/mo), $35/mo monthly |
| **Responses** | 100/mo on Starter |
| **Forms** | Unlimited |
| **Branding** | Clean, no Typeform branding on embed |
| **Logic** | Advanced — conversational logic, calculator logic |
| **Mobile UX** | Best-in-class — truly conversational, one question at a time |
| **Embed** | Yes — inline, popup, or chat widget |
| **Integrations** | Zapier, Make, Slack, HubSpot, Brevo, Gmail |
| **Email notify** | Yes — native + via Zapier/Make |
| **AI assist** | Built-in AI to help write questions |
| **Analytics** | Built-in completion rates, drop-off points |

**Best for:** The experience matters — Niah brand presentation at its best
**Key limitation:** 100 responses/mo is tight. If 500 people take the survey, you need $83/mo Business plan (1,000 responses). Not viable for large events on lower tiers.
**Setup time:** 1-2 hours

**Pricing tiers:**
| Plan | Monthly (annual) | Responses/mo |
|------|-----------------|-------------|
| Free | $0 | 10 |
| Basic | $25 | 100 |
| Plus | $50 | 1,000 |
| Business | $83 | 1,000 |
| Enterprise | Custom | Unlimited |

---

### Option D: Jotform (STANDARD — $39/mo)
| Factor | Detail |
|--------|--------|
| **Cost** | $39/mo (1,000 submissions/mo, 10 forms) |
| **Responses** | 1,000/mo |
| **Forms** | 10 on Standard |
| **Branding** | Remove Jotform branding on all paid plans |
| **Logic** | Very strong — conditional logic, form fields, calculations |
| **Mobile UX** | Good, functional |
| **Integrations** | 100+ native integrations (Brevo, Mailchimp, Slack, Google Sheets) |
| **Email notify** | Native — send email on submission, with PDF attachment option |
| **Payment** | Built-in Stripe/PayPal — could charge for the service |
| **Approval flow** | Built-in — review submissions before they go live |

**Best for:** If Niah might charge for access (ticketed after-party), Jotform handles payments too
**Key limitation:** 10 forms limit on Standard — enough for this event but constraining long-term
**Setup time:** 1-2 hours

---

### RECOMMENDED for Survey: Tally (free) or Typeform ($25/mo)

**For MVP (budget-only):** Google Forms — 0 cost, gets the job done, data goes to Google Sheets automatically.

**For actual event presence:** Tally free tier (no cost, unlimited responses, beautiful UX, native email notification) until we hit 500 responses where we need Pro ($29/mo).

**For brand presentation:** Typeform Starter ($25/mo) — the conversational format fits Niah's networking vibe exactly, and 100 responses/mo covers our first 100-200 attendees before we need to upgrade.

---

## Category 2: Email Platform

**What it does:** Sends the survey invite, reminders, and match notifications to attendees. Handles the full email sequence automatically.

### Option A: Brevo (formerly Sendinblue) — Standard Yearly
| Factor | Detail |
|--------|--------|
| **Cost** | $8.08/mo billed annually (20K emails/mo) |
| **Emails included** | 20,000/mo |
| **Contacts** | Unlimited (unique contacts matter, not total) |
| **Email builder** | Drag-and-drop, good templates |
| **Automation** | Yes — multi-step automation, triggered by action |
| **SMS** | Yes — add SMS for €0.10-0.13/SMS |
| **CRM** | Built-in — contact management, deal tracking |
| **Transactional email** | Yes — separate API for match notifications |
| **Deliverability** | Good, improving rapidly |
| **Free tier** | 300 emails/day (9K/mo) — not enough for 20K attendee event |
| **PAYG top-up** | €0.0005/email above plan limit |

**Best for:** Full-stack email + SMS from one platform. Best value at this scale.
**Real cost for South Summit:** €45 for 3 months + €20 PAYG for 40K extra emails = **€65**
**Setup time:** 2-3 hours (import list, build sequence, set up automation)

---

### Option B: Mailchimp (STANDARD — $13/mo for 500 contacts)
| Factor | Detail |
|--------|--------|
| **Cost** | $13/mo for 500 contacts; $23/mo for 2,500; $59/mo for 5,000 |
| **Contacts** | Based on total audience size — expensive as list grows |
| **Email builder** | Very good — best-in-class editor |
| **Automation** | Yes — multi-step available |
| **SMS** | Add-on (Mandrill) — more expensive than Brevo SMS |
| **Deliverability** | Very good — industry standard |
| **Analytics** | Excellent — best reporting in class |
| **Templates** | Huge library, good quality |

**Best for:** Teams that prioritize email editor quality and analytics over cost
**Key limitation:** Pricing is per-contact, not per-email-volume. For 20K emails/mo with 5K contacts = $59/mo. At 20K contacts = $149/mo. Gets expensive fast.
**Setup time:** 1-2 hours

---

### Option C: Kit (formerly ConvertKit) — Creator Plan
| Factor | Detail |
|--------|--------|
| **Cost** | $39/mo (1,000 subscribers), $99/mo (10K subscribers) |
| **Subscribers** | All contacts count — expensive for large lists |
| **Email builder** | Simple, text-focused — not design-forward |
| **Automation** | Yes — visual automation builder |
| **Landing pages** | Built-in — good for lead capture |
| **Paid newsletters** | Built-in — could monetize Niah content |
| **Tag-based segmentation** | Excellent — very flexible |

**Best for:** Creator economy, paid newsletter model
**Key limitation:** Not designed for event outreach. Contact-based pricing hurts for one-time large events.
**Setup time:** 1-2 hours

---

### Option D: Moosend (STANDARD — $9/mo)
| Factor | Detail |
|--------|--------|
| **Cost** | $9/mo for unlimited emails (on all paid plans) |
| **Contacts** | Based on list size — starts at 500: $9/mo |
| **Email builder** | Good drag-and-drop |
| **Automation** | Yes — good automation, includes AI writing assistant |
| **SMS** | No — email only |
| **Free trial** | 30-day free trial (no forever-free plan) |

**Best for:** Budget email — cheapest paid tier for unlimited emails
**Key limitation:** No SMS. No free forever plan. Contact-based pricing.
**Setup time:** 1-2 hours

---

### Option E: HubSpot (STARTER — $15/mo for 1K contacts)
| Factor | Detail |
|--------|--------|
| **Cost** | $15/mo for 1K contacts; $205/mo for 5K contacts |
| **Contacts** | All contacts count toward limit |
| **Email builder** | Good |
| **Automation** | Powerful — CRM-native automation |
| **CRM** | Full CRM — contacts, deals, pipeline |
| **Landing pages** | Built-in, good |
| **SMS** | Add-on, separate product |

**Best for:** If Niah needs a full CRM long-term (sales pipeline, investor tracking)
**Key limitation:** Contact-based pricing scales badly. 5K contacts = $205/mo. Not good for event-scale one-time sends.
**Setup time:** 3-4 hours (CRM setup, list hygiene, import)

---

### Option E: Twilio SendGrid (ESSENTIAL — $15/mo for 5K emails)
| Factor | Detail |
|--------|--------|
| **Cost** | $15/mo for 5K emails/mo, $25/mo for 100K emails/mo |
| **Email builder** | Transactional focused — not design-forward |
| **API** | Excellent — best-in-class developer docs |
| **Automation** | Yes — marketing automation on higher tiers |
| **Transactional email** | Native — built for it (password resets, match notifications) |
| **Deliverability** | Excellent — very high inbox rates |

**Best for:** Developer-first teams, transactional emails, high-volume sends
**Key limitation:** UI is less intuitive for non-technical users. Best for API-driven sending rather than visual campaign building.
**Setup time:** 1-2 hours (can be fully API-driven, no UI needed)

---

### Option F: HubSpot Email (Marketing Hub Starter — $15/mo, Professional — $89/mo)
| Factor | Detail |
|--------|--------|
| **Cost** | $15/mo Starter (1K contacts), $89/mo Professional (2K contacts) |
| **Email builder** | Good drag-and-drop, AI assist on Professional |
| **Automation** | Workflows — yes, very powerful on Professional |
| **CRM** | Full CRM native — contacts, deals, pipeline |
| **Survey forms** | Yes — native HubSpot forms |
| **Event management** | Yes — Marketing Events app |
| **SMS** | ❌ **SMS ONLY available for US/Canada phone numbers (+1). Cannot send SMS to Spain (+34).** |
| **Forms** | Native form builder, strong |
| **Lead scoring** | Yes — Professional+ |
| **Analytics** | Excellent — full attribution |

**Best for:** If Niah wants a unified CRM + email + automation + event tracking — all in one place.
**Key limitation:** **HubSpot SMS does NOT work in Spain.** The SMS add-on is geographically restricted to US/Canada only. For the South Summit event in Madrid, we'd need a separate SMS tool (MessageBird or Twilio) regardless.
**Contact-based pricing:** Scales expensively. 5K contacts = $320+/mo Professional.
**Setup time:** 3-5 hours (CRM setup, list import, workflow building)

---

### Can HubSpot Do Everything? Answer: NO for SMS + Spain

HubSpot is excellent for:
- ✅ Email campaigns + automation
- ✅ Survey form collection
- ✅ CRM (contacts, deals, pipeline)
- ✅ Event registration + tracking
- ✅ Analytics + attribution
- ❌ **SMS to Spain** — blocked, US/Canada only
- ❌ **Website hosting** — not a hosting platform

**For the South Summit event, the stack would be:**
- HubSpot for CRM + email + automation
- Tally for survey (or HubSpot forms, they're good)
- MessageBird or Twilio for SMS (HubSpot can't do Spain SMS)
- Squarespace for web hosting

**If the goal is to consolidate tools:** HubSpot + MessageBird covers everything except Squarespace hosting. That's a 2-platform solution instead of 4-5 separate tools.

---

### RECOMMENDED for Email: Brevo Standard (yearly)

Best value at scale. $8.08/mo for 20K emails/mo covers the full South Summit sequence (survey invite → 2 reminders → match notification → post-event follow-up) for all 20K attendees.

**Real scenario:**
- 20K attendee list from South Summit
- 3 pre-event emails (60K total) + match notification (20K) + follow-up (20K) = ~100K emails total
- Brevo Standard 3 months = €24 (yearly rate × 3)
- PAYG top-up for 40K extra emails = €20
- **Total email cost: ~€44-65**

---

## Category 3: SMS Notifications

**What it does:** Sends match notifications via SMS as a backup to email (and for real-time late sign-ups during the event).

### Option A: Twilio
| Factor | Detail |
|--------|--------|
| **Cost (Spain outbound)** | ~€0.081/SMS (international rate, $0.0875 × EUR exchange) |
| **2K recipients** | ~€162 |
| **API** | Best-in-class — massive ecosystem, docs are gold |
| **Setup time** | 1 hour |
| **Reliability** | Very high |
| **Templates** | Yes — pre-approve message templates for faster sending |
| **Phone number** | $1/month for a Spanish number |

**Best for:** Highest reliability needed, complex multi-channel integration
**Key limitation:** Most expensive option

---

### Option B: Plivo
| Factor | Detail |
|--------|--------|
| **Cost (Spain outbound)** | ~€0.047/SMS (€0.046/SMS EU rate, vs Twilio's €0.081) |
| **2K recipients** | ~€94 (saves ~€68 vs Twilio) |
| **API** | Good — similar to Twilio, clean docs |
| **Setup time** | 1-2 hours |
| **Reliability** | Good — direct carrier connections in EU |
| **Phone number** | ~€0.80/month for Spanish number |

**Best for:** Cost-conscious but still reliable. Undercuts Twilio by ~40%.
**Key limitation:** Smaller ecosystem than Twilio. Fewer pre-built integrations.

---

### Option C: MessageBird (Bird)
| Factor | Detail |
|--------|--------|
| **Cost (Spain outbound)** | ~€0.031/SMS (EU premium rate) |
| **2K recipients** | ~€62 (saves ~€100 vs Twilio) |
| **API** | Good — omnichannel (SMS, WhatsApp, Email in one platform) |
| **Setup time** | 1-2 hours |
| **Reliability** | Strong in Europe (EU-based infrastructure, GDPR-compliant) |
| **Phone number** | €0.80/month for Spanish number |
| **WhatsApp** | Same platform — could add WhatsApp notifications |

**Best for:** European events, GDPR compliance is important, want SMS + WhatsApp in one place
**Key limitation:** Less known in US/Asia. Good for European-first events like South Summit.

---

### Option D: Telnyx
| Factor | Detail |
|--------|--------|
| **Cost (Spain outbound)** | ~€0.037/SMS (lower EU rate) |
| **2K recipients** | ~€74 |
| **API** | Good — owned global IP network, low latency |
| **Setup time** | 1 hour |
| **Reliability** | Very high — owns its network infrastructure |
| **Phone number** | ~€1/month for Spanish number |

**Best for:** Infrastructure-minded teams who want carrier-grade reliability at lower cost
**Key limitation:** Smaller team support. Steeper learning curve.

---

### Option E: Bandwidth (US + EU)
| Factor | Detail |
|--------|--------|
| **Cost (US domestic)** | $0.004/SMS via 10DLC — very cheap |
| **Cost (Spain outbound)** | Higher — ~€0.04/SMS international |
| **2K recipients** | ~€80 |
| **API** | Good — high throughput |
| **Setup time** | 1-2 hours |
| **Best use** | US-focused events more than European |

**Best for:** US-based events first; secondary for EU
**Key limitation:** Not optimized for European event SMS

---

### RECOMMENDED for SMS: MessageBird (Bird)

Best value for European SMS. €62 for 2K messages vs Twilio's €162. EU-based infrastructure means GDPR compliance is native. Omnichannel platform (SMS + WhatsApp) means if Niah wants to add WhatsApp notifications later, it's the same platform.

**Key insight:** If South Summit provides their Twilio account or has an existing SMS gateway, we can use theirs and reduce our SMS cost to €0. Always ask event partners what SMS infrastructure they have.

---

## Category 4: Survey + Email + SMS Combined Platforms

Some platforms do all three in one place — reducing complexity and tool costs.

### Option A: Brevo (Full Stack)
| Factor | Detail |
|--------|--------|
| **Survey** | ❌ No survey builder — use Typeform/Tally + Brevo |
| **Email** | ✅ Best-in-class value |
| **SMS** | ✅ Yes, SMS + WhatsApp |
| **Automation** | ✅ Multi-step automation |
| **CRM** | ✅ Built-in |

**Best for:** Full email + SMS platform. Survey separate.

---

### Option B: HubSpot (Full Stack)
| Factor | Detail |
|--------|--------|
| **Survey** | ✅ Forms built-in |
| **Email** | ✅ Yes |
| **SMS** | ✅ Add-on |
| **Automation** | ✅ Very powerful |
| **CRM** | ✅ Full CRM included |
| **Cost** | $15/mo entry, $205/mo for 5K contacts — expensive |

**Best for:** Long-term Niah CRM + marketing. Overkill for single event.

---

### Option C: MessageBird / Bird (Full Stack)
| Factor | Detail |
|--------|--------|
| **Survey** | ❌ No survey builder |
| **Email** | ✅ Yes (via SMTP/API) |
| **SMS** | ✅ Core strength |
| **WhatsApp** | ✅ Built-in |
| **Automation** | ✅ Flow builder |
| **CRM** | ✅ Contact management |

**Best for:** European SMS-first + omnichannel. Survey separate.

---

### Option D: Pabbly Email Marketing (UNLIMITED — $79/mo)
| Factor | Detail |
|--------|--------|
| **Cost** | $79/mo flat — unlimited contacts, unlimited emails, unlimited SMS |
| **Email** | Yes — unlimited |
| **SMS** | Yes — but SMS costs extra (carrier rates) |
| **Automation** | Yes |
| **Forms** | Yes — built-in form builder |
| **Survey** | Not really — more for email campaigns than profiling |

**Best for:** If Niah sends to large lists regularly, $79/mo flat is exceptional value
**Key limitation:** $79/mo is 10× Brevo's cost for a single event. Better for recurring use.

---

## Category 5: Web Hosting (Matching Interface)

**What it does:** Hosts a simple web page where attendees complete the survey, see their match, and get their match's contact details.

### Option A: Vercel (FREE — Hobby Tier)
| Factor | Detail |
|--------|--------|
| **Cost** | $0 free (fair use, commercial allowed) |
| **Bandwidth** | 100GB/month — more than enough for event |
| **Storage** | 100GB |
| **Custom domain** | Yes — free |
| **SSL** | Yes — automatic |
| **Builds** | 100 deployments/month |
| **Serverless functions** | Yes — can run matching logic server-side |
| **Deployment** | GitHub integration — push to deploy |

**Best for:** Most projects at this scale. Free tier is very generous.
**Key limitation:** No server-side database (need to use an external DB like Supabase or Airtable for matching data)
**Setup time:** 30 minutes

---

### Option B: Netlify (FREE — Starter)
| Factor | Detail |
|--------|--------|
| **Cost** | $0 free |
| **Bandwidth** | 100GB/month |
| **Forms** | Native form handling — could replace Tally/Typeform |
| **Identity** | User authentication built-in — could handle match logins |
| **Split testing** | A/B testing native |
| **Custom domain** | Yes — free |
| **Deployment** | GitHub integration, drag-and-drop deploy |

**Best for:** If you want built-in forms + identity + hosting all in one
**Key limitation:** Serverless functions more limited than Vercel. Matching logic needs external tool.
**Setup time:** 30-60 minutes

---

### Option C: Cloudflare Pages (FREE)
| Factor | Detail |
|--------|--------|
| **Cost** | $0 free — unlimited bandwidth |
| **Bandwidth** | Unlimited — no caps at all |
| **Edge locations** | 300+ — fastest global performance |
| **Deployment** | GitHub integration |
| **Workers** | Serverless — can run matching logic |
| **Custom domain** | Yes — free |
| **Forms** | No — need external form solution |

**Best for:** High-traffic events where bandwidth could spike. Fastest CDN.
**Key limitation:** Workers is V8 isolate-based (not Node.js) — some npm packages don't work. Matching logic needs a workaround.
**Setup time:** 45 minutes

---

### Option D: Railway (HOBBY — $5/mo)
| Factor | Detail |
|--------|--------|
| **Cost** | $5/mo |
| **Type** | Full server (not serverless) — Node.js, Python, etc. |
| **Database** | Yes — PostgreSQL, MySQL built-in |
| **Custom domain** | Yes |
| **SSL** | Automatic |
| **Deploy** | GitHub, CLI, Docker |

**Best for:** Full backend — matching algorithm + database in one place. Most powerful option.
**Key limitation:** More complex to set up. $5/mo adds to cost.
**Setup time:** 2-3 hours

---

### Option E: GitHub Pages (FREE)
| Factor | Detail |
|--------|--------|
| **Cost** | $0 free |
| **Type** | Static only — HTML/CSS/JS only, no server |
| **Custom domain** | Yes — free |
| **SSL** | Yes — automatic (via Cloudflare or fastly) |
| **Matching logic** | Client-side only (in the browser) — attendees' data visible in URL params |

**Best for:** Pure static landing page. Matching needs to happen via external service.
**Key limitation:** Can't run server-side code — all matching logic exposed client-side (privacy issue)
**Setup time:** 15 minutes

---

### RECOMMENDED for Web Hosting: Vercel (free) + Airtable (free tier)

**Architecture:**
- Vercel hosts the static matching page (survey form → submit → show match)
- Airtable stores survey responses and matching results (free tier: 1,000 records)
- When survey is submitted → webhook to Make/Zapier → writes to Airtable → runs matching → sends notification

**This keeps costs at $0 for hosting and data storage.**

For the matching logic — can be a simple JavaScript function that runs in the browser on Vercel's static page, reading from Airtable's API. No server needed.

**Alternative (if more complex):** Railway $5/mo for full Node.js backend + database.

---

## Category 6: Automation (Connecting Survey → Matching → Notifications)

**What it does:** When someone submits the survey, automatically runs the matching logic, finds their pair, and sends the match notification — without manual intervention.

### Option A: Zapier (FREE — 100 tasks/mo)
| Factor | Detail |
|--------|--------|
| **Cost** | $0 free (100 tasks/mo), $49/mo Professional (2,000 tasks/mo) |
| **Integrations** | 7,000+ apps |
| **Survey triggers** | Typeform, Tally, Google Forms, Jotform |
| **Email actions** | Brevo, Mailchimp, Gmail, SendGrid |
| **SMS actions** | Twilio, Plivo |
| **Logic** | Basic — if/then, filter, lookup |
| **Multi-step** | Yes — up to 3 steps on free |

**Best for:** Quick automation setup, non-technical users
**Key limitation:** Task-based pricing gets expensive. Survey submission (1 task) → write to Airtable (1 task) → find match (1 task) → send email (1 task) = 4 tasks per person. 500 respondents = 2,000 tasks = need $49/mo Professional plan.
**Setup time:** 1-2 hours for simple automations

---

### Option B: Make (formerly Integromat) — Core Plan
| Factor | Detail |
|--------|--------|
| **Cost** | $9/mo (10,000 operations/mo) |
| **Integrations** | 1,500+ apps |
| **Logic** | Visual canvas — routers, iterators, aggregators, filters |
| **Survey triggers** | Typeform, Tally, Google Forms, Jotform |
| **Email actions** | Brevo, Mailchimp, Gmail, SendGrid |
| **SMS actions** | Twilio, Plivo, MessageBird |
| **Error handling** | Built-in — retry on failure |
| **Data stores** | Built-in — store matching pairs |
| **Operations** | A 3-step scenario runs 1,000 times = 3,000 operations |

**Best for:** Complex logic (matching algorithm) and budget. 60% cheaper than Zapier at equivalent volumes.
**Key limitation:** Steeper learning curve (3-5 hours to full productivity)
**Setup time:** 3-4 hours for matching automation

---

### Option C: n8n (Self-hosted — FREE)
| Factor | Detail |
|--------|--------|
| **Cost** | $0 (server costs only) |
| **Platform** | Self-hosted on Railway ($5/mo server) or local |
| **Integrations** | 400+ native, HTTP node for anything else |
| **Logic** | Advanced — loops, conditional branches, custom JavaScript |
| **AI** | Native LangChain integration — could add AI matching |
| **Data ownership** | Full — all data on your server |
| **Deployment** | Docker, Railway, local |

**Best for:** Technical teams who want unlimited automation and full data control. Could run the entire matching system on n8n.
**Key limitation:** Requires DevOps knowledge. Not for non-technical users. Setup time longer.
**Setup time:** 4-6 hours

---

### Option D: Pabbly Connect (UNLIMITED — $19/mo starter)
| Factor | Detail |
|--------|--------|
| **Cost** | $19/mo flat — unlimited tasks, unlimited operations |
| **Integrations** | 200+ apps |
| **Logic** | Good — conditional, filters, iterations |
| **Email** | Brevo, Mailchimp, SendGrid, Gmail |
| **SMS** | Twilio, Plivo |

**Best for:** If Zapier's task limits are too constraining, Pabbly's flat model is better at $19/mo vs $49/mo for Professional.
**Key limitation:** Smaller integration library than Zapier/Make.

---

### RECOMMENDED for Automation: Make ($9/mo Core) or n8n (free self-hosted)

**For MVP (simple matching):** Make at $9/mo — 10K operations/mo covers 2,500 survey submissions at 4 ops each.

**For full control and no cost:** n8n self-hosted on Railway ($5/mo total). Runs all matching logic, writes to database, sends notifications. Requires technical setup.

**Jordan's rule:** "No n8n unless explicitly asked." → Use Make for this use case. It's visual, $9/mo, and handles the full matching automation.

---

## Category 7: Matching Logic / Algorithm

**What it does:** Takes survey responses, runs a matching algorithm, returns pairs.

### Option A: Google Sheets + Manual Scoring (FREE)
| Factor | Detail |
|--------|--------|
| **Cost** | $0 |
| **How it works** | Survey responses → Google Sheet → Human reviews and assigns matches |
| **Scale** | 50-100 people max before it becomes a full-time job |
| **Accuracy** | Human judgment — highest quality |
| **Automation** | None — manual matching |

**Best for:** MVP proof-of-concept with small attendee list
**Key limitation:** Doesn't scale. For 20K attendees, impossible.

---

### Option B: Simple Scoring Formula in Google Sheets (FREE)
| Factor | Detail |
|--------|--------|
| **Cost** | $0 |
| **How it works** | Each profile gets a "vector" — role score (0-3) + industry score (0-3) + goal alignment score (0-3). Match pairs with complementary scores. |
| **Scale** | Can handle thousands if formula is automated |
| **Accuracy** | Basic — works for role + industry matching, misses nuanced goals |
| **Automation** | Google Sheets formula → sorted automatically |

**Scoring approach:**
- Investor seeking founders → founders seeking investors = high match
- Same industry, different company = medium match
- Different industry, different role = low match
- Formula: `MATCH_SCORE = (role_complement × 3) + (industry_overlap × 2) + (goal_alignment × 4)`

**Best for:** Budget matching that actually scales
**Key limitation:** Doesn't capture text-based goal matching (what if someone wants to meet "AI founders for healthcare"?)

---

### Option C: Airtable + Make Automation (FREE TIER)
| Factor | Detail |
|--------|--------|
| **Cost** | $0 free (1,000 records, 2GB) |
| **How it works** | Survey → Airtable base (roles table + goals table) → Make runs scoring formula → outputs matched pairs |
| **Scale** | 1,000 records on free tier — covers first event |
| **Accuracy** | Basic scoring formula, Airtable views for filtering |
| **Automation** | Make triggers on new Airtable record, runs match finder |

**Airtable base structure:**
- Table 1: Survey Responses (name, role, industry, goal, email, phone)
- Table 2: Match Pairs (person_a, person_b, match_score, status)
- Table 3: Notification Log (sent_email?, sent_sms?, timestamp)

**Best for:** Full data tracking with matching — works for first event
**Key limitation:** Free tier 1,000 record limit. Need to upgrade or archive old events.

---

### Option D: OpenAI API — AI Matching (~$0.01 per match)
| Factor | Detail |
|--------|--------|
| **Cost** | $0.01-0.05 per match calculation via GPT-4o mini |
| **How it works** | Send 2 profiles to GPT-4o mini → ask "should these people meet? why?" → get match score + reasoning in natural language |
| **Scale** | For 500 attendees (125,000 pairs), $1,250 — too expensive |
| **Accuracy** | Best — understands nuanced goals and reasoning |
| **Better approach** | Use simple scoring first → only run AI matching on the "close calls" (score 5-8 out of 12) |

**Hybrid approach (recommended):**
1. Simple scoring filters all pairs → 80% clear matches/non-matches
2. AI scoring for the 20% ambiguous pairs → "Is this a good match?" → GPT-4o mini at ~$0.01 each
3. For 500 attendees: 125K pairs × 20% = 25K AI calls × $0.01 = **$250** for AI matching
4. Better: reduce pair count by pre-filtering by industry first → only cross-industry ambiguous pairs get AI review

**Best for:** High-value matching where the "why" matters (investors + founders)
**Key limitation:** Cost adds up fast at scale. Use sparingly.

---

### Option E: Mix of Simple Formula + Manual Review
| Factor | Detail |
|--------|--------|
| **Cost** | $0 |
| **How it works** | Algorithm assigns 80% of matches automatically. 20% (close calls) flagged for human review. Human reviewer assigns in 30 seconds each. |
| **Scale** | 500 attendees = 100 flagged for review = 50 minutes of human review |
| **Accuracy** | High — algorithm handles easy cases, human handles complex |
| **Automation** | Simple scoring automated, human review async |

**Best for:** Proof of quality without full automation cost
**Key limitation:** Requires someone to do the manual review during setup sprint

---

### RECOMMENDED for Matching: Airtable + Make (free tier) + Hybrid AI for edge cases

**Architecture:**
1. Survey responses land in Airtable automatically (via Make webhook)
2. Make runs a simple scoring formula against all new responses
3. Matches with high scores (9+/12) → auto-approve → trigger email/SMS notification
4. Matches with medium scores (5-8) → flag for review → human reviews in Airtable grid view
5. Low scores (<5) → no match (attendee may be too niche)

This gives us fully automated matching for the clear cases, with human quality control for the edge cases — all without any AI cost.

---

## Category 8: Domain Name

**What it does:** Gives Niah a branded web address for the after-party page.

### Options:

| Domain | Cost | Where |
|--------|------|-------|
| `niah.io` | ~$12-15/yr | Namecheap, Cloudflare Registrar |
| `niah.afterparty` | ~$10-15/yr | .afterparty is a real TLD now |
| `niah.events` | ~$12-15/yr | Namecheap |
| `match.niah.io` | Free | Subdomain of existing domain (if Jordan has one) |
| `southsummit.niah.io` | Free | Subdomain — quick and dirty |
| `getmatched.io` | ~$12/yr | Available, memorable |
| `networking.app` | ~$15/yr | Namecheap |

**Recommendation:** Use a free subdomain like `southsummit.niah.io` for now. Register `niah.io` or `getmatched.io` as the primary domain when budget allows. $12-15/yr is low priority cost.

---

## Category 9: Physical Materials (Print)

For on-site presence at La Nave — match cards, QR codes, branded signage.

| Item | Cost Estimate | Notes |
|------|--------------|-------|
| Match cards (100 printed) | €20-30 | A6 cards, double-sided, matte finish |
| QR code standees (5) | €30-40 | A4 standees with QR code to survey |
| Branded table banner | €40-50 | Roll-up banner, 80×200cm |
| Stickers (500) | €25-35 | Branded stickers with Niah logo |
| **Total** | **€115-155** | |
| **Budget option** | €30-50 | Just match cards + QR code on phone |

**Where:** Print in Madrid — look for "Imprenta online" or local print shops near La Nave. Canva Design (free) + local print = professional result at low cost.

---

## Full Tool Stack Recommendations — Three Tiers

### Tier 1: Minimum Viable (€57 total)
**For:** Just enough to prove the concept works with 2 weeks to set up

| Category | Tool | Cost |
|----------|------|------|
| Survey | Google Forms | €0 |
| Email | Brevo (free tier — 300/day) | €0 |
| SMS | Don't send SMS yet | €0 |
| Web hosting | GitHub Pages | €0 |
| Matching | Google Sheets manual | €0 |
| Domain | `southsummit.niah.io` (subdomain) | €0 |
| Print | Match cards only | €30 |
| **Total** | | **€30** |

**Limitation:** 300 emails/day limit — only works if South Summit attendee list is <5,000. Email-only (no SMS backup). Manual matching.

---

### Tier 2: Standard (€289 total)
**For:** Real event presence at South Summit after-party

| Category | Tool | Cost |
|----------|------|------|
| Survey | Tally Forms (free) | €0 |
| Email | Brevo Standard yearly (3 mo) | €45 |
| SMS | MessageBird (2K msgs) | €62 |
| Web hosting | Vercel (free) | €0 |
| Database | Airtable (free tier) | €0 |
| Automation | Make Core ($9/mo × 3) | €27 |
| Domain | `southsummit.niah.io` (subdomain) | €0 |
| Print | Match cards + QR standees + banner | €130 |
| **Total** | | **€264** |

**This is the production stack.** Covers all bases. Professional result.

---

### Tier 3: Premium (€450 total)
**For:** Full Niah experience, South Summit as case study

| Category | Tool | Cost |
|----------|------|------|
| Survey | Typeform Starter (yearly) | €75 (3 mo) |
| Email | Brevo Standard yearly | €45 |
| SMS | MessageBird (2K msgs) | €62 |
| Web hosting | Railway hobby | €15 |
| Database | Railway PostgreSQL | €0 (included) |
| Automation | Make Core | €27 |
| AI matching | GPT-4o mini (edge cases only) | €50 |
| Domain | `getmatched.io` yearly | €12 |
| Print | Full kit | €130 |
| **Total** | | **~€416** |

**For:** When Niah needs to impress South Summit and generate a real case study. Most professional presentation.

---

## What to Cron — Three Options

### Cron Option A: South Summit Lead Scout (Daily Research)

**What it does:** Monitors South Summit announcements for:
- New speaker additions (who just joined — warm outreach targets)
- Investor/VC announcements (LP Forum speakers, Deeptech Forum)
- Partnership/sponsorship opportunities
- Event logistics updates (venue changes, after-party details)
- Media/press registrations (who's covering the event)

**Schedule:** Daily at 8:00 AM (May 27 – June 5)
**Skill:** `last30days-research`

**Prompt:**
```
Search for South Summit Madrid 2026 news from the past 48 hours.

Look for:
1. New speaker announcements (name, title, company, topic)
2. New investor/VC added to LP Forum or Deeptech Forum
3. Sponsorship or partnership announcements
4. Changes to Social Summit after-party logistics (venue, time, capacity)
5. Media/press covering South Summit

Format each finding as:
- [Type] Name / Title / Org — Brief description + link

If nothing new found in 48h, report "No new South Summit announcements in the past 48 hours."

After each report, add to /Users/jordan/workspace/007-Axton/niah-south-summit-leads.md with date + finding.
```

**Tools needed:** Web search, file write, append to leads log

---

### Cron Option B: Niah Outreach Tracker (Weekly Sequence)

**What it does:** Weekly reminder + execution checkpoint for South Summit partnership outreach

**Schedule:** Every Monday at 9:00 AM (May 19 – June 9)
**Skill:** `notion` (or file-based tracking)

**Prompt:**
```
Check /Users/jordan/workspace/007-Axton/niah-south-summit-outreach-log.md

For each contact in the outreach log:
- If status = "Sent" and sent_date < 5 days ago → follow up
- If status = "No response" and sent_date < 3 days ago → send alternate template
- If status = "Confirmed" → log the commitment and next step

Generate a weekly outreach report:
1. Pending outreach (who we haven't contacted yet)
2. Awaiting response (sent but no reply)
3. Hot leads (replied, need follow-up)
4. Confirmed partnerships

If outreach log doesn't exist, create it with these contacts:
- partners@southsummit.io (partnership email — initial outreach)
- South Summit LinkedIn page (for DM outreach if email fails)

Use the email templates from /Users/jordan/workspace/007-Axton/niah-south-summit-proposal.md
```

**Tools needed:** File read/write, web search for contact updates

---

### Cron Option C: Pre-Event Launch Sprint (June 1-4)

**What it does:** Executes the full sequence — email campaign, matching, notifications

**Schedule:** Daily at 7:00 AM (June 1-4)
**Skill:** `last30days-research` + `make`

**Prompt:**
```
Read /Users/jordan/workspace/007-Axton/niah-south-summit-execution-log.md

Based on the date:
- June 1: Execute Email 1 (survey invite) to full South Summit list. Log sends.
- June 2: Execute Email 2 (reminder) to non-openers. Log sends.
- June 3: Execute Email 3 (final reminder). Run matching algorithm on all responses. Prepare match notification emails. Log completion.
- June 4: Send match notification emails (morning). Send SMS to matched pairs (MessageBird). On-site report (if Hermès is at La Nave).

Each day:
1. Report send count, open rate, survey completion rate
2. Flag any issues (email bounced, survey form not working, etc.)
3. Update execution log with final status
4. If completion rate <40% → alert Jordan immediately (South Summit may need to boost promotion)
```

**Tools needed:** Brevo API, MessageBird API, Airtable (matching), file write

---

### Cron Option D: All Three — Combined Weekly + Daily Research

**Structure:**
- Daily at 8:00 AM: South Summit research (news, announcements, leads)
- Monday at 9:00 AM: Outreach sequence review + execute outreach
- June 1-4 at 7:00 AM: Pre-event launch sprint

**This gives you:**
1. Always-current South Summit intelligence
2. Persistent outreach pressure (no follow-ups falling through)
3. Automated event execution once June 1 hits

---

## Decision: Which Cron to Create?

Tell me:
1. **Which tool stacks** you want to use from the three tiers above?
2. **Which cron options** (A/B/C/D) to create?
3. **What delivery format** — back to Telegram, or to a file in the repo?

I'll build the crons from there. All research is done — now it's an execution decision.