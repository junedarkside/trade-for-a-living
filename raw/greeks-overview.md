---
title: Greeks — Overview
type: source
tags: [options, derivatives, greek/delta, greek/gamma, greek/theta, greek/vega, greek/rho]
---

# Greeks — Overview

**The Greeks** measure how an option's price (premium) reacts to changes in the
underlying inputs. They are the core risk-management toolkit for any options
trader.

## Quick reference

| Greek | Measures | Long call | Long put |
|-------|----------|-----------|----------|
| **Delta** | Price change per $1 move in underlying | Positive (0 to +1) | Negative (−1 to 0) |
| **Gamma** | Rate of change of delta per $1 move | Positive | Positive |
| **Theta** | Price decay per day (time passing) | Negative (loses) | Negative (loses) |
| **Vega** | Price change per 1% change in volatility | Positive | Positive |
| **Rho** | Price change per 1% change in interest rate | Positive | Negative |

## Delta (Δ)
- **Definition**: option price change for a 1-unit move in the underlying.
- **Read as probability**: |delta| ≈ rough probability of finishing ITM.
  - ATM call ≈ 0.50 delta.
- **Position delta**: sum across legs = directional exposure (share-equivalents).
- **Delta-hedging**: trade the underlying to bring net delta to ~0 (market-neutral).

## Gamma (Γ)
- **Definition**: how fast delta itself changes as spot moves.
- **Highest at ATM**, lowest deep ITM/OTM.
- **Risk**: high gamma = delta swings fast → hard to hedge, big moves hurt short
  gamma holders. Long options are **long gamma** (good in big moves).

## Theta (Θ)
- **Definition**: daily erosion of time value as expiration approaches.
- **Sign**: long options lose (negative theta); short options gain (positive
  theta).
- **Accelerates** in the last ~30 days, fastest for ATM options.
- **Income strategies** (covered calls, cash-secured puts) profit from theta.

## Vega (ν)
- **Definition**: sensitivity to **implied volatility** (IV). Price change per
  1-point change in IV.
- **Long options are long vega**: rising IV helps buyers, hurts sellers.
- **IV crush**: after earnings/events, IV drops → long options lose value even
  if direction is right.
- **Long straddle** needs rising IV *or* a big move to overcome theta.

## Rho (ρ)
- **Definition**: sensitivity to interest rates (per 1% change).
- **Usually minor** for short-dated options; matters more for LEAPS.
- Calls positive rho (rates up → call value up); puts negative.

## How Greeks evolve

- As **time passes**: theta drains long options; gamma concentrates near ATM.
- As **spot moves**: delta drifts (driven by gamma); ITM options approach ±1 delta.
- As **volatility moves**: vega dominates short-term P&L around events.
- Greeks of a **multi-leg** strategy = sum of each leg's Greeks.

## Why it matters

Strategy selection = picking a Greeks profile:
- Want income from time decay → **positive theta** (short options).
- Want to profit from a big move → **long gamma + long vega** (straddles).
- Want to cap downside → **long puts** (negative delta, positive gamma/vega).
