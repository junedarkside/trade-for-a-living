---
title: Board Lot
type: glossary
status: learning
tags: [spot, market/thailand]
---

# Board Lot

The **board lot** is the **minimum trade size** permitted on the SET. Round
lots are standard; **odd lots** (less than one board lot) trade on a separate
board with worse liquidity and usually worse prices.

## SET board lot rules

The lot size scales with the stock price band (SET adjusts periodically):

| Price band (Baht) | Board lot (shares) |
|---|---|
| 0.01 – 0.50 | 100 |
| 0.50 – 2.00 | 50 |
| 2.00 – 5.00 | 10 |
| 5.00 – 10.00 | 5 |
| 10.00 – 25.00 | 1 |
| 25.00 – 100.00 | (varies — common 100) |
| 100.00 – 200.00 | 50 |
| 200.00 – 500.00 | 20 |
| 500.00 – 1,000.00 | 10 |
| 1,000.00+ | 2 |

## Why it matters

- **Liquidity** — odd-lot fills widen the effective [[Bid-Ask Spread]]; avoid
  them on entries/exits unless deliberately accumulating odd shares.
- **Sizing** — position sizing math must round to a whole board lot or the
  broker will reject the order.
- **Index replication** — SET50 / SET100 ETFs and futures use baskets sized to
  round lots. Drift between basket and index happens when constituents change
  price band.

## Related
- [[Spot — Basics]] · [[Tick Size]] · [[Settlement]]

## Sources
[^1]: `raw/spot-basics.md`
[^2]: SET — board lot and price-band rules.
