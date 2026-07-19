---
title: Basis
type: concept
status: learning
aliases: [Bs]
tags: [futures, derivatives]
---

# Basis

**Price relationship.** The difference between a futures price and the
**reference price** (spot or theoretical fair value) for the same underlying.

## Definition

```
Basis = Futures price − Spot price
       (or)
Basis = Futures price − Fair value
```

Two common conventions:
- **Spot basis** = `F − S` — the actual cash-futures gap at a point in time.
- **Fair-value basis** = `F − F_fair` — how far the futures market deviates
  from cost-of-carry theory.

## Components of basis

| Component | Sign convention | Effect on basis |
|-----------|-----------------|-----------------|
| Financing cost (r) | + for long future | Increases F → positive basis |
| Storage / insurance | + for storable commodities | Increases F → positive basis |
| Convenience yield | − for storable commodities | Decreases F → reduces basis |
| Expected spot moves | variable | Drives spot basis away from fair value |

## Normal vs inverted basis

| State | Spot basis | Term structure |
|-------|-----------|----------------|
| **Contango** | Positive (F > S) | Upward-sloping curve |
| **Backwardation** | Negative (F < S) | Downward-sloping curve |
| **Flat** | ≈ 0 | Flat curve |

## Trading basis
- **Basis traders** (typically commercial hedgers) trade the **cash + futures**
  pair to capture deviations from fair value. Convergence at expiry → basis
  collapses to ~0.
- **Cross-market basis** — between two related futures (e.g. Brent vs WTI crude,
  or SET50 futures vs underlying basket) — used in arbitrage.

## Use in multi-leg strategies
- Calendar spreads ([[Calendar Spread]]) explicitly trade the basis between
  near and far contracts.
- Delta-hedging an option book with futures ([[Delta-Neutral Hedging]]) relies
  on futures tracking spot closely (small basis).

## Related
- [[Contango]] · [[Backwardation]] · [[Roll Yield]] · [[Calendar Spread]] ·
  `raw/futures-basics.md`

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/futures-basics.md`
[^3]: Hindu Business Line — Mastering derivatives: how to optimally combine futures and options.