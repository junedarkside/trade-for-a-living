---
title: Greeks — Overview
type: source
tags: [options, derivatives, greek/delta, greek/gamma, greek/theta, greek/vega, greek/rho]
---

# Greeks — Overview

The **Greeks** are risk measures that tell you how an option's price is expected
to change when key inputs change (underlying price, time, volatility, interest
rates). They come from the option pricing model (e.g., Black-Scholes / Black for
futures options).

## 1. The main Greeks

### Delta (Δ) — price sensitivity to the underlying

**Definition:** Delta measures how much the option's price changes for a **$1
change in the underlying** price.

- Call delta: between **0 and +1**
- Put delta: between **0 and −1**

**Example:**
- Long call with delta = **+0.45**: if the stock rises by $1, the option price
  should rise by about **$0.45**.
- Long put with delta = **−0.35**: if the stock rises by $1, the option price
  should fall by about **$0.35**.

**Uses:**
1. **Directional exposure** — portfolio delta of +200 behaves roughly like being
   long 200 shares of the underlying for small moves.
2. **Hedge ratio** — to make a position delta-neutral, offset total delta with
   the underlying (or futures). Example: long 10 calls, each delta 0.40 → total
   delta = 10 × 0.40 × 100 = 400 share-equivalents. Sell 400 shares (or
   equivalent futures) to neutralize.
3. **Rough "probability ITM" proxy** — traders often treat |delta| ≈ probability
   the option expires ITM (not exact, but useful intuition).

**Behavior:**
- ITM calls: delta → +1; ITM puts: delta → −1
- OTM calls/puts: delta → 0
- ATM options: delta around ±0.50 (calls/puts respectively).

### Gamma (Γ) — how delta changes

**Definition:** Gamma measures how much **delta changes** for a **$1 change in
the underlying**. It is the **second derivative** of the option price with
respect to the underlying.

**Example:** Call with delta = 0.50, gamma = 0.08:
- If stock rises $1, delta goes from 0.50 → ~0.58
- If stock falls $1, delta goes from 0.50 → ~0.42

**Why it matters:**
- High gamma means delta can change quickly → position risk can shift fast.
- Gamma is highest for **ATM options** and for **near-expiry** options.
- Long options → **positive gamma**
- Short options → **negative gamma**

**Practical impact:**
- Long gamma: as the market moves in your favor, your delta increases (for calls)
  or becomes more negative (for puts), accelerating gains. Against you, delta
  moves against you less aggressively.
- Short gamma: small moves can cause large delta swings; dangerous in fast markets.

### Theta (Θ) — time decay

**Definition:** Theta measures how much the option's price changes as **one day
passes**, assuming underlying price and volatility stay constant. Often called
**time decay**.

- Typically expressed as **change per day**.
- Long options: **negative theta** (you lose value each day).
- Short options: **positive theta** (you gain as time passes).

**Example:**
- Long call with theta = **−0.05**: option loses about **$0.05 per day**.
- Short put with theta = **+0.04**: you gain about **$0.04 per day** from time decay.

**Behavior:**
- Theta decay is fastest for **ATM options** and as expiration approaches.
- OTM and deep ITM options have lower absolute theta.
- Long straddles/strangles: heavily negative theta (need a big move to offset daily decay).

### Vega (ν) — sensitivity to implied volatility

**Definition:** Vega measures how much the option's price changes for a **1%
change in implied volatility (IV)**.

- Long options: **positive vega** (benefit from rising IV).
- Short options: **negative vega** (hurt by rising IV).

**Example:** Call with vega = **0.12**:
- IV rises from 30% → 31%: option price should increase by about **$0.12**.
- IV falls from 30% → 29%: option price should decrease by about **$0.12**.

**Behavior:**
- Vega is highest for **ATM** and **longer-dated** options.
- Around events (earnings, policy decisions), IV often spikes → long vega positions
  can gain even if the underlying doesn't move much.
- After events, IV often collapses ("vol crush"), hurting long vega and helping short vega.

### Rho (ρ) — sensitivity to interest rates

**Definition:** Rho measures how much the option's price changes for a **1%
change in the risk-free interest rate**.

- Call options: **positive rho** (higher rates → higher call prices).
- Put options: **negative rho** (higher rates → lower put prices).

In many short-dated equity/futures options, rho is relatively small compared to
delta/theta/vega, but it can matter for **long-dated options (LEAPS)** or in
environments with big rate moves.

## 2. How the Greeks interact

An option's price change can be approximated (for small moves) by:

```
ΔP ≈ Δ · ΔS + ½ · Γ · (ΔS)² + Θ · Δt + ν · Δσ + ρ · Δr
```

Where:
- `ΔS` = change in underlying price
- `Δt` = change in time (days or years)
- `Δσ` = change in implied volatility
- `Δr` = change in interest rate

**Key interactions:**
- **Delta + Gamma**: delta tells you the first-order move; gamma tells you how
  that delta itself changes as the market moves.
- **Theta + Vega**: both relate to the "time value" part of the premium.
  Long options: negative theta, positive vega. Short options: positive theta, negative vega.
- **Gamma vs Theta**: high gamma usually comes with high negative theta (especially
  near expiry). You pay for rapidly changing delta with faster time decay.

## 3. Individual option Greeks vs. position Greeks

You can sum Greeks across all legs to get **position Greeks**:

- **Position delta** = sum of (quantity × contract multiplier × delta) for each leg
- Same for gamma, theta, vega, rho.

**Example (simplified):**
- Long 5 calls, delta = 0.40 each
- Short 3 calls, delta = 0.60 each
- Contract size = 100 shares

Position delta = 5 × 0.40 × 100 − 3 × 0.60 × 100 = 200 − 180 = **+20**

The whole structure behaves like being long ~20 shares for small moves.

Professional traders monitor:
- **Net delta** (directional exposure)
- **Net gamma** (how fast delta can change)
- **Net theta** (daily P&L from time decay)
- **Net vega** (exposure to vol changes)

See `wiki/Position Greeks.md`.

## 4. How Greeks behave by moneyness and time

### By moneyness

| State | Delta | Gamma | |Theta| | |Vega| |
|-------|-------|-------|---------|--------|
| Deep ITM call | ≈ +1 | low | moderate | low |
| ATM call | ≈ +0.50 | **high** | **high** | **high** |
| Deep OTM call | ≈ 0 | low | low | low |

Similar logic for puts (with negative deltas).

### By time to expiration

| Horizon | Gamma | Theta | Vega |
|---------|-------|-------|------|
| Near expiry | **very high** (ATM) | **very high** (ATM) | lower |
| Long dated | lower | lower (per day) | **higher** |

## 5. Using Greeks in practice

### For directional trades
- Choose delta to match your intended exposure.
- Watch gamma: high gamma near expiry means your delta can swing quickly → more
  active management.
- Consider theta: if you're long options, ensure your expected move is big enough
  to beat time decay.

### For income / short premium
- Positive theta is your friend (you collect time decay).
- But you're often **short gamma** and **short vega**:
  - Short gamma → big moves can hurt fast.
  - Short vega → IV spikes can hurt even before price moves.
- Manage risk with:
  - Defined-risk structures (spreads, iron condors, butterflies).
  - Stops or adjustment rules.

### For volatility trades
- Long straddle/strangle: high positive vega, high negative theta, significant
  gamma. Need a big move or an IV increase to profit.
- Short straddle/strangle: negative vega, positive theta, negative gamma. Profit
  if price stays quiet and/or IV falls.

### For hedging
- Use delta to size hedges: hedge ratio = −(position delta) / (delta of hedge instrument).
- Monitor gamma to know how often you may need to re-hedge.
- Vega and theta matter if your hedge horizon is more than a few days.

## 6. Common pitfalls

- Ignoring **gamma**: assuming delta is constant; it isn't, especially near expiry
  or for ATM options.
- Underestimating **theta**: long options can lose value quickly even if the
  underlying doesn't move much.
- Overlooking **vega**: entering long options just before an event when IV is
  already very high; then "vol crush" kills value even if direction is right.
- Treating Greeks as exact: they are **approximations** based on models and
  current conditions; they change as the market moves ("dynamic Greeks").

## Sources

[^1]: `raw/greeks-overview.md` (this file).
[^2]: youtube.com/watch?v=SFebmSYSZA8 — Greeks primer.
[^3]: youtube.com/watch?v=3C-NQadRRfo — delta + hedging + probability-ITM intuition.
[^4]: ryanoconnellfinance.com — option Greeks. https://ryanoconnellfinance.com/option-greeks/
[^5]: simplify.us — what are option greeks. https://www.simplify.us/simplify101/what-are-option-greeks
[^6]: learnsignal.com — Greeks options trading. https://www.learnsignal.com/blog/greeks-options-trading-delta-gamma-theta-vega-rho/
[^7]: wealthsimple.com — option Greeks. https://www.wealthsimple.com/en-ca/learn/option-greeks