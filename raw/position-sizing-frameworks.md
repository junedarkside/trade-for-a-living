---
title: Position Sizing Frameworks
type: source
tags: [options, derivatives, risk]
---

# Position Sizing Frameworks — Research Notes

Sizing rules convert a trade idea into a specific quantity. Wrong sizing
destroys accounts faster than wrong direction. Six standard frameworks.

## 1. Kelly Criterion

Optimal fraction that maximises long-run log-wealth growth.

**Binary** (e.g., binary option):
```
f* = (bp − q) / b
```
Where `b` = net odds, `p` = win prob, `q = 1 − p`.

**Continuous** (long-biased asset with drift `μ`, vol `σ`, risk-free `r`):
```
f* = (μ − r) / σ²
```

**Example — long SET50 with μ=8%/yr, σ=20%/yr, r=2%:**
```
f* = (0.08 − 0.02) / 0.04 = 1.50 (150%)
```
Full Kelly impractical (margin + leverage + drawdown pain). **Quarter-Kelly (37.5% of equity) is the practitioner standard.**

**Drawdown risk of full Kelly:**
- Kelly=1.0 → 80% prob of 20% DD, 50% prob of 50% DD, 20% prob of 80% DD.
- Half-Kelly roughly halves both growth and DD probability.

## 2. Fixed Fractional

Risk fixed % of equity per trade. Simplest framework.

```
shares = (equity × risk%) / (entry − stop)
```

**Example — PTT SSF:**
- Equity: ฿1,000,000. Risk: 1% = ฿10,000.
- Entry ฿150, stop ฿148.80 → risk per share ฿1.20.
- Shares = ฿10,000 / ฿1.20 = **8,333 shares = 8 SSF contracts** (1,000
  shares each).

## 3. Vol-Targeted / Vol-Adjusted

Scale position to hit a target portfolio vol. Institutional standard.

```
position_THB = (target_vol × equity) / instrument_vol
```

**Example — SET50 futures:**
- Equity ฿1M, target vol 10%, SET50 30-day RV = 16%.
- Position notional = (0.10 × 1,000,000) / 0.16 = **฿625,000**.
- SET50 at 950 → ฿200/pt → ฿625,000 / (950 × 200) ≈ **3 contracts**.

## 4. Risk Parity / Equal Risk Contribution

Allocate so each position contributes equal risk. Cross-asset framework.

```
w_i = (1/σ_i) / Σ(1/σ_j)
```

**Example — 3-asset portfolio:**
| Asset | Vol (σ) | Weight | Risk contribution |
|-------|---------|--------|-------------------|
| Bonds | 5% | 63% | 3.15% |
| Equities | 20% | 16% | 3.15% |
| Gold | 15% | 21% | 3.15% |

Sum of weights = 100%. Equal risk per dollar.

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

Pro-martingale mathematically ruinous (Kaufman, Tharp, Pardo). Anti-
martingale rational **only** in confirmed trends.

```
size_after_N_wins = base × m^N     (m = 1.0–1.5)
size_after_N_losses = base × r^N   (r = 0.5–1.0)
```

## Sources

- Thorp, *A Man for All Markets*, 2017 (Kelly in practice).
- Vince, *The Mathematics of Money Management*, 1992 (optimal f).
- Kaufman, *Trading Systems and Methods*, 2013 (money management).
- Tharp, *Trade Your Way to Financial Freedom*, 2006 (R-multiples, fixed fractional).
- Qian, AQR, *Risk Parity Portfolios*, 2005.
- Pardo, *Design, Testing, and Optimization of Trading Systems*, 2008.
- Quantpedia — Kelly Criterion reference.
