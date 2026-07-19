---
title: Protective Put on Future
type: strategy
status: learning
aliases: [PPF]
tags: [futures, options, derivatives, strategy/hedge, market/thailand]
---

# Protective Put on Future

**Hedge strategy.** Go long a futures contract and buy a put on it as "insurance."
The put floors your downside at the strike; you give up only the premium.

## Overview
Bullish on the underlying but want a hard floor — e.g. into an event or shaky tape.
Same logic as the equity [[Protective Put]], but with a futures leg instead of stock.

## Legs

| Leg | Action | Instrument | Contract | Strike | Expiry |
|-----|--------|-----------|----------|--------|--------|
| 1 | Long | Future | e.g. S50U26 | — | Same as put |
| 2 | Long | Put option | e.g. S50U26 | At/near spot (ATM) or below (OTM) | Same as future |

## Max profit
**Uncapped** as the future rises, minus premium paid.

## Max loss
**(Future entry − Put strike) + Premium paid**, per contract (× multiplier).
- Capped: yes — the put guarantees exit-equivalent at the strike.

## Breakeven
**Future entry + Premium paid** (premium raises your cost basis).

## Greeks behavior
- **Delta**: positive (long future dominates) — still bullish.
- **Gamma / Vega**: long (from the put) — big moves / rising IV help the hedge.
- **Theta**: negative — you pay time decay on the insurance.

## Payoff shape (at expiry)
```
P&L
 │        /  ← upside tracks future (− premium)
 │      /
 │    /
 ┼──────────── Strike
 │  ← floor: losses stop at strike − premium
```

## When to use
- Bullish on the underlying (e.g. SET50) but want a hard floor into an event.
- Insuring an existing futures position.
- Prefer defined risk over a naked future hold.

## Risks
- **Premium cost** — insurance isn't free; drags returns in flat markets.
- **Time decay** — value bleeds; put expires worthless if no drop (best-case outcome).
- **Strike choice** — lower strike = cheaper but bigger deductible.

## Example — SET50 / TFEX
- Long 1 S50 future at 950. Buy 1 S50 put, strike 920, 30 days out, pay ฿8/index
  point × ฿200 multiplier = ฿1,600.
- **Max loss**: (950 − 920) × 200 + 1,600 = ฿7,600.
- **Breakeven**: 950 + 8 = **958**.
- Index crashes to 880 → exit-equivalent at 920, loss capped at ฿7,600 instead of
  (950 − 880) × 200 = ฿14,000 naked-future loss.

## Related
- [[Protective Put]] (stock variant) · [[Futures Collar]] (put + short call) ·
  [[Covered Call on Future]] (long future + short call) · [[Synthetic Futures]] ·
  [[Greeks]] ([[Delta]], [[Gamma]], [[Vega]])

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/futures-basics.md`
[^3]: Hindu Business Line — Mastering derivatives: how to optimally combine futures and options.