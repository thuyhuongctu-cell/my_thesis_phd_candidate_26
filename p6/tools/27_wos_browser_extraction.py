#!/usr/bin/env python3
"""
27_wos_browser_extraction.py — WoS browser automation for P6 meta-analysis.

Navigates to Web of Science, logs in with institutional credentials,
runs the P6 advanced search query, and exports results in batches of 500.

SECURITY: Credentials are NEVER hardcoded. They MUST be passed as env vars.

Usage:
    export WOS_EMAIL="your-email@institution.edu"
    export WOS_PASSWORD="your-password"
    python3 27_wos_browser_extraction.py

    # Dry run (show steps only, no browser interaction):
    python3 27_wos_browser_extraction.py --dry-run

    # Use remote browser (headless server):
    python3 27_wos_browser_extraction.py --remote

    # Skip login (already logged in):
    python3 27_wos_browser_extraction.py --skip-login

Options:
    --dry-run       Print steps without executing browser commands
    --remote        Start remote Browser Use cloud session
    --skip-login    Skip login step (assume already authenticated in browser)
    --batch-size N  Records per export batch (default: 500, WoS max: 500)
    --output DIR    Output directory (default: results/wos_export_YYYYMMDD/)
    --screenshots   Save screenshots at each step (default: enabled)
"""

import argparse
import os
import subprocess
import sys
import textwrap
import time
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Configuration — from environment variables ONLY
# ---------------------------------------------------------------------------

WOS_EMAIL    = os.environ.get("WOS_EMAIL", "")
WOS_PASSWORD = os.environ.get("WOS_PASSWORD", "")

WOS_URL      = "https://www.webofscience.com/wos/woscc/advanced-search"
BATCH_SIZE   = 500       # WoS maximum records per export
STEP_WAIT    = 2.0       # seconds between steps

OUTPUT_DIR   = Path(__file__).parent / "results" / f"wos_export_{datetime.today().strftime('%Y%m%d')}"
SCREENSHOT_DIR = OUTPUT_DIR / "screenshots"

# ---------------------------------------------------------------------------
# P6 Search Query — WoS Advanced Search (TS= syntax)
# From: p6/p6_wos_search_guide.md v2 (global search, no geographic filter)
# ---------------------------------------------------------------------------

P6_QUERY = (
    'TS=(internationaliz* OR internationalis* OR multinationality '
    'OR "degree of internationalization" OR "degree of internationalisation" '
    'OR "international diversification" OR "geographic diversification" '
    'OR "foreign sales" OR "foreign sales to total sales" OR FSTS '
    'OR "foreign assets" OR "foreign assets to total assets" OR FATA '
    'OR "export intensity" OR "export scope" OR "export ratio" '
    'OR "foreign market entry" OR "foreign subsidiaries") '
    'AND '
    'TS=("firm performance" OR "enterprise performance" OR "corporate performance" '
    'OR "financial performance" OR "business performance" '
    'OR "labor productivity" OR "labour productivity" OR profitability '
    'OR "Tobin\'s q" OR "return on assets" OR ROA OR "return on equity" '
    'OR "return on sales" OR "total factor productivity" OR "firm efficiency") '
    'AND '
    'TS=(correlation OR regression OR coefficient OR "effect size" OR "r =")'
)

# WoS filters applied after search
WOS_FILTERS = {
    "timespan": "1977-2026",
    "document_type": "Article",
    "language": "English",
    "database": "WOS",  # Web of Science Core Collection
}


# ---------------------------------------------------------------------------
# Browser-harness runner
# ---------------------------------------------------------------------------

def bh(code: str, timeout: int = 180, dry_run: bool = False) -> str:
    """Execute a browser-harness Python snippet. Returns stdout."""
    if dry_run:
        print(f"[DRY-RUN] browser-harness:\n{textwrap.indent(code.strip(), '  ')}\n")
        return ""
    result = subprocess.run(
        ["browser-harness"],
        input=code,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if result.returncode != 0 and result.stderr.strip():
        print(f"  [warn] browser-harness stderr: {result.stderr.strip()[:200]}", file=sys.stderr)
    return result.stdout.strip()


def save_screenshot(name: str, dry_run: bool = False) -> None:
    """Take a screenshot and save to SCREENSHOT_DIR."""
    if dry_run:
        print(f"[DRY-RUN] screenshot: {name}")
        return
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    code = f"""
import base64, os
data = capture_screenshot()
# data may be base64 string or already bytes
path = "{SCREENSHOT_DIR}/{name}.png"
if isinstance(data, str) and data.startswith("data:image"):
    img_data = base64.b64decode(data.split(",", 1)[1])
elif isinstance(data, str):
    img_data = base64.b64decode(data)
else:
    img_data = data
with open(path, "wb") as f:
    f.write(img_data)
print("saved:", path)
"""
    out = bh(code, dry_run=dry_run)
    if out:
        print(f"  screenshot → {name}.png")


# ---------------------------------------------------------------------------
# Step functions
# ---------------------------------------------------------------------------

def step_open_wos(dry_run: bool) -> None:
    print("\n[Step 1] Opening Web of Science Advanced Search...")
    bh(f"""
new_tab("{WOS_URL}")
wait_for_load()
print(page_info())
""", dry_run=dry_run)
    save_screenshot("01_wos_home", dry_run)
    time.sleep(STEP_WAIT)


def step_login_institutional(email: str, password: str, dry_run: bool) -> None:
    """
    WoS institutional login via federated identity (Shibboleth/SAML).
    CTU students: email = huongp1323001@gstudent.ctu.edu.vn
    Flow: Sign In → Federated Organizations → enter institutional email →
          redirected to CTU IdP → enter password
    """
    print("\n[Step 2] Attempting institutional login...")
    save_screenshot("02a_before_login", dry_run)

    # Click "Sign In" button (top navigation)
    bh("""
info = page_info()
print(info)
# Find and click Sign In link
result = js("document.querySelector('[data-ta=\\'sign-in\\']')?.click() || " +
            "document.querySelector('a[href*=\\"sign-in\\"]')?.click() || " +
            "document.querySelector('button[class*=\\"signin\\"]')?.click()")
print("clicked signin:", result)
import time; time.sleep(2)
""", dry_run=dry_run)
    save_screenshot("02b_signin_clicked", dry_run)

    # Look for "Federated Organizations" or "Institutional Login" option
    bh("""
import time
# Try clicking "Federated Organizations" or similar link
options = js(\"""
    Array.from(document.querySelectorAll('a, button, span')).filter(el =>
        el.textContent.includes('Institutional') ||
        el.textContent.includes('Federated') ||
        el.textContent.includes('Organization')
    ).map(el => ({text: el.textContent.trim(), tag: el.tagName}))
\""")
print("federated options:", options)
time.sleep(1)
""", dry_run=dry_run)

    # Enter institutional email to trigger SSO redirect
    bh(f"""
import time
# Try the "Sign in via email" field
email_input = js("document.querySelector('input[type=\\"email\\"], input[name=\\"email\\"], input[placeholder*=\\"email\\"]')")
print("email input found:", bool(email_input))
if email_input:
    js("document.querySelector('input[type=\\"email\\"], input[name=\\"email\\"]').value = {repr(email)}")
    js("document.querySelector('input[type=\\"email\\"], input[name=\\"email\\"]').dispatchEvent(new Event('input', {{bubbles: true}}))")
    time.sleep(0.5)
    # Press Enter or click Continue
    js("document.querySelector('button[type=\\"submit\\"], button[class*=\\"continue\\"]')?.click()")
    time.sleep(3)
print(page_info())
""", dry_run=dry_run)
    save_screenshot("02c_email_entered", dry_run)

    # Handle CTU identity provider page (enter password)
    bh(f"""
import time
time.sleep(2)
info = page_info()
print("After email submit:", info.get('url', ''))
# On CTU IdP page — find password field
pwd_input = js("document.querySelector('input[type=\\"password\\"]')")
print("password field found:", bool(pwd_input))
if pwd_input:
    js("document.querySelector('input[type=\\"password\\"]').value = {repr(password)}")
    js("document.querySelector('input[type=\\"password\\"]').dispatchEvent(new Event('input', {{bubbles: true}}))")
    time.sleep(0.5)
    js("document.querySelector('input[type=\\"submit\\"], button[type=\\"submit\\"]')?.click()")
    time.sleep(5)
print(page_info())
""", dry_run=dry_run)
    save_screenshot("02d_after_login", dry_run)
    print("  Login attempt completed. Check screenshot for result.")


def step_verify_login(dry_run: bool) -> bool:
    """Check if we're logged in by looking for user account indicators."""
    print("\n[Step 3] Verifying login status...")
    out = bh("""
info = page_info()
url = info.get('url', '')
print("current_url:", url)
# Check for sign-out or user account elements
logged_in = js(\"""
    !!document.querySelector('[data-ta="sign-out"], [aria-label*="account"], .username, #username') ||
    document.documentElement.innerHTML.includes('Sign Out')
\""")
print("logged_in_indicator:", logged_in)
""", dry_run=dry_run)
    save_screenshot("03_verify_login", dry_run)
    if not dry_run:
        return "logged_in_indicator: True" in out or "signed in" in out.lower()
    return True


def step_run_search(dry_run: bool) -> str:
    """Navigate to Advanced Search and run the P6 query."""
    print("\n[Step 4] Running P6 Advanced Search...")

    # Navigate to Advanced Search
    bh(f"""
import time
goto_url("{WOS_URL}")
wait_for_load()
time.sleep(2)
print(page_info())
""", dry_run=dry_run)
    save_screenshot("04a_advanced_search_page", dry_run)

    # Clear existing query and enter P6 query
    query_escaped = P6_QUERY.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    bh(f"""
import time
# Find and clear the query textarea
textarea = js("document.querySelector('textarea[class*=\\"querybox\\"], textarea[id*=\\"querybox\\"], #advancedSearchInputArea')")
print("textarea found:", bool(textarea))
js(\"""
    const ta = document.querySelector('textarea[class*=\\"querybox\\"], textarea[id*=\\"querybox\\"], #advancedSearchInputArea');
    if (ta) {{
        ta.value = '';
        ta.dispatchEvent(new Event('input', {{bubbles: true}}));
    }}
\""")
time.sleep(0.3)
js(f\"""
    const ta = document.querySelector('textarea[class*=\\"querybox\\"], textarea[id*=\\"querybox\\"], #advancedSearchInputArea');
    if (ta) {{
        ta.value = "{query_escaped}";
        ta.dispatchEvent(new Event('input', {{bubbles: true}}));
        ta.dispatchEvent(new Event('change', {{bubbles: true}}));
    }}
\""")
time.sleep(1)
print("Query entered")
""", dry_run=dry_run)
    save_screenshot("04b_query_entered", dry_run)

    # Apply timespan filter and run search
    out = bh("""
import time
# Click Search button
js("document.querySelector('button[aria-label*=\\"Search\\"], button[data-ta=\\"run-search\\"], button[class*=\\"search-button\\"]')?.click()")
time.sleep(5)
wait_for_load()
info = page_info()
print("search_url:", info.get('url', ''))
print(info.get('title', ''))
# Try to get result count
count = js(\"""
    const el = document.querySelector('[data-ta="results-count"], .search-results-count, [class*="results-count"]');
    el ? el.textContent.trim() : 'count not found'
\""")
print("result_count:", count)
""", dry_run=dry_run)
    save_screenshot("04c_search_results", dry_run)

    if not dry_run:
        for line in out.splitlines():
            if "result_count:" in line:
                print(f"  Search returned: {line.replace('result_count:', '').strip()}")
    return out


def step_apply_filters(dry_run: bool) -> None:
    """Apply Article/English/1977-2026 filters in the results page."""
    print("\n[Step 5] Applying filters (Article, English, 1977-2026)...")
    bh("""
import time
# Look for filter/refine options
filters = js(\"""
    Array.from(document.querySelectorAll('[data-ta*="filter"], .refine-sidebar label, .filter-option'))
         .map(el => el.textContent.trim())
         .filter(t => t.length > 0 && t.length < 50)
\""")
print("available filters:", filters[:10])
""", dry_run=dry_run)
    save_screenshot("05_filters", dry_run)
    # Note: Filters may need manual interaction — WoS filter UI varies by version
    print("  NOTE: Verify Article/English/1977-2026 filters via screenshot.")


def step_export_batch(batch_num: int, start: int, end: int, output_path: Path,
                      dry_run: bool) -> bool:
    """Export one batch of records from WoS."""
    print(f"\n[Step 6.{batch_num}] Exporting records {start}–{end}...")
    filename = output_path / f"wos_export_batch{batch_num:02d}_{start}-{end}.xls"

    bh(f"""
import time
# Click Export button
js("document.querySelector('[data-ta=\\"export\\"], button[aria-label*=\\"Export\\"], [class*=\\"export-button\\"]')?.click()")
time.sleep(2)
print(page_info())
""", dry_run=dry_run)
    save_screenshot(f"06a_export_menu_batch{batch_num}", dry_run)

    # Select Excel export format
    bh("""
import time
# Look for Excel or Tab-delimited option
js(\"""
    const opts = Array.from(document.querySelectorAll('[role=\\"option\\"], li, button'));
    const excel = opts.find(el => el.textContent.includes('Excel') || el.textContent.includes('Tab-delimited'));
    if (excel) excel.click();
\""")
time.sleep(1)
""", dry_run=dry_run)

    # Set record range
    bh(f"""
import time
# Enter custom range
range_input = js("document.querySelector('input[placeholder*=\\"from\\"], input[name*=\\"from\\"], #exportFrom')")
if range_input:
    js("document.querySelector('input[placeholder*=\\"from\\"], input[name*=\\"from\\"], #exportFrom').value = '{start}'")
    js("document.querySelector('input[placeholder*=\\"to\\"], input[name*=\\"to\\"], #exportTo').value = '{end}'")
    time.sleep(0.3)
# Select "Full Record" content
js(\"""
    const opts = Array.from(document.querySelectorAll('input[type=\\"radio\\"], option'));
    const full = opts.find(el => (el.value || el.textContent).includes('Full'));
    if (full) full.click();
\""")
time.sleep(0.5)
# Click Export/OK
js("document.querySelector('button[data-ta=\\"export-ok\\"], button[aria-label*=\\"Export\\"], button[class*=\\"ok\\"]')?.click()")
time.sleep(10)
print("Export submitted for records {start}-{end}")
""", dry_run=dry_run)
    save_screenshot(f"06b_export_dialog_batch{batch_num}", dry_run)

    print(f"  Batch {batch_num} export submitted. File will download to browser's download folder.")
    print(f"  Move exported file to: {filename}")
    return True


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(description="WoS browser extraction for P6 meta-analysis")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show steps without executing browser commands")
    parser.add_argument("--remote", action="store_true",
                        help="Start a remote Browser Use cloud session")
    parser.add_argument("--skip-login", action="store_true",
                        help="Skip login (assume already authenticated)")
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE,
                        help=f"Records per export batch (default: {BATCH_SIZE})")
    parser.add_argument("--max-records", type=int, default=10000,
                        help="Maximum records to export (default: 10000)")
    parser.add_argument("--output", type=str, default=str(OUTPUT_DIR),
                        help=f"Output directory (default: {OUTPUT_DIR})")
    parser.add_argument("--no-screenshots", action="store_true",
                        help="Disable screenshots")
    return parser.parse_args()


def check_credentials(args) -> None:
    if args.dry_run:
        return
    if not args.skip_login:
        if not WOS_EMAIL:
            sys.exit(
                "ERROR: WOS_EMAIL not set.\n"
                "  export WOS_EMAIL='your-email@ctu.edu.vn'"
            )
        if not WOS_PASSWORD:
            sys.exit(
                "ERROR: WOS_PASSWORD not set.\n"
                "  export WOS_PASSWORD='your-password'"
            )


def start_remote_browser(dry_run: bool) -> None:
    """Start a Browser Use remote cloud session for headless operation."""
    print("[Remote] Starting Browser Use cloud session...")
    bh("""
start_remote_daemon("wos-extraction")
print("Remote browser started. Check the liveUrl above to monitor.")
""", dry_run=dry_run)
    time.sleep(5)


def main():
    args = parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("P6 WoS Browser Extraction")
    print(f"  Email:      {WOS_EMAIL or '(not set)'}")
    print(f"  Output:     {output_dir}")
    print(f"  Batch size: {args.batch_size}")
    print(f"  Dry run:    {args.dry_run}")
    print(f"  Remote:     {args.remote}")
    print(f"  Skip login: {args.skip_login}")
    print("=" * 60)

    check_credentials(args)

    dry = args.dry_run

    # Start remote session if needed (headless server)
    if args.remote:
        start_remote_browser(dry)

    # Step 1: Open WoS
    step_open_wos(dry)

    # Step 2: Login
    if not args.skip_login:
        step_login_institutional(WOS_EMAIL, WOS_PASSWORD, dry)

        # Step 3: Verify login
        logged_in = step_verify_login(dry)
        if not logged_in and not dry:
            print("\nWARNING: Could not confirm login automatically.")
            print("  Check screenshot 03_verify_login.png")
            print("  If login failed, try: python3 27_wos_browser_extraction.py --skip-login")
            answer = input("  Continue anyway? [y/N] ").strip().lower()
            if answer != "y":
                sys.exit("Aborted. Please login manually then re-run with --skip-login")
    else:
        print("\n[Step 2-3] Skipping login (--skip-login set)")

    # Step 4: Run search
    step_run_search(dry)
    time.sleep(STEP_WAIT)

    # Step 5: Apply filters
    step_apply_filters(dry)
    time.sleep(STEP_WAIT)

    # Step 6: Get total record count
    if not dry:
        out = bh("""
count_el = js(\"""
    document.querySelector('[data-ta=\\"results-count\\"], .search-results-count, [class*=\\"results-count\\"]')
\""")
count_text = js(\"""
    const el = document.querySelector('[data-ta=\\"results-count\\"], .search-results-count');
    el ? el.textContent.trim() : ''
\""")
print("total:", count_text)
""")
        total = 0
        for line in out.splitlines():
            if "total:" in line:
                import re
                nums = re.findall(r'\d[\d,]*', line)
                if nums:
                    total = int(nums[0].replace(",", ""))
                    break
        if total == 0:
            total = args.max_records
            print(f"  Could not read result count. Assuming max: {total}")
        else:
            print(f"\n  Total results found: {total:,}")
    else:
        total = args.max_records
        print(f"\n[DRY-RUN] Assuming {total} total results")

    # Step 6: Export in batches
    total_export = min(total, args.max_records)
    batch_size = args.batch_size
    n_batches = (total_export + batch_size - 1) // batch_size

    print(f"\n[Step 6] Exporting {total_export:,} records in {n_batches} batch(es) of {batch_size}...")

    for i in range(n_batches):
        start = i * batch_size + 1
        end = min((i + 1) * batch_size, total_export)
        success = step_export_batch(i + 1, start, end, output_dir, dry)
        if success and not dry:
            print(f"  Waiting 10s before next batch...")
            time.sleep(10)

    print("\n" + "=" * 60)
    print("Export complete!")
    print(f"  Batch files: {output_dir}/wos_export_batch*.xls")
    print(f"  Screenshots: {output_dir}/screenshots/")
    print("")
    print("Next steps:")
    print("  1. Move downloaded .xls files to this output directory")
    print(f"  2. Run: python3 01_parse_wos_export.py --input {output_dir}")
    print("  3. Run: python3 03_deduplicate_merge.py to merge with existing data")
    print("=" * 60)


if __name__ == "__main__":
    main()
