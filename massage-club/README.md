# Massage Club — Workspace

Subscription massage booking platform for Madrid. Massages booked through a web app, therapists onboarded as partners.

---

## Launch Brief (Start Here)

**`campaigns/01-madrid-launch-brief.md`** — Full launch plan, micro-launch model, week-by-week actions

---

## What This Workspace Does

- Campaign management (Madrid launch)
- Partner onboarding flow
- Lead generation (Madrid studios via FB groups/forums)
- Copy drafts and templates

## Active Campaign

**Madrid Launch** (May 2026)
- Target: Spanish speakers in Madrid FB groups/forums
- Goal: 5 studios + 10 customers in one neighborhood first (Chamberí)
- Strategy: Niche-first, then expand

## Key Files

| File | What |
|---|---|
| `campaigns/01-madrid-launch-brief.md` | Full launch plan — read this first |
| `drafts/outreach-templates.md` | Spanish outreach messages for studios + clients |
| `drafts/landing-page-copy.md` | Landing page headline/sub/CTA variants |
| `data/competitor-analysis.md` | Booksy, Treatwell, Fulero — positioning gaps |
| `data/madrid-neighborhoods.md` | Chamberí + Salamanca — neighborhood selection logic |
| `data/madrid_leads.csv` | Scraped studios (name, address, phone, rating) |

---

## Tech Stack
- **Frontend:** Vercel (`https://your-massage-pass-2rmjyzjtr-jordanjayhays-cpus-projects.vercel.app`)
- **Backend:** Supabase (project: `jglftdstrowwckwqmpue`)
- **Code:** Lovable (`https://lovable.dev/projects/13ab3b1d-1034-4ac7-b40c-8e51807e553c`)
- **Repo:** `jordanjayhays-cpu/your-massage-pass`
- **Domain:** `massageclub.io` (Squarespace, DNS not yet configured)

---

## Cron Jobs Attached
- `1bdcb5a0900e` — Madrid Massage Leads scout (daily 9am)

---

## Current Blockers
1. `vercel.json` missing SPA rewrite rules → `/partner` and sub-pages return 404
2. Supabase service_role key not yet in Hermes env
3. Domain DNS not pointed to Vercel

## Naming Convention

```
Campaign:    {date}-madrid-launch-{type}.md
Draft:       massage-club-{description}-draft-v{N}.md
Final:       {date}-massage-club-{description}-final.md
```

---

## Process
1. Scout leads (cron or manual)
2. Write outreach copy (humanizer skill)
3. Push to FB groups/forums
4. Track bookings via Supabase
5. Monitor with `supabase_booking_monitor` skill
