#!/usr/bin/env python3
"""Call the TradingView Data API with automatic key and backend management.

Recommended backend (Console):
  https://api.tradingviewapi.com
  Authorization: Bearer <KEY>

Alternate backend (RapidAPI):
  https://tradingview-data1.p.rapidapi.com
  x-rapidapi-host + x-rapidapi-key

Key resolution order:
  1. --key CLI argument
  2. TRADINGVIEW_API_KEY environment variable
  3. RAPIDAPI_KEY environment variable (legacy RapidAPI)
  4. .api-key file in the skill root directory
  5. .rapidapi-key file in the skill root directory (legacy)

Save the key for future calls (only after explicit user consent):
    python3 tv_api.py --save-key 'YOUR_KEY'

Usage examples:
  python3 tv_api.py GET '/api/quote/NASDAQ:AAPL'
  python3 tv_api.py GET '/api/price/BINANCE:BTCUSDT?timeframe=60&range=20'
  python3 tv_api.py GET '/api/metadata/markets'
  python3 tv_api.py POST '/api/screener/scan' --body '{"market":"america","range":[0,20]}'
  python3 tv_api.py POST '/api/quote/batch' --body '{"symbols":["NASDAQ:AAPL","NASDAQ:MSFT"]}'
  python3 tv_api.py --rapid GET '/api/quote/NASDAQ:AAPL'
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

CONSOLE_HOST = "api.tradingviewapi.com"
RAPIDAPI_HOST = "tradingview-data1.p.rapidapi.com"
CONSOLE_BASE = f"https://{CONSOLE_HOST}"
RAPIDAPI_BASE = f"https://{RAPIDAPI_HOST}"
SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY_FILE = os.path.join(SKILL_ROOT, ".api-key")
LEGACY_KEY_FILE = os.path.join(SKILL_ROOT, ".rapidapi-key")


def load_key(cli_key):
    """Return (key, source) or (None, None). source is used to infer backend."""
    if cli_key and cli_key.strip():
        return cli_key.strip(), "cli"
    env_key = os.environ.get("TRADINGVIEW_API_KEY", "").strip()
    if env_key:
        return env_key, "tradingview"
    rapid_key = os.environ.get("RAPIDAPI_KEY", "").strip()
    if rapid_key:
        return rapid_key, "rapidapi"
    if os.path.isfile(KEY_FILE):
        with open(KEY_FILE) as f:
            key = f.read().strip()
            if key:
                return key, "file"
    if os.path.isfile(LEGACY_KEY_FILE):
        with open(LEGACY_KEY_FILE) as f:
            key = f.read().strip()
            if key:
                return key, "rapidapi-file"
    return None, None


def save_key(key):
    key = key.strip()
    if not key:
        print("ERROR: refusing to save an empty key.", file=sys.stderr)
        sys.exit(2)
    with open(KEY_FILE, "w") as f:
        f.write(key + "\n")
    os.chmod(KEY_FILE, 0o600)
    print(f"Key saved to {KEY_FILE}")


def resolve_backend(explicit, key_source):
    env_backend = os.environ.get("TRADINGVIEW_API_BACKEND", "").strip().lower()
    env_base = (
        os.environ.get("TRADINGVIEW_API_BASE", "").strip()
        or os.environ.get("TV_API_BASE", "").strip()
    )
    if explicit:
        backend = explicit
    elif env_backend in ("console", "rapid", "rapidapi"):
        backend = "rapid" if env_backend in ("rapid", "rapidapi") else "console"
    elif env_base:
        backend = "rapid" if "rapidapi.com" in env_base.lower() else "console"
    elif key_source in ("rapidapi", "rapidapi-file"):
        backend = "rapid"
    else:
        backend = "console"

    if env_base:
        base_url = env_base.rstrip("/")
        if backend == "rapid" and "rapidapi.com" not in base_url.lower():
            base_url = RAPIDAPI_BASE
        elif backend == "console" and "rapidapi.com" in base_url.lower():
            base_url = CONSOLE_BASE
        return backend, base_url
    return backend, RAPIDAPI_BASE if backend == "rapid" else CONSOLE_BASE


def apply_auth(req, backend, key):
    if backend == "rapid":
        req.add_header("x-rapidapi-host", RAPIDAPI_HOST)
        req.add_header("x-rapidapi-key", key)
        return
    req.add_header("Authorization", f"Bearer {key}")


def main():
    parser = argparse.ArgumentParser(description="TradingView Data API client")
    parser.add_argument("method", nargs="?", choices=["GET", "POST"], help="HTTP method")
    parser.add_argument("path", nargs="?", help="API path, e.g. /api/quote/NASDAQ:AAPL")
    parser.add_argument("--body", help="JSON body for POST requests")
    parser.add_argument("--key", help="API key (overrides env/file)")
    parser.add_argument("--save-key", help="Save the key to the skill root and exit")
    parser.add_argument(
        "--backend",
        choices=["console", "rapid"],
        help="API backend (default: console, or rapid when only a RapidAPI key is present)",
    )
    parser.add_argument(
        "--rapid",
        action="store_true",
        help="Use the RapidAPI host and headers (alias for --backend rapid)",
    )
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()

    if args.save_key:
        save_key(args.save_key)
        return

    if not args.method or not args.path:
        parser.error("method and path are required (unless using --save-key)")

    key, key_source = load_key(args.key)
    if not key:
        print(
            "ERROR: no API key found.\n"
            "Provide it via --key, TRADINGVIEW_API_KEY, RAPIDAPI_KEY, or save it once with:\n"
            "  python3 tv_api.py --save-key 'YOUR_KEY'",
            file=sys.stderr,
        )
        sys.exit(2)

    explicit = "rapid" if args.rapid else args.backend
    backend, base_url = resolve_backend(explicit, key_source)

    url = base_url + (args.path if args.path.startswith("/") else "/" + args.path)
    data = args.body.encode() if args.body else None
    req = urllib.request.Request(url, data=data, method=args.method)
    apply_auth(req, backend, key)
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
