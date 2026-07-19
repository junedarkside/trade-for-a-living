---
title: Greeks
type: concept
status: reviewed
tags: [options, derivatives, greek/delta, greek/gamma, greek/theta, greek/vega, greek/rho]
---

# Greeks

**The Greeks** measure how an option's premium reacts to changes in the
underlying inputs. They are the core risk-management toolkit for any options
trader. Strategy selection = picking a Greeks profile.

## Quick reference

| Greek | Measures | Long call | Long put |
|-------|----------|-----------|----------|
| **[[Delta]]** | Price change per $1 move in underlying | Positive (0 to +1) | Negative (−1 to 0) |
| **[[Gamma]]** | Rate of change of delta per $1 move | Positive | Positive |
| **[[Theta]]** | Price decay per day (time passing) | Negative (loses) | Negative (loses) |
| **[[Vega]]** | Price change per 1% change in volatility | Positive | Positive |
| **[[Rho]]** | Price change per 1% change in interest rate | Positive | Negative |

## At a glance — what each tells you

- **Delta** — directional exposure (and ~prob. of finishing ITM). Position delta
  = your "share-equivalent" exposure.
- **Gamma** — how stable your delta is. High gamma near ATM; long options are
  long gamma (good in big moves).
- **Theta** — the cost of holding options over time. Income strategies profit
  from positive theta.
- **Vega** — volatility exposure. Watch for **IV crush** after events.
- **Rho** — interest-rate sensitivity (usually minor except for long-dated).

## Greek-driven strategy choice

| Want | Greeks profile | Strategies |
|------|---------------|------------|
| Income from time decay | +Theta (short options) | [[Covered Call]], [[Cash-Secured Put]] |
| Big move either way | +Gamma, +Vega | [[Long Straddle]] |
| Capped downside | +Gamma, +Vega (long puts) | [[Protective Put]] |
| Defined-risk directional | balanced, reduced cost | [[Vertical Spread]] |

## Evolution over time
- Time passes → theta drains long options; gamma concentrates near ATM.
- Spot moves → delta drifts (driven by gamma); ITM options approach ±1 delta.
- Volatility moves → vega dominates short-term P&L around events.
- Multi-leg Greeks = sum of each leg's Greeks — see [[Position Greeks]] for the
  full framework (Taylor expansion, hedge sizing, design patterns).

## From theory to practice
- For the trader-focused view (sizing, hedging, trade templates, pre-trade
  checklists, common mistakes), see [[Greeks in Practice]].

## Example — SET50 context

S50 ATM call: **spot 890, strike 900, 30 DTE, σ = 20%, r = 1.5%**.

| Greek | Value | Interpretation |
|-------|-------|----------------|
| **Delta** | +0.42 | Position moves ฿84/point (0.42 × ฿200 multiplier) |
| **Gamma** | +0.018 | Delta changes 0.018 per 1-point move in S50 |
| **Theta** | −0.35 pts/day | Loses ≈ ฿70/day (0.35 × ฿200) from time decay |
| **Vega** | +0.62 pts / 1% vol | Gains ฿124 per +1 vol-point move in IV |
| **Rho** | +0.08 | Minor; ฿16 per +1% rate move |

**Reading:** if S50 rallies 10 points → delta gain ≈ 4.2 index points (฿840).
But gamma will push delta to ~0.60, so a further 10-point rally earns even more.
If market flat for 7 days → theta costs ≈ ฿490 regardless of direction.

## Sources
[^1]: `raw/greeks-overview.md`
[^2]: `raw/greeks-trading-practice.md`
[^3]: youtube.com — Greeks primer + position Greeks walkthrough.
