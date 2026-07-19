---
title: Greeks — Trading Practice
type: source
tags: [options, derivatives, greek/delta, greek/gamma, greek/theta, greek/vega, greek/rho]
---

# Greeks — Trading Practice

When you trade options, the Greeks are your real-time risk dashboard: they tell
you how your position will react to moves in price, time, and volatility, and
how to size and adjust trades.

A practical, trader-focused view — companion to `raw/greeks-overview.md` (the
theoretical primer).

## 1. Delta: your directional exposure

**What it tells you**
- How much the option price changes for a **$1 move in the underlying**.
- Roughly, how "stock-like" the option behaves.

**Trading uses**
- **Sizing directional bets** — Call delta 0.50 ≈ 50% of a share's move. If you
  want the equivalent of 200 shares, you might use 4 calls with delta ~0.50
  (4 × 0.50 × 100 = 200).
- **Hedging** — if your options portfolio has net delta +300, you can sell 300
  shares (or equivalent futures) to make it delta-neutral.
- **Probability intuition** — many traders treat |delta| as an approximate
  probability of expiring ITM (e.g., 0.30 delta ≈ ~30% chance). Not exact, but useful.

**In practice**
- High delta (|0.7–0.9|): behaves more like the stock, less leverage, more expensive.
- Low delta (|0.1–0.3|): cheap, high leverage, lower probability ITM.

## 2. Gamma: how fast your delta changes

**What it tells you**
- How much **delta changes** for a **$1 move** in the underlying.
- It's the "acceleration" of your position.

**Trading uses**
- **Risk management around key levels** — high gamma near ATM and near expiry
  means your delta can swing quickly as price moves. A small move can turn a
  slightly bullish position into strongly bullish (or vice versa).
- **Deciding how actively to manage** — high gamma positions need more frequent
  monitoring and possibly more frequent re-hedging.
- **Choosing expiries** — short-dated ATM options: very high gamma → big delta
  swings, big P&L swings. Longer-dated: smoother delta, lower gamma.

**In practice**
- Long options: **positive gamma** (delta moves in your favor as the market moves).
- Short options: **negative gamma** (delta moves against you as the market moves)
  → dangerous in fast markets.

## 3. Theta: daily cost/benefit of time

**What it tells you**
- How much the option's price changes as **one day passes**, all else equal.
- Known as **time decay**.

**Trading uses**
- **Income strategies** — short premium (e.g., short strangles, iron condors,
  covered calls): you want **positive theta** so you collect decay each day.
- **Event/volatility trades** — long straddles/strangles: heavily **negative
  theta**; you need a big move or IV increase to overcome daily decay.
- **Expiry selection** — near expiry: theta decays very fast (good for sellers,
  brutal for buyers). Longer dated: slower daily decay, more time for your view
  to play out.

**In practice**
- Long options: theta is your enemy; every day you're "bleeding" value if the
  market doesn't move.
- Short options: theta is your friend, but you're often short gamma/vega, so
  you can get blown up by a big move or vol spike.

## 4. Vega: sensitivity to implied volatility

**What it tells you**
- How much the option price changes for a **1% change in implied volatility (IV)**.

**Trading uses**
- **Volatility trades** — long straddle/strangle: **positive vega**; you profit
  if IV rises or if a big move comes with high vol. Short straddle/strangle,
  iron condor: **negative vega**; you profit if IV falls and price stays quiet.
- **Timing around events** — before earnings / major news: IV often high;
  buying options can be expensive. After the event: "vol crush" often drops IV,
  hurting long vega positions even if direction is right.

**In practice**
- Long-dated options: higher vega (more sensitive to vol changes).
- Short-dated: lower vega, more dominated by gamma/theta.

## 5. Rho: interest rate sensitivity (often secondary)

**What it tells you**
- How much the option price changes for a **1% change in interest rates**.
- Calls: usually **positive rho**; puts: **negative rho**.

**Trading uses**
- Mainly relevant for:
  - **Long-dated options (LEAPS)**
  - Environments with large or fast rate moves
- For short-dated equity/index options, rho is often small compared to
  delta/theta/vega.

## 6. Putting Greeks to work in real trades

### Directional trade (e.g., bullish call)

You might look for:
- **Delta**: 0.40–0.60 for a balanced mix of leverage and probability.
- **Gamma**: understand that as price moves, your delta will change; near expiry,
  this is faster.
- **Theta**: know your daily time cost; if you expect a slow grind up, high theta
  can kill you.
- **Vega**: if IV is already high, a drop in vol can offset some gains even if
  price goes up.

**Practical checklist:**
- "If the stock doesn't move for 5 days, how much does theta cost me?"
- "If IV drops 5%, how much does vega hurt me?"
- "If price moves +$3, how much does delta increase (gamma) and how does that
  change my risk?"

### Income trade (e.g., short strangle / iron condor)

**Typical profile:**
- **Delta**: near zero (neutral view).
- **Theta**: strongly positive (you collect daily decay).
- **Vega**: negative (you want IV to fall or stay low).
- **Gamma**: negative (big moves hurt; delta can swing against you quickly).

**Risk management focus:**
- Define max loss (use spreads/condors instead of naked strangles).
- Set rules for:
  - When to close if underlying approaches a short strike.
  - When to reduce size if IV starts spiking.

### Volatility/event trade (e.g., long straddle)

**Typical profile:**
- **Delta**: near zero initially (you don't care about direction, just magnitude).
- **Gamma**: positive and high near expiry (big moves rapidly increase delta
  in your favor).
- **Theta**: strongly negative (you lose value every day if nothing happens).
- **Vega**: positive (you benefit if IV rises).

**Key questions:**
- "Is the expected move large enough to overcome theta?"
- "Is IV already pricing in a huge move, leaving little room for vol to increase?"
- "What's my exit plan if price stays flat and theta bleeds me?"

## 7. Position Greeks: managing the whole book

Instead of looking at single options, professionals monitor:
- **Net delta**: total directional exposure.
- **Net gamma**: how quickly that exposure can change.
- **Net theta**: daily P&L from time decay.
- **Net vega**: total sensitivity to vol.

**Example (simplified):**
- Long 10 calls, delta 0.40 → delta = 10 × 0.40 × 100 = +400
- Short 5 calls, delta 0.70 → delta = −5 × 0.70 × 100 = −350
- Net delta = +50 (behaves like long ~50 shares).

You adjust by:
- Adding/removing legs.
- Hedging with underlying or futures to bring net delta closer to your target
  (often 0 for neutral strategies).

See `wiki/Position Greeks.md` for the full framework (Taylor expansion, formulas,
design patterns).

## 8. Common mistakes when using Greeks

- Treating **delta as constant** and ignoring gamma, especially near expiry.
- Underestimating **theta** on long options; expecting "time to work for you"
  when it's working against you.
- Buying options when **IV is extreme**, then getting crushed by vol crush even
  with a correct directional call.
- Running **short premium** with high negative gamma and no defined risk, then
  getting caught in a fast move.

## Sources

[^1]: `raw/greeks-trading-practice.md` (this file).
[^2]: youtube.com/watch?v=SFebmSYSZA8 — Greeks dashboard.
[^3]: youtube.com/watch?v=P23VyHIaZJw — sizing & theta walkthrough.
[^4]: youtube.com/watch?v=3C-NQadRRfo — delta/hedging/volatility trades.
[^5]: simplify.us — what are option greeks. https://www.simplify.us/simplify101/what-are-option-greeks
[^6]: ryanoconnellfinance.com — option Greeks. https://ryanoconnellfinance.com/option-greeks/
[^7]: wealthsimple.com — option Greeks. https://www.wealthsimple.com/en-ca/learn/option-greeks