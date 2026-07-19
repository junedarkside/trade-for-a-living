---
title: TFEX Position Limits
type: source
tags: [futures, options, derivatives, market/thailand]
---

# TFEX Position Limits — Research Notes

TFEX enforces **speculative position limits (SPL)** per product to prevent
market manipulation and concentration risk. Limits apply per account, aggregated
across months and across futures + delta-equivalent options for index products.

## Per-product SPL table [^1]

| Product | Speculative Position Limit (net, one side) | Price limit |
|---------|-------------------------------------------|-------------|
| **SET50 Index Futures** | **100,000** delta-equivalent (futures + options combined) | +30% of latest settlement |
| **SET50 Index Options** | **100,000** delta-equivalent (combined with futures) | +30% of prior-day SET50 |
| **Sector Index Futures** | **20,000** contracts (any month or aggregated) | +30% of latest settlement |
| **USD/THB Futures** | **20,000** delta-equivalent (futures + options combined) | ±2% initial → ±4% expanded |
| **Gold Futures (GF / GF10)** | Exchange-determined | ±10% initial → ±20% expanded |
| **Single-Stock Futures** | Tied to underlying share count (∝ float) | Per spec; varies by issue |

> Direct quote (SET50 Options spec): *"Net 100,000 delta equivalent SET50
> Index Futures contracts on one side of the market in any contract months
> of SET50 Index Futures and SET50 Index Options combined."* [^1]

## Aggregation rules

- **Index products**: delta-equivalent aggregation across futures +
  options (combined cap).
- **Sector index**: any-month or aggregated count (no delta weighting).
- **SSF**: per underlying share; tied to float since the **14 January 2013**
  rule change. Tier table published via TFEX circulars (not on public
  product spec sheets). [^2]
- **USD/THB**: futures + options combined (delta-equivalent).

## Hedger / market maker exemptions

- TFEX allows **position-limit exemptions** for:
  - Market makers
  - Hedgers with legitimate offsetting exposure
  - Deliverable swap contracts
- Application via TFEX Chapter 600 regulations. [^3]

## Penalty for breach

Per IOSCO-aligned Thai exchange practice, breach of SPL can trigger:

- Forced position reduction / liquidation
- Margin call escalation
- Regulatory penalties (fines, trading suspension)
- Specific penalty schedule in TFEX regulations Chapter 600.

## Practical trader implications

| Cadence | Action |
|---------|--------|
| **Daily** | Check broker open-position report against TFEX SPL per contract month |
| **Monthly** | SSF limits shift when underlying shares outstanding change (post-IPO secondary offerings) |
| **Annual** | SPL tables refreshed; review the latest TFEX revised-trading-criteria circular |

## Sources

[^1]: TFEX — Contract Specifications (SET50 Futures, Options, Sector, USD, Gold).
    https://www.tfex.co.th/en/products/
[^2]: TFEX — SSF SPL Notice (id=105236500).
    https://www.tfex.co.th/en/market-data/news-and-notice/trading-notice/newsdetails?id=105236500&symbol=TFEX
[^3]: TFEX — Chapter 600 Listing of Derivatives Contracts.
    https://media.tfex.co.th/rulebook/regulation/Chapter600TFEX_ListingofDerivativesContracts.pdf
[^4]: TFEX — Handbook for Foreign Investors.
    https://storage.googleapis.com/sg-prd-set-mis-cms/common/document/TFEX_Handbook.pdf
