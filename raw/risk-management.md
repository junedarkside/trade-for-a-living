---
title: Risk Management — Options & Futures
type: source
tags: [options, futures, derivatives, risk]
---

# Risk Management — Options & Futures

Options and futures can dramatically increase both **profit potential** and
**loss potential** compared to trading the underlying asset alone. The key is
understanding **where risk is limited vs unlimited**, how **leverage and margin**
work, and how different strategies change your risk profile.

## 1. Core risk differences: futures vs options

### Futures
- **Obligation**, not a right: both buyer and seller must fulfill the contract
  at expiry (or roll/close before).
- **Linear payoff**: long future P&L moves 1:1 with the underlying price; short
  future inverts.
- **Risk**: **unlimited** in both directions. Daily **mark-to-market**: losses
  trigger margin calls; you may need to add cash quickly or be liquidated.

### Options
- **Right vs obligation**: buyer has the right; seller has the obligation if
  exercised.
- **Non-linear payoff**: option value depends on underlying price, time, and
  volatility.
- **Risk by role**:
  - **Long call / long put**: max loss = **premium paid** (limited). Profit can
    be very large (uncapped for calls, large for puts).
  - **Short call / short put**: max gain = **premium received** (limited). Loss
    can be very large or effectively unlimited (especially naked short calls).

**Hierarchy of raw risk (no hedging, no spreads):**
- **Limited risk**: buying options (long calls/puts).
- **Unlimited / very large risk**: long/short futures, short (naked) calls and puts.

## 2. Risk drivers in options and futures strategies

### Leverage and margin
- **Futures**: trade on margin. Small % moves in the underlying can cause large
  % moves in your equity. Margin calls force exits at bad prices.
- **Options**: long = no margin beyond premium; short = margin required;
  losses can exceed premium many times. Multi-leg strategies can reduce margin
  via spread offsets.

### Time decay (theta)
- Only affects **options**, not futures.
- Long options: lose value every day if the underlying doesn't move enough.
  Over 90% of options expire worthless — buyers often face many small losses.
- Short options: benefit from time decay, but with large tail risk if the
  market moves sharply.

### Volatility risk (vega)
- **Options**: prices depend heavily on IV. Long options hurt by falling IV
  ("vol crush" after events); short options hurt by rising IV.
- **Futures**: no direct vega, but vol affects margin requirements and the
  likelihood of stop-outs.

### Liquidity and gap risk
- Both: wide bid-ask spreads in illiquid strikes/expiries; gaps at opens or
  around news.
- Options: illiquid legs in multi-leg strategies make adjustment/exiting costly.

## 3. Risk by common strategy type

### Directional speculation
- **Long futures**: simple, linear, highly leveraged. Risk: large, potentially
  unlimited losses if trend goes against you.
- **Long calls / long puts**: limited risk (premium), high leverage. Risk: high
  probability of small losses; need big, timely moves.

### Income / short premium
- **Short straddle/strangle, naked short options**: positive theta, but
  unlimited or very large risk if market moves. Negative gamma and vega.
  Many small wins, occasional catastrophic loss.
- **Covered calls / cash-secured puts**: lower risk than naked, but still
  exposed to large moves; opportunity cost on upside.

### Hedging
- **Protective put**: limits downside, cost = premium. "Wastes" premium if no
  crash.
- **Collar**: defines floor and ceiling. Capped upside; complexity; early
  assignment risk on short call.

### Multi-leg / combination strategies
- **Spreads, condors, butterflies, calendars**: defined max P&L by design.
  Risks: still leveraged; complex adjustments; legging risk if not using
  multi-leg orders; liquidity risk on thin legs.

## 4. Common pitfalls that blow up accounts

- **Using futures like stocks** — ignoring margin and daily MTM; one bad gap
  wipes months of gains.
- **Selling naked options for "easy income"** — many small premiums, one event
  wipes years of gains.
- **Buying cheap OTM options repeatedly** — many small losses; occasional big
  win may not cover drawdown.
- **Over-leveraging** — too much notional vs account size; normal volatility
  triggers margin calls.
- **No defined exit plan** — no stop-loss, no max loss per trade, no scenario
  analysis; emotional decisions.

## 5. Practical risk management rules

1. **Position sizing** — risk only a small fixed % of capital per trade (e.g.,
   0.5–2% of equity). Size based on **worst-case loss** of the strategy, not
   expected profit.
2. **Defined-risk structures** — prefer spreads, condors, butterflies, collars
   over naked short options. Know **max loss, max profit, break-evens** before
   entering.
3. **Stops and exit rules** — futures: stop-loss/take-profit levels and respect
   them. Options: define exit by price level, time, P&L, or Greeks thresholds.
4. **Leverage control** — keep total notional exposure (futures + option deltas)
   within a comfortable range relative to equity. Reduce size in high-vol
   regimes or around events.
5. **Scenario and stress testing** — ask "what if market gaps ±5% overnight?".
   Check P&L under large price moves, vol spikes/drops, time decay over flat days.
6. **Use multi-leg orders** — enter/exit complex strategies as a single package
   to avoid legging risk and improve margin efficiency.

## 6. Which is "riskier": futures or options?

Depends on **how** you use them:
- **Raw, unhedged**: futures unlimited risk both ways; short options effectively
  unlimited; long options limited but high probability of small losses.
- **With strategy**: well-structured option combos (spreads, collars, condors)
  can have more controlled risk than naked futures. Futures with tight stops and
  small size can be simpler than complex option books.

**In practice, biggest risks:**
- Unlimited-risk structures (naked short options, oversized futures).
- Excessive leverage.
- Lack of defined exit and risk limits.

## Sources

[^1]: `raw/risk-management.md` (this file).
[^2]: ampfutures.com — NFA Educational Guide to Trading Futures and Options on Futures. https://www.ampfutures.com/hubfs/AMP%20Futures%20(USA)%20-%20Website/NFA-%20Opportunity%20and%20Risk-%20An%20Educational%20Guide%20to%20Trading%20Futures%20and%20Options%20on%20Futures.pdf
[^3]: metrotrade.com — trading futures vs options. https://www.metrotrade.com/trading-futures-vs-options/
[^4]: youtube.com/watch?v=Qb2BGoomHfg — option payoff/risk walkthrough.
[^5]: livemint.com — what is much riskier, futures or options. https://www.livemint.com/market/stock-market-news/what-is-much-riskier-futures-or-options-11663925308179.html
[^6]: samco.in — risk factor in futures vs options trading. https://www.samco.in/knowledge-center/articles/risk-factor-futures-trading-or-options-trading/
[^7]: cmegroup.com — trading options on futures using strategies you already know. https://www.cmegroup.com/education/courses/options-on-futures-for-equity-traders/trading-options-on-futures-using-strategies-you-already-know
[^8]: yesinvest.in — risk management and strategies. https://yesinvest.in/knowledge-hub/futures-and-options/risk-management-and-strategies
[^9]: 5paisa.com — how to manage risk in futures and options trading. https://www.5paisa.com/hindi/blog/how-to-manage-risk-in-futures-and-options-trading