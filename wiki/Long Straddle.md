---
title: Long Straddle
type: strategy
status: learning
tags: [options, derivatives, strategy/speculation, market/thailand]
---

# Long Straddle

**Speculative / volatility strategy.** Buy an ATM call and an ATM put, same
strike, same expiry. Profit from a big move in **either** direction; risk is the
total premium paid.

## Overview
Direction-agnostic — you're long volatility. Best when you expect a large move
(event, catalyst, breakout) but not the direction. Also long vega: rising IV
helps even before the move.

## Legs

| Leg | Action | Type | Strike | Expiry |
|-----|--------|------|--------|--------|
| 1 | Long | Call | ATM (≈ spot) | Event-window expiry |
| 2 | Long | Put | ATM (same strike) | Same |

## Max loss
**Total premium paid** (call + put).
- Capped: yes — both legs can expire worthless if spot stays at the strike.

## Max profit
**Unlimited** (the call side runs as spot rallies).
- Capped: no.

## Breakeven
**Two breakevens**: **Strike + Total premium** (upside) and
**Strike − Total premium** (downside).

## Greeks behavior
- **Delta**: ~0 at entry (call + put offset); drifts with the move.
- **Gamma**: **long** — big moves in either direction help (this is the engine).
- **Theta**: **strongly negative** — you pay every day the move doesn't come.
- **Vega**: **long** — rising IV expands both legs' value.

## Payoff shape (at expiry)
```
P&L
 │\        /   ← profits on either tail
 │ \      /
 │  \    /
 ├───\──/──── Strike
 │    \/      ← max loss at the strike (= premium paid)
```

## When to use
- Expect a large move but not the direction (earnings, policy, expiry of a range).
- Expect IV to rise into the event.
- Comfortable paying time decay for convexity.

## Risks
- **Time decay** — theta bleeds daily; flat market = slow death.
- **IV crush** — after the event, IV drops and both legs lose value even if you
  got direction right.
- **Move must exceed total premium** to profit at expiry.

## Example — SET50 / TFEX
- SET50 at 1,300 before a major policy event.
- Buy ATM call + ATM put, strike 1,300, 14 days out. Call ฿25 + Put ฿25 = ฿50
  total premium (per index point).
- **Max loss**: ฿50.
- **Breakevens**: 1,300 ± 50 → **1,250 / 1,350**.
- SET50 moves to 1,380 → call profits. To 1,220 → put profits. Stays 1,300 →
  lose ฿50.

## Short straddle (variant)
Sell the ATM call + ATM put (same strike/expiry) instead of buying.
- **Max profit**: net credit (price pins at the strike).
- **Max loss**: **unlimited** either side — gap risk.
- **Breakevens**: strike ± total credit.
- **Greeks**: ~0 delta, **−gamma**, **+theta** (collect decay), **−vega**.
- Use: range-bound, high-IV, **defined controls only** — undefined loss makes
  this advanced. See [[Strangle]] for the OTM (wider) version and [[Iron
  Butterfly]] for the defined-risk version (add wings).

## Related
- [[Options Strategy]] · [[Strangle]] (OTM legs, cheaper, wider breakevens) ·
  [[Options Chain]] (find ATM strike + IV) · [[Greeks]] ([[Gamma]], [[Theta]], [[Vega]])

## Sources
[^1]: `raw/options-strategies-overview.md`
[^2]: `raw/greeks-overview.md`
