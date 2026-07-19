---
title: Options — Basics
type: concept
status: learning
tags: [options, derivatives]
---

# Options — Basics

**An option is a standardized contract giving the buyer the right (not the
obligation) to buy or sell an underlying asset at a fixed price before or on a
set date.** The buyer pays a **premium**; the seller (writer) collects it and
takes the obligation.

## Overview
Options are the atoms from which every options strategy is built
([[Long Call]], [[Short Call]], [[Long Put]], [[Short Put]] → multi-leg →
multi-strategy). Before any strategy makes sense, internalize the four
building blocks and the core vocabulary on this page.

## What an option has

| Component | Description |
|-----------|-------------|
| **Underlying** | Stock, index, ETF, future, commodity. |
| **Contract size** | 1 equity option = 100 shares (TFEX S50 options = ฿200/index point). |
| **Expiration** | Last day the option can be exercised. Equity options expire 3rd Friday of month (often weekly available). |
| **Style** | **American** = exercise any time up to expiry (most equity options). **European** = exercise only at expiry (most index options). |

## Calls vs. puts

| | Call | Put |
|---|------|-----|
| Holder's right | **Buy** at strike | **Sell** at strike |
| Buyer wants | Price ↑ | Price ↓ |
| Seller obligated to | **Sell** if assigned | **Buy** if assigned |

See [[Long Call]], [[Short Call]], [[Long Put]], [[Short Put]] for the four
building-block positions.

## Key terms

- [[Strike Price]] — the fixed buy/sell price if exercised.
- [[Premium]] — what the buyer pays (seller collects); price per share × 100 = contract cost.
- [[Moneyness]] — ITM / ATM / OTM (where the strike sits relative to spot).
- [[Intrinsic and Extrinsic Value]] — intrinsic = immediate exercise value; extrinsic = the rest (time + vol).
- **Expiration** — last valid day; weekly or monthly cycles (see [[Options Chain]]).
- **Assignment** — seller being obliged to deliver (call) or take delivery (put) on exercise.

## Why people use options

| Objective | Pattern |
|-----------|---------|
| **Speculation** | Directional bet with limited capital ([[Long Call]] vs buying stock). |
| **Hedging** | Insure an existing position ([[Protective Put]]). |
| **Income** | Sell premium against holdings ([[Covered Call]], [[Cash-Secured Put]]). |
| **Leverage** | More exposure per dollar of capital. |

## Why options are risky

- **Total loss of premium** — long options can expire worthless.
- **[[Theta|Time decay]]** erodes long-option value daily.
- **Volatility shocks** move premiums even if the underlying doesn't.
- **Short options** can have very large or undefined losses (margin required).
- Regulatory disclosure (OCC "Characteristics and Risks of Standardized Options")
  is mandatory before approval to trade.

## Quick numerical example (long call)

- Stock = ฿170. Buy 1 ATM call, strike ฿170, 1 month. Premium = ฿3.50/share.
- **Cost** = 3.50 × 100 = **฿350**.
- At expiry, stock = ฿180 → intrinsic = 10 → option value = ฿1,000 → **profit ฿650**.
- At expiry, stock = ฿165 → expires worthless → **loss ฿350** (the premium).

Shows limited loss + leveraged upside. The same logic inverts for puts (subtract).

## Where to go next

- **Pick a side** → [[Long Call]] (bullish) · [[Short Put]] (bullish income) ·
  [[Long Put]] (bearish) · [[Short Call]] (bearish income, naked).
- **Build a strategy** → [[Options Strategy]] (decision guide) ·
  [[Multi-Strategy Options]] (combining).
- **Manage risk** → [[Greeks]] ([[Delta]], [[Gamma]], [[Theta]], [[Vega]]) ·
  [[Options Chain]] (read the market) ·
  [[Strategy Payoff Table]] (compare at a glance).

## Related
- [[Options Strategy]] · [[Options Chain]] · [[Multi-Strategy Options]] ·
  [[Greeks]] · [[Strategy Payoff Table]] ·
  [[Long Call]] · [[Short Call]] · [[Long Put]] · [[Short Put]]

## Sources
[^1]: `raw/options-basics.md`
[^2]: investopedia.com — options basics tutorial.
[^3]: optionseducation.org — options basics.
[^4]: optionsplaybook.com — options introduction.