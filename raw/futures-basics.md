---
title: Futures — Basics
type: source
tags: [futures, derivatives]
---

# Futures — Basics

A **futures contract** is a binding agreement to buy or sell an underlying asset
at a fixed price on a set future date. Unlike options, **both sides are
obligated** — no premium, symmetric P&L.

## Key terms

- **Contract size / multiplier**: e.g. SET50 index futures (TFEX **S50**) have a
  fixed multiplier per index point.
- **Tick size / tick value**: minimum price increment and its money value.
- **Margin**: not full notional — you post **initial margin** (good-faith deposit)
  and must hold **maintenance margin**. A loss below maintenance triggers a
  **margin call** (top-up).
- **Mark-to-market (MTM)**: P&L settled daily into your account.
- **Notional value**: contract size × price.

## Long vs short

| Position | Obligation | Profits when |
|----------|-----------|--------------|
| **Long** | Buy at fixed price at expiry | Price rises |
| **Short** | Sell at fixed price at expiry | Price falls |

Leverage is inherent: small margin controls large notional → gains and losses
amplified.

## The term structure

The curve = futures prices across expirations.

| Structure | Shape | Meaning |
|-----------|-------|---------|
| **Contango** | Upward-sloping (later > sooner) | Cost of carry normal; longs roll at a loss |
| **Backwardation** | Downward-sloping (later < sooner) | Scarcity / strong demand; longs roll at a gain |

Roll yield matters for anyone holding futures past expiry: rolling a long in
contango costs money ("roll bleed"); backwardation pays you.

## Settlement

- **Physical delivery**: deliver/receive the actual asset (commodities, some
  bonds). Most retail avoid by rolling before delivery month.
- **Cash settlement**: settle the P&L in cash at expiry. Common for **index**
  futures (no deliverable) — e.g. SET50 index futures settle to the index value.

## Thailand context (TFEX)

- **TFEX** = Thailand Futures Exchange (under SET group). Products include:
  **SET50 index futures (S50)**, **SET50 index options**, single-stock futures
  on blue-chip SET names, and gold/oil-linked contracts.
- S50 futures are **cash-settled** to the SET50 index — primary leveraged tool
  for directional SET50 exposure.
- Margin set by TFEX/broker; intraday vs overnight rates differ.

## Futures vs options (quick)

| | Futures | Options |
|---|---------|---------|
| Obligation | Both sides | Buyer only has right |
| Premium | None (margin only) | Buyer pays premium |
| P&L | Symmetric, linear | Asymmetric for buyer |
| Greeks | Linear delta = 1, no gamma/vega | Full Greek profile |
