---
title: Implied Volatility
type: concept
status: learning
tags: [options, derivatives, market/thailand]
aliases: [IV, Implied Vol, IVol]
---

# Implied Volatility (IV)

**Implied volatility** is the market's forward-looking estimate of how much the
underlying will move over the option's life, expressed as an **annualised
standard deviation**. It is "implied" because it is **backed out** from the
option's market price using a pricing model — [[Black Model]] (or Black-Scholes
for equity options). IV is the **price of volatility**.

## Why IV matters

- **Forward-looking** — distinct from historical volatility (HV), which only
  describes the past. IV is what the market is **paying** for expected future
  movement.
- **Drives premium** — higher IV = higher premiums at every strike; lower IV =
  cheaper premiums. All option P&L is driven in part by IV changes (see
  [[Vega]]).
- **Standard read** — spot 100, IV 20% → ~68% probability price ends in
  [80, 120] over one year (one σ). Annualised.
- **IV crush** — IV typically **rises** into known events (earnings, policy
  decisions), then **collapses** after as uncertainty resolves. Long option
  holders can lose money even if the underlying moves the right way.

## How traders use IV

| Question | Tool |
|----------|------|
| Is IV cheap or expensive vs its own history? | **IV rank / IV percentile** (current IV vs 52-week range) |
| Is IV cheap or expensive vs actual vol? | **VRP** = IV − RV (see [[Volatility Risk Premium]]) |
| Will an upcoming event reprice IV? | Calendar of dividends, earnings, policy decisions |
| How should I trade? | High IV → favor short-premium; low IV → favor long-options |

IV is a **context input**, not a signal. Always combine with directional view,
risk limits, and other Greeks.

## Worked example — SET50 option

- SET50 spot = **25,500**.
- 30-day ATM option mid = **฿80 / contract** (multiplier ฿200).
- Back out IV with [[Black Model]] → **22%** annualised.
- Read: market prices **~22% annual vol** for SET50 over the next 30 days. One
  σ move ≈ 22% × √(30/365) ≈ **3.6%** → expected range ≈
  **[24,580 – 26,420]**.
- Compare to HV (30-day realised): if RV = 16% → VRP = +6 vol points → IV is
  **rich** vs realised. Lean short-premium per [[Volatility Risk Premium]].

## IV crush — the long-option trap

Event-driven IV spike is **predictable**: option prices inflate into the
event, then deflate as the event passes. If you bought options ahead of an
event expecting a move but the IV collapse is larger than the realised move,
you lose.

**Rule of thumb:** before buying long options, check the IV term structure —
short-dated IV materially above longer-dated IV usually signals event risk
already priced in.

## IV rank vs IV percentile

- **IV rank** = (current IV − 52w low) ÷ (52w high − 52w low), expressed %.
  Tells you where IV is in its own range.
- **IV percentile** = % of days in the lookback window where IV was lower
  than today. More robust to outliers.

High IV rank (>50%) and high IV percentile → options historically expensive
→ short-premium lean. Low rank (<25%) → options cheap → long-options lean.

## Related

- [[Volatility Risk Premium]] · [[IV Skew, Smile & Surface]] · [[Black Model]]
  · [[Vega]] · [[Options Chain]] · [[Options Strategy]] · [[Options — Basics]]

## Sources

[^1]: `raw/iv-and-market-mechanics.md` (section 1).
[^2]: en.wikipedia.org — Implied volatility.
[^3]: ig.com — "What is implied volatility and how to use it".
[^4]: tastylive.com — Implied volatility concepts.
[^5]: fool.com — Implied volatility definition.
[^6]: quantt.co.uk — IV crush explained.
