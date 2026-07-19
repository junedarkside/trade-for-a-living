---
title: USD-THB Futures
type: concept
status: learning
tags: [futures, derivatives, market/thailand]
aliases: [USDTHB, USD/THB Futures, USD Futures]
---

# USD/THB Futures

The **USD/THB futures** contract on [[TFEX Market Structure|TFEX]] gives Thai
traders direct exposure to the baht/dollar exchange rate in a centrally cleared,
on-exchange format. **1 contract = 1,000 USD notional**. P&L settles in THB.

This is the workhorse FX future for Thai traders — used for FX carry, hedging
USD-denominated assets, and short-term speculation on the baht.

## Contract specifications

| Spec | Value |
|------|-------|
| **Exchange** | TFEX (Thailand Futures Exchange) |
| **Underlying** | USD/THB spot rate |
| **Contract size** | **1,000 USD** |
| **Tick size** | **0.01 THB** |
| **Tick value** | **10 THB / contract** |
| **Multiplier** | 1,000 |
| **Settlement** | Cash (no physical USD delivery) |
| **Currency** | THB |
| **Margin** | Variable (SPAN-equivalent methodology, set by TFEX / broker) |
| **Options** | Yes — European style |

Trading sessions: **Morning / Afternoon / Night** (longer than US futures,
covers Asian + European sessions).

## Expiration

| Item | Rule |
|------|------|
| **Listed months** | 3 nearest months + next quarterly (Mar/Jun/Sep/Dec) |
| **Last trading day** | Business day **immediately preceding** the last business day of contract month |
| **Trading cutoff** | **11:00 AM Bangkok time** on the last trading day |
| **Final settlement** | **WM/Reuters USD/THB reference rate** at 11:00 AM on the last trading day |
| **Delivery** | **None** — cash settlement in THB |

### Worked expiration dates

| Contract Month | Last Business Day | Last Trading Day |
|----------------|-------------------|------------------|
| July 2026      | Thu 31 Jul        | Wed 30 Jul (11:00 AM) |
| August 2026    | Fri 29 Aug        | Thu 28 Aug (11:00 AM) |
| September 2026 | Tue 30 Sep        | Mon 29 Sep (11:00 AM) |

*(Dates shift with weekends and Thai public holidays — always check TFEX
rulebook.)*

> **Pin risk analogue:** the WM/Reuters fix at 11:00 AM is the **single
> number** that settles the contract. Movement between 11:00 AM and your
> position close is real P&L you can't hedge after the fix.

## Roll convention

Most active traders **don't hold until expiration**. Instead they **roll**:

- **3–5 trading days before** expiration, or
- When the **next contract's volume / OI exceeds the current contract's**
  (liquidity migration).

### Worked roll — long USDQ26 → USDU26

- You hold long **USDQ26** (Aug 2026).
- Approaching expiry (e.g., 5 days out):
  1. **Sell** USDQ26 at the current market.
  2. **Buy** USDU26 (Sep 2026).
- Net result: same USD-long exposure, just in the new contract month.
- **Roll cost** = price difference between the two contracts (USDU26 usually
  at slight premium to USDQ26 if curve is in contango; negative roll = you
  pay to maintain exposure). See [[Contango]] / [[Backwardation]] / [[Basis]].

Systematic strategies (trend-following, mean-reversion) **must** encode a roll
rule — otherwise backtest fills happen in illiquid expiring contracts, with
artificial slippage.

## Margin mechanics

- **Initial margin (IM)** and **maintenance margin (MM)** set by TFEX using a
  SPAN-equivalent methodology. Variable — change with broker and market
  conditions.
- See [[Margin Mechanics]] for the general framework.
- Day-only margin roughly halves capital required; position must be **flat by
  session close** or overnight margin applies.

## Settlement

- **Daily MTM** — P&L credited / debited to account each session.
- **At expiry** — final settlement in THB based on the WM/Reuters fix at
  11:00 AM. No USD account needed — you're never long or short physical USD
  through the future.

> If you have a **separate USD-denominated position** (e.g., US stocks, USD
> bonds), USD/THB futures give you a clean hedge without FX conversion
> friction.

## Worked example — long 1 contract

- Spot USD/THB = **35.50**.
- You buy 1 USD/THB future at **35.55** (1,000 USD notional).
- Required initial margin ≈ ฿2,000–฿5,000 (variable).
- USD/THB rises to **35.80**:
  - P&L per contract = (35.80 − 35.55) × 1,000 = **+฿250** (before fees).
- USD/THB drops to **35.20**:
  - P&L per contract = (35.20 − 35.55) × 1,000 = **−฿350**.

Leverage: small margin controls ฿35,000+ notional → 50–100× effective leverage.
**Gap risk** is real — baht moves on BOT policy decisions, USD news, capital
flow data.

## Strategy uses

| Use | Example |
|-----|---------|
| **FX carry** | Long USD future when US rates > TH rates (carry positive); short when reversed |
| **Import / export hedge** | Importer long USD future to lock ฿/USD cost; exporter short |
| **Hedge USD-denominated assets** | Long NVDR / US ETFs? Short USD future to neutralise FX |
| **Speculation** | Short-term baht view around BOT meeting, US Fed, capital-flow data |
| **Cross-asset overlay** | Combine with [[Delta-Neutral Hedging\|delta-neutral]] SET50 position to neutralise currency if SET50 has USD sensitivity |

## Pitfalls

1. **Last-day liquidity drop** — expiring contract widens bid/ask; roll early
   or you'll pay the spread.
2. **Settlement timing risk** — final fix at 11:00 AM is single point. Movement
   after that you can't hedge.
3. **Curve misread** — if you treat the front contract as "the USD/THB rate",
   you're actually trading the **front-month forward**, which may differ from
   spot by the [[Basis]] / [[Contango]] adjustment.
4. **Leverage blow-up** — high effective leverage means small adverse moves
   wipe margin fast. Size conservatively; use stops or defined-risk hedge
   structures.
5. **Holidays** — Thai and US holiday calendars differ. Settlement can fall
   on a half-day or shift; check TFEX announcements.

## Related

- [[TFEX Market Structure]] · [[Futures — Basics]] · [[Margin Mechanics]] ·
  [[Tick Size]] · [[Settlement]] · [[Contango]] · [[Backwardation]] ·
  [[Basis]] · [[NVDR]] · [[Delta-Neutral Hedging]]

## Sources

[^1]: `raw/usdthb-futures.md`
[^2]: TFEX — USD/THB Futures Contract Specification.
    https://www.tfex.co.th/en/products/currency/usd-thb-futures/contract-specification
