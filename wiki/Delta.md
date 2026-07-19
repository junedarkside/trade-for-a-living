---
title: Delta
type: greek
status: learning
aliases: [Δ, delta]
tags: [options, derivatives, greek/delta]
---

# Delta

**Δ — price sensitivity to the underlying.** How much the option's price moves
per $1 move in the underlying. The first-derivative of the option price w.r.t.
spot.

## Definition
```
Δ = ∂P / ∂S
```
- **Call delta**: between **0 and +1**
- **Put delta**: between **0 and −1**
- For options on **futures** (Black model), delta is scaled by `e^(−rT)` — still
  bounded but slightly compressed.

## Sign convention
- **Long call**: positive delta (you want the underlying to rise).
- **Long put**: negative delta (you want it to fall).
- **Long stock**: delta = +1 (per share).
- **Short futures**: delta = −1 per contract.

## Long-holder meaning
| Position | Delta sign | Directional bias |
|----------|-----------|------------------|
| Long call | + (0 to +1) | Bullish |
| Long put | − (−1 to 0) | Bearish |
| Long stock | +1 | Bullish |
| Short call | − (0 to −1) | Bearish |
| Short put | + (0 to +1) | Bullish |

|delta| ≈ **probability proxy** for finishing ITM (heuristic, not exact).

## Behavior over time and with spot

| State | Call Δ | Put Δ |
|-------|--------|-------|
| Deep ITM | → +1 | → −1 |
| ATM | ≈ +0.50 | ≈ −0.50 |
| Deep OTM | → 0 | → 0 |

As time to expiry shrinks (ATM options), delta becomes **more bimodal** —
gravitating toward 0 or ±1 depending on whether spot is above or below strike.

## Practical use

1. **Directional exposure** — position delta ≈ share-equivalent count.
   - Example: +400 delta = behaves like being long 400 shares for small moves.
2. **Hedge sizing** — see [[Delta-Neutral Hedging]].
   - Hedge ratio = −(position Δ) / (Δ of hedge instrument).
3. **Strike selection** — choose an option whose delta matches the exposure you want.
   - ATM call ≈ 0.50 delta ≈ 50% of a stock's directional exposure.
4. **ITM proxy** — pick a strike whose delta matches your confidence in the move
   (0.30 delta = tentative view; 0.70 delta = strong view).

### Trading-focused sizing examples

- **Replicate a stock position with options**: to mimic long 200 shares, use 4
  ATM calls at delta ≈ 0.50: `4 × 0.50 × 100 = 200` share-equivalents. Cheaper
  capital than 200 shares, capped loss = premium paid.
- **High vs low delta trade-off**:
  - High delta (|0.7–0.9|): behaves more like the stock, less leverage, more
    expensive premium. Less room for vol to help.
  - Low delta (|0.1–0.3|): cheap, high leverage, low probability of profit.
    Big moves or big IV spikes needed to win.
- **Hedge formula**: to delta-hedge, trade the underlying so net delta = 0.
  Example: net delta +300 → sell 300 shares (or equivalent futures). See
  [[Delta-Neutral Hedging]] for the full re-hedging workflow.

For trader-focused framing (sizing templates, hedge checklists): see [[Greeks in Practice]].

## Related
- [[Greeks]] (hub) · [[Gamma]] (delta's derivative) · [[Delta-Neutral Hedging]] ·
  [[Position Greeks]] · [[Black Model]] (theoretical Δ for futures options)

## Sources
[^1]: `raw/greeks-overview.md`
[^2]: youtube.com/watch?v=3C-NQadRRfo — delta + hedging walkthrough.