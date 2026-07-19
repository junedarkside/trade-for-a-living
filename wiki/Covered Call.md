---
title: Covered Call
type: strategy
status: learning
aliases: [CC]
tags: [options, derivatives, strategy/income, market/thailand]
---

# Covered Call

**Income strategy.** You own the underlying and sell (write) a call option
against it. You collect premium upfront; in exchange you cap your upside at the
call's strike.

## Overview
Neutral-to-mildly-bullish income play. Best when you own a stock you're happy to
hold and would be willing to sell at a modestly higher price. The premium is
yours to keep regardless of outcome.

## Legs

| Leg | Action | Type | Strike | Expiry |
|-----|--------|------|--------|--------|
| 1 | Long | Stock (100 shares / lot) | — | — |
| 2 | Short (write) | Call | Above spot (OTM) | 30–45 days typical |

## Max loss
**Stock purchase price − Premium received** (if stock falls to zero).
- Capped at the stock going to zero; you still bear the underlying's downside.
  The premium only partially offsets a big drop.

## Max profit
**(Strike − Stock purchase price) + Premium received**, per share.
- Capped: yes — if stock rockets past the strike, shares are called away at the
  strike.

## Breakeven
**Stock purchase price − Premium received.** The premium lowers your cost basis.

## Greeks behavior
- **Delta**: positive (long stock dominates) — you want the stock up.
- **Gamma**: short (from the call) — modest.
- **Theta**: **positive** — time decay works in your favor; this is the income.
- **Vega**: short (negative) — rising IV hurts the short call (unrealized).

## Payoff shape (at expiry)
```
P&L
 │        __________  ← capped at strike + premium
 │      /
 │    /
 │  /  ← profit grows with stock to the strike
 ┼────────────── Strike
 │
 │  ← below strike, P&L tracks stock (minus premium cushion)
```

## When to use
- Neutral to mildly bullish on a stock you already own (or want to acquire).
- Want income in a flat/slowly-drifting market.
- Willing to sell the stock at the strike price.

## Risks
- **Upside capped** — miss outsized rallies.
- **Downside unchanged** — still a long stock position; premium only cushions.
- **Early assignment** — unlikely on OTM calls but possible near expiry/dividend.
- **Opportunity cost** — capital tied up in the stock.

## Example — SET50 / SET
- Own 1,000 shares of a SET blue-chip at ฿100.
- Write 10 calls (1,000 shares), strike ฿105, 35 days out, collect ฿2.00/share
  = ฿2,000 premium.
- **Max profit**: (105 − 100) × 1,000 + 2,000 = ฿7,000.
- **Breakeven**: 100 − 2 = ฿98.
- If stock stays ≤ 105, keep premium + shares. If > 105, shares called at 105.

## Related
- [[Options Strategy]] · [[Cash-Secured Put]] (the put-side income play) ·
  [[Collar]] (covered call + protective put) · [[Greeks]] ([[Theta]], [[Delta]])

## Sources
[^1]: `raw/options-strategies-overview.md`
