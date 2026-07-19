---
title: Iron Butterfly
type: strategy
status: learning
tags: [options, derivatives, strategy/income, market/thailand]
---

# Iron Butterfly

**Tight-range income strategy.** Sell an ATM straddle (call + put at the same
strike) and buy OTM wings (a call above, a put below) to cap the risk. Maximum
profit if price pins to the strike; defined loss if it moves past a wing.

## Overview
The "ATM-body" sibling of the [[Iron Condor]]. Higher credit than a condor
(because the short straddle is at the money), but a narrower profit zone — you're
betting price sits very close to the strike at expiry.

## Legs

| Leg | Action | Type | Strike | Expiry |
|-----|--------|------|--------|--------|
| 1 | Short | Call | ATM (= body) | Same |
| 2 | Short | Put | ATM (same strike) | Same |
| 3 | Long | Call | Above ATM (wing) | Same |
| 4 | Long | Put | Below ATM (wing) | Same |

## Max profit
**Net credit received** (price settles exactly at the body strike).
- Capped: yes.

## Max loss
**(Wing width − Net credit)** × multiplier.
- Capped: yes — wings define it.

## Breakeven
**Two breakevens**: **Body strike + Net credit** and **Body strike − Net credit**.

## Greeks behavior
- **Delta**: ~0 at entry (centered); tilts fast as spot leaves the strike.
- **Gamma**: short — large near the body (delta whips around the pin).
- **Theta**: **strongly positive** — fastest decay at the ATM body.
- **Vega**: **short (negative)** — you want IV to fall.

## Payoff shape (at expiry)
```
P&L
 │__________        __________  ← max loss at/through wings
 │          \      /
 │           \____/            ← max profit = credit (at body strike)
 ├─────────┬─────┬─────────
        WingP  Body  WingC
```

## When to use
- Expect price to **pin** near a specific strike into expiry (e.g. SET50 gravitating
  to a round level).
- High IV you expect to crush.
- Want more credit than a condor, accepting a tighter profit zone.

## Risks
- **Tight profit zone** — small move away from the body erodes profit fast.
- **Gamma / pin risk** — delta swings sharply around the strike near expiry.
- **Early assignment** — short ATM legs are assignment magnets.
- **Gap risk** — a move through a wing = max loss.

## Example — SET50 / TFEX
- SET50 at 1,300; expect it to pin near 1,300 over 14 days.
- Sell 1,300 call + 1,300 put (credit ฿30); buy 1,350 call + 1,250 put (debit
  ฿10). Net credit ฿20; wing width ฿50.
- **Max profit**: ฿20 (settles at 1,300).
- **Max loss**: 50 − 20 = ฿30.
- **Breakevens**: 1,300 ± 20 → **1,280 / 1,320**.

## Related
- [[Iron Condor]] (wider, lower-credit sibling) · [[Long Straddle]] (the body,
  long) · [[Butterfly Spread]] (one-sided body) · [[Options Chain]] ·
  [[Greeks]] ([[Theta]], [[Gamma]], [[Vega]])

## Sources
[^1]: `raw/multi-strategy-options.md`
[^2]: `raw/greeks-overview.md`
