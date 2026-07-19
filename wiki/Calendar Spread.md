---
title: Calendar Spread
type: strategy
status: learning
aliases: [Cal]
tags: [options, futures, derivatives, strategy/speculation]
---

# Calendar Spread

**Vol/time strategy.** Sell a near-dated option and buy a longer-dated option,
same strike, same underlying. Profits from **differential time decay** between
the two expiries.

## Overview
A classic "theta-harvest with defined risk" structure. The short near-term
option decays faster than the long back-month (theta is concentrated near expiry
for ATM options). The position benefits if the underlying stays near the strike
through the short expiry.

## Legs — Calendar Call Spread (long calendar)

| Leg | Action | Instrument | Contract | Strike | Expiry |
|-----|--------|-----------|----------|--------|--------|
| 1 | Short | Call option | e.g. S50U26 | ATM (same as leg 2) | Near (e.g. 30 days) |
| 2 | Long | Call option | e.g. S50U26 | ATM | Far (e.g. 90 days) |

Mirror for **Calendar Put Spread**: short near ATM put + long far ATM put.

## Max profit
**Achieved near short-leg expiry**, when the underlying is at or near the strike
and the long back-month retains meaningful time value. Hard to bound — depends
on IV at that point.

## Max loss
**Net debit paid** (long back-month premium − short near-month premium received),
realized if the long back-month expires worthless or the underlying gaps far
from the strike at short-expiry.
- Capped: yes — at the net debit.

## Breakeven
**Strike ± (extrinsic value captured at short-leg expiry)** — path-dependent,
not a single level.

## Greeks behavior
- **Delta**: ≈ 0 near expiry of short leg (assuming underlying at strike).
- **Gamma**: long (long back-month dominates) — benefits from large moves.
- **Theta**: **positive** at entry (short near decays faster than long far).
  Theta decays to zero as short leg approaches expiry.
- **Vega**: **long** (long back-month has more vega than short near-month).

## Payoff shape (at short-leg expiry, in P&L)
```
P&L
 │       _____
 │      /     \      ← peak near strike (ATM)
 │    /         \
 ┼──/─────────────\── Strike
 │ /
 │/                ← losses capped at net debit
```

## When to use
- **Neutral view** on the underlying over the short window (front-month expiry).
- **Expectation of stable IV** (or willing to be long vega into the back-month).
- **Time decay harvest** — selling expensive near-dated premium.

## Risks
- **Vol crush** — back-month IV dropping hurts the long leg's value.
- **Pin risk at short expiry** — if underlying lands exactly on strike, max profit;
  if it gaps, max loss can be near the debit.
- **Liquidity** — far-dated strikes may be thinner; check OI before entry.
- **Early assignment** — short ITM option near ex-div can be assigned.

## Example — SET50 / TFEX
- Sell 1 S50 call strike 950, 30 days to expiry, collect ฿12 × 200 = ฿2,400.
- Buy 1 S50 call strike 950, 90 days to expiry, pay ฿20 × 200 = ฿4,000.
- **Net debit**: ฿1,600.
- If S50 stays near 950 → short expires near worthless, long retains ~฿15 extrinsic
  → profit ≈ ฿3,000 − ฿1,600 = **฿1,400** at short-expiry.
- If S50 gaps to 1,000 → both legs ITM; loss capped near debit (calendar narrows).

## Related
- [[Diagonal Spread]] (calendar + different strikes) · [[Long Straddle]] (long vol, no time spread) ·
  [[Greeks]] ([[Theta]], [[Vega]], [[Gamma]]) · [[Multi-Leg Order]]

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/greeks-overview.md`
[^3]: youtube.com — payoff diagrams reference.
[^4]: Hindu Business Line — Mastering derivatives: how to optimally combine futures and options.