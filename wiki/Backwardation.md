---
title: Backwardation
type: concept
status: learning
aliases: [B]
tags: [futures, derivatives]
---

# Backwardation

**Term structure state.** Futures prices are **lower** for farther-dated
contracts than for nearer-dated ones. Often signals **scarcity** or **strong
near-term demand**.

## Overview
If you plot futures prices vs expiry, backwardation is a **downward-sloping
curve**. The market is paying a premium for **immediate** delivery. Common when:
- Near-term supply is tight (harvest before next harvest, OPEC cuts).
- Convenience yield > financing + storage costs.
- Risk-off flight to spot (bid up nearby).

## Mechanics

```
Price
 │   \
 │      \
 │         \                  ← Backwardation (downward-sloping curve)
 │            \
 │               \
 │                  \
 ┼──────────────────────────── Time
     Near              Far
```

Fair value: `F(T) = S · e^((r + storage − convenience yield) · T)`.
When observed F(T) < fair value, the contract is in **excess backwardation** —
typically transient.

## Roll yield implication
Long holders rolling a long future in backwardation **buy the new (lower)
contract and sell the old (higher) one** → gain. This is **positive roll yield**
(see [[Roll Yield]]).

## Strategy impact
- **Long-only index trackers** benefit from roll yield in persistent backwardation.
- **Short-future speculators** suffer roll loss in backwardation.
- **Event-driven trades** (pre-harvest, OPEC meetings) often play backwardation
  flattening as the catalyst passes.

## Related
- [[Contango]] (opposite state) · [[Roll Yield]] · [[Basis]] ·
  `raw/futures-basics.md`

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/futures-basics.md`
[^3]: Hindu Business Line — Mastering derivatives: how to optimally combine futures and options.