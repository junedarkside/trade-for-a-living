---
title: Execution & Slippage
type: concept
status: learning
tags: [futures, options, derivatives, market/thailand]
aliases: [Slippage, Fill Quality, Execution Cost]
---

# Execution & Slippage

**Slippage** = the difference between the intended price and the actual fill.
It is a **real cost** that compounds across trades and often determines
whether a strategy with theoretical edge survives live trading.

```
Total execution cost = bid-ask spread paid + market impact slippage + commission
```

## Bid-ask spread cost (TFEX)

| Product | Typical bid-ask | Spread cost (1 contract) |
|---------|----------------|--------------------------|
| S50 futures | 0.1–0.5 index pts | ฿20–฿100 |
| S50 options (near ATM, liquid) | 0.2–1.0 pts | ฿40–฿200 |
| S50 options (far OTM) | 1–5+ pts | ฿200–฿1,000+ |
| Gold futures (GF) | 10–30 THB/troy oz | ฿100–฿300 |
| USD/THB futures | 0.01–0.05 THB/USD | ฿100–฿500 |
| Single-stock futures (SSF) | Wide; varies | 0.5–2% notional |

**Far OTM options** often have spreads = 20–50% of the option premium.
Strategies relying on cheap OTM options may lose the edge before the
position starts.

## Market impact (TFEX liquidity limits)

TFEX order book depth is thin vs US equity index markets:
- Orders > 50 contracts on S50 options can visibly move the bid-ask.
- Multi-leg orders (condor, strangle) fill better as net combinations.

**Practical limit:** keep single-leg size ≤ 20–30 contracts to avoid
significant market impact. For larger size, stagger fills over 15–30 minutes (TWAP approach).

## Multi-leg execution — legging risk

| Approach | Pros | Cons |
|----------|------|------|
| **Sequential** (leg by leg) | May capture favorable prices on individual legs | Market moves between fills → worse net |
| **Combination order** | Atomic fill; no legging risk | Harder to fill; wider net required |

**Best practice for TFEX:** use combination order when the product supports
it. If not available, fill the higher-premium leg first (locks in the primary
credit), then immediately fill the remaining leg.

## Commission costs (Thailand, approximate)

| Product | Commission / contract |
|---------|-----------------------|
| S50 futures | ฿25–฿60 |
| S50 options | ฿25–฿60 |
| Gold futures | ฿60–฿120 |
| USD/THB futures | ฿60–฿120 |
| SSF | ฿30–฿80 |

4-leg Iron Condor: 4 × ฿50 = ฿200 round-trip minimum. Net credit target
must exceed 2× commission per unit as a floor.

## When NOT to trade (execution red flags)

1. **Spread > 10% of expected P&L** — cost erodes edge before position starts.
2. **OI at target strike < 200 contracts** — insufficient depth; any size moves market.
3. **Within 30 min of SET open / close** — spreads widen; order book unstable.
4. **Pre-event** (FOMC, BoT rate decision, major Thai data) — dealers widen spreads.
5. **Day of TFEX expiry** — only close existing positions; don't open new ones.

## Fill quality tracking

Track in [[Trade Journaling]]:
- **Average slippage per leg** = actual fill − midprice at order time.
- **Fill rate** = % of limit orders filled within X ticks.
- **Edge erosion** = backtest expectancy vs live expectancy net of costs.

If average slippage > 25% of expected P&L per trade → strategy may not
survive live execution despite positive backtest.

## Worked example — S50 Iron Condor execution cost

- Sell 25,800 call @ 35 pts / Buy 25,900 call @ 20 pts / Sell 25,200 put @ 30 pts / Buy 25,100 put @ 18 pts.
- Theoretical net credit: (35 − 20) + (30 − 18) = 15 + 12 = **27 pts × ฿200 = ฿5,400**.
- Bid-ask cost per leg (0.5 pt each): 4 × 0.5 × ฿200 = **฿400 implicit cost**.
- Commission: 4 × ฿50 = **฿200**.
- **Real net credit: ฿5,400 − ฿400 − ฿200 = ฿4,800** (vs theoretical ฿5,400).
- Execution cost = 11% of gross credit → material; size accordingly.

## Related

- [[Multi-Leg Order]] · [[Order Types]] · [[Margin Mechanics]] ·
  [[Trade Journaling]] · [[Edge & Expectancy]] · [[Bid-Ask Spread]] ·
  [[TFEX Market Structure]] · [[Iron Condor]]

## Sources

[^1]: `raw/execution-and-slippage.md`
[^2]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 2 (futures markets, execution).
[^3]: CME Group — "Guide to Futures and Options Trading" (execution best practices).
[^4]: TFEX — Rules and Regulations, trading hours, order types (tfex.co.th).
[^5]: Augen, *The Volatility Edge in Options Trading* (cost-aware execution, real fills vs backtest).
