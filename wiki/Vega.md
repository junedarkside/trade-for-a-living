---
title: Vega
type: greek
status: learning
aliases: [ν, vega]
tags: [options, derivatives, greek/vega]
---

# Vega

**ν — sensitivity to implied volatility.** How much the option's price changes
for a **1% change in IV**. Drives **event-driven** P&L.

## Definition
```
ν = ∂P / ∂σ
```
Where σ = implied volatility (decimal form, e.g. 0.30 for 30% IV).

## Sign convention
- **Long options** (long call or long put): **positive vega** — benefit from rising IV.
- **Short options** (short call or short put): **negative vega** — hurt by rising IV.
- **Stock / futures**: zero vega.

## Long-holder meaning

**Long options** = you want IV to **rise**. Buying before an event (when IV is
expected to spike) is the classic long-vol setup. After the event, IV often
collapses → "vol crush" can hurt long-option P&L even if the direction was right.

**Short options** = you want IV to **fall or stay low**. You collect premium
when IV is high; ideally it falls further as expiry nears.

## Behavior over time and with spot

| State | Vega | Notes |
|-------|------|-------|
| ATM | **highest** | Maximum uncertainty about whether it'll expire ITM. |
| Deep ITM / OTM | low | Outcome largely known; vol doesn't matter much. |

| Time to expiry | Vega |
|----------------|------|
| Near expiry | **lower** (less time for vol to matter). |
| Long dated (LEAPS) | **higher** (more time for vol to move price). |

**Vega peaks ATM, near expiry for short-dated, longer-dated for long-dated.**
Long-dated ATM options have the most vega of any single contract.

## Practical use

1. **Event trades** — long options before earnings / policy decisions: you're
   long vega, hoping the IV spike + move outweighs the vol crush after.
2. **Vol crush awareness** — if you buy options when IV is already very high
   (before earnings), even a correct directional move can lose money because
   IV collapses after the event.
3. **Vega-neutral hedging** — to hedge only directional risk without vol exposure,
   construct a position with zero net vega (e.g., long call + short call at
   different strikes with matched vega).
4. **Selling premium** — short-option strategies collect vega-negative P&L when
   IV falls. Favorable in stable, low-vol environments.

### Trading-focused vega decisions

- **Event timing** — before earnings / major news, IV is often high → buying
  options can be expensive. After the event, "vol crush" often drops IV,
  hurting long vega positions even if direction is right. Size or skip long
  vega plays in the elevated-IV window.
- **Long-dated = higher vega** — long-dated options are more sensitive to vol
  changes; short-dated options are dominated by gamma/theta, vega is lower.
  Use long-dated for pure vol expression, short-dated for tactical directional
  bets.
- **Short premium vega risk** — if you're short vol (iron condors, short
  straddles), an IV spike hurts before price moves. Cut size if IV starts
  spiking; define exits by IV level, not just price.

For trade templates (long vol / short vol profiles): see [[Greeks in Practice]].

## Vega vs theta trade-off
- Long options: **positive vega, negative theta** (you want IV up, time to pass hurts).
- Short options: **negative vega, positive theta** (you want IV down, time passing helps).
- These are two sides of the same "time value" coin.

## Related
- [[Greeks]] (hub) · [[Theta]] (paired with vega) · [[Position Greeks]] ·
  [[Long Straddle]] (long vega) · [[Iron Condor]] (short vega)

## Sources
[^1]: `raw/greeks-overview.md`
[^2]: youtube.com/watch?v=3C-NQadRRfo — vega walkthrough.
[^3]: simplify.us — what are option greeks.