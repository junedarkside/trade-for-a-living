---
title: Futures — Basics
type: concept
status: learning
tags: [futures, derivatives, market/thailand]
aliases: [Futures, Futures Contract, S50, TFEX]
---

# Futures — Basics

A **futures contract** is a **binding agreement** to buy or sell an underlying
asset at a fixed price on a set future date. **Both sides are obligated** —
unlike an option there is no premium to pay up-front and no "right without
obligation." P&L is **symmetric** and **linear** in the underlying.

## Overview

A futures position is **delta-one with leverage**. The full notional is not
posted — only **margin** — so gains and losses are amplified by the leverage
ratio. Daily **mark-to-market (MTM)** realises P&L into the account each
session. This is what differentiates futures from spot (no margin, no daily
settlement) and from options (asymmetric, non-linear, premium-based).

## Key building blocks

| Term | What it means |
|------|---------------|
| **Contract size / multiplier** | Deliverable per contract. SET50 (S50) = ฿200 / index point. Single-stock futures (SSF) = 1,000 shares. USD/THB = ฿500,000 notional. |
| [[Tick Size\|**Tick size / tick value**]] | Minimum price increment × multiplier = money value per tick. S50 = ฿2 / contract. |
| **Margin** | Initial (good-faith deposit) + maintenance (floor). Loss past maintenance = **margin call**. See [[Margin Mechanics]] _(Phase B article)_. |
| **Mark-to-market (MTM)** | P&L settled into cash every end-of-day. You realise gains/losses without closing. |
| **Notional value** | Contract size × price. E.g. 1 S50 contract at index 25,500 = ฿5,100,000 notional. |
| **Leverage ratio** | Notional ÷ margin. S50 ≈ 25–30× at typical margin. |

## Long vs short

| Position | Obligation | Profits when |
|----------|-----------|--------------|
| **Long** | Buy at fixed price at expiry | Price **rises** |
| **Short** | Sell at fixed price at expiry | Price **falls** |

Leverage is inherent: small margin controls large notional. **Both directions
have unlimited loss potential** in theory (gap risk vs maintenance margin in
practice).

## Term structure

The **futures curve** = prices across expirations. Shape encodes
cost-of-carry / scarcity:

| Structure | Shape | Meaning | [[Roll Yield\|Roll]] for long |
|-----------|-------|---------|----------|
| [[Contango]] | Upward-sloping (later > sooner) | Cost-of-carry normal, ample supply | **Negative** (you pay to roll) |
| [[Backwardation]] | Downward-sloping (later < sooner) | Scarcity / strong nearby demand | **Positive** (you earn to roll) |

Rolling a long in contango is the well-known "roll bleed" that drags on
long-only futures returns — see [[Basis]] for the spot–futures relationship.

## Settlement

| Type | How it works | Examples |
|------|--------------|----------|
| **Cash settlement** | Settle the P&L in cash at expiry. No asset moves. | **SET50 index futures (S50)** — settle to SET50 closing value. |
| **Physical delivery** | Deliver / receive the actual asset. Most retail rolls before delivery month. | Single-stock futures (SSF) — 1,000 shares; USD/THB — actual FX; commodities. |

## Thailand context (TFEX)

- **TFEX** = **Thailand Futures Exchange**, under the SET group.
- Core products:
  - **SET50 index futures (S50)** — cash-settled, primary leveraged tool for
    directional SET50 exposure.
  - **Single-stock futures (SSF)** on blue-chip SET names — physical delivery of
    1,000 shares.
  - **USD/THB futures** — FX exposure with ฿500,000 notional.
  - Gold futures, agricultural futures, sector index futures.
  - **SET50 index options** (see [[Options — Basics]]).
- **Margin** set by TFEX / your broker; intraday vs overnight rates differ —
  paying only intraday margin roughly halves the capital required for day
  trades, but the position **must be flat by session close or the broker
  collects overnight margin**.
- **Trading hours** cover day + night sessions (Asian + European hours
  overlap). See TFEX contract specs for each product.

## Futures vs options vs spot

| | [[Spot — Basics\|Spot]] | Futures | [[Options — Basics\|Options]] |
|---|------|--------|---------|
| Obligation | None post-settle | Both sides | Buyer has right, seller has obligation |
| Premium | None | None (margin only) | Buyer pays premium |
| P&L | Linear, no leverage | Linear, leveraged | Asymmetric, non-linear |
| Greeks | N/A | Linear delta = 1, no gamma/vega | Full Greek profile (Δ, Γ, Θ, ν, ρ) |
| Settlement | T+2 ([[Settlement]]) | Daily MTM + final | Exercise / expiry |
| Max loss | Position value | Position value (more on margin) | Premium (long) / margin (short) |

## Worked example — TFEX S50 futures

- Index at **25,500**. You buy **1 S50 contract** (multiplier ฿200).
- **Notional** = 25,500 × 200 = **฿5,100,000**.
- **Initial margin** ≈ ฿200,000 (≈ 4% of notional) → leverage ≈ **25.5×**.
- Index rises to **25,700**:
  - **MTM gain** = (25,700 − 25,500) × 200 = **+฿40,000** (one day, no close).
  - On **margin ฿200,000**, that's a **20% return on margin** for a 0.78% move
    in the underlying.
- Index drops to **24,500** before you stop out:
  - **MTM loss** = (24,500 − 25,500) × 200 = **−฿200,000** — margin call, full
    margin gone on a 3.9% drop. **Liquidation is the cap on loss, not the
    notional.**

> Same mechanical pattern on SSF, USD/THB, gold. **Always know the multiplier,
> tick value, and margin schedule before sizing.**

## Related
- [[Spot — Basics]] · [[Options — Basics]] · [[Options Strategy]] ·
  [[Contango]] · [[Backwardation]] · [[Basis]] · [[Roll Yield]] ·
  [[Margin Mechanics]] _(Phase B article)_ · [[Settlement]] · [[Tick Size]] ·
  [[Delta-Neutral Hedging]] · [[Synthetic Futures]]

## Sources
[^1]: `raw/futures-basics.md`
[^2]: TFEX — contract specifications (S50, SSF, USDTHB, gold).
