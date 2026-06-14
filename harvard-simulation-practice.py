#!/usr/bin/env python3
"""
Harvard GSCM Simulation — Self-Scoring Practice Quiz
Prints all questions first, then all answers at the end.
Run once, read, check yourself.
"""

import random
import os

random.seed()  # Change seed each run for fresh numbers

SUPPLIERS = [
    {"name": "FarFarAway",   "cost": 10, "lead": 4},
    {"name": "Far Away",     "cost": 15, "lead": 2},
    {"name": "PrettyClose",  "cost": 20, "lead": 1},
    {"name": "Very Fast",    "cost": 25, "lead": 0.5},
]
DESIGNS = [
    {"id": "A1", "model": "A", "option": "Basic",    "cost_add": 0,  "qual_add": 0},
    {"id": "A2", "model": "A", "option": "Standard", "cost_add": 25, "qual_add": 2},
    {"id": "A3", "model": "A", "option": "Premium",  "cost_add": 50, "qual_add": 5},
    {"id": "A4", "model": "A", "option": "Deluxe",   "cost_add": 75, "qual_add": 8},
    {"id": "B1", "model": "B", "option": "Basic",    "cost_add": 0,  "qual_add": 0},
    {"id": "B2", "model": "B", "option": "Standard", "cost_add": 30, "qual_add": 3},
    {"id": "B3", "model": "B", "option": "Premium",  "cost_add": 60, "qual_add": 6},
    {"id": "B4", "model": "B", "option": "Deluxe",   "cost_add": 90, "qual_add": 9},
]
FORECASTER_NAMES = ["Andrei", "Aya", "Claire", "Lorenzo", "Byron", "Ruth"]
BOARD_PREFS = {
    "Mia":    "Flexible capacity — keep slack for surprises",
    "Ankit":  "Low variance — prefers steady, predictable orders",
    "Carla":  "Use mathematical average NOT consensus feeling",
    "Matheo": "Cost efficiency — minimize total supply chain cost",
    "Adele":  "Early Model B flexibility — start production early",
}
BOARD_SHUFFLED = list(BOARD_PREFS.items())
random.shuffle(BOARD_SHUFFLED)


# ─────────────────────────────────────────────────────────────────────────────
# ROOM 1 — DESIGN ROOM
# ─────────────────────────────────────────────────────────────────────────────
def room1():
    print("\n" + "═"*60)
    print("ROOM 1 — DESIGN ROOM")
    print("═"*60)

    model = random.choice(["A", "B"])
    price = 245 if model == "A" else 285
    base_cost = 175 if model == "A" else 195

    model_opts = [d for d in DESIGNS if d["model"] == model]
    random.shuffle(model_opts)

    rows = []
    for opt in model_opts:
        total_cost = base_cost + opt["cost_add"]
        profit = price - total_cost
        margin = profit / price * 100
        rows.append({
            "id": opt["id"],
            "option": opt["option"],
            "cost_add": opt["cost_add"],
            "total_cost": total_cost,
            "profit": profit,
            "margin": margin,
        })

    best = max(rows, key=lambda x: x["profit"])

    print(f"\nModel {model} | Price: ${price} | Base Cost: ${base_cost}")
    print()
    print(f"  {'ID':<5} {'Option':<12} {'+Cost':>6} {'Total':>8} {'Profit':>8} {'Margin':>8}")
    print(f"  {'-'*5} {'-'*12} {'-'*6} {'-'*8} {'-'*8} {'-'*8}")
    for r in rows:
        star = " ◄ BEST" if r["id"] == best["id"] else ""
        print(f"  {r['id']:<5} {r['option']:<12} +${r['cost_add']:>4}  ${r['total_cost']:>6}  ${r['profit']:>6}  {r['margin']:>6.1f}%{star}")

    print(f"\nQ1: Which design option has the HIGHEST profit/unit for Model {model}?")
    print(f"    Write the ID (e.g. A2, B3)")
    print()
    print("  ANSWER:", best["id"], f"({best['option']}) — Profit ${best['profit']}/unit")
    return best["id"]


# ─────────────────────────────────────────────────────────────────────────────
# ROOM 2 — FORECASTING ROOM
# ─────────────────────────────────────────────────────────────────────────────
def room2():
    print("\n" + "═"*60)
    print("ROOM 2 — FORECASTING ROOM")
    print("═"*60)

    base = random.randint(40, 80)
    estimates = []
    for name in FORECASTER_NAMES:
        val = max(10, base + random.randint(-15, 15))
        estimates.append((name, val))

    consensus = sum(v for _, v in estimates) // len(estimates)
    total = consensus * 8

    print("Six forecasters give you these estimates:")
    for name, val in estimates:
        print(f"  {name:<10} → {val:>4} units")
    print(f"  {'-'*30}")
    print(f"  Consensus (average of 6): {consensus}")
    print(f"  Sales window: 8 months (May–December)")

    print(f"\nQ1: What is the consensus forecast? (average of 6)")
    print("  ANSWER:", consensus)

    print(f"\nQ2: Sales window is 8 months. What is TOTAL demand?")
    print(f"  ANSWER: {consensus} × 8 = {total}")
    return consensus, total


# ─────────────────────────────────────────────────────────────────────────────
# ROOM 3 — PRODUCTION ROOM
# ─────────────────────────────────────────────────────────────────────────────
def room3():
    print("\n" + "═"*60)
    print("ROOM 3 — PRODUCTION ROOM")
    print("═"*60)

    print("Rules:")
    print("  Model A → cheapest supplier (price/cost sensitive)")
    print("  Model B → fastest supplier (lead time sensitive)")
    print()
    print(f"  {'Supplier':<14} {'Cost/Unit':>10} {'Lead Time':>10}")
    print(f"  {'-'*14} {'-'*10} {'-'*10}")
    for s in SUPPLIERS:
        print(f"  {s['name']:<14} ${s['cost']:>8}/unit {s['lead']:>8} weeks")

    cheapest = min(SUPPLIERS, key=lambda x: x["cost"])
    fastest  = min(SUPPLIERS, key=lambda x: x["lead"])

    print(f"\nQ1: Model A is cost-sensitive. Which supplier?")
    print(f"  ANSWER: {cheapest['name']} (${cheapest['cost']}/unit, cheapest)")

    print(f"\nQ2: Model B needs speed for demand spikes. Which supplier?")
    print(f"  ANSWER: {fastest['name']} ({fastest['lead']}-week lead, fastest)")
    return cheapest["name"], fastest["name"]


# ─────────────────────────────────────────────────────────────────────────────
# ROOM 4 — BOARDROOM
# ─────────────────────────────────────────────────────────────────────────────
def room4():
    print("\n" + "═"*60)
    print("ROOM 4 — BOARDROOM")
    print("═"*60)
    print("Match each board member to their priority:")
    print()

    for name, pref in BOARD_SHUFFLED:
        print(f"  {name}: {pref}")

    print("\nANSWERS (in order shown above):")
    for name, pref in BOARD_SHUFFLED:
        print(f"  {name} → {pref}")

    # Also show in fixed order for memorization
    print("\n Memorize this order:")
    for name in BOARD_PREFS:
        print(f"  {name} → {BOARD_PREFS[name]}")


# ─────────────────────────────────────────────────────────────────────────────
# NEWSVENDOR
# ─────────────────────────────────────────────────────────────────────────────
def newsvendor():
    print("\n" + "═"*60)
    print("BONUS — NEWSVENDOR (decides how much to produce for Model B)")
    print("═"*60)
    price = 285
    cost  = 195
    cu = price - cost   # underage = missed sale = price - cost
    co = cost          # overage = cost of making unsold unit
    # cu = $90, co = $195. Co > Cu → UNDERPRODUCE

    print(f"Model B | Price: ${price} | Cost: ${cost}")
    print(f"  Underage cost (Cu) = Price − Cost = ${price} − ${cost} = ${cu}")
    print(f"  Overage cost (Co)  = Cost = ${co}")
    print(f"  Rule: If Co > Cu → UNDERPRODUCE (risk of overstock is worse)")
    print(f"        If Cu > Co → OVERPRODUCE (risk of stockout is worse)")
    print()
    print(f"  Since Co (${co}) > Cu (${cu}) → UNDERPRODUCE")
    print(f"  You order LESS than forecast to avoid costly excess inventory.")
    print()
    print("Q: Should you overproduce or underproduce Model B?")
    print("  ANSWER: UNDERPRODUCE")


# ─────────────────────────────────────────────────────────────────────────────
# SUPPLIER DECISION TABLE
# ─────────────────────────────────────────────────────────────────────────────
def supplier_table():
    print("\n" + "═"*60)
    print("SUPPLIER DECISION — QUICK REFERENCE")
    print("═"*60)
    print(f"  {'Model':<10} {'Priority':<20} {'Best Supplier':<15} {'Why':<20}")
    print(f"  {'-'*10} {'-'*20} {'-'*15} {'-'*20}")
    print(f"  {'Model A':<10} {'Cheapest':<20} {'FarFarAway':<15} {'$10/unit, 4wk':<20}")
    print(f"  {'Model B':<10} {'Fastest':<20} {'Very Fast':<15} {'0.5wk lead':<20}")
    print()
    print(f"  NEVER pick 'Far Away' or 'PrettyClose' for either model.")


# ─────────────────────────────────────────────────────────────────────────────
# MATH CHEAT SHEET
# ─────────────────────────────────────────────────────────────────────────────
def math_sheet():
    print("\n" + "═"*60)
    print("MATH CHEAT SHEET — 3 calculations you need")
    print("═"*60)
    print()
    print("1. PROFIT PER UNIT")
    print("   Profit = Price − Total Cost")
    print("   Total Cost = Base Cost + Design Add-on Cost")
    print()
    print("2. MARGIN %")
    print("   Margin% = (Profit / Price) × 100")
    print()
    print("3. TOTAL DEMAND")
    print("   Total Demand = Consensus Forecast × 8")
    print("   (8-month sales window: May–December)")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────
def main():
    os.system('clear')
    print("="*60)
    print("HARVARD GSCM — PRACTICE QUIZ")
    print("="*60)
    print("Write your answer DOWN FIRST, then check the ANSWER.")
    print("Study all 4 rooms + Newsvendor + Math + Suppliers.")
    print("Run it again for fresh random numbers.")
    print()

    room1()
    room2()
    room3()
    supplier_table()
    room4()
    newsvendor()
    math_sheet()

    print("\n" + "="*60)
    print("Run again for new numbers: python3 harvard-simulation-practice.py")
    print("="*60)


if __name__ == "__main__":
    main()