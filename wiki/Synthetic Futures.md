---
title: Synthetic Futures
type: strategy
status: learning
aliases: [SynF]
tags: [futures, options, derivatives, market/thailand]
---

# Synthetic Futures

**Replication strategy.** Replicate a futures exposure using only options. Useful
when futures are illiquid/expensive, or to fine-tune margin/Greek profile.

By **put-call parity**, holding a call and a short put (same strike, same expiry)
is economically equivalent to a long futures position (ignoring carry). The reverse
combination replicates a short future.

## Overview
- **Synthetic Long Future** = Long call (K) + Short put (K)
- **Synthetic Short Future** = Short call (K) + Long put (K)

Choose a strike near the money; same expiry. Treat the pair as a single
futures-equivalent unit.

## Legs — Synthetic Long Future

| Leg | Action | Instrument | Contract | Strike | Expiry |
|-----|--------|-----------|----------|--------|--------|
| 1 | Long | Call option | e.g. S50U26 | At/near spot (ATM) | e.g. 30 days |
| 2 | Short | Put option | e.g. S50U26 | Same as call | Same as call |

## Legs — Synthetic Short Future

| Leg | Action | Instrument | Contract | Strike | Expiry |
|-----|--------|-----------|----------|--------|--------|
| 1 | Short | Call option | e.g. S50U26 | At/near spot (ATM) | e.g. 30 days |
| 2 | Long | Put option | e.g. S50U26 | Same as call | Same as call |

## Max loss (both orientations)
- **Synthetic Long**: strike K (the put leg assigns you a long at K).
- **Synthetic Short**: strike K (the call leg assigns you a short at K).

## Max profit (both orientations)
- **Synthetic Long**: uncapped as underlying rises (call leg).
- **Synthetic Short**: uncapped as underlying falls (put leg).

## Breakeven
Strike K plus/minus net option premium. Parity holds closely; residual = time value
extrinsic (vanishes at expiry).

## Greeks behavior
- **Delta**: ≈ +1 (synthetic long) or ≈ −1 (synthetic short) — same as the future.
- **Gamma**: net **zero** (long call + short put at same strike cancel).
- **Theta**: net **zero** (offsetting time decay).
- **Vega**: net **zero** (offsetting vol exposure).
- Net: behaves like a future, not like an option — exposure is linear in spot.

## Payoff shape (at expiry)
Both orientations produce a **straight line** through (S_T = K, P&L = 0) with slope
+1 (long) or −1 (short), minus net premium paid (or plus net credit).

```
Synthetic Long Future
P&L
 │           /
 │         /
 │       /
 ┼─────/──── Strike K (P&L = 0 − premium)
 │   /
 │ /
```

## When to use
- **Illiquid futures** but liquid options market on the same underlier.
- **Margin profile**: margin on the synthetic can differ (often **lower** for
  long synthetic via spread offsets — see [[Portfolio Margin]]).
- **Fine-tuning Greeks**: combine with [[Delta-Neutral Hedging]] to add/subtract
  linear exposure without changing option Greeks.
- **Expiry arbitrage**: when futures are mispriced vs option parity bounds.

## Risks
- **Pin risk at K** — near expiry, parity can break down by a few ticks; test exits.
- **American-style early assignment** — short leg (put or call) can be assigned early.
- **Skew / smile distortion** — deep ITM/OTM strikes can deviate from parity.
- **Liquidity** — both legs must be liquid; illiquid leg → legging risk.

## Example — SET50 / TFEX
- Long 1 S50 call strike 950 @ ฿15 × 200 = ฿3,000.
  Short 1 S50 put strike 950 @ ฿13 × 200 = ฿2,600.
  **Net debit: ฿400** (≈ cost-of-carry over the holding period).
- Net position behaves like long 1 S50 future at ~950, but margin profile differs
  (spread margin on short put, no futures margin).
- At expiry, parity holds: payoff = S_T − 950 − net premium (≈ futures P&L).

## Related
- [[Risk Reversal]] (synthetic long call + short put + long future — adds delta via the future leg) ·
  [[Black Model]] (the pricing framework for both legs) · [[Greeks]] ·
  [[Delta-Neutral Hedging]]

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/futures-basics.md`
[^3]: Hindu Business Line — Mastering derivatives: how to optimally combine futures and options.