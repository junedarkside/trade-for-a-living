---
title: Gamma
type: greek
status: learning
aliases: [Γ, gamma]
tags: [options, derivatives, greek/gamma]
---

# Gamma

**Γ — how fast delta changes.** The second derivative of option price w.r.t. spot.
Determines how **stable** your delta is as the underlying moves.

## Definition
```
Γ = ∂Δ / ∂S = ∂²P / ∂S²
```
Same for calls and puts (gamma is always positive for long options).

## Sign convention
- **Long options** (long call or long put): **positive gamma**.
- **Short options** (short call or short put): **negative gamma**.
- **Long stock / short stock / futures**: **zero gamma** (delta is constant at ±1).

## Long-holder meaning

**Long gamma** = your delta **moves in your favor** as the underlying moves:
- Long call, spot rises → delta increases → larger directional exposure as you win.
- Long put, spot falls → delta becomes more negative → larger directional exposure as you win.

**Short gamma** = your delta **moves against you** as the underlying moves:
- Short call, spot rises → delta becomes more negative → bigger loss as you lose.
- This is why **uncovered short options blow up** in fast markets.

## Behavior over time and with spot

| State | Gamma | Notes |
|-------|-------|-------|
| Deep ITM | → 0 | Delta already pinned near ±1; little room to move. |
| ATM | **highest** | Delta has maximum room to swing. |
| Deep OTM | → 0 | Delta pinned near 0. |
| Near expiry (ATM) | **spikes** | Binary-like behavior in last days. |
| Long dated | lower | Delta changes slowly with time. |

Gamma concentrates at ATM and **concentrates more as expiry approaches** — the
last-week ATM option has very high gamma.

## Practical use

1. **Re-hedge frequency** — high gamma means delta drifts fast → re-hedge more
   often (see [[Delta-Neutral Hedging]]).
2. **Risk warning for short options** — short gamma positions (naked short options,
   short straddle, etc.) are vulnerable to fast market moves.
3. **Long-volatility trades profit from gamma** — long straddles/strangles are
   long gamma; large moves accelerate gains.
4. **Gamma scalping** — a delta-neutral long-gamma position can lock in profits
   by re-hedging after each move (capture path).

### Trading-focused gamma management

- **Risk management around key levels** — high gamma near ATM and near expiry
  means delta swings quickly with price. A small move can flip a slightly
  bullish position into strongly bullish (or vice versa). Plan stops accordingly.
- **Decide management intensity** — high gamma positions need more frequent
  monitoring and possibly more frequent re-hedging. Low gamma (deep ITM/OTM,
  long-dated) = smoother delta, less babysitting.
- **Expiry choice by gamma tolerance**:
  - Short-dated ATM options: very high gamma → big delta swings, big P&L swings.
    Suited for active traders expecting a discrete move.
  - Longer-dated: smoother delta, lower gamma. Suited for slower thesis-style bets.

For trade templates (directional / income / vol) and gamma's role in each: see [[Greeks in Practice]].

## Gamma vs theta trade-off
- **High gamma** usually comes with **high negative theta** (especially near expiry).
- You pay for the ability to have rapidly changing delta with faster time decay.
- Selling gamma (short options) collects theta but bleeds in fast moves.

## Related
- [[Greeks]] (hub) · [[Delta]] (gamma is its derivative) ·
  [[Delta-Neutral Hedging]] · [[Position Greeks]] · [[Long Straddle]] (long gamma)

## Sources
[^1]: `raw/greeks-overview.md`
[^2]: simplify.us — what are option greeks.