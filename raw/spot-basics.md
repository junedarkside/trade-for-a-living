---
title: Spot — Basics
type: source
tags: [spot]
---

# Spot — Basics

The **spot** (cash) market is where you buy or sell the actual asset for
immediate settlement — e.g. SET-listed shares, ETF units. No leverage unless you
trade on margin. The foundation: derivatives (futures, options) are priced
*against* the spot.

## Key terms

- **Board lot**: minimum trade size (e.g. SET uses lot sizes that vary by price).
- **Tick size**: minimum price increment.
- **Settlement**: T+2 on the SET for equities (trade day + 2 business days).
- **Bid / ask**: best buy / sell prices; **spread** = the gap (liquidity proxy).
- **Commission + fees**: broker fee, exchange fee, clearing (varies by broker).

## Order types

| Order | Meaning |
|-------|---------|
| **Market** | Fill at best available price (immediate, price not guaranteed) |
| **Limit** | Fill only at your price or better (price guaranteed, fill not) |
| **Stop** | Triggers a market order once a stop price is hit |
| **Stop-limit** | Triggers a limit order at the stop price |
| **GTC / Day** | Good-till-cancelled / good-for-day |

## SET specifics (Thailand)

- Trading hours (cash equities): morning + afternoon sessions; pre-open auction.
- Price limits: daily **ceiling/floor** (± a percentage of prior close) cap
  intraday moves.
- **Credit Balance** / settlement via Thailand Securities Depository (TSD).
- Foreign-investor limits and the **Thai NVDR** (non-voting depository receipt)
  for foreign access without board-seat restrictions.

## Why spot matters for a derivatives trader

- Futures and options are priced off the **spot** + cost of carry.
- Hedging a derivatives position often means buying/shorting spot (or the
  reverse).
- **Arbitrage** between spot and futures/options keeps prices aligned.
- Spot positions are the "delta-one" baseline before adding convexity (options).

## Related

- [[Options — Basics]], [[Futures — Basics]]
