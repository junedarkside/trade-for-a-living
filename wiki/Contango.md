---
title: Contango
type: concept
status: learning
aliases: [C]
tags: [futures, derivatives]
---

# Contango

**Term structure state.** Futures prices are **higher** for farther-dated
contracts than for nearer-dated ones. The normal state for most markets due to
**cost of carry** (financing + storage + insurance).

## Overview
If you plot futures prices vs expiry, contango is an **upward-sloping curve**.
The market is "paying more" for delivery later. Common when:
- Interest rates are positive (futures embed financing cost).
- Commodities have storage costs (oil in contango = "tank tops" glut).
- No immediate supply shortage.

## Mechanics

```
Price
 │                          /
 │                       /
 │                   /          ← Contango (upward-sloping curve)
 │              /
 │         /
 │     /
 ┼──────────────────────────── Time
     Near              Far
```

Fair value: `F(T) = S · e^((r + storage − convenience yield) · T)`.
When observed F(T) > fair value, the contract is in **excess contango**.

## Roll yield implication
Long holders rolling a long future in contango **buy the new (higher) contract
and sell the old (lower) one** → loss. This is **negative roll yield**
(see [[Roll Yield]]).

## Strategy impact
- **Long-only index trackers** (futures-backed ETFs, CTAs) suffer persistent
  drag in persistent contango.
- **Short-future speculators** benefit from roll yield in contango (sell high,
  buy lower when rolling short).
- **Calendar spreads** ([[Calendar Spread]]) often price contango as the "natural"
  backwardation of front-month vs back-month premium.

## Related
- [[Backwardation]] (opposite state) · [[Roll Yield]] · [[Basis]] ·
  `raw/futures-basics.md`

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/futures-basics.md`
[^3]: Hindu Business Line — Mastering derivatives: how to optimally combine futures and options.