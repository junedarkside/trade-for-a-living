---
title: Order Types
type: source
tags: [spot, futures, options, derivatives]
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

For Thai market (SET) and TFEX:
- Day orders auto-cancel at session close.
- GTC is supported on most products (check broker).
- IOC / FOK availability varies by broker / exchange.

## Advanced order types

| Type | Use |
|------|-----|
| **Iceberg / hidden** | Display only small portion; used to mask size |
| **TWAP** (time-weighted avg price) | Slice order over time; reduce market impact |
| **VWAP** (volume-weighted avg price) | Match typical volume profile |
| **Trailing stop** | Stop follows price by fixed amount/percentage |
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

## Sources

[^1]: SET — Order types and trading rules.
    https://www.set.or.th/en/trading/trading-system
[^2]: TFEX — Order entry rules per contract.
    https://www.tfex.co.th/en/
[^3]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 3
    (mechanics of futures markets).
[^4]: Investopedia — Types of Orders.
    https://www.investopedia.com/terms/o/order-types.asp
