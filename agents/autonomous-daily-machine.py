#!/usr/bin/env python3
"""
AUTONOMOUS DAILY MACHINE
========================
Think → Criticize → Decide → Build → Deliver
No human required. Ever.

Run manually: python3 autonomous-daily-machine.py
Run on cron: fires at 9am, delivers to Telegram
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# ─────────────────────────────────────────────
# STATE — what we know, what we did
# ─────────────────────────────────────────────
STATE_FILE = Path("/Users/jordan/.hermes/cron/state/daily-machine-state.json")

def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {
        "day": 0,
        "last_run": None,
        "last_company": None,
        "calls_made": 0,
        "replies_received": 0,
        "what_worked": [],
        "what_failed": [],
        "called_companies": [],
        "today_focus": None
    }

def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))

# ─────────────────────────────────────────────
# THINKER — what do we see right now?
# ─────────────────────────────────────────────
def think(state):
    print("\n=== THINKER ===")
    day = state["day"] + 1
    print(f"Day {day} analysis:")
    print(f"  Calls made: {state['calls_made']}")
    print(f"  Replies received: {state['replies_received']}")
    print(f"  Last company: {state['last_company']}")
    print(f"  What worked: {state['what_worked']}")
    print(f"  What failed: {state['what_failed']}")
    
    if state["calls_made"] == 0:
        focus = "FIRST CALL — we need one conversation today. Any reply is a win."
    elif state["replies_received"] == 0:
        focus = "FOLLOW-UP mode — nobody replied. Need better opener or skip to next company."
    else:
        focus = "MOMENTUM — we got a reply! Follow up until close or die."
    
    state["today_focus"] = focus
    print(f"  FOCUS: {focus}")
    return state

# ─────────────────────────────────────────────
# CRITIC — what could go wrong?
# ─────────────────────────────────────────────
def criticize(state):
    print("\n=== CRITIC ===")
    concerns = []
    
    if state["calls_made"] >= 3 and state["replies_received"] == 0:
        concerns.append("⚠️ 3+ calls, zero replies — pitch is broken. Don't call another company until we fix the opener.")
        state["today_decision"] = "SKIP — fix pitch first"
    
    if state["replies_received"] > 0 and state["calls_made"] < 3:
        concerns.append("💡 We got a reply — don't switch companies. Follow up.")
    
    if not concerns:
        concerns.append("✅ No red flags. Execute.")
    
    print("  CONCERNS: " + " ".join(concerns))
    return state

# ─────────────────────────────────────────────
# DECIDER — what are we doing today?
# ─────────────────────────────────────────────
def decide(state):
    print("\n=== DECIDER ===")
    
    all_companies = ["INBRAIN", "BrainQ", "Saluda Medical", "Theranica", "Neuroelectrics", "SetPoint Medical", "Phantom Neuro", "brain.space", "Sychedelic", "Connectome Health"]
    called = state.get("called_companies", [])
    remaining = [c for c in all_companies if c not in called]
    
    if not remaining:
        remaining = all_companies
        state["called_companies"] = []
    
    today = remaining[0]
    state["today_company"] = today
    state["called_companies"] = state["called_companies"] + [today]
    print(f"  DECISION: Call {today} today ({len(state['called_companies'])}/{len(all_companies)} cycled)")
    return state

# ─────────────────────────────────────────────
# BUILDER — generate today's card
# ─────────────────────────────────────────────
def build(state):
    print("\n=== BUILDER ===")
    company = state["today_company"]
    
    data = {
        "INBRAIN": {
            "country": "Spain", "funding": "€50M Series B",
            "product": "AI-powered BCIs for spinal cord injury",
            "contact": "+34 625 411 406", "ceo": "Iñigo Cócola",
            "why_now": "Completes clinical study → entering commercial phase → needs US channel partners",
            "opener": "I saw INBRAIN's spinal cord trial completed — you're moving into commercial stage. I'm helping non-US medtech companies build US sales channels. Do you have 15 minutes?",
            "close": "Can I send you a one-pager on how we'd approach the US market together?"
        },
        "BrainQ": {
            "country": "Israel", "funding": "$40M Series B",
            "product": "AI BCI for post-stroke recovery",
            "contact": "+972 54 000 0000", "ceo": "Eyal Roter",
            "why_now": "FDA breakthrough designation — accelerating US entry 2025",
            "opener": "BrainQ got FDA breakthrough designation for post-stroke recovery. That's a US market signal I can't ignore. I'm building channel partnerships for non-US neuro companies. 15 minutes?",
            "close": "Want me to map out the US rehab hospital landscape for BrainQ?"
        },
        "Saluda Medical": {
            "country": "Australia", "funding": "$66M Series C",
            "product": "Closed-loop SCS for chronic pain",
            "contact": "+1 512 000 0000", "ceo": "John Parker",
            "why_now": "FDA approved Evoke SCS system — actively building US commercial team",
            "opener": "Saluda's Evoke got FDA approved — that's your US market entry. You're probably building a US sales force right now. I place people who know neuro modulation and US hospital systems. 15 minutes?",
            "close": "Should I send you a list of US pain management groups actively hiring?"
        },
        "Theranica": {
            "country": "Israel", "funding": "$45M Series B",
            "product": "Neuromodulation for migraine (Nerivio)",
            "contact": "+1 844 000 0000", "ceo": "Alon Ironi",
            "why_now": "Nerivio FDA cleared — scaling US commercial footprint 2025",
            "opener": "Theranica's Nerivio is FDA cleared and scaling in the US. You need people who understand US headache clinic networks. I place neuro sales talent. 15 minutes?",
            "close": "Want me to send you a short list of US headache specialists who've moved in the last 6 months?"
        },
        "Neuroelectrics": {
            "country": "Spain", "funding": "€14M Series A",
            "product": "tCS/EEG for epilepsy and depression",
            "contact": "+34 93 000 0000", "ceo": "Ana Aldea",
            "why_now": "Enobio + Starstim — moving from research to clinical US market",
            "opener": "Neuroelectrics is moving from research accounts to clinical sales in the US. That's a different motion than what you've been doing. I help neuro companies make that transition. 15 minutes?",
            "close": "Can I send you a one-pager on US epilepsy monitoring centers actively adopting new tech?"
        },
        "SetPoint Medical": {
            "country": "France/USA", "funding": "$60M Series C",
            "product": "Vagus nerve stimulation for rheumatoid arthritis",
            "contact": "+1 650 000 0000", "ceo": "John Morrey",
            "why_now": "Positive Phase 3 data — preparing for commercial launch, needs US sales infrastructure",
            "opener": "SetPoint's RA Phase 3 came back positive — you're heading to commercial launch. Building a US sales team from scratch takes time. I know the immunology sales landscape. 15 minutes?",
            "close": "Want me to identify the US rheumatology key opinion leaders who will drive adoption?"
        },
        "Phantom Neuro": {
            "country": "Germany/USA", "funding": "$19M Series A",
            "product": "Neural interface for prosthetics and robotics",
            "contact": "Ottobock partnership (US office)", "ceo": "(verify)",
            "why_now": "$19M Series A led by Ottobock — German ortho giant has US hospital + VA network. Phantom entering US prosthetics market via Ottobock channel.",
            "opener": "Phantom Neuro just raised $19M backed by Ottobock — that's a US distribution channel built in. You're entering the US prosthetics market. I place people who know US VA and hospital systems. 15 minutes?",
            "close": "Should I send you a list of US VA prosthetics centers actively adopting new technology?"
        },
        "brain.space": {
            "country": "Israel", "funding": "$11M Series A",
            "product": "Brain data platform for AI mental modeling",
            "contact": "(verify via website)", "ceo": "(verify)",
            "why_now": "Raised $11M Series A March 2025 to build brain data AI models. AI companies need brain data — US is the target market.",
            "opener": "brain.space raised $11M to build brain data AI models — that's a US market signal. AI companies are your potential partners. I'm helping Israeli neuro companies find US channel partners. 15 minutes?",
            "close": "Want me to map US AI companies that could use brain data as an AI input?"
        },
        "Sychedelic": {
            "country": "India", "funding": "$3.5M Seed",
            "product": "AI-powered neurotech wearable for mental wellness",
            "contact": "(verify via website)", "ceo": "(verify)",
            "why_now": "Raised $3.5M seed to scale neurotech wearables globally. US mental wellness market is 10x larger than India.",
            "opener": "Sychedelic just raised $3.5M to scale neurotech wearables globally. US mental wellness market is the prize. I help Indian companies find US distribution. 15 minutes?",
            "close": "Want me to send you US wellness retailers and digital health channels looking for neurotech products?"
        },
        "Connectome Health": {
            "country": "Switzerland", "funding": "$2M Pre-Seed",
            "product": "Real-time brain change tracking",
            "contact": "(verify via website)", "ceo": "(verify)",
            "why_now": "Zurich ETH spinout backed by Redstone VC. Early stage — track for Series A.",
            "opener": "Connectome Health raised $2M pre-seed from Redstone in Zurich. Real-time brain tracking — early stage but strong science. I help Swiss neuro companies find US academic partnerships. 15 minutes?",
            "close": "Want me to identify US universities doing active real-time brain mapping research?"
        }
    }.get(company, {})

    state["today_data"] = data
    card = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📞 TODAY'S CALL — DAY {state['day'] + 1}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏢 {company} · {data.get('country','?')} · {data.get('funding','?')}
📡 {data.get('product','?')}
⏰ {data.get('why_now','?')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📱 {data.get('contact','?')} · CEO: {data.get('ceo','?')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OPENER: "{data.get('opener','?')}"
CLOSE: "{data.get('close','?')}"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Goal: Get a reply. Any reply = win.
""".strip()
    
    state["today_card"] = card
    state["last_company"] = company
    state["last_run"] = datetime.now().isoformat()
    state["day"] += 1
    print(f"  Built card for {company}")
    return state

# ─────────────────────────────────────────────
# DELIVER — save output
# ─────────────────────────────────────────────
def deliver(state):
    print("\n=== DELIVER ===")
    output_file = Path("/Users/jordan/.hermes/cron/output/today-deal.txt")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(state["today_card"])
    print(f"  Saved → {output_file}")
    print("\n" + state["today_card"])
    return state

# ─────────────────────────────────────────────
# MAIN LOOP
# ─────────────────────────────────────────────
def run():
    print("AUTONOMOUS DAILY MACHINE starting...")
    print(f"Timestamp: {datetime.now().isoformat()}\n")
    
    state = load_state()
    state = think(state)
    state = criticize(state)
    
    if state.get("today_decision") == "SKIP":
        print("\n=== DECIDER → SKIP ===")
        print("  Pitch broken. Not calling today. Need human review.")
        state["today_card"] = "⏸️ SKIPPED — pitch needs fix. Check what_worked/what_failed in state file."
        deliver(state)
    else:
        state = decide(state)
        state = build(state)
        state = deliver(state)
    
    save_state(state)
    print("\n=== RUN COMPLETE ===")
    return state

if __name__ == "__main__":
    run()