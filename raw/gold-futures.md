---
title: Gold Futures
type: source
tags: [futures, commodities, market/thailand]
---

# TFEX Gold Futures — Research Notes

TFEX lists **5 distinct gold contracts**: GF, GF10, GD (Gold-D), GO (Gold
Online), MGO (Mini Gold Online). NOT fungible — each has its own contract
size, quoting currency, and settlement convention.

## Contract family summary

| | GF | GF10 | GD (Gold-D) | GO | MGO |
|---|---|---|---|---|---|
| Ticker | GF | GF10 | GD | GO | MGO |
| Quotation | THB / baht | THB / baht | USD / oz | USD / oz | USD / oz |
| Purity ref | 96.5% | 96.5% | 99.99% | 99.50% | 99.50% |
| Contract size | 50 baht (762.2 g) | 10 baht (152.44 g) | 100 g (3.2148 oz) | 300× / oz | 30× / oz |
| Tick size | THB 10 / baht | THB 10 / baht | USD 0.10 | USD 0.10 | USD 0.10 |
| Tick value | THB 500 | THB 100 | ~USD 0.32 | THB 30 | THB 3 |
| Settlement | **Cash THB** | **Cash THB** | **Physical** (99.99% gold) | **Cash THB** | **Cash THB** |
| Listed months | 3 nearest even months | Same | 1 nearest quarterly | 2 nearest quarterly | Same |
| Daily limit | ±10% → ±20% | Same | +10% → +20% | ±10% → ±20% | Same |
| Trading hours | Day 09:45–16:55; Night 18:50–03:00 | Same | Same | Same | Same |
| Position limit | Exchange discretion | Exchange discretion | 5,000 contracts (any month) | Exchange discretion | Exchange discretion |
| Last trading day | Bus day before last bus day of month; ends 16:30 | Same | Same | Same | Same |
| Exchange fee | THB 35 / side max | THB 7 / side max | THB 5 / side max | THB 14 / side max | THB 0.75–1.50 |

## Final settlement

- **GF / GF10**: `London Gold AM Fix × (15.244 / 31.1035) × (0.965 / 0.995) × (THB/USD)`. Purity and weight conversion applied. FX = Refinitiv THBTRDF=BKTH.
- **GO / MGO**: LBMA Gold AM Fix on last trading day; no FX adjustment (FX risk embedded in multiplier conversion).
- **GD**: physical delivery of 99.99% gold — not for retail.

## Practical differences

| Factor | Best choice |
|--------|-------------|
| **Retail size** | GF10 or MGO (smaller tick value) |
| **THB-denominated** | GF / GF10 |
| **USD-denominated** | GO / MGO / GD |
| **Physical delivery** | GD only |
| **OSE-referenced** | None (Thai contracts) |
| **Highest liquidity** | GO (Gold Online) — ~4.3M cumulative contracts vs ~407k for GF |

## Hedging / cross-contract basis

Different purity references create **structural basis risk** between
contracts. Hedging GF (96.5%) with GO (99.50%) leaves residual exposure.
Most Thai retail traders stick to one contract family (typically GF10 for
THB, GO/MGO for USD).

## Sources

[^1]: TFEX — Gold Futures Contract Specification.
    https://www.tfex.co.th/en/products/precious-metal/gold-futures/contract-specification
[^2]: TFEX — Gold Online Futures Contract Specification.
    https://www.tfex.co.th/en/products/precious-metal/gold-online-futures/contract-specification
[^3]: TFEX — Gold-D Contract Specification.
    https://www.tfex.co.th/en/products/precious-metal/gold-d/contract-specification
[^4]: TFEX — Product Catalogue.
    https://www.tfex.co.th/en/products
[^5]: CSI Data — TFEX Commodity Factsheet.
    https://apps.csidata.com/factsheets.php?type=commodity&format=exchange&exchangeid=TFEX
