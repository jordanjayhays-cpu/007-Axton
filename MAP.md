# 007-Axton — Project Map

**Read this first.** Every session, I start here.

---

## Active Projects

| Project | What | Status |
|---|---|---|
| **Massage Club** | Subscription massage booking, Madrid launch | Active |
| **Niah** | B2B event networking, Madrid + South Summit 2026 | Active |
| **Neurotech / Neuromatch** | Job market intelligence dashboard | Active |
| **Master Dashboard** | Central hub linking all sub-dashboards | Active |
| **PISCO** | Staffing outreach pipeline | Pending action |
| **MBA / IMBA** | Business school tracking | Ongoing |

---

## Folder Structure (Clean)

```
007-Axton/
├── MAP.md
│
├── massage-club/
│   └── README.md
│
├── niah/
│   ├── README.md
│   ├── dashboards/
│   │   └── niah-dashboard.html
│   └── south-summit/
│       ├── niah-south-summit-n8n-workflow.json
│       ├── niah-south-summit-proposal.md
│       ├── niah-south-summit-setup-guide.md
│       └── niah-south-summit-tool-research.md
│
├── neurotech/
│   ├── README.md
│   └── dashboards/
│       └── neurotech-dashboard.html
│
├── master-dashboard/
│   └── master-dashboard.html
│
├── picos/
│   └── README.md
│
└── mba/
    └── README.md
```



## Naming Conventions

```
Drafts:      {project}-{description}-draft-v{N}.md
Final:       {date}-{project}-{description}-final.md
Campaigns:   {date}-{campaign-name}.md
Data exports: {date}-{source}-{type}.csv
```

---

## Active Now

### Massage Club
- **Focus:** Madrid launch — partner onboarding + lead gen via FB groups/forums
- **Cron:** Madrid Massage Leads scout runs daily 9am (job_id: `1bdcb5a0900e`)
- **Stack:** Vercel (frontend) + Supabase (backend) + Lovable (code)
- **Live URL:** `https://your-massage-pass-2rmjyzjtr-jordanjayhays-cpus-projects.vercel.app`
- **Domain:** `massageclub.io` (Squarespace, not yet pointed to Vercel)
- **Blocker:** SPA routing (`vercel.json` missing rewrite rules for sub-pages)

### Niah
- **Focus:** South Summit June 2026 — sponsor/outreach prep
- **Tools:** Tally (survey), Mailchimp (email), Squarespace (web), Zapier (automation)
- **Key contact:** Agustin Torres (CloserStill Spain MD)
- **Stack:** Manual Phase 1 first, automation after live
- **Blocker:** Mailchimp SMS doesn't work in Spain (US/Canada only)

### Neurotech / Neuromatch
- **Focus:** Job market intelligence — 80+ companies tracked, $4.8B funding
- **Cron:** Daily research 8am (job_id: `b02c73ebc139`) + Dashboard refresh 10am + Weekly Mon 9am
- **Key cos:** Neuralink ($9B), Paradromics ($500M), Inbrain Neuroelectronics (hiring)
- **Blocker:** Git not initialized — dashboard updates not auto-pushed

### PISCO
- **Focus:** Staffing outreach
- **Pending:** Rachel King (Spire Healthcare), Victor Presa (Meliá Hotels)
- **Dashboard:** `PROJECTS/analytics/analytics.html`

---

## Cron Jobs

| Job | Schedule | Project |
|---|---|---|
| `1bdcb5a0900e` — Madrid Massage Leads | Daily 9am | Massage Club |
| `b02c73ebc139` — Neurotech Research | Daily 8am | Neurotech |
| `0030ecbdc269` — Neurotech Dashboard Refresh | Daily 10am | Neurotech |
| `e6a5b17c7dbb` — Neurotech Weekly Update | Mon 9am | Neurotech |

---

## Blockers — Action Needed

| Blocker | Impact |
|---|---|
| Vercel API token | Massage Club deployment |
| Notion API key | CRM + MBA tracking |
| Supabase service_role key | Booking monitor |
| `vercel.json` SPA fix | Massage Club sub-pages 404 |
| Git init for 007-Axton | Dashboard auto-push |

---

## How to Work With Me

1. Tell me which project you're in → I load that workspace's README
2. I read MAP.md first every session
3. I follow naming conventions — files I create follow the pattern above
4. For dashboards, I sync to `/Users/jordan/workspace/007-Axton/` then send you the link via Telegram

---

## Skills I Have Loaded

- `massage-pass` — Massage Club product context
- `niah` — Niah event networking context
- `supabase_booking_monitor` — Polls Supabase bookings
- `last30days-research` — Multi-source research pipeline
- `powerpoint` — Deck creation
- `humanizer` — Strip AI voice from copy

---

*Last updated: 2026-05-11*
