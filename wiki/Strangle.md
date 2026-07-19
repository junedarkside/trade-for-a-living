---
title: Strangle
type: strategy
status: learning
tags: [options, derivatives, strategy/speculation, strategy/income, market/thailand]
---

# Strangle

A **strangle** uses an OTM call + an OTM put (same expiry, different strikes).
Two variants: **long strangle** (buy both → long vol) and **short strangle**
(sell both → range income). Cheaper than a straddle but needs a bigger move.

## Long strangle

### Legs
| Leg | Action | Type | Strike | Expiry |
|-----|--------|------|--------|--------|
| 1 | Long | Call | OTM (above spot) | Same |
| 2 | Long | Put | OTM (below spot) | Same |

### Max profit / loss
- **Max profit**: unlimited (either side runs).
- **Max loss**: total premium paid (capped).

### Breakeven
**Call strike + Total premium** (up) and **Put strike − Total premium** (down).

### Greeks
- Delta ~0; **+gamma**; **−theta** (paying decay); **+vega** (long vol).

### When to use
- Expect a large move, direction unknown, but want cheaper entry than a straddle.
- Trade-off: wider breakevens (needs a bigger move to profit).

## Short strangle

### Legs
Same structure, **sell** both legs instead of buying.

### Max profit / loss
- **Max profit**: net credit received (capped).
- **Max loss**: **unlimited** on either side (gap risk).

### Breakeven
Same formulas: **Short call strike + Credit** / **Short put strike − Credit**.

### Greeks
- Delta ~0; **−gamma** (short); **+theta** (collect decay); **−vega** (short vol).

### When to use
- Range-bound view with high IV to sell.
- **High risk** — undefined loss; only with strict risk control and margin.

## Payoff shape (at expiry)
```
Long:   profits on tails       Short:  profits in the middle
  /\                              /\        /
 /  \                            /  \______/
 ↑    ↑ (breakevens)            ↑    ↑
```

## Risks
- **Long**: time decay + IV crush; needs a move bigger than a straddle would.
- **Short**: catastrophic gap risk; undefined loss; pin/assignment near strikes.

## Example — SET50 / TFEX
- SET50 at 1,300.
- **Long strangle**: buy call 1,350 (฿10) + put 1,250 (฿10) = ฿20 premium.
  Breakevens: 1,350 + 20 = **1,370** / 1,250 − 20 = **1,230**. Needs SET50 beyond
  that band to profit.
- **Short strangle** (advanced): sell the same strikes, collect ฿20 credit.
  Breakevens identical; profits if SET50 stays in [1,230, 1,370].

## Related
- [[Long Straddle]] (ATM version) · [[Iron Condor]] (defined-risk short
  strangle) · [[Multi-Strategy Options]] · [[Options Chain]] ·
  [[Greeks]] ([[Gamma]], [[Theta]], [[Vega]])

## Sources
[^1]: `raw/multi-strategy-options.md`
[^2]: `raw/greeks-overview.md`
