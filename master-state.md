# Master State — Trade For A Living

> Self-contained handoff doc. Latest session block (Section 1) + open items
> (Section 2). Older sessions → `07-logs/session-history.md`. Closed items →
> `07-logs/closed-items.md`. Daily session log → `07-logs/log.md`.

## Section 1 — Session Handoff

**Updated:** 2026-07-19 (session #8)

**Achieved this session (#8) — Deep Research: Strategy Selection Framework:**
- 3-agent parallel research: vol regime classification (TastyTrade backtested thresholds, IV Rank vs IV Percentile), trend regime classification (Hurst exponent, ADX source, GEX, regime base rates), Thai SET50 specifics + position sizing by regime (Wysocki 2025 Kelly-IV hybrid).
- `wiki/Strategy Selection Framework.md`: 130 → **321 lines**. Added IV Rank/Percentile distinction, calibrated thresholds with win-rate data, Hurst exponent classifier, regime base rates, position sizing per quadrant (Kelly-IV hybrid), regime transition signals, Thai-specific TVIX/SEV/AGARCH/election cycle. 14 sources cited.
- `raw/strategy-selection-framework.md`: full rewrite from research.
- **Article status: `learning` → ready to promote to `reviewed` after one live trading cycle.**

**Achieved previous session (#7) — Phase 2 Synthesis Layer:**
- **4 new wiki articles** (closes pro-trader synthesis gap):
  - `Options Flow Analysis` — UOA, PCR, dealer positioning, TFEX OI report reading
  - `Edge & Expectancy` — expectancy formula, win%/R:R tradeoff, sample size math, SET50 iron condor example
  - `Strategy Selection Framework` — 2×2 regime matrix (vol × trend), SET50 indicators per axis
  - `Execution & Slippage` — TFEX bid-ask by product, legging risk, commission table, cost example
- **2 articles expanded:**
  - `Gamma Exposure` — full GEX pinning mechanics, dealer hedge chain, gamma flip point, worked S50 pin example
  - `Open Interest` — OI trend signals table, roll OI mechanics, roll vs new positioning distinction
- **Vault:** 93 → **97 wiki articles**.
- **Vault assessment:** Gap between intermediate and pro is now closed for knowledge base. Remaining gap is execution (live trading experience) not knowledge.

**Resume point:**
1. **Live trading** — vault is knowledge-complete for pro level. Real edge comes from execution experience, journal data, and refining strategy selection via actual P&L.
2. **Status promotions** — 93 articles still at `learning`; promote as you trade and master each concept.
3. **wrapup skill verify** — confirm `.claude/skills/wrapup/skill.md` matches CLAUDE.md L82-88 SOP.
4. **Future additions (on demand):** Portfolio Greeks Management article; Oil Futures if TFEX relists; advanced skew trading playbook.

## Section 2 — Loose Ends

| # | Item | Status |
|---|------|--------|
| 1 | wrapup skill verify — confirm `.claude/skills/wrapup/skill.md` matches CLAUDE.md L82-88 | open |
| 2 | Oil Futures article — defer until TFEX Brent product is confirmed active | open |
| 3 | 93 articles still at `status: learning` — promote progressively as knowledge reviewed in trading | ongoing |
| 4 | Portfolio Greeks Management article — on demand when running concurrent multi-strategy positions | future |

## See also

- `[[vault-protocol]]` — *(not yet created; add when API/auth surfaces emerge)*
- `[[vault-guardrails]]` — *(not yet created; add when risk/DB patterns emerge)*
- [[session-history]] — older session blocks
- [[closed-items]] — resolved loose ends
- `vault-wrapup.sh` — git state collector for wrap-up
- `wiki/log.md` — per-note ingest audit trail (Obsidian layer)
- `/Users/charuwatnaranong/.claude/plans/check-vault-scan-knowkedge-sprightly-wolf.md` — pro-trader gap roadmap (5 tiers)
