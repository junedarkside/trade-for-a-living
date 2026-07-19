---
title: Portfolio Margin
type: concept
status: learning
aliases: [PM]
tags: [futures, options, derivatives, risk]
---

# Portfolio Margin

**Margin methodology.** Calculate margin on a derivatives portfolio as a **net
risk-based amount** rather than summing per-leg requirements. Multi-leg
structures (spreads, collars, hedged positions) typically get **lower margin**
than the sum of standalone leg margins.

## Overview
Two common frameworks:
- **Standard / Reg-T margin** — fixed percentages per leg, conservative.
- **Portfolio margin** — stress-test the whole portfolio across price/vol scenarios
  (TIMSS/TIMS in US, similar in other jurisdictions). Margin = worst-case loss
  across scenarios, plus an add-on.

For Thailand (TFEX), brokers offer **spread-margin** packages: combinations like
[[Futures Collar]], covered calls, vertical spreads get reduced margin vs leg-by-leg.

## Why it matters for multi-leg strategies

| Structure | Per-leg margin (rough) | Portfolio-margin (typical) |
|-----------|------------------------|----------------------------|
| Long future + short OTM call (covered call on future) | Future IM + naked-call margin | Long future IM only (short call covered) |
| Long future + long put + short call (collar) | Future IM + put + naked call | Future IM + small add-on (defined risk) |
| Short straddle (naked) | Large naked-call + naked-put | Full premium + add-on (unhedged) |
| Calendar spread | Two naked short/short combos | Reduced (spread offset) |

The key idea: **defined-risk** packages (max loss known) get much better margin
than **unbounded-risk** packages.

## Mechanics (conceptual)

1. **Aggregate** all positions into a single portfolio.
2. **Stress-test** across a grid of price shocks (±X%) and vol shocks (±Y%).
3. Margin = largest loss observed + a buffer (often 10–25%).
4. **Intra-day** mark-to-market applies (see `raw/futures-basics.md`).
5. **Intraday vs overnight** rates may differ — overnight margin typically higher.

## Spread offsets — the practical effect

When legs hedge each other:
- Long call + short call (same expiry, different strike) → **vertical spread margin**
  (max loss of the spread, not full naked-call + naked-call).
- Long future + short OTM call → call is "covered" by the future; margin ≈
  long future initial margin only.
- Long put + short put (different strikes) → put spread margin.

These are the offsets that make multi-leg packages capital-efficient.

## Risks and caveats
- **Higher leverage** = faster margin calls if wrong.
- **Scenario-dependent** — past stress doesn't guarantee future stress (gap risk, vol shocks).
- **Liquidity** — closing a complex package mid-stress can be expensive.
- **Broker variation** — calculation details differ; check TFEX/broker specs.

## When to use
- Any multi-leg options + futures position (most of the time).
- Larger accounts where capital efficiency matters more than absolute margin levels.
- Market-makers and hedgers who run continuous delta-neutral books
  (see [[Delta-Neutral Hedging]]).

## Related
- [[Multi-Leg Order]] (atomic execution complements spread margin) · [[Futures Collar]] ·
  [[Covered Call on Future]] · [[Delta-Neutral Hedging]] · `raw/futures-basics.md`

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/futures-basics.md`
[^3]: asx.com.au — implementing multi-legged strategies.
[^4]: fxoptions.com — managing multi-leg options positions.