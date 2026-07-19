---
title: Short Strangle
type: source
tags: [options, derivatives]
---

# Short Strangle

A **short strangle** is an advanced, **non-directional** options strategy:
sell an **OTM call** + an **OTM put** (same expiry, different strikes).
Profits if the underlying stays in a range AND/OR implied volatility falls.
You collect premium as time decay works in your favor. [^1]

## Setup

- Sell 1 OTM call at strike `K_c`
- Sell 1 OTM put at strike `K_p`
- Same underlying, same expiry
- Typically: `K_p < spot < K_c` (both options OTM at entry)

## Market view

- Expect **low realized volatility** — underlying stays between `K_p` and
  `K_c` until expiry.
- Benefit if **IV drops** after entry (options become cheaper to buy back).
  See [[Volatility Risk Premium]] for context.

## Payoff variables

- `C` = premium received for short call
- `P` = premium received for short put
- Net credit = `C + P`

## Max loss

- **Upside**: theoretically **unlimited** (short call risk).
- **Downside**: very large — up to `K_p − (C + P)` if underlying → 0.
- Position is **short premium, short gamma, short vega**. Big moves and
  vol spikes hurt.

## Max profit

- Occurs if both options expire worthless (underlying between `K_p` and
  `K_c` at expiry).
- **Max profit = total premium received = C + P.** [^1]

## Breakevens

- **Upside**: `S_BE_up = K_c + (C + P)`
- **Downside**: `S_BE_down = K_p − (C + P)`

Profit if underlying ends between the breakevens; loss otherwise.

## Greeks (short strangle)

| Greek | Sign | Meaning |
|-------|------|---------|
| Delta | ~0 initially | Becomes positive if spot falls toward short put; negative if rises toward short call |
| Gamma | **negative** | Delta moves against you as spot moves; risk accelerates |
| Theta | **positive** | You collect time decay daily |
| Vega | **negative** | Falling IV helps; rising IV causes MTM losses even if spot unchanged |

Best in **calm, range-bound markets with stable or falling vol**. Dangerous
in trending / crisis environments.

## Short strangle vs short straddle

| | Short straddle | Short strangle |
|---|---|---|
| Strikes | Both ATM (same) | OTM (different) |
| Premium | Higher | Lower |
| Breakeven range | Narrower | **Wider** |
| Gamma risk near spot | High | Lower (legs further from ATM) |
| Use | Pure short-vol, expect very tight range | Short-vol with wiggle room around spot |

## When to use

- Range-bound index/stock (support/resistance bracket).
- High IV expected to fall (event-driven fear regime normalising).
- Income overlay harvesting VRP across portfolio (see
  [[Volatility Risk Premium]]).

Strike selection:
- Technical levels (support / resistance).
- Expected move (from IV or HV range).
- Probability of expiring OTM target (often 16–25 delta shorts).

## Risk management

| Rule | Action |
|------|--------|
| **Sizing** | Worst-case loss = key input. Risk 1–2% of equity per trade. Size contracts so worst case ≠ account-threatening. |
| **Price stops** | Exit if underlying breaches key support/resistance or moves beyond X% from entry. |
| **P&L stops** | Close if loss reaches X% of max potential loss OR Y% of account equity. |
| **Time stops** | Close before known events (earnings, BOT, Fed). |
| **Adjustments** | Roll threatened side for time/credit. Convert to [[Iron Condor]] by buying OTM wings. |

> Many pros prefer starting with [[Iron Condor]] instead of naked short
> strangle — risk explicitly bounded from day one.

## Margin and assignment

- **Margin** — large, undefined risk. Brokers require margin based on the
  more demanding leg + offset. Portfolio margin (if available) reduces
  requirements for hedged books. See [[Margin Mechanics]].
- **Assignment** — early assignment possible on short calls (deep ITM
  ex-div) and short puts (sharp selloffs). For TFEX S50 options (European),
  no early assignment risk — see [[Assignment]].

## Sources

[^1]: optionseducation.org — Short Strangle.
    https://www.optionseducation.org/strategies/all-strategies/short-strangle
[^2]: optionalpha.com — Short Strangle strategy guide.
    https://optionalpha.com/strategies/short-strangle
[^3]: optionsplaybook.com — Short Strangle mechanics.
    https://www.optionsplaybook.com/option-strategies/short-strangle
[^4]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 12.
