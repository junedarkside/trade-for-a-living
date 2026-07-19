---
title: Position Greeks
type: concept
status: learning
tags: [options, derivatives, greek/delta, greek/gamma, greek/theta, greek/vega, greek/rho]
---

# Position Greeks

**The Greeks of an entire position, summed across all legs.** Professional option
desks monitor position Greeks (not per-leg) to manage the book.

## Overview
Each leg has its own Greeks. The position's exposure = the **weighted sum** of
each leg's Greeks. This is how multi-leg strategies
([[Vertical Spread]], [[Iron Condor]], [[Synthetic Futures]], etc.) get their
distinct risk profiles — the legs offset, amplify, or transform each other.

## Taylor expansion of price change

For small moves, the change in an option's price is approximated by:

```
ΔP ≈ Δ · ΔS + ½ · Γ · (ΔS)² + Θ · Δt + ν · Δσ + ρ · Δr
```

Where:
- `ΔS` = change in underlying price
- `Δt` = change in time (days or years depending on convention)
- `Δσ` = change in implied volatility
- `Δr` = change in interest rate

For a **position** (sum across legs), use **position Greeks**:

```
ΔP_position ≈ Δ_pos · ΔS + ½ · Γ_pos · (ΔS)² + Θ_pos · Δt + ν_pos · Δσ + ρ_pos · Δr
```

## Formula

For each Greek, position Greek = `Σ (leg quantity × contract multiplier × leg Greek)`.

```
Δ_pos = Σ_i (qty_i × multiplier_i × Δ_i)
Γ_pos = Σ_i (qty_i × multiplier_i × Γ_i)
Θ_pos = Σ_i (qty_i × multiplier_i × Θ_i)
ν_pos = Σ_i (qty_i × multiplier_i × ν_i)
ρ_pos = Σ_i (qty_i × multiplier_i × ρ_i)
```

For futures, multiplier is the contract's point value (e.g. ฿200 for SET50).
For equity options, multiplier is 100.

## Worked example

Position: long 5 calls (delta = 0.40 each) + short 3 calls (delta = 0.60 each).
Contract size = 100 shares.

```
Δ_pos = (5 × 100 × 0.40) − (3 × 100 × 0.60)
      = 200 − 180
      = +20
```

The whole structure behaves like being **long ~20 shares** for small moves.

## What professional desks monitor

| Greek | Meaning | Use |
|-------|---------|-----|
| **Net delta** | Directional exposure | Size directional bets; basis for [[Delta-Neutral Hedging]] |
| **Net gamma** | How fast delta can change | Decide re-hedge frequency |
| **Net theta** | Daily P&L from time decay | Income target for short-premium books |
| **Net vega** | Exposure to vol changes | Manage event risk; vol-crush exposure |
| **Net rho** | Exposure to rate moves | Mostly relevant for long-dated books |

## Design patterns

- **Delta-neutral, long gamma, long vega, negative theta**: long volatility
  ([[Long Straddle]]) — you want big moves or rising IV; you pay theta.
- **Delta-neutral, short gamma, short vega, positive theta**: short volatility
  ([[Iron Condor]]) — you want quiet markets and falling IV; you collect theta.
- **Long delta, low gamma**: directional bet via deep ITM options or futures
  (delta = ~1, low convexity).
- **Zero vega**: matched-vol positions for directional plays without IV exposure.

## Common pitfalls

- **Treating position Greeks as static** — they drift as spot, time, and vol move.
  Re-compute frequently (intraday for short-dated books).
- **Ignoring gamma** — position delta is only first-order; near expiry or for
  ATM positions, gamma effects (the `½·Γ·ΔS²` term) can dominate.
- **Cross-Greek effects** — hedging delta can leave you exposed to vega or theta.
  Professional books target **multiple Greeks at zero** (delta-neutral AND
  vega-neutral, etc.).

## Related
- [[Greeks]] (hub) · [[Delta]] · [[Gamma]] · [[Theta]] · [[Vega]] · [[Rho]] ·
  [[Delta-Neutral Hedging]] · [[Dynamic Hedging]] (operational playbook) ·
  [[Multi-Strategy Options]] · [[Black Model]] · [[Synthetic Futures]]

## Sources
[^1]: `raw/greeks-overview.md`
[^2]: youtube.com/watch?v=SFebmSYSZA8 — position Greeks.
[^3]: youtube.com/watch?v=3C-NQadRRfo — hedging walkthrough.