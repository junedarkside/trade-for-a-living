---
title: Short Call
type: strategy
status: learning
aliases: [SC]
tags: [options, derivatives, strategy/income, strategy/speculation, market/thailand]
---

# Short Call

**Income / speculation.** Sell (write) a call option. Neutral-to-bearish — you
collect premium upfront; if the underlying rises past the strike you take losses
(unlimited when naked).

## Overview
The "other half" of every call trade. Naked short call = collect premium, accept
unlimited upside risk. Most often used **covered** (against a long stock position
— see [[Covered Call]]) or **as part of a spread** (see [[Vertical Spread]],
[[Collar]]).

## Legs — naked short call

| Leg | Action | Type | Strike | Expiry |
|-----|--------|------|--------|--------|
| 1 | Short (write) | Call | OTM (above current spot) | Typically 30–45 days |

## Max profit
**Premium received.** Realized if the option expires worthless (spot ≤ strike
at expiry).
- Capped: yes — at the premium.

## Max loss
**Unlimited** (theoretically) for a naked short call. As spot rises, loss =
(Spot − Strike) × 100 − Premium received.
- Capped: no — only when paired with a long position (covered call) or a long
  call higher up (bull call spread).

## Breakeven
**Strike + Premium received** (per share).

## Greeks behavior
- **[[Delta]]**: negative (mirror of long call) — short delta hurts you as price rises.
- **[[Gamma]]**: negative — losses accelerate as price approaches/runs past strike.
- **[[Theta]]**: **positive** — time decay works in your favor (this is the income).
- **[[Vega]]**: negative — rising IV hurts (unrealized loss on short option).

## Payoff shape (at expiry)
```
P&L
 │  ___________      ← capped profit at premium
 │  \
 │    \
 │      \
 ┼────────\───────── Strike + premium (breakeven)
 │         \
 │           \      ← losses grow as spot rises
 │             \
 │               \   ← uncapped downside (naked)
```

## When to use
- **Naked short call**: only with a margin account and strict risk controls; you're
  betting the underlying stays below the strike.
- **Covered short call**: against a long stock position ([[Covered Call]]) —
  defined upside, capped profit, partial downside cushion.
- **As a spread leg**: in a [[Vertical Spread]] or [[Collar]] to define risk
  and reduce margin (see [[Portfolio Margin]]).

## Risks
- **Unlimited loss potential** (naked).
- **Early assignment** — possible on American-style calls near ex-dividend or
  deep ITM.
- **Margin call risk** — short option margin can change intraday.
- **Pin risk** — at exactly strike at expiry, assignment lottery.

## Example — SET / TFEX
- Stock = ฿170. Write 1 OTM call, strike ฿180, 30 days. Premium = ฿2.00/share.
- **Credit**: 2.00 × 100 = **฿200**.
- At expiry, stock ≤ ฿180 → keep ฿200.
- At expiry, stock = ฿200 → loss = (200 − 180) × 100 − 200 = ฿1,800.
- At expiry, stock = ฿250 → loss = (250 − 180) × 100 − 200 = ฿6,800 (and grows).

## Related
- [[Long Call]] (the other side) · [[Covered Call]] (covered variant) ·
  [[Vertical Spread]] (short call + long call) · [[Collar]] ·
  [[Greeks]] ([[Theta]], [[Delta]]) · [[Options — Basics]]

## Sources
[^1]: `raw/options-basics.md`
[^2]: optionseducation.org — options basics.
[^3]: optionsplaybook.com — options introduction.