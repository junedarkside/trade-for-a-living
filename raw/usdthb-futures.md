---
title: USD/THB Futures
type: source
tags: [futures, derivatives, market/thailand]
---

# USD/THB Futures (TFEX) — Contract Spec & Expiration

```yaml
Exchange: TFEX
Asset Class: Currency Futures
Underlying: USD/THB
Contract Size: 1000 USD
Tick Size: 0.01 THB
Tick Value: 10 THB
Settlement: Cash
Multiplier: 1000
Currency: THB
Margin: Variable (SPAN)
Trading Sessions:
  - Morning
  - Afternoon
  - Night
Expiration:
  - 3 nearest months
  - Next quarterly month
Options Available: Yes (European style)
```

## Last Trading Day

Contract expires on **the business day immediately preceding the last
business day of the contract month**. Trading for the expiring contract
**stops at 11:00 AM Bangkok time** on that day. [^1]

| Contract Month | Last Business Day | Last Trading Day      |
| -------------- | ----------------- | --------------------- |
| July           | Thu 31 Jul        | Wed 30 Jul (11:00 AM) |
| August         | Fri 29 Aug        | Thu 28 Aug (11:00 AM) |
| September      | Tue 30 Sep        | Mon 29 Sep (11:00 AM) |

*(Exact date depends on weekends and Thai public holidays.)*

## At expiration

- **Cash settlement only** — no physical USD delivery.
- P&L automatically settled in THB.
- Final settlement price = **WM/Reuters USD/THB reference rate at 11:00 AM**
  on the last trading day. [^1]

## Roll convention

Most active traders **don't hold until expiration**. Instead, **roll** into the
next month's contract a few days before expiry:

- Roll **3–5 trading days before expiration**, or
- Roll when **next contract's volume / OI exceeds the current contract's**.

Example: long **USDQ26** (Aug) → sell USDQ26, buy **USDU26** (Sep). Maintains
exposure without interruption.

Systematic trend-following backtests / live systems **must** include a roll
rule — otherwise backtest fills use illiquid expiring contract prices.

## Sources

[^1]: TFEX — USD/THB Futures Contract Specification.
    https://www.tfex.co.th/en/products/currency/usd-thb-futures/contract-specification
