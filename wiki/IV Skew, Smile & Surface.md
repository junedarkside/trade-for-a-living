---
title: IV Skew, Smile & Surface
type: concept
status: learning
tags: [options, derivatives]
aliases: [Volatility Skew, Skew, Smile, Vol Surface, IV Skew]
---

# IV Skew, Smile & Surface

In Black-Scholes with constant volatility, all strikes share one IV. In
reality, IV varies by strike — this is the **volatility skew** (or "smile" /
"smirk" depending on shape). When you stack skew across expirations you get
the **volatility surface**: `IV(strike, expiry)`.

## Skew

| Pattern | Shape | Where |
|---------|-------|-------|
| **Negative skew (smirk)** | OTM puts >> OTM calls in IV | Equity indices (e.g., SET50), single stocks with downside risk |
| **Symmetric smile** | Both wings elevated vs ATM | FX, commodities |
| **Positive skew** | OTM calls > OTM puts | Energy / commodity upside tail |

**Why equity index skew is negative:** structural demand for downside
protection (hedgers, pension funds, tail-risk funds) pushes OTM put IV higher
than OTM call IV. The market **pays** for crash insurance.

## Why skew matters for a trader

1. **Pricing** — OTM puts are more expensive than equidistant OTM calls. A
   "symmetric" strangle is not actually symmetric in premium or risk.
2. **Strategy selection:**
   - **Sell OTM puts** in steep skew → rich premium, but tail risk (sharp
     downside) is real.
   - **Buy OTM puts** for protection → expensive; consider put spreads
     instead.
   - **Risk reversals** (long OTM call + short OTM put, or vice versa) capture
     skew mispricing — see [[Risk Reversal]].
3. **Risk** — skew can **widen** sharply in stress (VIX spikes often widen
   the put wing dramatically), moving position values even when spot barely
   moves.
4. **Strike selection** — heavy OI walls in the [[Options Chain]] (call-OI
   resistance / put-OI support) cluster around where the market expects
   defence; skew often steepens away from those strikes.

## Volatility surface

```
IV
 │   \           /
 │    \   ATM   /
 │     \_______/      ← smile (FX/commodities)
 │
 │   \                ← smirk (equity indices)
 │    \
 │     \_______
 └─────────────── strike
        spot
```

- **Skew slice** at one expiry: IV vs strike.
- **Term structure**: ATM IV vs expiry (often upward sloping in calm markets,
  inverted after shocks).
- **Surface**: both together — the full pricing landscape.

### What traders actually use

Most traders don't model the full surface; they read a few slices:

| Slice | Question answered |
|-------|-------------------|
| **ATM term structure** | Is near-term vol priced higher than long-term? (Event risk priced in?) |
| **25-delta skew** (risk reversal) | How expensive is downside protection? |
| **Butterfly** (25d call + 25d put − 2× ATM) | How convex is the smile? Event / pin-risk gauge |
| **Skew at weekly vs monthly** | Is short-dated put demand spiking? (Earnings / event) |

## Worked example — SET50 30-day chain

- Spot = 25,500, 30 days to expiry.
- 25-delta put IV = **24%**, 25-delta call IV = **20%** → risk reversal = +4 vol
  pts (puts rich).
- 10-delta put IV = **30%**, 10-delta call IV = **18%** → deep OTM put very
  expensive (heavy crash hedging demand).
- ATM 30-day IV = **22%**, ATM 90-day IV = **21%** → near-term slightly
  elevated, normal term structure.
- Read: market is **defensive** (negative skew), no acute event risk priced
  into near-term ATM. Trade implications:
  - Selling 25-delta put (CSP-like on futures) collects rich premium per
    [[Volatility Risk Premium]] logic — but tail risk = the very thing being
    priced.
  - Buying 10-delta puts for crash hedge is expensive; 5–10 delta put spreads
    better capital efficiency.

## Related

- [[Implied Volatility]] · [[Volatility Risk Premium]] · [[Options Chain]] ·
  [[Risk Reversal]] · [[Vega]] · [[Black Model]]

## Sources

[^1]: `raw/iv-and-market-mechanics.md` (section 2).
[^2]: sciencedirect.com — Implied volatility topic page (skew / surface).
[^3]: en.wikipedia.org — Implied volatility (smile/smirk).
