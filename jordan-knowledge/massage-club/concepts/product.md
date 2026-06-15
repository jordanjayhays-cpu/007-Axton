---
type: product
title: Massage Club — Product
tags: [massage-club, product, core]
timestamp: 2026-06-15
---

# Massage Club — Product

## What It Does

Subscription massage booking platform for Madrid. "Uber for massage" — open, tap, done.

**Tagline:** "Open, tap, done. No manual last-mile."

## Pain Point

Current massage booking is "like emailing a taxi to pick you up." Manual back-and-forth, scheduling friction, no instant booking.

## Target

- **Customers:** Spanish speakers in Madrid, urban professionals
- **Therapists:** Independent massage therapists onboarded as partners
- **Neighborhood-first:** Chamberí first, then expand

## Model

- Subscription / membership
- On-demand booking via web app
- Therapists receive bookings via the platform

## Current Status

- **Live URL:** https://your-massage-pass-2rmjyzjtr-jordanjayhays-cpus-projects.vercel.app
- **Domain:** massageclub.io (SqualSquarespace, DNS not configured)
- **Stack:** Vercel + Supabase + Lovable
- **Repo:** jordanjayhays-cpu/your-massage-pass

## Blocker

- `vercel.json` missing SPA rewrite rules — `/partner` and sub-pages return 404
- Supabase service_role key not in Hermes secrets
- Domain DNS not pointed to Vercel

## Launch Status

- Micro-launch model: 5 studios + 10 customers in Chamberí first
- Lead gen via FB groups/forums (Spanish outreach)
- Cron job `1bdcb5a0900e` runs daily 9am for lead scouting

## Competitors

- Booksy, Treatwell, Fulero — positioning gaps around subscription + instant booking

## Process

1. Scout leads (cron or manual)
2. Write outreach copy (humanizer skill)
3. Push to FB groups/forums
4. Track bookings via Supabase
