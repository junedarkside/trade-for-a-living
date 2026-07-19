---
title: Options Flow Analysis
source: Claude-draft from CME Group options flow education, CBOE market data guides, Hull Ch. 9/17, SpotGamma methodology, TFEX daily OI report structure
date: 2026-07-19
---

# Options Flow Analysis

## What it is

Options flow analysis = reading the footprints of large, informed, or hedging trades in the options market to infer directional bias, key price levels, and vol regime shifts.

Three data streams:
1. **Volume + OI changes** — where contracts are being opened/closed
2. **Unusual Options Activity (UOA)** — sweeps, blocks, odd-lot spikes above normal volume
3. **Put/Call ratios** — aggregate sentiment gauge

## Why it works

Dealers (market makers) hedge every option sold. Their hedging creates *predictable buying/selling at specific price levels*. Large option buyers (funds, institutions) who take directional positions leave a trail in volume and OI. Reading that trail = front-running their hedging flow.

Key insight: options flow is NOT always informational. Hedging flow from funds covering physical equity positions can look directional but isn't. Context matters.

## Volume vs OI

| Signal | What to look for |
|--------|-----------------|
| High volume + rising OI | New positions being opened — conviction |
| High volume + falling OI | Existing positions closing — exhaustion / profit-taking |
| High volume + flat OI | Offsetting trades — no net new positioning |

Volume alone is noise. OI change is signal.

## Unusual Options Activity (UOA)

Defined as: option volume > 2× OI (fresh opening) OR volume > 5× average daily volume for that strike.

Types:
- **Sweep** — single large order routed across multiple exchanges for immediate fill; price-insensitive = urgency = likely informed
- **Block** — single large print negotiated off-exchange; often hedging, less directional signal
- **Repeat buyer** — same strike bought multiple days in a row; accumulation = conviction

TFEX equivalent: watch for single-day OI spikes on a specific strike in the TFEX daily report. A strike that adds 2,000+ contracts in one session warrants investigation.

## Put/Call ratio (PCR)

```
PCR (volume) = daily put volume / daily call volume
PCR (OI)     = total put OI / total call OI
```

| PCR level | Interpretation | Contrarian read |
|-----------|---------------|-----------------|
| PCR > 1.2 | Heavy put buying — fear / hedging | Potential floor forming |
| PCR < 0.7 | Heavy call buying — greed / speculation | Potential top forming |
| PCR 0.8–1.1 | Neutral | No signal |

**Contrarian use**: extreme PCR often marks reversals. Funds hedging with puts = they're already protected = selling pressure may be exhausted.

## Reading the TFEX daily OI report

TFEX publishes end-of-day OI by strike and expiry for SET50 options. Steps:

1. Download or screen-read the daily OI table.
2. Identify the 3 strikes with highest call OI → **call wall** (resistance).
3. Identify the 3 strikes with highest put OI → **put wall** (support).
4. Compare today vs yesterday OI per strike → rising OI = accumulation.
5. Note the **net delta of large OI clusters** (use Black Model delta for each strike's gamma, scale by OI) → this is your rough GEX proxy.

## Dealer positioning model

For options sold to clients (typical retail flow):
- Client buys call → dealer sells call → dealer is **short gamma** at that strike → dealer **buys spot as price rises, sells as falls** (amplifying at that strike).
- Client buys put → dealer sells put → dealer **sells spot as price falls, buys as rises** → amplifying on downside.

Heavy OI strikes = where dealers have the most hedging obligation = price magnets into expiry (pin risk) and zones of amplified vol if broken.

## Thai-specific nuances

- TFEX SET50 options have lower liquidity than US equity index options; large OI clusters are rarer but more powerful because the hedging flow is proportionally larger vs daily volume.
- Expiry is the last Thursday of each month; OI concentrates there for the last 2 weeks. Watch for pin toward peak OI the week before expiry.
- Thai institutional flows (mutual funds, LTF/RMF portfolios) often hedge via puts near quarter-end — creates systematic put OI buildup.

## Sources

- CME Group, "Understanding Options Flow" (education)
- CBOE, "Market Statistics" methodology guide
- Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 9 (options markets), Ch. 17 (OI and positioning)
- SpotGamma — GEX and flow methodology
- TFEX daily OI report (tfex.co.th, free public download)
