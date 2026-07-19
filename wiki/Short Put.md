---
title: Short Put
type: strategy
status: learning
aliases: [SP]
tags: [options, derivatives, strategy/income, strategy/speculation, market/thailand]
---

# Short Put

**Income / speculation.** Sell (write) a put option. Neutral-to-bullish — you
collect premium upfront; if the underlying falls past the strike, you may be
assigned (forced to buy at the strike).

## Overview
The "other half" of every put trade. Naked short put = collect premium, accept
the risk of buying the underlying at the strike. Most often used **cash-secured**
(see [[Cash-Secured Put]] — hold enough cash to buy if assigned) or **as part of
a spread** (see [[Vertical Spread]] bull put spread, or a put spread collar).

## Legs — naked / cash-secured short put

| Leg | Action | Type | Strike | Expiry |
|-----|--------|------|--------|--------|
| 1 | Short (write) | Put | OTM (below current spot) | Typically 30–45 days |

## Max profit
**Premium received.** Realized if the option expires worthless (spot ≥ strike).
- Capped: yes — at the premium.

## Max loss
**(Strike − 0) × 100 − Premium received** (theoretical max if underlying → 0).
- Capped: yes — at the underlying going to zero (large loss in practice).

## Breakeven
**Strike − Premium received** (per share).

## Greeks behavior
- **[[Delta]]**: positive (mirror of long put) — short delta hurts you as price falls.
- **[[Gamma]]**: negative — losses accelerate as price approaches/falls past strike.
- **[[Theta]]**: **positive** — time decay works in your favor (this is the income).
- **[[Vega]]**: negative — rising IV hurts (unrealized loss).

## Payoff shape (at expiry)
```
P&L
 │  ___________      ← capped profit at premium
 │  \
 │    \
 │      \
 ┼────────\───────── Strike − premium (breakeven)
 │          \
 │            \  ← losses grow as spot falls, capped at ~strike
 │              \
 ┼────────────────\── Strike
```

## When to use
- **Cash-secured**: willing to buy the underlying at the strike (you're paid to
  wait) — see [[Cash-Secured Put]].
- **Naked short put**: only with margin account + strict risk controls.
- **As a spread leg**: in a bull put spread ([[Vertical Spread]]) or put spread
  collar to define risk and reduce margin (see [[Portfolio Margin]]).

## Risks
- **Large loss potential** if the underlying falls sharply (capped at strike − 0).
- **Assignment risk** — if assigned, you own the underlying at the strike (and
  its full downside).
- **Opportunity cost** — capital tied up as cash reserve (cash-secured) or
  margin (naked).
- **Early assignment** — possible on American-style puts near ex-dividend or
  deep ITM.

## Example — SET / TFEX
- Stock = ฿170. Write 1 OTM put, strike ฿160, 30 days. Premium = ฿2.50/share.
- **Credit**: 2.50 × 100 = **฿250**. (Cash-secured: hold ฿16,000 to buy 100 shares.)
- At expiry, stock ≥ ฿160 → keep ฿250.
- At expiry, stock = ฿140 → loss = (160 − 140) × 100 − 250 = ฿1,750 (and you own the stock).
- At expiry, stock = ฿0 → loss = (160 × 100) − 250 = ฿15,750 (theoretical max).

## Related
- [[Long Put]] (the other side) · [[Cash-Secured Put]] (cash-secured variant) ·
  [[Vertical Spread]] (short put + long put = bull put spread) ·
  [[Covered Put on Short Future]] (futures variant) ·
  [[Greeks]] ([[Theta]], [[Delta]]) · [[Options — Basics]]

## Sources
[^1]: `raw/options-basics.md`
[^2]: optionseducation.org — options basics.
[^3]: optionsplaybook.com — options introduction.