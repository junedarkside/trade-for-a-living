---
title: Theta
type: greek
status: learning
aliases: [Θ, theta]
tags: [options, derivatives, greek/theta]
---

# Theta

**Θ — time decay.** How much the option's price changes as one day passes,
holding spot and vol constant. Usually quoted per day.

## Definition
```
Θ = ∂P / ∂t
```

## Sign convention
- **Long options** (long call or long put): **negative theta** — you lose value each day.
- **Short options** (short call or short put): **positive theta** — you gain as time passes.
- **Stock / futures**: zero theta (no expiry).

## Long-holder meaning

**Long options bleed every day** even if the underlying doesn't move. This is the
**cost of optionality** — you're paying for time plus volatility.

**Short options collect every day**. This is the **income** from being an option seller.
But theta income can be dwarfed by gamma/vega losses in fast markets.

## Behavior over time and with spot

| State | |Theta| | Notes |
|-------|---------|-------|
| ATM | **highest** | Maximum time premium → maximum daily decay. |
| Deep ITM | moderate | Mostly intrinsic value; less to decay. |
| Deep OTM | low | Already mostly time, but small. |

| Time to expiry | Theta decay |
|----------------|-------------|
| Long dated (60+ days) | low per day, fairly linear. |
| 30 days | starts to accelerate. |
| Last week (ATM) | **highest absolute theta** — daily decay largest. |
| Last day | extreme if ATM; small if deep ITM/OTM. |

**Theta decay is non-linear** — accelerates in the last ~30 days, peaking just
before expiry for ATM options.

## Practical use

1. **Income strategies profit from theta** — short options ([[Covered Call]],
   [[Cash-Secured Put]], [[Iron Condor]], short strangles) all rely on positive
   net theta.
2. **Long-option holders need a big enough move** to beat theta. If you buy a
   30-day ATM straddle, you need a move larger than the total time decay over
   the holding period.
3. **Time horizon matters** — if your view is 1 week, paying 30 days of theta
   is wasted cost. Match option expiry to your horizon.
4. **Theta-gamma trade-off** — collecting theta (short options) means accepting
   negative gamma (vulnerable to fast moves). See [[Gamma]].

### Trading-focused theta decisions

- **Expiry selection by horizon**:
  - Near expiry: theta decays very fast — gold for sellers, brutal for buyers.
  - Longer-dated: slower daily decay, more time for your view to play out.
- **Event/vol trade theta cost** — long straddles/strangles have heavily
  negative theta. Need a big move or IV increase to overcome daily decay.
  Pre-flight question: "is the expected move large enough to beat theta?"
- **"5-day hold" checklist** — for a long-option position: compute
  `|theta × 5|` and ask "if the stock doesn't move for 5 days, how much do I lose?"
  If the answer is too close to your max acceptable loss, the trade is sized wrong
  or the expiry is too long.

For trade templates and the pre-trade checklist: see [[Greeks in Practice]].

## Related
- [[Greeks]] (hub) · [[Vega]] (paired with theta in time value) ·
  [[Position Greeks]] · [[Covered Call]] (theta-positive) · [[Long Straddle]] (theta-negative)

## Sources
[^1]: `raw/greeks-overview.md`
[^2]: youtube.com/watch?v=SFebmSYSZA8 — theta behavior.