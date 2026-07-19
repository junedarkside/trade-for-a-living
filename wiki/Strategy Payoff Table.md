---
title: Strategy Payoff Table
type: reference
status: learning
tags: [options, derivatives, risk]
---

# Strategy Payoff Table

At-a-glance comparison of the core options strategies. Payoff shapes sketched
at **expiry** (x = underlying price, y = P&L). Always size to your **max loss**.

## Comparison

| Strategy | Legs | Max Profit | Max Loss | Breakeven | Payoff shape (expiry) | Best outlook |
|----------|------|-----------|----------|-----------|-----------------------|--------------|
| **[[Covered Call]]** | Long stock + short call | Premium (+ stock upside to strike) | Stock → 0 | Stock purchase − premium | `/` capped flat at strike | Neutral → mildly bullish |
| **[[Cash-Secured Put]]** | Short put (cash backed) | Premium | Strike − premium × 100 (if assigned) | Strike − premium | `\` then flat above strike | Neutral → mildly bullish; willing to own |
| **[[Protective Put]]**** | Long stock + long put | Unlimited (stock up − premium) | Stock purchase − strike + premium | Stock purchase + premium | `\` floored at strike − premium | Bullish, want a floor |
| **[[Collar]]** | Long stock + long put + short call | Capped at call strike | Reduced (put strike) | near stock purchase | flat floor + flat cap | Bullish, cheap protection |
| **[[Long Straddle]]** | Long call + long put (same strike/exp) | Unlimited | Total premium paid | Strike ± total premium | `\/` (V) — profits both tails | Volatile, direction unknown |
| **[[Vertical Spread]]** (bull call) | Long call + short call (higher strike) | (Width − net debit) × 100 | Net debit paid | Long strike + net debit | `_/` then flat | Moderately bullish, defined risk |

## Payoff shape legend

```
/   = rises with underlying (long delta)
\   = falls with underlying (short delta)
_   = flat (max profit or max loss reached)
\/  = V-shape: profits from moves in either direction
/\  = inverted V: profits if price stays put (short straddle)
```

## How to read this
- **Max Loss first.** Every row — know what you can lose before chasing profit.
- **Breakeven** = the spot price the underlying must reach at expiry for the
  position to net zero.
- **Payoff shape** tells you the *risk profile*; pair it with the Greeks in
  [[Greeks]] to understand behavior *before* expiry.
- Spreads and collars trade profit potential for defined risk / lower cost.

## Related
- [[Options Strategy]] — when to use each.
- [[Greeks]] — how positions behave before expiry.

## Sources
[^1]: `raw/options-strategies-overview.md`
