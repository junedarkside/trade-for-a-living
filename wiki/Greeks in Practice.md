---
title: Greeks in Practice
type: concept
status: learning
tags: [options, derivatives, greek/delta, greek/gamma, greek/theta, greek/vega, greek/rho, risk]
---

# Greeks in Practice

**The Greeks are your real-time risk dashboard** — they tell you how a position
will react to moves in price, time, and volatility, and how to size and adjust
trades. This article is the **trader-focused companion** to the theoretical
material in [[Greeks]] and the per-Greek articles ([[Delta]], [[Gamma]],
[[Theta]], [[Vega]], [[Rho]]).

## Overview
A practical view: which Greek drives which trading decision, what target
profiles look like for each major strategy family, and the mistakes that wreck
trades even when the "view" is right.

## Per-Greek trading uses

| Greek | Drives decision | Concrete use |
|-------|-----------------|--------------|
| [[Delta]] | Sizing, hedging | Choose strike to match intended exposure; compute hedge ratio. |
| [[Gamma]] | Re-hedge frequency, expiry choice | Decide how actively to manage; pick short-dated (high) vs long-dated (smooth). |
| [[Theta]] | Expiry, holding horizon | Match option expiry to your horizon; budget daily decay for long-option positions. |
| [[Vega]] | Event timing, vol-regime selection | Avoid buying options when IV is already extreme; size vol trades by vega. |
| [[Rho]] | Long-dated pricing | Mostly for LEAPS / rate-sensitive environments; usually minor. |

## Trade templates

### Directional (e.g., bullish call — [[Long Call]])
- **Delta**: target **0.40–0.60** — balanced leverage vs. probability of profit.
- **Gamma**: watch near expiry — delta can swing fast.
- **Theta**: budget it. If your view is "slow grind up," high theta can kill the trade.
- **Vega**: check IV. If IV is already elevated (pre-event), vol crush can offset direction.

### Income (e.g., short strangle / [[Iron Condor]], [[Covered Call]])
- **Delta**: ≈ 0 (neutral view).
- **Theta**: **strongly positive** (you collect daily decay).
- **Vega**: **negative** (want IV to fall or stay low).
- **Gamma**: **negative** (big moves hurt; delta can swing against you fast).

Risk rules:
- Define max loss — prefer defined-risk spreads/condors over naked short strangles.
- Set rules for closing when underlying approaches a short strike.
- Cut size if IV starts spiking (you're short vega).

### Volatility / event (e.g., [[Long Straddle]])
- **Delta**: ≈ 0 initially (you don't care about direction, just magnitude).
- **Gamma**: positive and high near expiry (big moves accelerate gains).
- **Theta**: **strongly negative** (loses every day if nothing happens).
- **Vega**: **positive** (benefits if IV rises).

Pre-trade questions:
- Is the expected move large enough to overcome theta?
- Is IV already pricing in a huge move (leaving little room for further vol increase)?
- What's the exit plan if price stays flat and theta bleeds you?

## Position Greeks management

Monitor at the **book level**, not per-leg:
- **Net delta** — total directional exposure (share-equivalents).
- **Net gamma** — how fast delta can change.
- **Net theta** — daily P&L from time decay.
- **Net vega** — total sensitivity to vol.

**Worked example:**
- Long 10 calls (delta 0.40) → +400 delta.
- Short 5 calls (delta 0.70) → −350 delta.
- **Net delta = +50** (behaves like long ~50 shares).

Adjust by:
- Adding/removing legs.
- Hedging with underlying or futures to bring net delta to your target
  (often 0 for neutral strategies — see [[Delta-Neutral Hedging]]).

Full framework (Taylor expansion, formulas, design patterns): see
[[Position Greeks]].

## Common mistakes

- **Treating delta as constant** — gamma is non-trivial near expiry and ATM.
- **Underestimating theta** — long options bleed every day the market doesn't
  move; "time works for you" applies to short options, not long.
- **Buying options when IV is extreme** — vol crush after events can wipe
  directional gains.
- **Running short premium with high negative gamma** — naked short strangles /
  straddles blow up in fast markets; use defined-risk structures.

## Practical checklist (run before every trade)

- "If the stock doesn't move for 5 days, how much does theta cost me?"
- "If IV drops 5%, how much does vega hurt me?"
- "If price moves +$3 (or whatever your expected move is), how much does delta
  increase (via gamma) and how does that change my risk?"
- "What's my max loss, and is the position sized to survive that loss?"
- "What's my exit rule?" (price level, time stop, IV condition)

## Related
- [[Greeks]] (hub, theory) · [[Delta]] · [[Gamma]] · [[Theta]] · [[Vega]] ·
  [[Rho]] (per-Greek articles, theory + brief practical use) ·
  [[Position Greeks]] · [[Delta-Neutral Hedging]] ·
  [[Dynamic Hedging]] (operational playbook for rebalancing) ·
  [[Long Straddle]] · [[Iron Condor]] · [[Covered Call]] ·
  [[Risk Management]] (cross-cutting discipline: sizing, stops, leverage) ·
  [[Options Risk Management]] (pre-trade rules + sizing formula) ·
  [[Pre-Trade Checklist]] (quick-reference card)

## Sources
[^1]: `raw/greeks-trading-practice.md`
[^2]: youtube.com/watch?v=SFebmSYSZA8 — Greeks dashboard.
[^3]: youtube.com/watch?v=3C-NQadRRfo — delta/hedging/volatility trades.
[^4]: simplify.us — what are option greeks.