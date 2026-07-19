---
title: Moneyness
type: glossary
status: learning
aliases: [ITM, ATM, OTM]
tags: [options, derivatives]
---

# Moneyness

**The relationship between the strike price and the current spot price of the
underlying.** Determines whether an option has intrinsic value and how the
payoff behaves.

## Overview
Moneyness describes **where the strike sits relative to spot** — and it flips
direction depending on whether you hold a call or a put.

## Definitions

| State | Call (right to buy) | Put (right to sell) | Intrinsic value |
|-------|---------------------|----------------------|-----------------|
| **In-the-money (ITM)** | Spot > Strike | Spot < Strike | Yes |
| **At-the-money (ATM)** | Spot ≈ Strike | Spot ≈ Strike | ≈ 0 |
| **Out-of-the-money (OTM)** | Spot < Strike | Spot > Strike | No |

## How to read it

- **ITM** = the option would make money if exercised right now. Has intrinsic
  value.
- **ATM** = strike right at (or very near) spot. No intrinsic value, maximum
  extrinsic (time value).
- **OTM** = the option would not be exercised today. No intrinsic value; the
  premium is pure extrinsic (time + vol).

## Examples

| Spot | Strike | Call is | Put is |
|------|--------|---------|--------|
| 170 | 170 | ATM | ATM |
| 180 | 170 | ITM (intrinsic = 10) | OTM |
| 160 | 170 | OTM | ITM (intrinsic = 10) |

## Why it matters

- **Intrinsic value** = how much ITM the option is. See [[Intrinsic and Extrinsic Value]].
- **Time decay** is **fastest at ATM** (gamma is highest there).
- **Liquidity** is usually best at the strikes nearest the money.
- **Strategy choice** often starts here:
  - ITM long call ≈ stock replacement with defined risk + leverage.
  - ATM long straddle = pure volatility bet.
  - OTM short call = cheaper income, lower delta (less likely to be assigned).

## Related
- [[Options — Basics]] · [[Strike Price]] · [[Intrinsic and Extrinsic Value]] ·
  [[Premium]] · [[Delta]] (delta magnitude tracks moneyness)

## Sources
[^1]: `raw/options-basics.md`
[^2]: optionseducation.org — options basics.