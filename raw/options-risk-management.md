---
title: Options Risk Management — Practical Framework
type: source
tags: [options, derivatives, risk]
---

# Options Risk Management — Practical Framework

You manage risk in options by **controlling how much you can lose on each trade**,
using **defined-risk structures**, sizing positions conservatively, and having
clear **exit and hedging rules** before you enter.

A practical framework you can apply directly. Companion to
`raw/risk-management.md` (the broader futures+options conceptual hub).

## 1. Define your risk per trade and per portfolio

### Risk per trade
- Decide a fixed % of capital you're willing to lose on any single trade
  (commonly **0.5–2%** of total equity).
- Measure risk as **max possible loss** of the strategy, not premium or margin.
- Example: account = ฿1,000,000, risk 1%/trade → max loss = ฿10,000/trade.
  If strategy max loss = ฿2,000/lot → 5 lots (5 × 2,000 = 10,000).

### Portfolio-level risk
- Cap total risk across all open trades (e.g., total max loss ≤ 5–10% of equity).
- Avoid too many positions that all lose in the same scenario (e.g., all short
  premium, all long calls on tech).

## 2. Prefer defined-risk strategies

Use structures where **max loss is known and limited** at entry:
- **Vertical spreads** (bull call spread, bear put spread)
- **Iron condors / iron butterflies**
- **Butterflies, calendars, diagonals**
- **Collars** on long positions

Avoid or strictly limit:
- **Naked short calls/puts** (unlimited or very large risk)
- Over-leveraged directional bets without a clear stop or hedge.

Before entering, always know: max profit, max loss, break-even points, what
market view the trade expresses.

## 3. Use position sizing and lot-size discipline

Size based on **worst-case loss**, not potential profit:
1. Determine risk per trade (e.g., 1% of capital).
2. Compute max loss per lot for your strategy.
3. Lots = (risk per trade) ÷ (max loss per lot), rounded down.

Example:
- Account: ฿500,000. Risk: 1% = ฿5,000. Iron condor max loss: ฿8,000/lot.
- Allowed lots = 5,000 ÷ 8,000 = 0.625 → **0 lots** (trade smaller or reduce risk).

## 4. Set explicit exit rules

Decide **before entry** how you'll exit:

### Price-based exits
- Underlying hits a technical level (support/resistance, trendline break).
- Option price hits a stop-loss (e.g., −50% of premium) or profit target
  (e.g., +50–100%).

### Time-based exits
- Close before a known event (earnings, policy decision).
- Exit X days before expiry to avoid extreme gamma risk (especially 0DTE /
  very short-dated options).

### Greeks-based exits
- Close or adjust if delta becomes too large, theta decay is unacceptable for
  the thesis, or vega exposure is too high in a volatile environment.

Write these rules down and stick to them to avoid emotional decisions.

## 5. Use stop-losses intelligently

- **Long options**: stop-loss on the option price (exit if premium drops 40–60%)
  or stop on the underlying (e.g., stock breaks support).
- **Short options / spreads**: stop-loss on the **net debit/credit** or on the
  underlying level that invalidates the thesis. Mental stops or alerts if broker
  doesn't support conditional orders on multi-leg strategies.

Adjust stop distance for:
- Volatility (wider in high vol).
- Time to expiry (tighter near expiry for short premium).

## 6. Hedge with options

- **Protective put**: own stock/future + buy put. Caps downside; cost = premium.
  Good for high-conviction longs.
- **Covered call**: own stock/future + sell call. Income, reduces cost basis;
  caps upside.
- **Collar**: long underlying + long put + short call. Floor + ceiling; often
  low net cost.
- **Convert naked to spread**:
  - Long call → **bull call spread** (sell higher-strike call). Reduces net
    premium and max loss.
  - Naked short call → **call spread** (buy higher-strike call). Caps
    otherwise-unlimited risk.

## 7. Diversify across strategies, underlyings, and expiries

- **Strategy diversification**: mix income (covered calls, condors), directional
  (spreads), hedging (protective puts).
- **Underlying diversification**: different sectors, indices, asset classes.
- **Expiry diversification**: stagger weekly/monthly expirations.

## 8. Manage leverage and avoid overtrading

- Options are highly leveraged; small moves can cause large % changes.
- Control leverage by limiting number of lots; avoid 0DTE unless you fully
  understand gamma risk.
- Avoid overtrading: too many small impulsive trades increases transaction
  costs and error risk. Focus on quality setups.

Rule: "if you wouldn't take the trade with half the size, you probably shouldn't
take it at all."

## 9. Use scenarios and stress tests

Before placing a trade, ask:
- "What if the underlying moves **±5–10%** overnight?"
- "What if implied volatility **spikes or collapses** by 20–30%?"
- "What if the market stays flat for 5–10 days?"

Use option calculators / payoff tools + Greeks to estimate sensitivity. If the
worst-case outcome is unacceptable, reduce size or don't take the trade.

## 10. Pre-trade checklist

Before every options trade, answer:
1. What is my **market view** (direction, vol, time)?
2. Which **strategy** best expresses this view with defined risk?
3. What are **max profit, max loss, and break-evens**?
4. How much **capital** am I risking (in % and absolute terms)?
5. What are my **exit rules** (price, time, Greeks, P&L)?
6. How does this trade fit with my **other open positions**?
7. What happens in a **stress scenario** (big gap, vol spike)?

If you can't answer these clearly, the trade isn't ready.

## Sources

[^1]: `raw/options-risk-management.md` (this file).
[^2]: youtube.com/watch?v=8Te4gQ1j-zE — options risk management overview.
[^3]: capmint.com — options risk management. https://www.capmint.com/learn/articles/options-risk-management
[^4]: insiderfinance.io — mastering risk management in options trading. https://www.insiderfinance.io/resources/mastering-risk-management-in-options-trading
[^5]: youtube.com/watch?v=pimfQh0Wczk — position sizing worked example.
[^6]: wrightresearch.in — risk management in options trading. https://www.wrightresearch.in/blog/risk-management-in-options-trading/
[^7]: youtube.com/watch?v=aS2IJWvtJHw — exit rules.
[^8]: moomoo.com — risk management in options trading. https://www.moomoo.com/us/learn/detail-risk-management-in-options-trading-117739-241273055
[^9]: tradingpartner.in — options trading risk management strategies. https://tradingpartner.in/options-trading-risk-management-strategies/
[^10]: youtube.com/watch?v=TJuAWQ0HI88 — pre-trade checklist.