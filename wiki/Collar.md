---
title: Collar
type: strategy
status: learning
tags: [options, derivatives, strategy/hedge, market/thailand]
---

# Collar

**Hedge strategy.** Own the stock, buy a protective put (floor), and sell a
covered call (cap) to fund the put. The result: defined downside, capped upside,
often near-zero net cost.

## Overview
A cheap-to-free hedge for a long stock position. You trade away upside above the
call strike to pay for downside protection at the put strike.

## Legs

| Leg | Action | Type | Strike | Expiry |
|-----|--------|------|--------|--------|
| 1 | Long | Stock (100 shares / lot) | — | — |
| 2 | Long | Put | Below spot (floor) | Same expiry |
| 3 | Short | Call | Above spot (cap) | Same expiry |

## Max loss
**(Stock purchase − Put strike) + Net debit** (or − Net credit).
- Capped at the put strike.

## Max profit
**(Call strike − Stock purchase) − Net debit** (or + Net credit).
- Capped at the call strike.

## Breakeven
**Stock purchase + Net debit** (− Net credit if the structure is done for a credit).

## Greeks behavior
- **Delta**: positive but muted — bullish with a leash.
- **Gamma**: small (long put + short call partly offset).
- **Theta**: roughly flat to slightly positive (short call funds the put).
- **Vega**: roughly flat (offsetting legs).

## Payoff shape (at expiry)
```
P&L
 │__________  ← flat cap at call strike
 │        /
 │      /
 ┼──────/───── Put strike ... Call strike
 │  ← floor: flat loss at put strike
```

## When to use
- Long stock you want to protect but don't want to pay full premium for a put.
- Willing to cap upside (e.g. you'd happily sell at the call strike anyway).
- Common on concentrated stock positions into volatile periods.

## Risks
- **Upside capped** — rallies past the call strike are given away.
- **Early assignment** — on the short call (American style), esp. deep ITM/dividend.
- **Gap below put strike** — protected at strike, but the stock is still assigned
  away if call triggers; plan the exits.

## Example — SET50 / SET
- Own 1,000 shares at ฿100.
- Buy 10 puts, strike ฿95 (฿1.50). Sell 10 calls, strike ฿110 (฿1.50). Net ฿0.
- **Max loss**: (100 − 95) × 1,000 = ฿5,000 (floor at 95, zero-cost).
- **Max profit**: (110 − 100) × 1,000 = ฿10,000 (cap at 110).
- **Breakeven**: ฿100 (zero-cost collar).

## Related
- [[Options Strategy]] · [[Protective Put]] · [[Covered Call]] ·
  [[Options Chain]] (pick floor/cap strikes via OI) · [[Greeks]]

## Sources
[^1]: `raw/options-strategies-overview.md`
[^2]: `raw/greeks-overview.md`
