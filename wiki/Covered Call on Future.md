---
title: Covered Call on Future
type: strategy
status: learning
aliases: [CCF]
tags: [futures, options, derivatives, strategy/income, market/thailand]
---

# Covered Call on Future

**Income strategy.** Long a futures contract and sell (write) a call against it.
Collect premium upfront; in exchange you cap your upside at the call's strike.

## Overview
Neutral-to-mildly-bullish income play on a futures position. Same logic as the
equity [[Covered Call]], but with a futures leg — no stock to be called away; the
"call-away" mechanic is the **futures closing trade at the strike-equivalent price**.

## Legs

| Leg | Action | Instrument | Contract | Strike | Expiry |
|-----|--------|-----------|----------|--------|--------|
| 1 | Long | Future | e.g. S50U26 | — | Same as call |
| 2 | Short (write) | Call option | e.g. S50U26 | Above spot (OTM) | 30–45 days typical |

## Max loss
**(Future entry − 0) − Premium received** (if underlying falls to zero, theoretically).
- Capped at the underlying going to zero; you still bear the linear downside of
  the future. The premium only partially offsets a big drop.

## Max profit
**(Call strike − Future entry) + Premium received**, per contract (× multiplier).
- Capped: yes — at the call strike.

## Breakeven
**Future entry − Premium received.** The premium lowers your cost basis.

## Greeks behavior
- **Delta**: positive (long future dominates) — you want price up.
- **Gamma**: short (from the call) — modest.
- **Theta**: **positive** — time decay works in your favor; this is the income.
- **Vega**: short (negative) — rising IV hurts the short call (unrealized).

## Payoff shape (at expiry)
```
P&L
 │        __________  ← capped at strike + premium
 │      /
 │    /
 │  /  ← profit grows with future to the strike
 ┼────────────── Strike
 │
 │  ← below strike, P&L tracks future (minus premium cushion)
```

## When to use
- Neutral to mildly bullish on an underlying you have a futures position in.
- Want income in a flat/slowly-drifting market.
- Willing to close the future at the call strike level.

## Risks
- **Upside capped** — miss outsized rallies past the call strike.
- **Downside unchanged** — still a long future; premium only cushions.
- **Early assignment** — unlikely on OTM calls but possible near expiry.
- **Margin on short call** — separate from the future's margin.

## Example — SET50 / TFEX
- Long 1 S50 future at 950. Write 1 S50 call, strike 990, 35 days out,
  collect ฿6/index point × ฿200 = ฿1,200 premium.
- **Max profit**: (990 − 950) × 200 + 1,200 = ฿9,200.
- **Breakeven**: 950 − 6 = **944**.
- Index stays ≤ 990 → keep premium + future. If > 990 → close future at 990 level.

## Related
- [[Covered Call]] (stock variant) · [[Protective Put on Future]] ·
  [[Covered Put on Short Future]] (the short-future mirror) · [[Greeks]] ([[Theta]], [[Delta]])

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/futures-basics.md`
[^3]: Hindu Business Line — Mastering derivatives: how to optimally combine futures and options.