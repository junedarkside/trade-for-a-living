---
title: Volatility Risk Premium
type: concept
status: reviewed
tags: [options, derivatives, strategy/income, strategy/speculation]
aliases: [VRP, Variance Risk Premium, Vol Premium]
---

# Volatility Risk Premium (VRP)

The **Volatility Risk Premium** is the persistent tendency for **implied
volatility (IV)** in options to be **higher than the realized volatility (RV)**
that actually occurs over the same period. Options are routinely priced as if
the market expects more movement than eventually happens — sellers of
volatility are "paid" a premium for bearing that risk.

VRP is the empirical foundation of nearly every **systematic short-vol /
premium-selling** strategy. Harvesting it (with strict tail-risk control) is a
core pro-trader alpha source.

## What VRP measures

| Term | Definition |
|------|------------|
| [[Implied Volatility\|Implied Volatility (IV)]] _(Phase B article)_ | Market's expectation of future vol, backed out from option prices (see [[Black Model]]). Reflects fear, hedging demand, supply/demand. |
| **Realized Volatility (RV)** | Actual historical volatility over a period, measured as standard deviation of log returns. |
| **VRP** | `VRP = IV − RV` (vol version) or `VRP_var = IV² − RV²` (variance / Variance Risk Premium). |

**Positive VRP** → options "expensive" relative to realized moves. **Negative
VRP** → options "cheap" relative to realized moves. Historically positive on
equity indices.

## Why VRP exists (economic drivers)

1. **Insurance demand** — hedgers pay up for puts (especially OTM), pushing IV
   above RV. Biggest driver for downside skew.
2. **Risk aversion** — participants overpay for downside protection; vol
   sellers bear tail risk and get compensated for it.
3. **Leverage / constraints** — some players can't run large short-vol books
   (margin, regulation, risk limits), so those who can capture a premium.

This is **not a free lunch** — it's compensation for bearing crash / spike
risk that historically realises occasionally.

## How to calculate

1. Pick a horizon (e.g., 30 days).
2. **IV** — ATM option IV for that horizon. For Thai market: SET50 option ATM
   IV (the closest analogue to VIX).
3. **RV** — rolling std-dev of daily log returns over 20–30 days, annualised if
   needed.
4. **VRP** = IV − RV. Forward-looking variant: IV today vs RV over the *next*
   period.

Many platforms show VRP as a **percentile** vs its own history
("VRP at 70th percentile of last 3 months") to flag cheap vs expensive vol.

## Interpreting VRP

| VRP level | Reading | Strategy lean |
|-----------|---------|---------------|
| **High / very positive** | IV ≫ RV, options richly priced, fear high | **Short-vol / premium selling** if fear is overdone |
| **Low / negative** | IV ≤ RV, options cheap, complacency | **Long-vol / buy convexity** if you expect bigger moves than priced |

VRP is a **context indicator**, not a standalone signal. Combine with:
- Your view on future vol and direction.
- Risk management (short vol blows up in crashes).
- Trend, regime, GEX, OI, macro.

## Strategies

### Short-vol when VRP is high

Sell OTM options or run defined-risk structures:

- [[Iron Condor]] — defined-risk range play.
- Short strangle / short straddle — undefined risk, higher premium.
- [[Covered Call]] / [[Cash-Secured Put]] — income against holdings.
- [[Risk Reversal]] — skewed short-vol exposure.

**Rationale:** collect rich premium; if RV ends up below IV, theta + slow
underlying = profit. Risks: tail events, known event risk, gap risk. Always
use defined-risk structures, position sizing, and stop-loss rules per
[[Options Risk Management]].

### Long-vol when VRP is low / negative

Buy calls/puts, straddles/strangles, or debit spreads. Rationale: underpriced
insurance; convex payoff if move > priced. Common in calm complacent markets
before expected vol expansion, or as cheap-delta hedge.

### VRP as regime filter

- **High VRP regime**: cautious with long options (expensive), favor premium
  selling with tight controls, consider smaller size or more hedging.
- **Low VRP regime**: cautious with heavy short premium, favor long options /
  cheap puts for hedging.

Combine VRP with **trend**, **macro regime**, and **positioning data** (OI,
GEX) to decide whether to lean long or short vol and how aggressively.

## Portfolio construction

Institutional vol-premium strategies: systematically sell ATM straddles /
strangles on indices, combined with **trend-following diversifier** to reduce
correlation and tail risk; dynamic scaling down when VRP low or risk
indicators flash warning. Steady premium most of the time, occasional large
drawdowns in vol spikes — managed via diversification and risk limits.

For a single-trader implementation, the equivalent is **diversifying across
underlyings and expirations** rather than concentrating short-vol in one
product.

## Pitfalls

1. **VRP is not a guarantee of quiet markets.** High VRP can precede big moves
   (the "calm before the storm" trap). Pair with risk management and scenario
   testing.
2. **Skew matters** — put IV can be far higher than call IV; aggregate VRP
   hides this. **Read strike-level IV**, not just ATM aggregate.
3. **Over-leverage** — many small wins, few huge losses. Size conservatively;
   prefer defined-risk structures. See [[Options Risk Management]] for sizing
   formula.
4. **Forward-looking bias** — backward-looking VRP (IV_today vs RV_past) is
   informative but not predictive. Forward-looking VRP (IV_today vs RV_future)
   is what matters for new trades.

## Worked example — Thai SET50

- SET50 ATM 30-day option IV = **22%**.
- 30-day realized vol (annualised, rolling) = **16%**.
- VRP = 22% − 16% = **6 vol points** (or ~27% of IV — elevated).
- Strategy lean: **short premium** defined-risk on SET50 (iron condor outside
  OI walls, short strangle with defined-risk wings). Size conservatively per
  [[Options Risk Management]] sizing rules.

If VRP = 0% or negative → lean long options, especially into events.

## Related

- [[Implied Volatility]] _(Phase B article)_ · [[Options Strategy]] ·
  [[Options Risk Management]] · [[Iron Condor]] · [[Short Strangle]] _(see
  Strangle)_ · [[Covered Call]] · [[Cash-Secured Put]] · [[Risk Reversal]] ·
  [[Vega]] · [[Options Chain]] · [[Position Greeks]] · [[Delta-Neutral Hedging]]

## Sources

[^1]: `raw/volatility-risk-premium.md`
[^2]: ecassets.com — "Volatility Risk Premium" guide.
[^3]: convextrade.com — VRP glossary.
[^4]: AQR — "Understanding the Volatility Risk Premium" (Ilmanen, 2012).
[^5]: flashalpha.com — VRP formula and calculation.
[^6]: menthorq.com — VRP trading guide and interpretation.
[^7]: daytrading.com — VRP and short-vol strategies.
[^8]: Imperial College — Shibo Lu thesis on VRP risk aversion.
[^9]: medium.com / Roshan Zambare — VRP and market regime classification.
