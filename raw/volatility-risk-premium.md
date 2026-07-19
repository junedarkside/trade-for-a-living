---
title: Volatility Risk Premium
type: source
tags: [options, derivatives]
---

# Volatility Risk Premium (VRP)

The **Volatility Risk Premium (VRP)** is the persistent tendency for **implied
volatility (IV)** in options to be **higher than the realized volatility (RV)**
that actually occurs over the same period. Options are often priced as if the
market expects more movement than eventually happens, and sellers of
volatility are "paid" a premium for bearing that risk. [^1]

## What VRP measures

- **Implied volatility (IV)** — market's expectation of future volatility, backed
  out from option prices (e.g., via Black-Scholes). Reflects fear, hedging
  demand, and supply/demand for options. [^2]
- **Realized volatility (RV)** — actual historical volatility over a period,
  measured as standard deviation of returns. [^3]
- **VRP** — the difference between IV and RV over the same horizon.

**Volatility version:** `VRP = IV − RV`
**Variance version (Variance Risk Premium):** `VRP_var = Implied Variance − Realized Variance` (variance = vol²). [^4]

- Positive VRP = options "expensive" relative to what happened.
- Negative VRP = options "cheap" relative to realized moves. [^5]

## Why VRP exists

- **Insurance demand** — hedgers pay up for puts (especially OTM puts), pushing
  IV higher than RV. [^6]
- **Risk aversion** — participants overpay for downside protection; sellers bear
  tail risk and get compensated. [^7]
- **Leverage / constraints** — some players can't hold large short-vol (margin,
  risk limits), so those who can demand premium. [^3]

Historically positive on equity indices.

## Calculation in practice

1. Pick a horizon (e.g., 30 days).
2. **IV** — ATM option IV for that horizon (e.g., 30-day ATM IV from index
   options). [^4]
3. **RV** — rolling std-dev of daily log returns over 20–30 days, annualized if
   needed. [^8]
4. **VRP** = IV − RV. Forward-looking variant: IV today vs RV over the *next*
   period. [^3]

Many platforms show VRP as a **percentile** vs its own history (e.g., "VRP at
70th percentile of last 3 months") to gauge cheap vs expensive vol. [^5]

## Interpretation

| VRP level | Reading | Strategy lean |
|-----------|---------|---------------|
| **High / very positive** | IV ≫ RV, options richly priced, fear high | Short-vol / premium selling if fear overdone |
| **Low / negative** | IV ≤ RV, options cheap, market complacent | Long-vol / buy convexity |

VRP is a **context indicator**, not a standalone signal. Combine with: view on
future vol, risk management, trend, regime, GEX, OI, macro. [^5]

## Strategies

### Short-vol (when VRP high)

- Sell OTM calls/puts; structures: [[Iron Condor]], short strangle/straddle
  (defined-risk variants preferred), [[Covered Call]], [[Cash-Secured Put]].
- Rationale: collect rich premium; if RV < IV, theta + slow underlying = profit.
- Risks: tail events, known event risk, gap risk. Use defined-risk + sizing. [^6]

### Long-vol (when VRP low/negative)

- Buy calls/puts, straddles/strangles, debit spreads.
- Rationale: underpriced insurance; convex payoff if move > priced. [^8]

### Regime filter

- **High VRP**: cautious long options, favor premium selling with tight limits.
- **Low VRP**: cautious heavy short premium, favor long options / cheap puts
  for hedging. [^5]

## Portfolio construction

Systematic vol-premium strategies: short ATM straddles/strangles on indices,
combined with trend-following diversifier; dynamic scaling down when VRP low.
Steady premium most of the time, occasional large drawdowns in vol spikes —
managed via diversification and risk limits. [^3]

## Pitfalls

- VRP is **not** a guaranteed quiet market — high VRP can precede big moves.
  Pair with risk management. [^5]
- **Skew matters** — put IV can be far higher than call IV; aggregate VRP hides
  this. Use strike-level IV. [^3]
- **Over-leverage** — many small wins, few huge losses. Size conservatively;
  prefer defined-risk structures. [^6]

## Sources

[^1]: ecassets.com — "Volatility Risk Premium" guide.
[^2]: convextrade.com — VRP glossary.
[^3]: AQR — "Understanding the Volatility Risk Premium" (Ilmanen, 2012).
[^4]: flashalpha.com — VRP formula and calculation.
[^5]: menthorq.com — VRP trading guide and interpretation.
[^6]: daytrading.com — VRP and short-vol strategies.
[^7]: Imperial College — Shibo Lu thesis on VRP risk aversion.
[^8]: medium.com / Roshan Zambare — VRP and market regime classification.
