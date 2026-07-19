---
title: Butterfly Spread
type: strategy
status: learning
tags: [options, derivatives, strategy/income, market/thailand]
---

# Butterfly Spread

**Pin-target income strategy.** Three strikes, ratio 1-2-1: buy 1 lower, sell 2
middle, buy 1 higher (same type, same expiry). Maximum profit if price lands at
the middle strike; defined risk (= the debit paid).

## Overview
A cheap, defined-risk way to bet that price finishes **near a specific level**
at expiry. Low cost because the two short middle calls fund the wings. The
"body-and-wings" structure shared with [[Iron Butterfly]], but built from one
option type instead of a straddle + wings.

## Legs (long call butterfly)

| Leg | Action | Type | Strike | Qty | Expiry |
|-----|--------|------|--------|-----|--------|
| 1 | Long | Call | Lower (wing) | 1 | Same |
| 2 | Short | Call | Middle (body) | 2 | Same |
| 3 | Long | Call | Higher (wing) | 1 | Same |

> Put butterflies are the mirror (same payoff shape, built from puts).

## Max profit
**(Middle strike − Lower strike) − Net debit paid** (× multiplier).
- Capped: yes — realised only at the middle strike.

## Max loss
**Net debit paid** (× multiplier).
- Capped: yes — both wings expire worthless at the tails.

## Breakeven
**Two breakevens**: **Lower strike + Debit** and **Higher strike − Debit**.

## Greeks behavior
- **Delta**: ~0 at entry (centered); tilts as spot moves off the body.
- **Gamma**: **positive at the body** (delta grows into the pin) — useful into a
  forecast level; negative at the wings.
- **Theta**: **positive near the body** (short 2 legs decay faster) — time helps
  if price sits at the middle.
- **Vega**: **short (negative)** overall — you want IV to fall.

## Payoff shape (at expiry)
```
P&L
 │       /\
 │      /  \              ← max profit at middle strike
 │     /    \
 ├───/────────\──────
   Lower    Higher
   (breakevens: Lower+debit ... Higher−debit)
```

## When to use
- Forecast a **specific expiry level** (e.g. SET50 gravitating to a round number).
- Want cheap, defined-risk exposure to a pin (vs the higher-credit iron fly).
- High IV you expect to settle lower.

## Risks
- **Narrow profit window** — must be near the middle strike at expiry.
- **Liquidity** — 3-leg structure; fill risk on all legs.
- **Gamma at wings** — delta moves against you if price overshoots the body.
- **IV** — a vega pop hurts the position before theta rescues it.

## Example — SET50 / TFEX
- SET50 at 1,300; forecast pin near 1,300 over 21 days.
- Buy 1× call 1,250, sell 2× calls 1,300, buy 1× call 1,350. Net debit ฿15.
- Wing/body width = ฿50.
- **Max profit**: 50 − 15 = ฿35 (settles at 1,300).
- **Max loss**: ฿15 (the debit).
- **Breakevens**: 1,250 + 15 = **1,265** / 1,350 − 15 = **1,335**.

## Related
- [[Iron Butterfly]] (straddle-body version) · [[Iron Condor]] ·
  [[Vertical Spread]] (the building block of each wing) · [[Options Chain]] ·
  [[Greeks]] ([[Gamma]], [[Theta]])

## Sources
[^1]: `raw/multi-strategy-options.md`
[^2]: `raw/greeks-overview.md`
