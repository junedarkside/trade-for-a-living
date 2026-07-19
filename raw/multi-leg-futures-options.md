---
title: Multi-Leg Futures + Options — Study Plan
type: source
tags: [futures, options, derivatives, market/thailand]
---

# Multi-Leg Futures + Options — Study Plan

To plan multi-leg strategies that combine **futures and options**, you need a mix of
**conceptual knowledge**, **pricing/risk math**, and **execution/margin discipline**.

## 1. Core concepts you must know first

### Derivatives basics
- What **futures** and **options** are, how they settle, and the difference between:
  - Exchange-traded vs OTC
  - Physical vs cash settlement
  - American vs European exercise
- Contract specs for your market (e.g., SET50 futures/options):
  - Tick size, lot size, expiry cycle, trading hours, margin requirements.

### Payoff profiles
- Be able to draw and interpret:
  - Long/short futures payoff (linear)
  - Long/short call and put payoff (kinked)
  - Combined payoffs for common structures:
    - **Synthetic long/short** (long call + short put ≈ long future)
    - **Protective put on future** (long future + long put)
    - **Covered call on future** (long future + short call)
    - **Collar on future** (long future + long put + short call)

## 2. Key "building block" strategies with futures + options

### Futures + one option (2-leg)
- **Long future + long put** (protective put on future):
  - Bullish with defined downside.
  - Max loss ≈ (future entry − put strike) + premium.
- **Long future + short call** (covered call on future):
  - Mildly bullish income trade; upside capped at short call strike minus premium received.
- **Short future + long call** (protective call on short future):
  - Bearish with defined upside risk.
- **Short future + short put** (covered put on short future):
  - Mildly bearish income; downside capped at short put strike plus premium.

### Futures + two options (3-leg)
- **Futures collar**:
  - Long future + long put + short call.
  - Defines both maximum loss and maximum gain; often low net cost.
- **Risk reversal**:
  - Long future + short put + long call (or variations).
  - Used to create a leveraged directional view with some financing from the short option.

### Multiple expiries / strikes (advanced)
- **Calendar/diagonal structures** using options on futures:
  - E.g., sell near-term option, buy longer-term option on the same future.
  - Exploits time decay and term structure of volatility.

For each structure: write the net payoff formula, sketch the P&L diagram by hand,
and explain in one sentence what market view it expresses.

## 3. Pricing and "Greeks" you must understand

### Futures pricing
- Fair value: `F = S · e^((r − q)T)` where `S` = spot, `r` = risk-free rate,
  `q` = dividend yield (or convenience yield for commodities), `T` = time to expiry.
- Basis = futures − fair value; understanding **roll yield** and **term structure**
  (contango / backwardation).

### Options on futures
- Black-type model for options on futures; key inputs: futures price `F`,
  strike `K`, time `T`, volatility `σ`, rate `r`.
- Greeks for options on futures:
  - **Delta**: sensitivity to futures price.
  - **Gamma, theta, vega**: how curvature, time decay, and vol sensitivity behave.

### Net delta and hedging
- `Δ_total = Σ (leg quantity) × Δ_leg`.
- Make a position **delta-neutral** using futures; adjust delta as market moves (re-hedging).

## 4. Risk and margin: what you must study

### Risk metrics
- Max profit / max loss for each structure.
- **Break-even points** (often 1–2 levels depending on structure).
- Sensitivity to: underlying moves (delta), volatility changes (vega), time decay (theta),
  rate shifts (rho).

### Margin and capital
- Futures are margin-based; options: long = premium paid, short = margin required.
- Multi-leg packages often reduce margin via **spread offsets**.
- Study **portfolio margin** / **spread margin** for combined positions.
- **Legging in/out** vs sending a **multi-leg order** on margin and execution risk.

## 5. Execution: thinking in "packages," not legs

- Treat the structure as one position, not separate trades.
- Decide the **net price** for the whole package; use **multi-leg orders** where available.
- Advantages: reduces **legging risk**, often lowers commission, improves margin efficiency.
- Always check: net debit/credit, max loss, max profit, break-evens, leg liquidity.

## 6. Concrete study plan (4–8 weeks)

- **Weeks 1–2:** Futures mechanics, M&M; options basics; draw payoff diagrams.
- **Weeks 3–4:** Protective put, covered call, collars on futures; synthetic long/short.
- **Weeks 5–6:** Black model; delta, gamma, theta, vega; delta-neutral hedging.
- **Weeks 7–8:** Multi-leg order types, margin; risk management; design 2–3 complete strategies.

## 7. Resources

- Exchange education material (SET, CME, ASX) on options on futures.
- Broker whitepapers / webinars on multi-leg options, futures + options strategies.
- Books: Hull for pricing & Greeks; practical options strategy guides.

## Sources

[^1]: `raw/multi-leg-futures-options.md` (this file — synthesized from the article below).
[^2]: Hindu Business Line — "Mastering derivatives: how to optimally combine futures and options". https://www.thehindubusinessline.com/portfolio/commodity-analysis/mastering-derivatives-how-to-optimally-combine-futures-and-options/article65439357.ece
[^3]: youtube.com/watch?v=rJ2RXabZdvM — payoff diagrams reference.
[^4]: fxoptions.com — managing multi-leg options positions. https://www.fxoptions.com/managing-multi-leg-options-positions-techniques-for-complex-trades/
[^5]: asx.com.au — implementing multi-legged strategies. https://www.asx.com.au/investors/investment-tools-and-resources/online-courses/advancing-in-options-course/implementing-multi-legged-strategies
[^6]: investopedia.com — multi-leg order definition. https://www.investopedia.com/terms/m/multilegorder.asp
[^7]: fidelity.com — one-leg or two learning center. https://www.fidelity.com/bin-public/060_www_fidelity_com/documents/learning-center/3._One_Leg_or_Two_v3.pdf