# Neurotech / Neuromatch — Workspace

Job market intelligence and funding tracker for neurotech companies. Used for career research and market monitoring.

---

## What This Workspace Does

- Track 80+ neurotech companies across BCI, Neuromodulation, NeuroAI, Wearables, NeuroTech-Therapy
- Monitor funding rounds and valuations
- Flag companies actively hiring
- Daily automated research + weekly summary

---

## Key Data

- **Total tracked funding:** $4.8B (2025)
- **2026 deals:** Neuralink ($650M Series E), Cognito Therapeutics ($105M)
- **Top valuations:** Neuralink ($9B), Paradromics ($500M)
- **Categories:** BCI, Neuromodulation, NeuroAI, Wearables, NeuroTech-Therapy

---

## Key Files

| File | What |
|---|---|
| `dashboards/neurotech-dashboard.html` | Main tracker — all companies, funding, hiring |
| `research/funding/` | Raw research, funding data |

---

## Cron Jobs Attached

- `b02c73ebc139` — Daily Neurotech Research (8am)
- `0030ecbdc269` — Daily Dashboard Refresh (10am)
- `e6a5b17c7dbb` — Weekly Update (Monday 9am)

---

## Hiring Signals

Companies flagged as actively recruiting:
- Inbrain Neuroelectronics
- Neuralink
- Phantom Neuro
- (More in dashboard)

---

## Naming Convention

```
Dashboard:   neurotech-dashboard.html (always in place)
Research:    neurotech-{date}-{topic}.md
Updates:     neurotech-weekly-{date}.md
```

---

## Blocker

- Git not initialized in `007-Axton/` — dashboard updates not auto-pushed to GitHub Pages
