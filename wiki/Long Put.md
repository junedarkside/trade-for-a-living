---
title: Long Put
type: strategy
status: learning
aliases: [LP]
tags: [options, derivatives, strategy/speculation, strategy/hedge, market/thailand]
---

# Long Put

**Speculation / hedge.** Buy a put option. Bearish — you want the underlying to
fall below the strike by more than the premium you paid. Also used as
**insurance** on a long stock position (see [[Protective Put]]).

## Overview
The basic bearish options trade. Limited loss (the premium), large profit
potential as the underlying falls, and far less capital than shorting the
underlying. Foundation of bearish plays ([[Long Straddle]] with a long call,
[[Protective Put]] for hedging, [[Vertical Spread]] defined-risk bearish).

## Legs

| Leg | Action | Type | Strike | Expiry |
|-----|--------|------|--------|--------|
| 1 | Long | Put | ATM or slightly OTM | Typically 30–60 days |

## Max profit
**(Strike − 0) × 100 − Premium paid** (theoretical max if underlying → 0).
- Capped at the underlying going to zero.

## Max loss
**Premium paid.** If spot ≥ strike at expiry, the put expires worthless.
- Capped: yes — at the premium.

## Breakeven
**Strike − Premium paid** (per share).

## Greeks behavior
- **[[Delta]]**: negative (−1 to 0) — moves toward −1 as it goes ITM.
- **[[Gamma]]**: positive — biggest near ATM.
- **[[Theta]]**: negative — you pay time decay daily.
- **[[Vega]]**: positive — rising IV helps.

## Payoff shape (at expiry)
```
P&L
 │  ← profit grows as spot falls, capped at strike (if underlying → 0)
 │  \
 │    \
 │      \
 ┼────────\───────── Strike − premium (breakeven)
 │          \
 │            \  ← loss bounded by premium above strike
 │              \
 ┼────────────────\── Strike
```

## When to use
- Bearish on the underlying, expect a move below strike − premium.
- Insuring a long stock position ([[Protective Put]]) — define the floor.
- Speculating on negative events (earnings miss, bad news) with capped risk.

## Risks
- **Total premium loss** — if the underlying doesn't fall enough, the put
  expires worthless.
- **[[Theta|Time decay]]** — erodes daily; long puts need the move to happen soon.
- **[[Vega|Volatility crush]]** — post-event IV drop can hurt even if direction is right.
- **Liquidity** — deep OTM puts may have wide bid/ask.

## Example — SET / TFEX
- Stock = ฿170. Buy 1 ATM put, strike ฿170, 30 days. Premium = ฿3.20/share.
- **Cost**: 3.20 × 100 = **฿320**.
- At expiry, stock = ฿150 → intrinsic 20 → option value ฿2,000 → **profit ฿1,680**.
- At expiry, stock = ฿175 → expires worthless → **loss ฿320** (the premium).

## Related
- [[Short Put]] (the other side) · [[Protective Put]] (long stock + long put) ·
  [[Options — Basics]] · [[Long Straddle]] · [[Vertical Spread]] ·
  [[Greeks]] ([[Delta]], [[Theta]], [[Vega]])

## Sources
[^1]: `raw/options-basics.md`
[^2]: investopedia.com — options basics tutorial.
[^3]: optionseducation.org — options basics.