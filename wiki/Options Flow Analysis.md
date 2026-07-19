---
title: Options Flow Analysis
type: concept
status: learning
tags: [options, derivatives, market/thailand]
aliases: [Flow Analysis, UOA, Options Flow]
---

# Options Flow Analysis

**Options flow analysis** reads the footprints of large, informed, and hedging
trades to infer directional bias, key price levels, and vol regime shifts.
The core insight: dealers must hedge every option sold — their hedging creates
**predictable buying and selling** at specific price levels.

## Three data streams

| Stream | What it reveals |
|--------|----------------|
| **Volume + OI change** | Where contracts are being opened/closed; conviction vs closure |
| **Unusual Options Activity (UOA)** | Sweeps, blocks, volume spikes — likely informed or hedging |
| **Put/Call ratio (PCR)** | Aggregate sentiment; extreme readings = contrarian signal |

## Volume vs OI — the key distinction

| Signal | Interpretation |
|--------|----------------|
| High volume + rising OI | New positions opened — **conviction** |
| High volume + falling OI | Existing positions closed — exhaustion / profit-taking |
| High volume + flat OI | Offsetting trades — no net new positioning |

**Volume alone is noise.** OI change is signal.

## Unusual Options Activity (UOA)

**Trigger:** volume > 2× OI for that strike (fresh opening), OR volume > 5×
average daily volume.

| Type | Characteristics | Signal strength |
|------|----------------|-----------------|
| **Sweep** | Single large order filled immediately across multiple exchanges; price-insensitive | High — suggests urgency / informed |
| **Block** | Large print negotiated off-exchange | Medium — often hedging; verify context |
| **Repeat buyer** | Same strike accumulated over multiple days | High — conviction accumulation |

For TFEX SET50: watch for single-day OI spikes of 2,000+ contracts at a
specific strike in the daily OI report. That concentration changes dealer hedging obligations at that strike.

## Put/Call Ratio (PCR)

```
PCR (volume) = daily put volume / daily call volume
PCR (OI)     = total put OI / total call OI
```

| PCR | Reading | Contrarian signal |
|-----|---------|------------------|
| PCR > 1.2 | Fear / heavy hedging demand | Potential floor; selling may be exhausted |
| PCR 0.8–1.1 | Neutral | No signal |
| PCR < 0.7 | Greed / call speculation | Potential top |

Extreme PCR marks reversals more reliably than moderate readings. Track
PCR trend over 5 days for regime confirmation.

## Dealer positioning model

When clients buy options, dealers sell them — leaving dealers with hedging obligations that drive predictable spot flows:

- **Client buys call → dealer short call → dealer buys spot as price rises** (amplifying).
- **Client buys put → dealer short put → dealer sells spot as price falls** (amplifying).

Heavy OI concentrations = where dealers have the most hedging obligation → those strikes become **magnets** into expiry (pin risk) and **amplification zones** if breached. See [[Gamma Exposure]] for the GEX framework that quantifies this.

## Reading the TFEX daily OI report

1. Identify top 3 strikes by **call OI** → **call wall / resistance**.
2. Identify top 3 strikes by **put OI** → **put wall / support**.
3. Compare today vs yesterday OI per strike → rising OI = fresh positioning.
4. Calculate change in total net OI (rising total = new market participants entering).

## Thai-specific nuances

- TFEX liquidity is thinner than US equity index options — OI walls are rarer
  but proportionally more powerful (dealers are a larger fraction of total flow).
- Thai institutional flows (mutual funds, LTF/RMF) hedge via puts near
  quarter-end → systematic put OI buildup in March, June, September, December.
- Final settlement is cash-based on SET50 closing value; options pin toward
  peak-OI strikes the week before expiry Thursday.

## What flow analysis does NOT tell you

- It cannot distinguish hedging flow from directional flow with certainty.
- Large block prints are often portfolio rebalancing — not signals.
- Even informed flow gets the direction wrong 30–40% of the time.

Use flow as **confirmation**, not as a standalone signal. Combine with
regime indicators from [[Strategy Selection Framework]] and [[Volatility Risk Premium]].

## Related

- [[Open Interest]] · [[Gamma Exposure]] · [[Options Chain]] ·
  [[Volatility Risk Premium]] · [[Strategy Selection Framework]] ·
  [[Mark-to-Market]] · [[TFEX Market Structure]]

## Sources

[^1]: `raw/options-flow-analysis.md`
[^2]: CME Group — "Understanding Options Flow" (education series).
[^3]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 9 (options markets), Ch. 17.
[^4]: SpotGamma — GEX and flow methodology.
[^5]: TFEX — Daily OI report (tfex.co.th, free public download).
