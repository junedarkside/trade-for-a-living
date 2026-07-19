---
title: Order Types
type: concept
status: learning
tags: [spot, futures, options, derivatives]
aliases: [Order, Market Order, Limit Order, Stop Order, GTC]
---

# Order Types

Order types define **how** an order is submitted, matched, and (if necessary)
triggered. Choosing the right order type is the cheapest edge in execution.

## Basic order types

| Type | Behaviour | Fill guarantee | Price guarantee |
|------|-----------|----------------|-----------------|
| **Market** | Fill at best available price now | Yes | No (slippage possible) |
| **Limit** | Fill at your price or better | No (may not fill) | Yes |
| **Stop (stop-market)** | Triggers a **market** order at stop price | Triggered → market | Triggered → no |
| **Stop-limit** | Triggers a **limit** order at stop price | No (may miss entirely) | Yes (if triggered) |

## Time-in-force

| TIF | Behaviour |
|-----|-----------|
| **Day** | Valid only for current session |
| **GTC** (Good-Till-Cancelled) | Stays open until filled or cancelled |
| **IOC** (Immediate-Or-Cancel) | Fill what you can now, cancel rest |
| **FOK** (Fill-Or-Kill) | Fill entire order immediately or cancel |

## Advanced order types

| Type | Use |
|------|-----|
| **Iceberg / hidden** | Display only small portion; mask size |
| **TWAP** (time-weighted avg price) | Slice order over time; reduce impact |
| **VWAP** (volume-weighted avg price) | Match typical volume profile |
| **Trailing stop** | Stop follows price by fixed amount / percentage |
| **OCO** (one-cancels-other) | Two linked orders; fill one cancels the other |

These are typically only available through broker APIs, not basic ticket
entry.

## Risk notes per type

- **Market** — pays the [[Bid-Ask Spread]] (potentially more if multiple
  price levels crossed). Don't use on illiquid names or wide-spread options.
- **Limit** — may never fill if price doesn't reach. Use for patient entries
  and exits.
- **Stop** — in fast markets, the triggered market order can fill far from
  the stop. Stop-limits can miss entirely.
- **GTC** — accumulates in your book. Audit periodically; stale GTC orders
  cause unexpected fills when conditions return.

## Order type selection by use case

| Use case | Best type |
|----------|-----------|
| Enter a liquid name at fair value | **Limit** at mid or slightly worse |
| Exit fast (stop-loss) | **Stop-market** or hard mental stop |
| Catch a breakout | **Stop** above resistance (expect slippage) |
| Protect profit on a winning trade | **Trailing stop** |
| Avoid signalling (large size) | **Iceberg** |
| Reduce impact on a big order | **TWAP / VWAP** (institutional) |

## Thai-market specifics

- **SET cash equities** — market, limit, stop, stop-limit, GTC supported.
  Day orders by default.
- **TFEX futures / options** — limit orders strongly recommended (no
  market order for options on most Thai platforms). Day orders default;
  GTC for next-session open on select contracts.
- **Auction periods** — morning pre-open uses a call auction; limit orders
  submitted during pre-open execute at the auction clearing price.

## Worked example — S50 option entry

- Goal: long 25,500 call, premium mid = ฿85, spread = ฿2.
- **Limit ฿85** (mid): fill at mid or better; may take minutes to hours.
- **Limit ฿87** (2 ticks through mid): fill likely fast; pays ฿4 extra.
- **Market**: fills immediately at ask (฿87), pays ฿2 spread = ฿4 extra.

For a 10-contract order, ฿4 / contract extra = **฿800 / leg** in execution
cost. On a ฿200 multiplier, 0.02 index points. Limit beats market by ~0.01
point over the trade. Over hundreds of trades, the cost compounds.

## Related

- [[Bid-Ask Spread]] · [[Settlement]] · [[Options Risk Management]] ·
  [[Tick Size]] · [[Spot — Basics]] · [[Futures — Basics]] ·
  [[Options Strategy]]

## Sources

[^1]: `raw/order-types.md`
[^2]: SET — Order types and trading rules.
    https://www.set.or.th/en/trading/trading-system
[^3]: TFEX — Order entry rules per contract.
    https://www.tfex.co.th/en/
[^4]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 3
    (mechanics of futures markets).
[^5]: Investopedia — Types of Orders.
    https://www.investopedia.com/terms/o/order-types.asp
