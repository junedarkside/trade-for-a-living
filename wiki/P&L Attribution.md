---
title: P&L Attribution
type: concept
status: learning
tags: [options, derivatives, risk]
aliases: [P&L Attribution, P&L Explain, Greek Attribution]
---

# P&L Attribution

P&L attribution decomposes daily / position-level P&L into its sources:
spot move, vol change, time decay, gamma, vega, etc. Without it, you
can't tell which positions drive results or whether risk is rising.

## Hull Taylor Expansion (1st-order)

```
ΔP ≈ δ · ΔS + ½ · Γ · (ΔS)² + Θ · Δt + vega · Δσ + ρ · Δr
```

For higher-order (vanna, charm, volga, vomma), extend.

### Variable definitions

| Var | Meaning | Unit |
|-----|---------|------|
| ΔP | Price change of position | THB |
| δ | Delta | per unit spot |
| ΔS | Spot change | index points / THB |
| Γ | Gamma | per unit spot² |
| Θ | Theta | THB per day |
| Δt | Time elapsed (days) | days |
| vega | Vega | THB per 1 vol point |
| Δσ | Vol change (annualised) | vol points |
| ρ | Rho | THB per 1% rate change |
| Δr | Rate change | % |

## Multi-leg Portfolio Form

For N legs:

```
ΔP_portfolio = Σ ΔP_i = Σ (δ_i · ΔS + ½Γ_i·ΔS² + Θ_i·Δt + vega_i·Δσ + ρ_i·Δr)
```

Useful diagnostic: sum each component (delta P&L, gamma P&L, theta P&L,
vega P&L) and check they sum to total P&L ± residual.

## Worked Example — Long SET50 950 call, 10 contracts, +5 spot, 1 day

Assume at entry: δ = 0.5, Γ = 0.02, Θ = −0.08 (per contract per day), S=950.

| Component | Formula | Per contract | 10 contracts |
|-----------|---------|--------------|--------------|
| Delta P&L | 0.5 × 5 × 200 (multiplier) | +500 THB | +5,000 |
| Gamma P&L | ½ × 0.02 × 5² × 200 | +50 THB | +500 |
| Theta P&L | −0.08 × 1 × 200 | −16 THB | −160 |
| **Total** | sum | **+534 THB** | **+5,340** |

Set IV change assumed = 0. If IV moved +0.5 vol points, vega P&L would
add `0.5 × vega × 200 × 10` — needs vega value.

## Three-Axis Decomposition

Daily P&L split into:

- **Spot contribution**: δ · ΔS + ½Γ · ΔS²
- **Time contribution**: Θ · Δt
- **Vol contribution**: vega · Δσ

Plus **residual** = total P&L − (sum of three). Residual > 5% of P&L
flags data error or model misspecification.

## Realized vs Unrealized P&L

| Type | Meaning | Cash impact |
|------|---------|-------------|
| **Realized** | Closed position; P&L locked in | Cash in/out |
| **Unrealized** | Open position marked to market | MTM only (futures) or none (spot) |

For TFEX futures: daily MTM at 16:30 ICT converts the day's unrealized
into realized cash. For options: MTM daily but cash only on close. See
[[Mark-to-Market]].

## Worked Example A — Long SET50 futures

- Position: 5 long S50 futures, entry at 25,500.
- SET50 closes at 25,508 → +8 points.
- Unrealized P&L = 8 × 200 × 5 = **+฿8,000**.
- After 16:30 daily settlement, **realized** = **+฿8,000** in account.

## Worked Example B — Short straddle post-earnings

- Short strangle: 25,800 call / 25,200 put, sold at implied vol 28%.
- Earnings beat → implied vol drops to 22% → −6 vol points.
- Vega exposure = +0.20 per leg × 2 legs × 200 (multiplier) × -6 (vol drop) =
  -0.4 × 200 × -6 = **+480 THB per contract pair** (favourable).
- Plus theta: 2 × 0.10 × 200 = **+40 THB / day**.
- Both vega and theta positive — short-premium benefits from vol crush AND
  time decay. See [[Volatility Risk Premium]].

## Reconciliation Workflow

1. **Internal trade blotter** (what you intended to trade).
2. **Broker daily MTM statement** (what the broker shows).
3. **Independent recompute** (Python / spreadsheet using Greeks).
4. **Reconcile**:
   - Spot P&L match?
   - Theta P&L match (1 day × theta)?
   - Vega P&L match if IV feed available?
5. **Residual investigation** if total P&L doesn't sum.

## Position-level Contribution Analysis

For a portfolio of N positions:

```
position_i_P&L = Σ Greeks_i · market moves
%_of_total_P&L_i = position_i_P&L / sum(all P&L)
```

Identify which positions drove the day's P&L. Useful for:

- Identifying risk concentration (one position = 80% of P&L).
- Checking if hedges are working (short hedge P&L offsets long leg).
- Deciding what to close / adjust before tomorrow.

## Residual Red Flags

| Red flag | Likely cause |
|----------|--------------|
| Large positive residual | Missing IV move / missed gamma path |
| Large negative residual | Position mis-booked; stale Greeks; dividend miss |
| Persistent residual pattern | Hedging model error; data feed lag |

## Related

- [[Mark-to-Market]] · [[Greeks]] · [[Position Greeks]] ·
  [[Delta-Neutral Hedging]] · [[Dynamic Hedging]] ·
  [[Trade Journaling]] · [[Volatility Risk Premium]] ·
  [[Risk Management]]

## Sources

[^1]: `raw/pnl-attribution.md`
[^2]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 19
    (Taylor series, Greeks).
[^3]: Taleb, *Dynamic Hedging*, 1997 (practical P&L attribution).
[^4]: TFEX — daily settlement mechanics.
