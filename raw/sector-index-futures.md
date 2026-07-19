---
title: Sector Index Futures
type: source
tags: [futures, derivatives, market/thailand]
---

# TFEX Sector Index Futures — Research Notes

TFEX lists **5 sector index futures** for traders who want single-sector
exposure without picking individual stocks. Narrower than [[SET50 Futures]]
(broad market).

## Contract family

| Sector | Ticker | Multiplier | Tick size | Tick value | Exchange fee |
|--------|--------|------------|-----------|------------|--------------|
| **Banking** | BANK | THB 1,000 / pt | 0.10 pt | **THB 100** | THB 20 / side |
| **Information & Comm Tech** | ICT | THB 1,000 / pt | 0.10 pt | **THB 100** | THB 10 / side |
| **Energy & Utilities** | ENERG | THB 1,000 / pt | 0.10 pt | **THB 100** | THB 10 / side |
| **Commerce** | COMM | **THB 10 / pt** | 1 pt | **THB 10** | THB 5 / side |
| **Food & Beverage** | FOOD | **THB 10 / pt** | 1 pt | **THB 10** | THB 5 / side |

### Two-tier structure

- **High-multiplier (BANK / ICT / ENERG)**: THB 1,000/pt, 0.10pt tick — for
  sectors with high absolute index levels (banking index runs in thousands).
- **Low-multiplier (COMM / FOOD)**: THB 10/pt, 1pt tick — for sectors with
  lower absolute index levels.

## Common fields (all 5 sectors)

| Field | Value |
|-------|-------|
| Underlying | Sector Indices computed by SET |
| Listed months | **Quarterly: Mar, Jun, Sep, Dec** (up to 4 quarters at once) |
| Quote | Sector index price |
| Daily price limit | **±30%** of latest settlement |
| Position limit | Net **20,000 contracts / side**, per month or combined |
| Last trading day | Bus day before last bus day of month; ends **16:30** |
| Final settlement | **Cash**. Avg of sector index over last 15 min + closing index, **excluding 3 highest and 3 lowest**, rounded to 2 dp |
| Trading hours | Day only — morning 09:45–12:30; afternoon 13:45–16:55 (no night) |

## Index methodology

Constituent lists and weights are managed by SET, not TFEX. TFEX spec pages
link to SET's Industry Group/Sectoral Index methodology. Rebalancing and
constituent changes are SET-controlled.

## Use cases

| Strategy | Implementation |
|----------|----------------|
| **Sector rotation** | Long ENERG / short BANK without picking individual stocks |
| **Hedge single-sector exposure** | Hold concentrated banking portfolio → short BANK futures to neutralise sector beta |
| **Pairs trades** | Long ICT / short COMM for tech-vs-traditional rotation view |
| **Lower notional access** | COMM / FOOD (THB 10/pt) — ~50× less margin than BANK/ICT/ENERG |

## SET50 vs Sector Futures

| Aspect | SET50 | Sector Futures |
|--------|-------|----------------|
| Underlying | Broad market (top 50) | Single industry sector |
| Number of contracts | 1 | 5 |
| Multiplier | THB 200 / pt | THB 1,000 or THB 10 / pt |
| Tick | 0.01 pt | 0.10 or 1 pt |
| Settlement | Quarterly | Quarterly |
| Hours | Day + Night | **Day only** |
| Use case | Beta / macro hedge | Sector rotation / single-sector hedge |

## Liquidity caveat

5 separate contracts split the already-smaller sector-trader base.
**BANK** and **ICT** are the most active; COMM and FOOD are thinner.
Check current ADV and OI before sizing.

## Sources

[^1]: TFEX — Sector Index Futures Contract Specification.
    https://www.tfex.co.th/en/products/equity/sector-index-futures/contract-specification
[^2]: TFEX — Sector Index Futures Overview.
    https://www.tfex.co.th/en/products/equity/sector-index-futures
[^3]: SET — Industry Group Indices.
    https://www.set.or.th/en/market/index
[^4]: TFEX — Product Catalogue.
    https://www.tfex.co.th/en/products
