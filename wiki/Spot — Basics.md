---
title: Spot — Basics
type: concept
status: learning
tags: [spot, derivatives, market/thailand]
aliases: [Spot, Cash Market, Equities, SET]
---

# Spot — Basics

The **spot** (cash) market is where the actual asset changes hands for
**immediate settlement**. On the SET this is T+2 for equities. No leverage by
default — you put up full notional (margin optional). Spot is the **foundation**:
every derivative ([[Futures — Basics|futures]], [[Options — Basics|options]]) is
priced *against* the spot plus a cost-of-carry / time / volatility adjustment.

## Overview

A spot position is **delta-one** by definition — your P&L tracks the underlying
1-for-1. Options and futures add convexity, leverage, or both. Spot is the
baseline from which you add risk layers, and the instrument you reach for when
hedging or arbitraging derivatives.

## Key building blocks

| Term | What it means |
|------|---------------|
| [[Board Lot]] | Minimum trade size on SET (lot size varies by price band). |
| [[Tick Size]] | Minimum price increment (e.g. SET equities tick = ฿0.01 for prices ≥ ฿100). |
| [[Bid-Ask Spread]] | Gap between best buy and best sell — liquidity proxy. |
| [[Settlement]] | T+2 for SET equities via Thailand Securities Depository (TSD). |
| **Notional** | Full position size in cash terms (no leverage unless margined). |
| **Commission + fees** | Broker fee + exchange fee + clearing + VAT (varies by broker). |

## Order types

| Order | Behaviour | Use when |
|-------|-----------|----------|
| **Market** | Fill at best available price now. Price **not** guaranteed — slippage possible. | Need immediate fill; liquidity is fine. |
| **Limit** | Fill at your price or better. Price guaranteed, fill **not**. | Patient entry, defining exit. |
| **Stop** | Triggers a market order once stop price is hit. | Stop-loss on a long, breakout entry. |
| **Stop-limit** | Triggers a limit order at stop price. | Avoid slippage on stop, accept miss risk. |
| **GTC / Day** | Good-till-cancelled / good-for-day. | Default time-in-force choice. |

> **Risk note:** stop orders do **not** guarantee execution price in fast markets —
> they convert to market orders on the trigger. Stop-limits can miss the fill
> entirely. Neither protects against gap risk overnight.

## SET specifics (Thailand)

- **Trading hours** — morning session (regular + pre-open auction) + afternoon
  session. After-hours / off-exchange exists but is thin.
- **Price limits** — daily **ceiling/floor** band relative to prior close caps
  intraday moves. Hitting the ceiling/floor halts trading temporarily.
- **Settlement** — T+2 via **TSD** (Thailand Securities Depository). Cash leg and
  share leg settle two business days after trade.
- **[[NVDR|Non-Voting Depository Receipt]]** — Thai wrapper for foreign investors
  who want SET exposure without the foreign-ownership limit per board seat.
- **Foreign-investor limits** — per-issuer caps on combined foreign holding
  (typically 49% unless company articles differ).

## Why spot matters for a derivatives trader

1. **Pricing anchor** — futures and options are priced off spot + carry ([[Basis]],
   [[Contango]]/[[Backwardation]]).
2. **Hedging tool** — delta-hedging an option book is done by buying/shorting
   spot (or the underlying future, which is usually cheaper).
3. **Arbitrage** — spot–futures basis must stay within the cost-of-carry band, or
   there's a trade. Index arbitrage links SET50 spot basket to S50 futures.
4. **Convexity baseline** — spot is the delta-one position. Adding [[Options
   — Basics|options]] introduces convexity (gamma, vega) on top.
5. **Income / carry** — owning spot stock is the foundation of [[Covered Call]],
   [[Collar]], and any premium-selling strategy that needs the underlying to
   deliver.

## Spot vs. futures vs. options (one-line each)

| | Spot | [[Futures — Basics|Futures]] | [[Options — Basics|Options]] |
|---|------|--------|---------|
| Leverage | None (unless margin) | Built-in via margin | Built-in via premium |
| Settlement | T+2 | Daily mark + final | Exercise / expiry |
| Max loss | Position value | Position value (more on margin) | Premium (long) / margin (short) |
| Cash flow | Bid-ask spread + fees | Roll yield + basis | Theta + IV changes |

## Related
- [[Futures — Basics]] · [[Options — Basics]] · [[Options Strategy]] ·
  [[Risk Management]] · [[NVDR]] · [[Board Lot]] · [[Tick Size]] ·
  [[Bid-Ask Spread]] · [[Settlement]]

## Sources
[^1]: `raw/spot-basics.md`
