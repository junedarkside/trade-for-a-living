---
title: Risk Management
type: concept
status: reviewed
tags: [options, futures, derivatives, risk]
---

# Risk Management

**The discipline of controlling loss potential and trade survival.** This is the
cross-cutting framework that applies to every strategy in the vault — futures,
options, single-leg, multi-leg, directional, income, hedging.

Risk management is not a strategy. It is the **meta-discipline** that determines
whether a strategy survives long enough to play out its edge.

## Overview
Options and futures can dramatically increase both profit potential AND loss
potential. The key questions:
1. **Where is risk limited vs unlimited?**
2. **How does leverage and margin amplify both?**
3. **How does my strategy change my risk profile?**

## Risk hierarchy (raw, unhedged)

| Position | Max loss | Max profit | Risk class |
|----------|----------|------------|------------|
| **Long call / long put** | Premium paid | Uncapped (call) / large (put) | **Limited** |
| **Long stock** | Total loss of position | Uncapped | Large but bounded |
| **Long future / short future** | Uncapped both ways | Uncapped both ways | **Unlimited** |
| **Naked short call** | Uncapped | Premium received | **Unlimited** |
| **Cash-secured short put** | Strike − 0 (large) | Premium received | Large but bounded |
| **Spread / collar / condor** | Defined by structure | Defined by structure | **Defined** |

**The two big dangers**: naked short options + oversized futures. Both have
unlimited or very large loss potential.

## Risk drivers

### Leverage and margin
- **Futures**: trade on margin. Small % moves → large % moves in equity. Margin
  calls force exits at bad prices.
- **Long options**: no margin beyond premium, but can lose 100% quickly.
- **Short options**: margin required; losses can exceed premium many times.
- **Multi-leg structures**: [[Portfolio Margin]] reduces margin via spread
  offsets, but leverage remains.

### Time decay ([[Theta]])
- **Only affects options**, not futures.
- Long options: bleed daily; >90% expire worthless — buyers face many small losses.
- Short options: collect decay, but tail risk if the market moves sharply.

### Volatility ([[Vega]])
- **Options only**: prices depend heavily on IV.
- Long options: hurt by falling IV ("vol crush" after events).
- Short options: hurt by rising IV; losses appear before price moves.
- Futures: no vega, but vol affects margin requirements and stop-out likelihood.

### Liquidity and gap risk
- Both: wide bid-ask in illiquid strikes; gaps at opens or around news.
- Options: illiquid legs in multi-leg strategies make adjustment costly.
- See [[Multi-Leg Order]] for how atomic execution reduces legging risk.

## Risk by strategy type

| Family | Examples | Raw risk profile |
|--------|----------|------------------|
| **Directional** | Long futures, [[Long Call]], [[Long Put]] | Futures: unlimited; long options: limited to premium but high % of small losses. |
| **Income / short premium** | Naked short call/put, short strangle, [[Iron Condor]], [[Covered Call]] | Many small wins, occasional catastrophic loss (if not defined-risk). Defined-risk variants cap the loss. |
| **Hedging** | [[Protective Put]], [[Collar]] | Defined downside; cost = premium; capped upside. |
| **Multi-leg** | [[Vertical Spread]], [[Iron Condor]], [[Calendar Spread]] | Defined max profit + max loss; still leveraged; complexity and legging risks. |

See `raw/options-strategies-overview.md` and [[Options Strategy]] for the strategy
selection framework.

## Common pitfalls (account-killers)

- **Using futures like stocks** — ignoring margin and daily MTM; one bad gap
  wipes months of gains.
- **Selling naked options for "easy income"** — many small premiums; one event
  wipes years of gains.
- **Buying cheap OTM options repeatedly** — many small losses; occasional big
  win may not cover drawdown.
- **Over-leveraging** — too much notional vs account; normal vol triggers
  margin calls.
- **No defined exit plan** — no stop-loss, no max loss per trade, no scenario
  analysis; emotional decisions under stress.

## Practical rules (baseline discipline)

1. **Position sizing** — risk only a small fixed % of capital per trade
   (e.g., **0.5–2% of equity**). Size based on **worst-case loss**, not
   expected profit.
2. **Defined-risk structures** — prefer spreads, condors, butterflies, collars
   over naked short options. Know **max loss, max profit, break-evens** before
   entering.
3. **Stops and exit rules** — futures: stop-loss/take-profit levels. Options:
   define exit by price level, time, P&L, or Greeks thresholds (e.g., delta
   too large). See [[Greeks in Practice]] for the pre-trade checklist.
4. **Leverage control** — keep total notional exposure (futures + option deltas)
   within a comfortable range relative to equity. Reduce size in high-vol regimes
   or around events.
5. **Scenario and stress testing** — "what if market gaps ±5% overnight?".
   Check P&L under large price moves, vol spikes/drops, time decay over flat days.
6. **Use multi-leg orders** — atomic execution, no legging risk, better margin.
   See [[Multi-Leg Order]].

## Futures vs options — which is riskier?

Depends on **how** you use them:

| Usage | Riskier |
|-------|---------|
| **Raw, unhedged** | Futures (unlimited both ways) ≈ naked short options (unlimited). Long options limited. |
| **Defined-risk option combos** | Often less risky than naked futures (defined max loss). |
| **Futures with tight stops + small size** | Can be simpler than complex option books. |

**Biggest practical risks**: unlimited-risk structures, excessive leverage, lack
of defined exit and risk limits. Strategy sophistication matters less than
position sizing and discipline.

## Related
- [[Options Strategy]] · [[Multi-Strategy Options]] · [[Options — Basics]] ·
  [[Greeks]] · [[Greeks in Practice]] · [[Position Greeks]] ·
  [[Delta-Neutral Hedging]] · [[Dynamic Hedging]] (operational playbook) ·
  [[Portfolio Margin]] · [[Multi-Leg Order]] · [[Black Model]] ·
  [[Covered Call]] · [[Protective Put]] · [[Collar]] · [[Iron Condor]] ·
  [[Vertical Spread]] · [[Long Straddle]] ·
  [[Options Risk Management]] (practical playbook: sizing formulas, exits, checklist) ·
  [[Pre-Trade Checklist]] (one-page reference)

## Sources
[^1]: `raw/risk-management.md`
[^2]: ampfutures.com — NFA Educational Guide to Trading Futures and Options on Futures.
[^3]: cmegroup.com — trading options on futures using strategies you already know.
[^4]: livemint.com — what is much riskier, futures or options.
[^5]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 1 (risk profiles) and Ch. 19 (volatility smiles and risk management).
[^6]: TFEX — Risk Disclosure Statement for Derivatives Trading (publicly available at tfex.co.th).