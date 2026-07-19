---
title: Roll Yield
type: concept
status: learning
aliases: [RY]
tags: [futures, derivatives]
---

# Roll Yield

**P&L component.** The gain or loss from **rolling** a futures position from
one contract month to the next. Determined by the term structure (see
[[Contango]] / [[Backwardation]]).

## Overview
Most futures positions are **rolled** before expiry (especially cash-settled
or hard-to-deliver contracts). Each roll = selling the current contract and
buying the next. The price difference between them is the roll yield (or
"roll cost" when negative).

## Formula

```
Roll yield (long) ≈ (F_near − F_far) / F_near, per roll
```

- **Contango** (F_far > F_near): long roll yields **negative** (you sell low, buy high).
- **Backwardation** (F_far < F_near): long roll yields **positive** (you sell high, buy low).

## Long vs short

| Term structure | Long holder | Short holder |
|----------------|-------------|--------------|
| Contango | Pays (negative roll) | Earns (positive roll) |
| Backwardation | Earns (positive roll) | Pays (negative roll) |

## Annualized
For a series of rolls:
```
Annual roll yield ≈ (P_near_end / P_near_start) − (P_far_end / P_far_start)
```
…adjusted for the time held. Many CTAs and futures-backed ETFs publish
**12-month rolling yield** as a key metric.

## Strategy impact
- **Index trackers / futures-backed ETFs**: persistent contango → persistent drag.
- **Long-term commodity holders**: roll yield can dominate total return for
  short-dated commodity futures.
- **Calendar spreads**: explicitly trade roll yield (long far vs short near
  profits from contango flattening; opposite for backwardation steepening).

## Related
- [[Contango]] · [[Backwardation]] · [[Basis]] · [[Calendar Spread]] ·
  `raw/futures-basics.md`

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/futures-basics.md`
[^3]: Hindu Business Line — Mastering derivatives: how to optimally combine futures and options.