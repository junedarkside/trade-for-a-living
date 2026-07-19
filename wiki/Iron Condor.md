---
title: Iron Condor
type: strategy
status: learning
aliases: [IC]
tags: [options, derivatives, strategy/income, market/thailand]
---

# Iron Condor

**Range-bound income strategy.** Sell an OTM call spread **and** an OTM put
spread on the same underlying/expiry. Profit if price stays inside the range;
risk is defined by the wings.

## Overview
Neutral view that collects premium from time decay while price chops between two
short strikes. The bought wings cap the loss on each side (unlike a naked short
strangle).

## Legs

| Leg | Action | Type | Strike | Expiry |
|-----|--------|------|--------|--------|
| 1 | Short | Put | OTM (lower short, e.g. put resistance) | Same |
| 2 | Long | Put | Below short put (wing) | Same |
| 3 | Short | Call | OTM (upper short, e.g. call resistance) | Same |
| 4 | Long | Call | Above short call (wing) | Same |

## Max profit
**Net credit received** (all four legs expire worthless).
- Capped: yes — the credit is the most you make.

## Max loss
**(Wing width − Net credit)**, per the **wider** side, × multiplier.
- Capped: yes — the long wings define it.

## Breakeven
**Two breakevens**: **Short put strike − Credit** and **Short call strike + Credit**.

## Greeks behavior
- **Delta**: ~0 at entry (balanced) if centered; tilts as spot moves.
- **Gamma**: short — delta grows against you near a short strike.
- **Theta**: **positive** — time decay is the income engine.
- **Vega**: **short (negative)** — rising IV hurts; you want IV to fall.

## Payoff shape (at expiry)
```
P&L
 │__________        __________  ← max loss on wings
 │          \      /
 │           \____/            ← max profit = credit (inside range)
 ├──────┬─────────┬─────
      PutS      CallS
   (breakevens at PutS−credit ... CallS+credit)
```

## When to use
- Neutral/range-bound view with a defined expected range (read [[Options Chain]]
  OI walls).
- Elevated IV (sell richness) you expect to fall.
- Want income with **defined risk** (vs naked short strangle).

## Risks
- **Pin risk** — if price lands exactly on a short strike near expiry.
- **Early assignment** — on a short leg that goes ITM (American style).
- **Gap risk** — a move through a wing still costs max loss, but a fast gap makes
  exit messy.
- **IV spike** — marks against you before theta can do its work.

## Example — SET50 / TFEX
- SET50 at 1,300; expect 1,250–1,350 range over 30 days.
- Sell put 1,250 / buy put 1,200 (credit ฿6); sell call 1,350 / buy call 1,400
  (credit ฿6). Net credit ฿12 (per index point), wing width ฿50.
- **Max profit**: ฿12.
- **Max loss**: 50 − 12 = ฿38.
- **Breakevens**: 1,250 − 12 = **1,238**; 1,350 + 12 = **1,362**.
- Settle in [1,250, 1,350] → keep ฿12.

## Related
- [[Multi-Strategy Options]] (condor as the range-income book) · [[Strangle]]
  (naked, higher-risk version) · [[Iron Butterfly]] (ATM-body variant) ·
  [[Options Chain]] · [[Greeks]] ([[Theta]], [[Vega]])

## Sources
[^1]: `raw/multi-strategy-options.md`
[^2]: `raw/greeks-overview.md`
