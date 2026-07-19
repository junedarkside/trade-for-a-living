---
title: Options — Basics
type: source
tags: [options, derivatives]
---

# Options — Basics

An **option** is a contract giving the buyer the right (not the obligation) to
buy or sell an underlying asset at a fixed **strike price** on or before an
**expiration date**. The buyer pays a **premium**; the seller (writer) collects it.

## The two types

| Type | Right | Buyer wants |
|------|-------|-------------|
| **Call** | Right to **buy** at strike | Price to rise |
| **Put** | Right to **sell** at strike | Price to fall |

- **Buy call** → bullish. **Sell (write) call** → neutral to bearish (collect premium).
- **Buy put** → bearish. **Sell (write) put** → neutral to bullish (collect premium).

## Key terms

- **Underlying**: the asset the option is on (stock, index, futures contract).
- **Strike price**: the fixed buy/sell price.
- **Expiration**: last day the option is valid. Index/settled options often
  cash-settle; equity options physically settle into shares.
- **Premium**: price of the option. Buyer's max loss; seller's max gain (naked).
- **Contract size**: equity options usually = 100 shares per contract.
- **Premium**: paid upfront; quoted per share.

## Moneyness

| State | Call | Put |
|-------|------|-----|
| **ITM** (in the money) | Spot > Strike | Spot < Strike |
| **ATM** (at the money) | Spot ≈ Strike | Spot ≈ Strike |
| **OTM** (out of the money) | Spot < Strike | Spot > Strike |

Intrinsic value = ITM amount. Time value = Premium − Intrinsic. ATM options have
the most time value (and the most time decay).

## Exercise & assignment

- **Exercise**: buyer invokes the right → counter-party (seller) is **assigned**.
- **American** options: exercisable any time before expiry (early-assignment risk).
- **European** options: exercisable only at expiry (no early assignment).
- Most equity options are American. Index options (e.g. SPX, and SET50-index
  products) are often European / cash-settled.

## Styles relevant to Thailand

- **TFEX** (Thailand Futures Exchange) lists **SET50 index options** (ticker **S50**)
  — European-style, cash-settled, on the SET50 index.
- Single-stock options on SET names are more limited than US markets; check your
  broker's product list.

## What drives premium

Price of an option depends on: underlying price, strike, time to expiry,
volatility, interest rate, dividends. These sensitivities are **the Greeks** —
see [[Greeks]] / `greeks-overview.md`.
