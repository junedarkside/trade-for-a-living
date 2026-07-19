---
title: Protective Call on Short Future
type: strategy
status: learning
aliases: [PCSF]
tags: [futures, options, derivatives, strategy/hedge, market/thailand]
---

# Protective Call on Short Future

**Hedge strategy.** Short a futures contract and buy a call on it as "insurance."
The call caps your upside risk at the strike; you give up only the premium.

## Overview
Bearish on the underlying but want a hard cap — e.g. shorting into an event or
uncertainty. Mirror of the long-future [[Protective Put on Future]].

## Legs

| Leg | Action | Instrument | Contract | Strike | Expiry |
|-----|--------|-----------|----------|--------|--------|
| 1 | Short | Future | e.g. S50U26 | — | Same as call |
| 2 | Long | Call option | e.g. S50U26 | At/near spot (ATM) or above (OTM) | Same as future |

## Max profit
**Uncapped** as the future falls, minus premium paid.

## Max loss
**(Call strike − Future entry) + Premium paid**, per contract (× multiplier).
- Capped: yes — the call lets you close-equivalent at the strike.

## Breakeven
**Future entry − Premium paid** (premium lowers your profit floor).

## Greeks behavior
- **Delta**: negative (short future dominates) — bearish.
- **Gamma / Vega**: long (from the call) — big moves / rising IV help the hedge.
- **Theta**: negative — you pay time decay on the insurance.

## Payoff shape (at expiry)
```
P&L
 │
 │  ← upside capped: losses stop at strike + premium
 ┼──────────── Strike
 │    \
 │      \
 │        \  ← profit grows as future falls (− premium)
```

## When to use
- Bearish but want a defined ceiling on a short futures position.
- Insuring against a short-squeeze / rally risk.
- Prefer defined risk over a naked short future hold.

## Risks
- **Premium cost** — insurance isn't free; drags returns in flat markets.
- **Time decay** — value bleeds; call expires worthless if no rally.
- **Strike choice** — higher strike = cheaper but bigger gap risk.

## Example — SET50 / TFEX
- Short 1 S50 future at 950. Buy 1 S50 call, strike 980, 30 days out,
  pay ฿7/index point × ฿200 = ฿1,400.
- **Max loss**: (980 − 950) × 200 + 1,400 = ฿7,400.
- **Breakeven**: 950 − 7 = **943**.
- Index rallies to 1,020 → close-equivalent at 980, loss capped at ฿7,400
  instead of (1,020 − 950) × 200 = ฿14,000 naked-short loss.

## Related
- [[Protective Put on Future]] (long-future mirror) · [[Covered Put on Short Future]] ·
  [[Risk Reversal]] (short future + long call + short put) · [[Greeks]] ([[Delta]], [[Gamma]])

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/futures-basics.md`
[^3]: Hindu Business Line — Mastering derivatives: how to optimally combine futures and options.