#!/usr/bin/env python3
"""Call the TradingView Data API (RapidAPI) with automatic key management.

Key resolution order:
  1. --key CLI argument
  2. RAPIDAPI_KEY environment variable
  3. .rapidapi-key file in the skill root directory (one line, the key)

Save the key for future calls (only after explicit user consent):
  python3 tv_api.py --save-key 'YOUR_KEY'

Usage examples:
  python3 tv_api.py GET '/api/quote/NASDAQ:AAPL'
  python3 tv_api.py GET '/api/price/BINANCE:BTCUSDT?timeframe=60&range=20'
  python3 tv_api.py GET '/api/metadata/markets'
  python3 tv_api.py POST '/api/screener/scan' --body '{"market":"america","range":[0,20]}'
  python3 tv_api.py POST '/api/quote/batch' --body '{"symbols":["NASDAQ:AAPL","NASDAQ:MSFT"]}'
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

HOST = "tradingview-data1.p.rapidapi.com"
BASE_URL = f"https://{HOST}"
SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY_FILE = os.path.join(SKILL_ROOT, ".rapidapi-key")


def load_key(cli_key):
    if cli_key and cli_key.strip():
        return cli_key.strip()
    env_key = os.environ.get("RAPIDAPI_KEY", "").strip()
    if env_key:
        return env_key
    if os.path.isfile(KEY_FILE):
        with open(KEY_FILE) as f:
            key = f.read().strip()
            if key:
                return key
    return None


def save_key(key):
    key = key.strip()
    if not key:
        print("ERROR: refusing to save an empty key.", file=sys.stderr)
        sys.exit(2)
    with open(KEY_FILE, "w") as f:
        f.write(key + "\n")
    os.chmod(KEY_FILE, 0o600)
    print(f"Key saved to {KEY_FILE}")


def main():
    parser = argparse.ArgumentParser(description="TradingView Data API client")
    parser.add_argument("method", nargs="?", choices=["GET", "POST"], help="HTTP method")
    parser.add_argument("path", nargs="?", help="API path, e.g. /api/quote/NASDAQ:AAPL")
    parser.add_argument("--body", help="JSON body for POST requests")
    parser.add_argument("--key", help="x-rapidapi-key (overrides env/file)")
    parser.add_argument("--save-key", help="Save the key to the skill root and exit")
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()

    if args.save_key:
        save_key(args.save_key)
        return

    if not args.method or not args.path:
        parser.error("method and path are required (unless using --save-key)")

    key = load_key(args.key)
    if not key:
        print(
            "ERROR: no RapidAPI key found.\n"
            "Provide it via --key, RAPIDAPI_KEY env var, or save it once with:\n"
            "  python3 tv_api.py --save-key 'YOUR_KEY'",
            file=sys.stderr,
        )
        sys.exit(2)

    url = BASE_URL + (args.path if args.path.startswith("/") else "/" + args.path)
    data = args.body.encode() if args.body else None
    req = urllib.request.Request(url, data=data, method=args.method)
    req.add_header("x-rapidapi-host", HOST)
    req.add_header("x-rapidapi-key", key)
    if data:
        req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req, timeout=args.timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"HTTP {e.code}", file=sys.stderr)
        print(body)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Request failed: {e.reason}", file=sys.stderr)
        sys.exit(1)

    try:
        print(json.dumps(json.loads(body), ensure_ascii=False, indent=2))
    except ValueError:
        print(body)


if __name__ == "__main__":
    main()
