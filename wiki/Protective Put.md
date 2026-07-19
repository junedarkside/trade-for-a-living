---
title: Protective Put
type: strategy
status: learning
aliases: [PP]
tags: [options, derivatives, strategy/hedge, market/thailand]
---

# Protective Put

**Hedge strategy.** You own the stock and buy a put as "insurance." The put
floors your downside at the strike; you give up only the premium.

## Overview
Bullish but want a defined floor — e.g. into earnings, an event, or a shaky
market. Like buying insurance on a position you intend to keep.

## Legs

| Leg | Action | Type | Strike | Expiry |
|-----|--------|------|--------|--------|
| 1 | Long | Stock (100 shares / lot) | — | — |
| 2 | Long | Put | At/near spot (ATM) or below (OTM) | Covers the risk window |

## Max loss
**Stock purchase price − Strike + Premium paid.**
- Capped: yes — the put guarantees an exit at the strike.

## Max profit
**(Stock rises unlimitedly) − Premium paid.**
- Capped: no (beyond the premium cost).

## Breakeven
**Stock purchase price + Premium paid** (premium raises your cost basis).

## Greeks behavior
- **Delta**: positive (long stock dominates) — still bullish.
- **Gamma / Vega**: long (from the put) — big moves / rising IV help the hedge.
- **Theta**: negative — you pay time decay on the insurance.

## Payoff shape (at expiry)
```
P&L
 │        /  ← upside tracks stock (− premium)
 │      /
 │    /
 ┼──────────── Strike
 │  ← floor: losses stop at strike − premium
```

## When to use
- Bullish on a holding but want a hard floor into an event/volatile patch.
- Insuring gains on a long-term position.
- Prefer defined risk over a naked stock hold.

## Risks
- **Premium cost** — insurance isn't free; drags returns in flat markets.
- **Time decay** — value bleeds; expires worthless if no drop (best-case outcome).
- **Strike choice** — lower strike = cheaper but bigger deductible.

## Example — SET50 / SET
- Own 1,000 shares at ฿100; want protection for 30 days.
- Buy 10 puts, strike ฿95, 30 days out, pay ฿1.50/share = ฿1,500.
- **Max loss**: (100 − 95) × 1,000 + 1,500 = ฿6,500.
- **Breakeven**: 100 + 1.50 = ฿101.50.
- Stock crashes to ฿80 → exit at ฿95, loss capped at ฿6,500 instead of ฿20,000.

## Related
- [[Options Strategy]] · [[Collar]] (protective put funded by a short call) ·
  [[Covered Call]] · [[Greeks]] ([[Delta]], [[Gamma]], [[Vega]])

## Sources
[^1]: `raw/options-strategies-overview.md`
[^2]: `raw/greeks-overview.md`
