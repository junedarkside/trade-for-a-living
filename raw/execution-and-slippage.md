---
title: Execution & Slippage
source: Claude-draft from CME Group execution guides, Hull Ch. 2 (futures markets), TFEX trading rules (tfex.co.th), market microstructure literature, practitioner notes on Thai market execution
date: 2026-07-19
---

# Execution & Slippage

## What slippage is

**Slippage** = the difference between the price you intended to trade at and the price you actually get. It is a **real cost** that compounds across trades and often determines whether a strategy with theoretical edge survives in practice.

Total execution cost per trade = **bid-ask spread paid + slippage from market impact**.

## Bid-ask spread cost (TFEX)

Each time you buy at the ask and sell at the bid, you pay the spread as an implicit cost.

| Product | Typical bid-ask spread | Spread cost (1 contract) |
|---------|----------------------|--------------------------|
| SET50 futures (S50) | 0.1–0.5 index points | ฿20–฿100 |
| SET50 options (near ATM, liquid) | 0.2–1.0 pts | ฿40–฿200 |
| SET50 options (far OTM) | 1–5+ pts | ฿200–฿1,000+ |
| Gold futures (GF) | 10–30 THB/troy oz | ฿100–฿300 |
| USD/THB futures | 0.01–0.05 THB/USD | ฿100–฿500 |
| Single-stock futures (SSF) | Wide; varies by underlying | Can be 0.5–2% notional |

Far OTM options can have spreads that represent 20–50% of the option premium → strategies relying on cheap OTM options often lose before the position starts.

## Market impact

Large orders move the market before they're filled. On TFEX, order book depth is thin compared to US equity index markets:

- Orders > 50 contracts on S50 options can visibly move the bid-ask.
- Multi-leg orders (condor, strangle) need to be priced as net debit/credit to minimize legging risk.

**Rule:** at TFEX liquidity levels, keep single-leg size ≤ 20–30 contracts to avoid significant market impact. For institutional sizes, use iceberg orders or negotiate blocks.

## Legging risk in multi-leg strategies

For strategies with 2+ legs (condor, strangle, calendar), two approaches:

| Approach | Pros | Cons |
|----------|------|------|
| **Sequential** (leg by leg) | Fill legs at favorable prices when possible | Risk: market moves between legs → fill at worse net price than intended |
| **Combination order (combo)** | TFEX supports combination orders for some standard structures; atomic fill | Harder to fill; wider net spread required to get both legs done |

**Best practice for TFEX:** always send as a net combination order when the product supports it. If not available, leg into the better-priced side first (usually the leg with more premium) then fill the other immediately.

## When NOT to trade (execution red flags)

1. **Spread > 10% of expected P&L** — cost erodes edge before the trade starts.
2. **OI at target strike < 200 contracts** — insufficient depth; any size moves the market.
3. **Within 30 minutes of SET open / close** — spreads widen, order book unstable.
4. **Morning of FOMC / BoT rate decision / large Thai economic data** — gap risk; execution quality degrades as market makers widen spreads pre-event.
5. **Day of TFEX product expiry** — bid-ask explodes on expiring strikes; only close existing positions, don't open new ones.

## Fill quality benchmarks

Track these in your journal (see [[Trade Journaling]]):

- **Average slippage per leg** = actual fill − midprice at time of order.
- **Fill rate** for limit orders = % of orders filled within X ticks.
- **Edge erosion** = strategy expectancy before costs vs after full execution costs.

If average slippage > 25% of expected P&L per trade, the strategy may not survive live execution even with positive backtest results.

## Commission costs (Thailand)

Approximate ranges (varies by broker, account size):

| Product | Approx. commission/contract |
|---------|-----------------------------|
| S50 futures | ฿25–฿60 |
| S50 options | ฿25–฿60 |
| Gold futures | ฿60–฿120 |
| SSF | ฿30–฿80 |

For a 4-leg iron condor: 4 × ฿50 = ฿200 round-trip minimum. Factor into net credit target (min credit > 2× commission).

## Size discipline

- Never size to fill speed — if you need to widen limit or go market to fill, the position is too large for current liquidity.
- Use TWAP (time-weighted average price) thinking for larger positions: stagger fills over 15–30 minutes rather than hitting all at once.

## Sources

- Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 2 (futures markets, margin, execution)
- CME Group — "Guide to Futures and Options Trading" (execution best practices)
- TFEX — Rules and Regulations, trading hours and order types (tfex.co.th)
- Augen, *The Volatility Edge in Options Trading* (cost-aware execution)
