---
title: Margin Mechanics
type: concept
status: learning
tags: [futures, options, derivatives]
aliases: [Margin, Initial Margin, Maintenance Margin, Margin Call]
---

# Margin Mechanics

**Margin** is the collateral you post to cover potential losses. Mechanics
differ sharply between **futures** and **options**, and between **long** and
**short** option positions. Understanding margin is non-negotiable: the wrong
margin model is what triggers liquidation cascades in crashes.

## Futures margin

| Term | Definition |
|------|------------|
| **Initial margin (IM)** | Required deposit to **open** a position. Set by exchange (TFEX) / broker. |
| **Maintenance margin (MM)** | Minimum equity to **hold** the position. Lower than IM. |
| **Mark-to-market (MTM)** | Daily (often intraday) P&L credited/debited to your account. |
| **Margin call** | Equity < MM → you must top up to IM or be **liquidated** by the broker. |

**Leverage effect.** Small underlying moves can wipe margin. See [[Futures —
Basics]] for a worked S50 example: 4% underlying move ≈ 100% margin loss.

### TFEX specifics

- TFEX sets **SPAN-equivalent** initial margins for S50, SSF, USDTHB etc.
  Margin schedules change — always re-check before sizing.
- Intraday margin < overnight margin (roughly halves capital needed for
  day-only positions). Position **must be flat by session close or overnight
  margin applies**.
- Margin call intraday: broker can liquidate **immediately** without further
  notice. You don't get to wait.

## Options margin

| Position | Margin requirement | Max loss |
|----------|-------------------|----------|
| **Long call / long put** | None beyond premium | Premium paid |
| **Short call (naked)** | Substantial (worst-case loss + vol buffer) | Large / unlimited in theory |
| **Short put (naked)** | Substantial | Strike − premium (if exercised) |
| **Multi-leg defined risk** (spreads, condors, butterflies) | **Margin offset** — usually ≈ max loss of structure | Defined by structure |
| **Multi-leg undefined risk** (short strangle naked) | Same as naked short call + put | Large / unlimited |

### Why defined-risk structures matter

Every spread, [[Iron Condor|iron condor]], [[Vertical Spread|vertical spread]],
[[Butterfly Spread|butterfly]] has a **capped max loss**. Margin = that max
loss (with small cushion). Risk is **known at entry**. This is why the
[[Options Risk Management]] playbook pushes defined-risk over naked shorts.

### Portfolio margin (PM)

- Looks at the **net risk** of the entire portfolio, including hedges.
- Multi-leg / hedged books get **much lower** margin than sum-of-legs.
- Requires approval + higher account minimums. Not all brokers offer it; in
  Thailand retail access may be limited.

For a hedged book (e.g., long stock + short OTM call), PM may allow
**substantially less** margin than Reg-T-style naked-short calculation.

## Practical rules

1. **Always know your margin schedule before entry.** IM, MM, intraday vs
   overnight rates, daily price limit (if any).
2. **Size for the loss you can survive, not the premium you want to collect.**
   A short strangle collecting ฿50K that risks ฿500K is a 10:1
   loss-to-premium — most of the time you'll win, but one black swan wipes
   years of gains.
3. **Don't over-leverage.** If normal vol triggers frequent margin calls,
   you're sized too big.
4. **Prefer defined-risk structures** when the view is right but the timing
   is uncertain — gives you margin = max loss, predictable and tradeable.
5. **Don't chase.** Adding to a losing naked short position because "it'll
   come back" is the classic blow-up pattern.
6. **Plan for gap risk.** Stop-loss orders don't trigger in a vacuum; a fast
   open against you can blow through stops and into margin call territory in
   minutes.

## Related

- [[Futures — Basics]] · [[Options — Basics]] · [[Settlement]] · [[Mark-to-
  Market]] _(alias for MTM)_ · [[Portfolio Margin]] · [[Multi-Leg Order]] ·
  [[Options Risk Management]] · [[Risk Management]] · [[Iron Condor]] ·
  [[Vertical Spread]] · [[Butterfly Spread]]

## Sources

[^1]: `raw/iv-and-market-mechanics.md` (section 3).
[^2]: ampfutures.com — Educational guide to futures and options on futures.
[^3]: cmegroup.com — Options on futures for equity traders.
[^4]: samco.in — Risk factor: futures vs options trading.
[^5]: TFEX — margin schedules and SPAN-equivalent methodology.
