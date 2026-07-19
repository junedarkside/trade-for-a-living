---
title: Vertical Spread
type: strategy
status: learning
tags: [options, derivatives, strategy/speculation, strategy/hedge, market/thailand]
---

# Vertical Spread

**Defined-risk directional strategy.** Buy and sell options of the **same type**
(both calls or both puts), **same expiry**, **different strikes**. Caps both
profit and loss, and costs less than a naked option.

## Overview
The workhorse directional spread. Two flavors:
- **Debit spread** (bull call / bear put) — pay a net debit; profit if your view
  plays out.
- **Credit spread** (bull put / bear call) — collect a net credit; profit if the
  short strike holds.

Canonical example below = **bull call spread** (bullish).

## Legs (bull call spread)

| Leg | Action | Type | Strike | Expiry |
|-----|--------|------|--------|--------|
| 1 | Long | Call | Lower (ITM/ATM) | Same |
| 2 | Short | Call | Higher (OTM) | Same |

## Max profit
**(Strike width) − Net debit paid** (× multiplier).
- Capped at the short strike.

## Max loss
**Net debit paid** (× multiplier).
- Capped — the most you can lose is what you paid.

## Breakeven
**Long strike + Net debit paid.**

## Greeks behavior (bull call)
- **Delta**: positive — moderately bullish, less than a naked long call.
- **Gamma**: small (legs offset).
- **Theta**: roughly neutral to slightly negative.
- **Vega**: reduced vs naked long call.

## Payoff shape (at expiry)
```
P&L
 │       ______  ← capped profit at/above short strike
 │     /
 │   /
 ├──/───────── Long strike ... Short strike
 │  ← capped loss = debit below long strike
```

## When to use
- Moderately directional view and want **defined risk / lower cost**.
- Want to dampen vega/theta vs a naked option.
- Fine capping upside in exchange for cheaper entry.

## Risks
- **Profit capped** — no home runs.
- **Early assignment** — on the short leg (American style), mostly ITM near expiry.
- **Liquidity** — two legs = two spreads to cross; trade liquid strikes.

## Example — SET50 / TFEX
- SET50 at 1,300; moderately bullish over 30 days.
- Buy call 1,300 (฿30), sell call 1,350 (฿12) → net debit ฿18.
- **Max profit**: (1,350 − 1,300) − 18 = ฿32 (per point).
- **Max loss**: ฿18 (the debit).
- **Breakeven**: 1,300 + 18 = **1,318**.
- Settle ≥ 1,350 → max profit. ≤ 1,300 → max loss. Between → partial.

### Bull put spread (credit, bullish)
Sell a higher-strike put, buy a lower-strike put.
- **Max profit**: net credit (price stays above the short put).
- **Max loss**: (width − credit).
- **Breakeven**: short put strike − credit.
- Use: moderately bullish; collect income, willing to buy at the short strike if
  it dips.

### Bear put spread (debit, bearish)
Buy a higher-strike put, sell a lower-strike put.
- **Max profit**: width − debit.
- **Max loss**: debit paid.
- **Breakeven**: long (higher) put strike − debit.
- Use: moderately bearish; cheaper than a naked long put.

### Bear call spread (credit, bearish)
Sell a lower-strike call, buy a higher-strike call.
- **Max profit**: net credit (price stays below the short call).
- **Max loss**: (width − credit).
- **Breakeven**: short call strike + credit.
- Use: moderately bearish / capped-upside; income-focused.

All four verticals share the same mechanics — same type, same expiry, two strikes
— differing only in view (bull/bear) and funding (debit/credit).

## Related
- [[Options Strategy]] · [[Options Chain]] (pick the two strikes via OI/IV) ·
  [[Greeks]] ([[Delta]]) · [[Strategy Payoff Table]]

## Sources
[^1]: `raw/options-strategies-overview.md`
[^2]: `raw/greeks-overview.md`
