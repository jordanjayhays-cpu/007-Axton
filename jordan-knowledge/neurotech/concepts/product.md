---
type: research
title: Neurotech — Product
tags: [neurotech, product, core]
timestamp: 2026-06-15
---

# Neurotech / Neuromatch — Product

## What It Is

Job market intelligence and funding tracker for neurotech companies. Used for career research and market monitoring.

## What Jordan Uses It For

- Track 80+ neurotech companies across: BCI, Neuromodulation, NeuroAI, Wearables, NeuroTech-Therapy
- Monitor funding rounds and valuations
- Flag companies actively hiring
- Daily automated research + weekly summary

## Key Data Points

- **Total tracked funding:** $4.8B (2025)
- **2026 deals:** Neuralink ($650M Series E), Cognito Therapeutics ($105M)
- **Top valuations:** Neuralink ($9B), Paradromics ($500M)
- **Categories tracked:** BCI, Neuromodulation, NeuroAI, Wearables, NeuroTech-Therapy

## Hiring Signals (Active)

- Inbrain Neuroelectronics
- Neuralink
- Phantom Neuro

## Dashboard

- Live dashboard: neurotech-dashboard.html
- 80+ companies tracked with funding, category, hiring status

## Cron Jobs

- `b02c73ebc139` — Daily Neurotech Research (8am)
- `0030ecbdc269` — Daily Dashboard Refresh (10am)
- `e6a5b17c7dbb` — Weekly Update (Monday 9am)

## Blocker

- Git not initialized in `007-Axton/` — dashboard updates not auto-pushed to GitHub Pages
