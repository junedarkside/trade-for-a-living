---
name: fetch-tfex
description: Fetch TFEX market data snapshot (SET50 spot, S50 options chain with Greeks, USD/THB rate) and display a structured market summary ready for trading advisory. Use when user types /fetch-tfex, "fetch market data", "get tfex data", or "refresh market snapshot".
---

# fetch-tfex — Pull TFEX market snapshot + display summary

CWD = vault root (`/Users/charuwatnaranong/Desktop/Fin/trade-for-a-living`).

`$ARGUMENTS` = optional flags passed through to the script (e.g. `--serpapi KEY`).

## SOP — run steps in order

1. **Run fetch script.**
   ```
   tools/.venv/bin/python tools/fetch_tfex.py $ARGUMENTS
   ```
   Script fetches: SET50 spot (yfinance), USD/THB spot (yfinance),
   S50 options chain EOD (TFEX official), S50 futures + USD/THB futures
   (TFEX official — only populated during market hours Mon–Fri ICT).
   Saves result to `tools/data/tfex_snapshot.json`.

2. **Read snapshot.**
   Read `tools/data/tfex_snapshot.json` (full file).

3. **Print market summary** in this format:

   ```
   ── TFEX MARKET SNAPSHOT ──────────────────────────────
   Fetched: <fetched_at UTC>  (TFEX hours: Mon-Fri 09:45-16:30 + 17:00-21:45 ICT)

   SET50 spot   : <last>  (prev close <prev_close>, chg <Δ> / <Δ%>%)
   USD/THB spot : <last> THB/USD

   S50 futures  : <last or "offline — market closed">  vol=<vol>  OI=<oi>
   USDTHB fut   : <nearest contract row or "offline">

   S50 OPTIONS CHAIN (EOD)
   ┌ ATM zone (±3 strikes from spot):
   │  Strike | Call Last | Call IV | Call OI | Put Last | Put IV | Put OI
   │  ...
   └ OI walls (top 3 strikes by total OI):
      <strike> — Call OI <n> / Put OI <n>

   Greeks at ATM (nearest strike):
     Call: Δ=<delta> Γ=<gamma> Θ=<theta> V=<vega> IV=<iv>%
     Put : Δ=<delta> Γ=<gamma> Θ=<theta> V=<vega> IV=<iv>%
   ──────────────────────────────────────────────────────
   ```

4. **Compute derived fields** from the JSON:
   - Change vs prev close: `last - prev_close`, formatted as `±N (±N%)`
   - ATM zone: filter options rows where `Strike Price` is within ±3 strikes of SET50 spot
   - OI walls: sort all rows by `Call OI + Put OI` descending, take top 3
   - Greeks: read Delta, Gamma, Theta, Vega, IV from the ATM row directly

5. **Flag data status:**
   - If futures rows empty → print `(market closed or off-hours)`
   - If options chain empty → print `(TFEX site unreachable — paste data manually)`
   - If yfinance fails → print `(yfinance error — check internet connection)`

6. **Close with advisory prompt:**
   ```
   Ready to advise. Describe your trade setup or ask a question.
   Vault context loaded: Strategy Selection Framework, Edge & Expectancy,
   Options Flow Analysis, Greeks, Execution & Slippage.
   ```

## Notes

- Venv path: `tools/.venv/bin/python` (pre-installed in vault).
- Options chain columns (from TFEX table): Series | OI (Contract) | Vol (Contract) |
  Theta | Vega | Gamma | Delta | IV | Bid | Offer | Last | Strike Price |
  Last | Bid | Offer | IV | Delta | Gamma | Vega | Theta | Vol (Contract) |
  OI (Contract) | Series
  Left side = Call, right side = Put (mirrored).
- Futures pages return empty outside ICT trading hours — normal behaviour.
- Do NOT run `olw` commands or modify wiki/ during this skill.
