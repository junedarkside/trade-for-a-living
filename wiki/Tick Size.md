---
title: Tick Size
type: glossary
status: learning
tags: [spot, futures, options, market/thailand]
---

# Tick Size

The **tick size** is the **minimum price increment** at which an instrument can
be quoted. Every price change must be a whole-number multiple of the tick.

## SET equities

- **Stocks ≥ ฿100**: tick = **฿0.01**
- **Stocks < ฿100**: tick scales with price band (often ฿0.001 to ฿0.05)

## TFEX futures

- **SET50 futures (S50)**: tick = **฿0.01 / index point**, multiplier **฿200**
  → minimum tick value = **฿2 / contract**.
- **Single-stock futures (SSF)**: tick = **฿0.01**, multiplier = 1,000 shares
  → minimum tick value = **฿10 / contract**.
- **USD/THB futures**: tick = **฿0.001**, multiplier = ฿500,000 → minimum tick
  value = **฿500 / contract**.

## TFEX options

- **SET50 index options**: tick = **฿0.01 / index point**, multiplier **฿200**
  → minimum tick value = **฿2 / contract**.

## Why ticks matter

- **Liquidity quote** — depth-at-best-bid divided by tick value = how many
  contracts can be filled at the inside before stepping down.
- **Edge erosion** — for low-premium options, wide ticks vs premium ratio means
  the bid-ask eats most of the edge.
- **Order placement** — never quote at a price that's not on the tick grid —
  it won't fill and may be rejected.

## Related
- [[Spot — Basics]] · [[Board Lot]] · [[Bid-Ask Spread]]

## Sources
[^1]: `raw/spot-basics.md`
[^2]: TFEX — contract specifications (S50, SSF, USDTHB).
