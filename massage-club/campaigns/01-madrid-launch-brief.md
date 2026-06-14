# Massage Pass — Madrid Launch Brief
**Version:** 1.0 | **Date:** May 11, 2026 | **Status:** Pre-launch

---

## What This Actually Is

Massage Pass is a two-sided marketplace:
- **Supply side:** Massage therapists and studios in Madrid — they have available slots, need clients
- **Demand side:** People in Madrid who want a massage and don't have a regular place

The product is simple: a booking page where clients pick a time, therapists get notified, you take a cut. Like Resy for massages. The tech is already built (Lovable → Vercel + Supabase). What's missing is the launch — getting the first 5 studios and 10 clients to make it worth everyone's while.

**The core tension:** You need both sides simultaneously. Studios won't join if there are no clients. Clients won't use it if there are no studios near them. Classic chicken-and-egg. The solution is geography-locked micro-launch: one neighborhood, tight radius, enough supply that demand has real options.

---

## The Micro-Launch Model (Week 1–3)

### Goal: 5 studios + 10 clients in Chamberí or Salamanca (one neighborhood)

**Why one neighborhood first:**
- If studios are 30 min apart, neither gets enough bookings to care
- If studios are 10 min apart and all in Chamberí, a client booking in Chamberí has real options
- Density makes the product work before the network effect does

**The offer to studios:**
- Free to list first month
- 0% commission on first 5 bookings (try it risk-free)
- After month 1: 15% commission on bookings you bring
- You handle your own scheduling — we just send you clients

**The offer to clients:**
- First massage: [X]% off or free first session with package purchase
- Package: 4 sessions for the price of 3 (puts money in your pocket upfront)
- No subscription required — pay per session or buy a package

---

## What to Do This Week (Action Items)

### Day 1–2: Warm Outreach to Studios
You're already scraping FB groups for therapists complaining about no clients. Those ARE your targets.

**Message template (Spanish, warm/DM):**
```
Hola [name], vi tu mensaje en [group] — estoy construyendo una plataforma para masajistas en Madrid y busco therapists pioneros para probarla gratis el primer mes.

Básicamente: te enviamos clientes nuevos, tú sigues con tu calendario como siempre. Sin comisión el primer mes.

¿Te animas a 5 minutos para contarte cómo funciona?
```

**Where to find them:**
- Facebook groups: "Masajistas España", "Autónomos Belleza Madrid", "Esteticistas Madrid"
- The cron job (`1bdcb5a0900e`) is already scraping these — check the leads it finds
- Physical walk-ins: walk into studios near Chamberí/Salamanca, introduce yourself

**Target studios:**
- Solo therapists with their own practice, not chains
- Studios with 1–3 therapists max
- 4+ star rating on Google Maps
- Near a Metro stop (Convenio, Rubén Darío, Goya — whatever neighborhood you pick)

### Day 3–4: Build the Landing Page Waitlist
You don't need the full booking flow working to start collecting demand.

**Landing page (simple):**
- Headline: "Masajes en Madrid — sin contrato, sin permanencia"
- Sub: "Reserva tu próxima sesión en 30 segundos. Therapeutas verificados cerca de ti."
- CTA: "Apúntame a la lista" → email capture
- Share in the same FB groups you're already scraping

**Why this first:** You need demand waiting before you ask studios to commit. A list of 10 interested clients makes the studio pitch 10x easier.

### Day 5: First Studio Onboardings
- Send onboarding link
- Ask them to fill in: services offered, pricing, availability, Metro proximity
- Set up their Supabase profile manually if needed (the backend is there, just not configured for self-serve yet)

### Day 7+: First Bookings
- DM the waitlist: "We have 3 studios near you — ready to book?"
- Be the concierge. Book the first few appointments manually if you have to.
- The goal isn't automation yet — it's proof that the transaction works end to end.

---

## The Participation Pointers

### "I don't know if anyone will want this"
**Evidence that it will:** The cron job finds posts in Spanish FB groups DAILY from masajistas complaining about no clients. That's supply-side pain. On the demand side: people search "masaje Madrid" constantly — Google Maps is full of 4-star studios with waitlists. You're not creating a market. You're connecting two people who are already looking for each other and failing to find each other efficiently.

**Your first data point:** If you can get 5 studios and 10 clients in one neighborhood to all have working experiences — that's your case study. That's what you show the next 5 studios.

### "I can't compete with Booksy"
**You shouldn't try.** Booksy is for established studios with full calendars. Your target is the solo therapist in Chamberí who just moved their practice online and has 4 empty slots a week. Booksy charges them €29/month. You're offering: free first month, then 15% per booking only. That's fundamentally different pricing for a fundamentally different customer.

### "I need to automate this"
**You don't. Not yet.** The first bookings should happen with you in the loop — DMing studios, texting clients, making sure nobody's confused. This is your QA phase. Automate after you've personally resolved 10 broken handoffs and know what breaks. That's when you know what to automate.

### "What if the tech doesn't work?"
**Fix it first.** The Vercel app has a 404 blocker on sub-pages (missing `vercel.json`). Fix that before you drive any traffic there. If someone clicks your link and gets a 404, they're gone.

---

## The Numbers to Track

| Metric | Week 1 Target | Week 4 Target |
|---|---|---|
| Studios listed | 3 | 5 |
| Clients booked | 3 | 10 |
| Revenue (take rate) | €0 | €15–30 |
| FB posts made | 5 | 15 |
| Waitlist signups | 10 | 50 |

---

## What's In This Folder

| File | Purpose |
|---|---|
| `campaigns/01-madrid-launch-brief.md` | This document — full launch plan |
| `drafts/outreach-templates.md` | Spanish outreach messages for studios + clients |
| `drafts/landing-page-copy.md` | Landing page headline/sub/CTA variants |
| `data/madrid-neighborhoods.md` | Chamberí + Salamanca — why these, metro map, studio density |
| `data/competitor-analysis.md` | Booksy, Treatwell, Fulero — positioning gaps |

---

## Current Blockers (Fix These First)

1. **Vercel 404 on sub-pages** — `vercel.json` missing SPA rewrite rules. Without this, `/partner` and `/book` return 404.
2. **Domain not configured** — `massageclub.io` on Squarespace, DNS not pointed to Vercel yet
3. **Supabase service_role key** — not in Hermes env, booking monitor skill can't run
4. **Lovvable → Vercel sync** — need to make sure Supabase backend actually connects to the frontend

---

## What Success Looks Like

Week 4, you have:
- 5 studios with active profiles
- 10 clients who have booked at least once
- 2–3 repeat bookings (clients who came back without you prompting)
- At least 1 studio asking: "Can I add another therapist from my studio?"

That's the signal. When a studio wants to add more of their people to the platform — that's when you know you've hit product-market fit in that micro-market.
