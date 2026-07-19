---
title: Long Call
type: strategy
status: learning
aliases: [LC]
tags: [options, derivatives, strategy/speculation, market/thailand]
---

# Long Call

**Speculation / leverage.** Buy a call option. Bullish — you want the underlying
to rise above the strike by more than the premium you paid.

## Overview
The most basic directional bullish options trade. Limited loss (the premium),
theoretically unlimited upside, and far less capital than buying the underlying.
Foundation of most speculative option plays (see [[Long Straddle]],
[[Vertical Spread]], etc.).

## Legs

| Leg | Action | Type | Strike | Expiry |
|-----|--------|------|--------|--------|
| 1 | Long | Call | ATM or slightly OTM | Typically 30–60 days |

## Max loss
**Premium paid.** If the option expires worthless (spot ≤ strike at expiry),
you lose 100% of the premium.
- Capped: yes — at the premium.

## Max profit
**Uncapped** as the underlying rises. Profit = (Spot − Strike) × 100 − Premium paid.

## Breakeven
**Strike + Premium paid** (per share).

## Greeks behavior
- **[[Delta]]**: positive (0 to +1) — moves toward +1 as it goes ITM.
- **[[Gamma]]**: positive — biggest near ATM.
- **[[Theta]]**: negative — you pay time decay daily.
- **[[Vega]]**: positive — rising IV helps; falling IV hurts.

## Payoff shape (at expiry)
```
P&L
 │              /   ← uncapped upside
 │            /
 │          /
 ┼────────/──────── Strike + premium (breakeven)
 │      /
 │    /  ← loss bounded by premium below strike
 │  /
 ┼────────────── Strike
```

## When to use
- Bullish on the underlying, expect a move above strike + premium.
- Want leveraged exposure with a known, capped loss.
- Speculating on earnings/events with defined risk.

## Risks
- **Total premium loss** — the option can expire worthless (most common outcome
  for OTM long calls).
- **[[Theta|Time decay]]** — erodes value every day, accelerating near expiry.
- **[[Vega|Volatility crush]]** — post-event IV drop can hurt even if the move is right.
- **Liquidity** — far-OTM or far-dated strikes may have wide bid/ask.

## Example — SET / TFEX
- Stock = ฿170. Buy 1 ATM call, strike ฿170, 30 days. Premium = ฿3.50/share.
- **Cost**: 3.50 × 100 = **฿350**.
- At expiry, stock = ฿180 → intrinsic 10 → option value ฿1,000 → **profit ฿650**.
- At expiry, stock = ฿165 → expires worthless → **loss ฿350** (the premium).

## Related
- [[Short Call]] (the other side) · [[Options — Basics]] · [[Options Strategy]] ·
  [[Vertical Spread]] (long call + short call = defined risk) ·
  [[Long Straddle]] (long call + long put) ·
  [[Greeks]] ([[Delta]], [[Theta]], [[Vega]])

## Sources
[^1]: `raw/options-basics.md`
[^2]: investopedia.com — options basics tutorial.
[^3]: optionseducation.org — options basics.