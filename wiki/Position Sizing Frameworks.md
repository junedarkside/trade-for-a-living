---
title: Position Sizing Frameworks
type: concept
status: learning
tags: [options, derivatives, risk]
aliases: [Position Sizing, Kelly, Fixed Fractional, Vol Targeting, Risk Parity]
---

# Position Sizing Frameworks

Sizing rules convert a trade idea into a specific quantity. **Wrong sizing
destroys accounts faster than wrong direction.** Six standard frameworks.

## 1. Kelly Criterion

Optimal fraction that maximises long-run log-wealth growth.

**Binary:**
```
f* = (bp − q) / b
```
`b` = net odds, `p` = win prob, `q = 1 − p`.

**Continuous (long-biased asset):**
```
f* = (μ − r) / σ²
```
`μ` = expected return, `σ` = vol, `r` = risk-free rate.

### Example — long SET50 with μ=8%/yr, σ=20%/yr, r=2%

```
f* = (0.08 − 0.02) / 0.04 = 1.50 (150% of equity)
```

Full Kelly impractical (margin + leverage + drawdown pain). **Quarter-
Kelly (37.5% of equity) is the practitioner standard.**

**Drawdown risk of full Kelly:**
- Kelly=1.0 → 80% prob of 20% DD, 50% prob of 50% DD, 20% prob of 80% DD
- Half-Kelly roughly halves both growth and DD probability

## 2. Fixed Fractional

Risk fixed % of equity per trade. Simplest framework.

```
shares = (equity × risk%) / (entry − stop)
```

### Example — PTT SSF

- Equity ฿1,000,000. Risk 1% = ฿10,000.
- Entry ฿150, stop ฿148.80 → risk per share ฿1.20.
- Shares = ฿10,000 / ฿1.20 = **8,333 shares = 8 SSF contracts** (1,000
  shares each).

## 3. Vol-Targeted / Vol-Adjusted

Scale position to hit a target portfolio vol. Institutional standard.

```
position_THB = (target_vol × equity) / instrument_vol
```

### Example — SET50 futures

- Equity ฿1M, target vol 10%, SET50 30-day RV = 16%.
- Position notional = (0.10 × 1,000,000) / 0.16 = **฿625,000**.
- SET50 at 950, ฿200/pt → ฿625,000 / (950 × 200) ≈ **3 contracts**.

## 4. Risk Parity / Equal Risk Contribution

Allocate so each position contributes equal risk. Cross-asset framework.

```
w_i = (1/σ_i) / Σ(1/σ_j)
```

### Example — 3-asset portfolio

| Asset | Vol (σ) | Weight | Risk contribution |
|-------|---------|--------|-------------------|
| Bonds | 5% | 63% | 3.15% |
| Equities | 20% | 16% | 3.15% |
| Gold | 15% | 21% | 3.15% |

Sum = 100%. Equal risk per dollar.

## 5. Drawdown-Constrained (Vince)

Size to cap drawdown within tolerance.

```
position = f* / BiggestLoss
```
Where `f*` = optimal f from TWR (Terminal Wealth Relative) maximization.

Risk-Constrained Kelly adds explicit `P(DD > δ) ≤ ε` constraint.

## 6. Anti-Martingale vs Pro-Martingale

| Mode | After win | After loss |
|------|-----------|------------|
| **Anti-martingale** | Size up | Size down |
| **Pro-martingale** | Size down | Size up |

Pro-martingale mathematically ruinous. Anti-martingale rational **only** in
confirmed trends:

```
size_after_N_wins = base × m^N     (m = 1.0–1.5)
size_after_N_losses = base × r^N   (r = 0.5–1.0)
```

## Framework selection guide

| Trader profile | Recommended framework |
|----------------|----------------------|
| **Trend-following systematic** | Anti-martingale + vol-targeting |
| **Mean-reversion / premium selling** | Fixed fractional + DD-constrained |
| **Multi-asset book** | Risk parity / ERC |
| **Single-strategy concentrated** | Kelly (quarter-Kelly) |
| **Options seller harvesting VRP** | Fixed fractional (1–2% per trade) |

## Related

- [[Options Risk Management]] · [[Margin Mechanics]] · [[Risk Management]] ·
  [[Volatility Risk Premium]] · [[Volatility Risk Premium|VRP]] ·
  [[Position Greeks]] · [[Trade Journaling]] · [[Backtesting & Forward
  Testing]]

## Sources

[^1]: `raw/position-sizing-frameworks.md`
[^2]: Thorp, *A Man for All Markets*, 2017 (Kelly in practice).
[^3]: Vince, *The Mathematics of Money Management*, 1992 (optimal f).
[^4]: Kaufman, *Trading Systems and Methods*, 2013.
[^5]: Tharp, *Trade Your Way to Financial Freedom*, 2006.
[^6]: Qian (AQR), *Risk Parity Portfolios*, 2005.
[^7]: Pardo, *Design, Testing, and Optimization of Trading Systems*, 2008.
[^8]: Quantpedia — Kelly Criterion reference.
