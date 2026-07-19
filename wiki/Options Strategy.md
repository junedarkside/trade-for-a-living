---
title: Options Strategy
type: concept
status: learning
tags: [options, derivatives]
---

# Options Strategy

An **options strategy** is a structured plan for trading options contracts to
achieve a specific financial goal — generating income, hedging risk, or
speculating on price moves — based on your outlook for the underlying asset.

## Objectives vs outlook

| Objective | Outlook | Example strategies |
|-----------|---------|--------------------|
| Income generation | Neutral to bullish | [[Covered Call]], [[Cash-Secured Put]] |
| Hedging / protection | Neutral to bearish | [[Protective Put]], [[Collar]] |
| Speculation | Directional or volatile | [[Long Straddle]], [[Vertical Spread]], [[Strangle]] |

## Strategy index

### Income
- [[Covered Call]] — own stock, write a call against it.
- [[Cash-Secured Put]] — write a put, hold cash to buy if assigned.

### Hedging / protection
- [[Protective Put]] — own stock, buy a put as insurance.
- [[Collar]] — own stock + protective put + short call to fund the put.

### Range-bound / income
- [[Iron Condor]] — sell OTM call spread + OTM put spread; profit if price stays in range.
- [[Iron Butterfly]] — sell ATM straddle + buy wings; profit if price pins to strike.
- [[Butterfly Spread]] — 1-2-1 strikes; profit if price lands at the middle strike.

### Speculation / volatility
- [[Long Straddle]] — long call + long put, same strike/expiry; profit from big moves.
- [[Strangle]] — OTM call + OTM put (long = vol, short = range income); wider than straddle.
- [[Vertical Spread]] — buy + sell same-type options, same expiry, different strikes.

> Running several of these together? See [[Multi-Strategy Options]].

## Choosing a strategy

Depends on:
- **Market view** — bullish / bearish / neutral / volatility view.
- **Risk tolerance** — defined vs undefined risk.
- **Capital & margin** — spreads need margin; CSPs need cash.
- **Time horizon** — short-dated vs longer-dated (LEAPS).
- **Costs** — more legs = more commissions/fees.

## Start here
- Learn the building blocks: [[Options — Basics]].
- Master [[Greeks]] (delta, gamma, theta, vega) — they define every position's risk.
- Compare payoff shapes at a glance: [[Strategy Payoff Table]].
- Read the [[Options Chain]] to pick strikes and expiries for any strategy.
- Combine strategies into a book: [[Multi-Strategy Options]].
- Paper-trade before risking capital.

## Sources
[^1]: `raw/options-strategies-overview.md`
