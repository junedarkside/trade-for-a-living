---
title: Covered Put on Short Future
type: strategy
status: learning
aliases: [CPSF]
tags: [futures, options, derivatives, strategy/income, market/thailand]
---

# Covered Put on Short Future

**Income strategy.** Short a futures contract and sell (write) a put against it.
Collect premium upfront; in exchange you cap your downside at the put's strike.

## Overview
Neutral-to-mildly-bearish income play on a short futures position. Same logic as
the equity [[Cash-Secured Put]] but on a futures underlier.

## Legs

| Leg | Action | Instrument | Contract | Strike | Expiry |
|-----|--------|-----------|----------|--------|--------|
| 1 | Short | Future | e.g. S50U26 | — | Same as put |
| 2 | Short (write) | Put option | e.g. S50U26 | Below spot (OTM) | 30–45 days typical |

## Max profit
**(Future entry − Put strike) + Premium received**, per contract (× multiplier).
- Capped: yes — at the put strike.

## Max loss
**(Future entry − 0) − Premium received** (theoretically).
- Capped at the underlying going to zero; you still bear the linear upside risk
  of the short future. Premium only partially offsets a big rally.

## Breakeven
**Future entry + Premium received.**

## Greeks behavior
- **Delta**: negative (short future dominates) — you want price down.
- **Gamma**: short (from the put) — modest.
- **Theta**: **positive** — time decay works in your favor; this is the income.
- **Vega**: short (negative) — rising IV hurts the short put.

## Payoff shape (at expiry)
```
P&L
 │
 │  ← above strike, P&L tracks short future (minus premium cushion)
 ┼────────────── Strike
 │  \
 │    \
 │      \__________  ← capped at strike − premium
```

## When to use
- Neutral to mildly bearish on an underlying you have a short futures position in.
- Want income in a flat/slowly-drifting market.
- Willing to close the future at the put strike level.

## Risks
- **Downside capped** — miss outsized sell-offs past the put strike (profits stop growing).
- **Upside unchanged** — short future has unlimited loss potential on a rally;
  premium only cushions.
- **Early assignment** — possible on the short put if deep ITM.
- **Margin on short put** — separate from the future's margin.

## Example — SET50 / TFEX
- Short 1 S50 future at 950. Write 1 S50 put, strike 910, 35 days out,
  collect ฿5/index point × ฿200 = ฿1,000 premium.
- **Max profit**: (950 − 910) × 200 + 1,000 = ฿9,000.
- **Breakeven**: 950 + 5 = **955**.
- Index stays ≥ 910 → keep premium + short future. If < 910 → close short at 910 level.

## Related
- [[Cash-Secured Put]] (stock variant) · [[Protective Call on Short Future]] ·
  [[Covered Call on Future]] (the long-future mirror) · [[Greeks]] ([[Theta]], [[Delta]])

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/futures-basics.md`
[^3]: Hindu Business Line — Mastering derivatives: how to optimally combine futures and options.