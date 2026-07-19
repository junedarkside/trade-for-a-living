#!/usr/bin/env python3
"""
fetch_tfex.py — Pull delayed TFEX market data for S50 and USD/THB.

Sources (all free, no API key required by default):
  - yfinance     : SET50 spot index (~15-min delay) + USD/THB spot FX
  - TFEX official: S50 options chain EOD (Greeks + OI included)
  - TFEX official: S50 futures + USD/THB futures (live during market hours only)

Note: TFEX futures/spot price pages return "No information found" outside
trading hours (Mon–Fri 09:45–16:30 + 17:00–21:45 ICT). Options chain EOD
snapshot is available anytime.

Output: tools/data/tfex_snapshot.json
Usage:
  python tools/fetch_tfex.py
  python tools/fetch_tfex.py --serpapi YOUR_KEY
  python tools/fetch_tfex.py --no-save
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests
import yfinance as yf
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

OUTPUT_DIR = Path(__file__).parent / "data"
OUTPUT_FILE = OUTPUT_DIR / "tfex_snapshot.json"


# ── helpers ──────────────────────────────────────────────────────────────────

def safe_float(val):
    try:
        return float(str(val).replace(",", "").strip())
    except (ValueError, TypeError):
        return None


def fetch_yfinance_spot():
    """SET50 index + USD/THB spot via yfinance."""
    result = {}
    try:
        s50 = yf.Ticker("^SET50.BK")
        info = s50.fast_info
        result["set50_spot"] = {
            "last": safe_float(info.last_price),
            "prev_close": safe_float(info.previous_close),
            "source": "yfinance ^SET50.BK",
            "delay": "~15min",
        }
    except Exception as e:
        result["set50_spot"] = {"error": str(e)}

    try:
        fx = yf.Ticker("THBUSD=X")
        info = fx.fast_info
        thb_per_usd = 1 / info.last_price if info.last_price else None
        result["usdthb_spot"] = {
            "last": round(thb_per_usd, 4) if thb_per_usd else None,
            "source": "yfinance THBUSD=X (inverted)",
            "delay": "realtime-ish",
        }
    except Exception as e:
        result["usdthb_spot"] = {"error": str(e)}

    return result


def fetch_tfex_table(url, label):
    """Generic TFEX market-data page table parser."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        tables = soup.find_all("table")

        for tbl in tables:
            rows = tbl.find_all("tr")
            header_row = None
            data_rows = []

            for row in rows:
                cells = [td.get_text(strip=True) for td in row.find_all(["th", "td"])]
                if not cells or not any(cells):
                    continue
                if header_row is None and len(cells) >= 5:
                    # Treat as header if no float-looking values
                    if not any(safe_float(c) for c in cells):
                        header_row = cells
                        continue
                if header_row:
                    data_rows.append(dict(zip(header_row, cells)))

            if data_rows and data_rows[0].get(header_row[0] if header_row else "") != "No information found.":
                return {label: {"rows": data_rows, "source": "TFEX official", "url": url}}

        return {label: {"rows": [], "note": "No data (market closed or off-hours)", "url": url}}
    except Exception as e:
        return {label: {"error": str(e), "url": url}}


def fetch_tfex_options_chain():
    """S50 options chain EOD — call + put sides parsed separately.

    TFEX table structure (23 cols per data row):
      [0]  call_series
      [1]  call_oi
      [2]  call_vol
      [3]  call_theta
      [4]  call_vega
      [5]  call_gamma
      [6]  call_delta
      [7]  call_iv
      [8]  call_bid
      [9]  call_offer
      [10] call_last
      [11] strike_price   ← pivot
      [12] put_last
      [13] put_bid
      [14] put_offer
      [15] put_iv
      [16] put_delta
      [17] put_gamma
      [18] put_vega
      [19] put_theta
      [20] put_vol
      [21] put_oi
      [22] put_series
    """
    url = "https://www.tfex.co.th/en/products/equity/set50-index-options/market-data"
    CALL_COLS = ["series", "oi", "vol", "theta", "vega", "gamma", "delta", "iv",
                 "bid", "offer", "last"]
    PUT_COLS  = ["last", "bid", "offer", "iv", "delta", "gamma", "vega", "theta",
                 "vol", "oi", "series"]
    STRIKE_IDX = 11

    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        tables = soup.find_all("table")

        if not tables:
            return {"s50_options_chain": {"error": "No tables found", "url": url}}

        tbl = tables[0]
        rows = tbl.find_all("tr")
        chain = []
        expiry = None

        for row in rows:
            cells = [td.get_text(strip=True) for td in row.find_all(["th", "td"])]
            if not cells or not any(cells):
                continue

            # Expiry month row (single non-empty cell, not a number)
            non_empty = [c for c in cells if c]
            if len(non_empty) == 1 and not safe_float(non_empty[0]):
                expiry = non_empty[0]
                continue

            # Skip header rows
            if "Strike Price" in cells or "StrikePrice" in " ".join(cells):
                continue
            if set(cells) <= {"Call", "Put", "Strike", "StrikePrice"}:
                continue

            # Data rows: must have exactly 23 cells
            if len(cells) != 23:
                continue

            strike = safe_float(cells[STRIKE_IDX])
            if strike is None:
                continue

            call = dict(zip(CALL_COLS, cells[:STRIKE_IDX]))
            put  = dict(zip(PUT_COLS,  cells[STRIKE_IDX + 1:]))

            chain.append({
                "strike": strike,
                "expiry": expiry,
                "call": call,
                "put": put,
            })

        return {
            "s50_options_chain": {
                "rows": chain,
                "count": len(chain),
                "source": "TFEX official EOD",
                "delay": "EOD",
                "url": url,
            }
        }
    except Exception as e:
        return {"s50_options_chain": {"error": str(e), "url": url}}


def fetch_serpapi(key):
    """Optional: test SerpAPI Google Finance coverage for TFEX."""
    results = {}
    for query in ["TFEX S50 SET50 futures", "USDTHB TFEX currency futures"]:
        try:
            resp = requests.get(
                "https://serpapi.com/search",
                params={"engine": "google_finance", "q": query, "api_key": key},
                timeout=15,
            )
            resp.raise_for_status()
            results[query] = resp.json()
        except Exception as e:
            results[query] = {"error": str(e)}
    return {"serpapi": results}


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Fetch TFEX market snapshot (S50 + USD/THB)")
    parser.add_argument("--serpapi", metavar="KEY", help="SerpAPI key (optional test)")
    parser.add_argument("--no-save", action="store_true", help="Print only, don't write JSON")
    args = parser.parse_args()

    print("Fetching TFEX data...", flush=True)

    snapshot = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "products": ["S50 futures+options", "USD/THB futures"],
        "note": "TFEX futures live data only available Mon-Fri 09:45-16:30 + 17:00-21:45 ICT",
    }

    print("  [1/4] SET50 spot + USD/THB spot (yfinance)...")
    snapshot.update(fetch_yfinance_spot())

    print("  [2/4] S50 futures (TFEX official)...")
    snapshot.update(fetch_tfex_table(
        "https://www.tfex.co.th/en/products/equity/set50-index-futures/market-data",
        "s50_futures"
    ))

    print("  [3/4] S50 options chain EOD (TFEX official)...")
    snapshot.update(fetch_tfex_options_chain())

    print("  [4/4] USD/THB futures (TFEX official)...")
    snapshot.update(fetch_tfex_table(
        "https://www.tfex.co.th/en/products/currency/usd-thb-futures/market-data",
        "usdthb_futures"
    ))

    if args.serpapi:
        print("  [+] SerpAPI test...")
        snapshot.update(fetch_serpapi(args.serpapi))

    if not args.no_save:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        OUTPUT_FILE.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False))
        print(f"\nSaved → {OUTPUT_FILE}")

    # ── summary ──
    print("\n── SNAPSHOT SUMMARY ─────────────────────────────")
    s50 = snapshot.get("set50_spot", {})
    print(f"SET50 spot      : {s50.get('last', 'n/a')}  (prev {s50.get('prev_close', 'n/a')})")

    fx = snapshot.get("usdthb_spot", {})
    print(f"USD/THB spot    : {fx.get('last', 'n/a')} THB/USD")

    fut = snapshot.get("s50_futures", {})
    rows = fut.get("rows", [])
    if rows:
        for r in rows[:3]:
            print(f"S50 fut         : {r}")
    else:
        print(f"S50 fut         : {fut.get('note', fut.get('error', 'n/a'))}")

    ufut = snapshot.get("usdthb_futures", {})
    urows = ufut.get("rows", [])
    if urows:
        print(f"USD/THB fut     : {urows[0]}")
    else:
        print(f"USD/THB fut     : {ufut.get('note', ufut.get('error', 'n/a'))}")

    chain = snapshot.get("s50_options_chain", {})
    n = chain.get("count", len(chain.get("rows", [])))
    print(f"S50 options     : {n} strikes parsed (call+put)")
    if chain.get("rows"):
        sample = chain["rows"][0]
        strike = sample.get("strike", "?")
        expiry = sample.get("expiry", "?")
        call_iv = sample.get("call", {}).get("iv", "?")
        put_iv  = sample.get("put",  {}).get("iv", "?")
        print(f"  sample        : strike={strike} expiry={expiry} call_IV={call_iv} put_IV={put_iv}")
    print("─────────────────────────────────────────────────")

    return 0


if __name__ == "__main__":
    sys.exit(main())
