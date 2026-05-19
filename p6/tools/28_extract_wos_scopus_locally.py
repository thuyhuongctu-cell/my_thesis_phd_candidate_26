#!/usr/bin/env python3
"""
28_extract_wos_scopus_locally.py — Run this on YOUR LOCAL MACHINE (not the server).

Automates WoS Advanced Search + Scopus search using Selenium.
Downloads exports to the current directory, then upload them to the server.

Requirements (install once on your local machine):
    pip install selenium

Chrome must be installed. ChromeDriver is auto-managed by selenium >= 4.6.

Usage:
    # On YOUR local machine (Windows/Mac/Linux with internet):
    python3 28_extract_wos_scopus_locally.py --wos
    python3 28_extract_wos_scopus_locally.py --scopus
    python3 28_extract_wos_scopus_locally.py --wos --scopus
    python3 28_extract_wos_scopus_locally.py --osf          # just verify OSF registration
"""

import argparse
import os
import sys
import time
from pathlib import Path
from datetime import datetime

# Check selenium
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
except ImportError:
    sys.exit("Install selenium first:\n  pip install selenium\nThen re-run this script.")


# ---------------------------------------------------------------------------
# Credentials — read from env vars or prompt once at runtime
# ---------------------------------------------------------------------------

def get_credentials():
    wos_email = os.environ.get("WOS_EMAIL") or input("WoS email: ").strip()
    wos_pass  = os.environ.get("WOS_PASSWORD") or input("WoS password: ").strip()
    scopus_email = os.environ.get("SCOPUS_EMAIL") or input("Scopus email (Gmail): ").strip()
    scopus_pass  = os.environ.get("SCOPUS_PASSWORD") or input("Scopus password: ").strip()
    return wos_email, wos_pass, scopus_email, scopus_pass


# ---------------------------------------------------------------------------
# P6 Search Queries
# ---------------------------------------------------------------------------

WOS_QUERY = (
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

SCOPUS_QUERY = (
    'TITLE-ABS-KEY(internationaliz* OR internationalis* '
    'OR multinationality OR "degree of internationalization" '
    'OR "degree of internationalisation" '
    'OR "international diversification" OR "geographic diversification" '
    'OR "foreign sales" OR "foreign sales to total sales" OR FSTS '
    'OR "foreign assets" OR "foreign assets to total assets" OR FATA '
    'OR "export intensity" OR "export scope" OR "export ratio" '
    'OR "foreign market entry" OR "foreign subsidiaries") '
    'AND '
    'TITLE-ABS-KEY("firm performance" OR "enterprise performance" '
    'OR "corporate performance" OR "financial performance" OR "business performance" '
    'OR "labor productivity" OR "labour productivity" OR profitability '
    'OR "return on assets" OR Tobin OR "return on equity" '
    'OR "return on sales" OR "total factor productivity" OR "firm efficiency") '
    'AND '
    'TITLE-ABS-KEY(correlation OR regression OR coefficient OR "effect size") '
    'AND PUBYEAR > 1976 AND PUBYEAR < 2027 '
    'AND DOCTYPE(ar) AND LANGUAGE(english)'
)

DOWNLOAD_DIR = Path.cwd() / f"wos_scopus_export_{datetime.today().strftime('%Y%m%d')}"


# ---------------------------------------------------------------------------
# Browser setup
# ---------------------------------------------------------------------------

def make_driver(download_dir: Path) -> webdriver.Chrome:
    download_dir.mkdir(parents=True, exist_ok=True)
    opts = Options()
    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("prefs", {
        "download.default_directory": str(download_dir),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    })
    # headless=False so you can see what's happening and intervene if needed
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(10)
    return driver


def wait_for(driver, by, selector, timeout=20):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, selector))
    )


def wait_click(driver, by, selector, timeout=20):
    el = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, selector))
    )
    el.click()
    return el


def slow_type(el, text):
    el.clear()
    for ch in text:
        el.send_keys(ch)
        time.sleep(0.02)


# ---------------------------------------------------------------------------
# WoS workflow
# ---------------------------------------------------------------------------

def wos_login(driver, email: str, password: str):
    print("\n[WoS] Navigating to Web of Science...")
    driver.get("https://www.webofscience.com/wos/woscc/advanced-search")
    time.sleep(3)

    # Handle cookie banner
    try:
        accept = driver.find_element(By.XPATH,
            "//button[contains(text(),'Accept') or contains(text(),'accept')]")
        accept.click()
        time.sleep(1)
    except NoSuchElementException:
        pass

    # Click Sign In
    print("[WoS] Clicking Sign In...")
    try:
        signin_btn = wait_click(driver, By.XPATH,
            "//a[contains(@href,'sign-in')] | //button[contains(text(),'Sign in')] | "
            "//button[contains(@class,'sign-in')] | //*[@data-ta='sign-in']",
            timeout=15)
        time.sleep(2)
    except TimeoutException:
        print("[WoS] Sign In button not found — may already be on login page")

    # Try email field for federated login
    try:
        email_input = wait_for(driver, By.XPATH,
            "//input[@type='email' or @name='email' or @placeholder[contains(.,'email')]]",
            timeout=10)
        email_input.clear()
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)
        time.sleep(3)
        print("[WoS] Email entered, waiting for password/IdP redirect...")
    except TimeoutException:
        print("[WoS] No email field found. Check browser window.")

    # Password field (may be on redirected institutional IdP page)
    try:
        pwd_input = wait_for(driver, By.XPATH,
            "//input[@type='password']", timeout=15)
        pwd_input.clear()
        pwd_input.send_keys(password)
        pwd_input.send_keys(Keys.RETURN)
        time.sleep(5)
        print("[WoS] Password submitted")
    except TimeoutException:
        print("[WoS] No password field found. May need manual login.")
        print("  → Please log in manually in the browser, then press Enter here...")
        input()


def wos_search_and_export(driver, download_dir: Path):
    print("\n[WoS] Navigating to Advanced Search...")
    driver.get("https://www.webofscience.com/wos/woscc/advanced-search")
    time.sleep(4)

    # Find query textarea
    query_box = None
    for sel in ["#queryBox", "textarea.queryBox", "textarea[name='query']",
                "textarea", "#advancedSearchInputArea"]:
        try:
            query_box = driver.find_element(By.CSS_SELECTOR, sel)
            break
        except NoSuchElementException:
            continue

    if not query_box:
        print("[WoS] Query box not found. Please paste query manually.")
        print("QUERY:\n", WOS_QUERY[:200], "...")
        input("Press Enter when query is pasted and searched...")
    else:
        print("[WoS] Entering P6 query...")
        query_box.click()
        query_box.clear()
        # Use JS to set value (more reliable for long strings)
        driver.execute_script("arguments[0].value = arguments[1]", query_box, WOS_QUERY)
        driver.execute_script(
            "arguments[0].dispatchEvent(new Event('input', {bubbles:true}))", query_box)
        time.sleep(1)

        # Click Search
        for sel in ["button[type='submit']", "button.search-button",
                    "*[data-ta='run-search']", "button#search"]:
            try:
                btn = driver.find_element(By.CSS_SELECTOR, sel)
                btn.click()
                break
            except NoSuchElementException:
                continue
        time.sleep(6)
        print("[WoS] Search submitted")

    # Get result count
    try:
        count_el = driver.find_element(By.CSS_SELECTOR,
            "[data-ta='results-count'], .search-results-count, "
            ".brand-result-count, .brand-results-count")
        print(f"[WoS] Results: {count_el.text.strip()}")
    except NoSuchElementException:
        pass

    # Apply filters if needed (Article, English, 1977-2026)
    print("[WoS] Please verify filters: Document Type=Article, Language=English, Timespan=1977-2026")
    print("      Press Enter when filters are applied...")
    input()

    # Export in batches of 500
    print("\n[WoS] Starting export. WoS allows max 500 records per export.")
    print("  You will need to export multiple batches if >500 results.")
    print("  Files will be saved to:", download_dir)

    batch = 1
    while True:
        start_rec = (batch - 1) * 500 + 1
        print(f"\n[WoS] Export batch {batch} (records {start_rec}–{start_rec+499})...")

        # Click Export
        try:
            export_btn = wait_click(driver, By.XPATH,
                "//button[contains(text(),'Export')] | "
                "//*[@data-ta='export'] | //button[contains(@class,'export')]",
                timeout=15)
            time.sleep(2)
        except TimeoutException:
            print("[WoS] Export button not found. Please click Export manually, then press Enter")
            input()

        # Choose Excel format
        try:
            excel_opt = wait_click(driver, By.XPATH,
                "//*[contains(text(),'Excel')] | //*[@value='excel']", timeout=10)
            time.sleep(1)
        except TimeoutException:
            print("[WoS] Excel option not found. Select it manually, then press Enter")
            input()

        # Set record range
        try:
            from_input = driver.find_element(By.XPATH,
                "//input[@id='ExportFromNumber' or @name='from' or @placeholder='1']")
            to_input = driver.find_element(By.XPATH,
                "//input[@id='ExportToNumber' or @name='to' or @placeholder='500']")
            from_input.clear()
            from_input.send_keys(str(start_rec))
            to_input.clear()
            to_input.send_keys(str(start_rec + 499))
        except NoSuchElementException:
            print(f"[WoS] Set range manually: {start_rec} to {start_rec+499}, then press Enter")
            input()

        # Select Full Record
        try:
            full_record = driver.find_element(By.XPATH,
                "//*[contains(text(),'Full Record')] | //input[@value='fullRecord']")
            full_record.click()
            time.sleep(0.5)
        except NoSuchElementException:
            pass

        # Click final Export/OK
        try:
            ok_btn = wait_click(driver, By.XPATH,
                "//button[contains(text(),'Export')] | //button[contains(text(),'OK')] | "
                "//*[@data-ta='export-ok']", timeout=10)
            time.sleep(8)  # wait for download to start
            print(f"[WoS] Batch {batch} export triggered")
        except TimeoutException:
            print("[WoS] Click Export/OK manually, then press Enter after download starts")
            input()

        cont = input(f"\nExport more batches? [y/N]: ").strip().lower()
        if cont != "y":
            break
        batch += 1

    print(f"\n[WoS] Export complete. Files saved to: {download_dir}")
    print("Upload the exported files to server:")
    print(f"  scp {download_dir}/*.xls server:/home/user/PAPERS_IN_PHD_2026/p6/tools/results/")


# ---------------------------------------------------------------------------
# Scopus workflow
# ---------------------------------------------------------------------------

def scopus_login(driver, email: str, password: str):
    print("\n[Scopus] Navigating to Scopus...")
    driver.get("https://www.scopus.com/search/form.uri?display=advanced")
    time.sleep(3)

    # Cookie banner
    try:
        accept = driver.find_element(By.XPATH,
            "//button[contains(text(),'Accept') or @id='onetrust-accept-btn-handler']")
        accept.click()
        time.sleep(1)
    except NoSuchElementException:
        pass

    # Sign in
    print("[Scopus] Clicking Sign In...")
    try:
        signin = wait_click(driver, By.XPATH,
            "//a[contains(text(),'Sign in')] | //button[contains(text(),'Sign in')]",
            timeout=10)
        time.sleep(2)
    except TimeoutException:
        print("[Scopus] Sign In not found — may already be logged in")
        return

    # Enter email
    try:
        email_inp = wait_for(driver, By.XPATH,
            "//input[@type='email' or @name='email']", timeout=10)
        email_inp.send_keys(email)
        email_inp.send_keys(Keys.RETURN)
        time.sleep(3)
    except TimeoutException:
        pass

    # Enter password
    try:
        pwd_inp = wait_for(driver, By.XPATH,
            "//input[@type='password']", timeout=15)
        pwd_inp.send_keys(password)
        pwd_inp.send_keys(Keys.RETURN)
        time.sleep(5)
        print("[Scopus] Login submitted")
    except TimeoutException:
        print("[Scopus] No password field. Manual login required.")
        input("Log in manually, then press Enter...")


def scopus_search_and_export(driver, download_dir: Path):
    print("\n[Scopus] Navigating to Advanced Search...")
    driver.get("https://www.scopus.com/search/form.uri?display=advanced")
    time.sleep(4)

    # Find query field
    try:
        qbox = driver.find_element(By.XPATH,
            "//textarea[@id='searchfield'] | //textarea[@name='queryField'] | "
            "//textarea[contains(@class,'search')]")
        driver.execute_script("arguments[0].value = arguments[1]", qbox, SCOPUS_QUERY)
        driver.execute_script(
            "arguments[0].dispatchEvent(new Event('input', {bubbles:true}))", qbox)
        time.sleep(1)

        # Click Search
        search_btn = driver.find_element(By.XPATH,
            "//button[@type='submit'] | //button[contains(text(),'Search')]")
        search_btn.click()
        time.sleep(8)
        print("[Scopus] Search submitted")
    except NoSuchElementException:
        print("[Scopus] Could not find query box. Please enter query manually:")
        print(SCOPUS_QUERY[:300], "...")
        input("Paste query, click Search, then press Enter...")

    # Get result count
    try:
        count_el = driver.find_element(By.XPATH,
            "//*[@data-testid='results-count'] | //*[contains(@class,'result-count')]")
        print(f"[Scopus] Results: {count_el.text.strip()}")
    except NoSuchElementException:
        pass

    # Export (Scopus allows up to 2000 at once with institutional access)
    print("\n[Scopus] Exporting results...")
    print("  Scopus allows up to 2000 records per export with institutional access.")

    try:
        export_btn = wait_click(driver, By.XPATH,
            "//button[contains(text(),'Export')] | "
            "//*[@data-testid='export-button']", timeout=15)
        time.sleep(2)
    except TimeoutException:
        print("[Scopus] Click Export manually, then press Enter")
        input()

    # Select CSV format
    try:
        csv_opt = driver.find_element(By.XPATH, "//*[contains(text(),'CSV')]")
        csv_opt.click()
        time.sleep(1)
    except NoSuchElementException:
        print("[Scopus] Select CSV format manually, then press Enter")
        input()

    # Select all fields
    try:
        all_info = driver.find_element(By.XPATH,
            "//*[contains(text(),'All available information')] | "
            "//*[@value='allinfo']")
        all_info.click()
    except NoSuchElementException:
        pass

    # Export
    try:
        export_ok = wait_click(driver, By.XPATH,
            "//button[contains(text(),'Export')] | //button[contains(text(),'Download')]",
            timeout=10)
        time.sleep(10)
        print("[Scopus] Export triggered")
    except TimeoutException:
        print("[Scopus] Click Export/Download manually, then press Enter")
        input()

    print(f"\n[Scopus] Export complete. File saved to: {download_dir}")


# ---------------------------------------------------------------------------
# OSF check
# ---------------------------------------------------------------------------

def check_osf(driver, email: str, password: str):
    print("\n[OSF] Checking pre-registration at https://osf.io/z37kn ...")
    driver.get("https://osf.io/z37kn")
    time.sleep(3)
    title = driver.title
    print(f"[OSF] Page title: {title}")
    print(f"[OSF] URL: {driver.current_url}")
    print("[OSF] OSF registration is public — no login needed to verify.")
    print("[OSF] DOI: 10.17605/OSF.IO/Z37KN")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="P6 data extraction from WoS and Scopus (run LOCALLY)")
    parser.add_argument("--wos", action="store_true", help="Run WoS extraction")
    parser.add_argument("--scopus", action="store_true", help="Run Scopus extraction")
    parser.add_argument("--osf", action="store_true", help="Check OSF registration")
    parser.add_argument("--output", default=str(DOWNLOAD_DIR),
                        help="Download directory")
    args = parser.parse_args()

    if not (args.wos or args.scopus or args.osf):
        parser.print_help()
        print("\nExample: python3 28_extract_wos_scopus_locally.py --wos --scopus")
        sys.exit(0)

    download_dir = Path(args.output)
    download_dir.mkdir(parents=True, exist_ok=True)

    wos_email = wos_pass = scopus_email = scopus_pass = ""

    if args.wos or args.scopus:
        print("=" * 55)
        print("P6 Data Extraction — Local Runner")
        print("Credentials are entered once and never saved.")
        print("=" * 55)

        if args.wos:
            wos_email = os.environ.get("WOS_EMAIL") or input("WoS email: ").strip()
            wos_pass  = os.environ.get("WOS_PASSWORD") or input("WoS password: ").strip()
        if args.scopus:
            scopus_email = os.environ.get("SCOPUS_EMAIL") or input("Scopus email (Gmail): ").strip()
            scopus_pass  = os.environ.get("SCOPUS_PASSWORD") or input("Scopus password: ").strip()

    print(f"\nDownload directory: {download_dir}")
    print("Starting Chrome browser (non-headless so you can assist if needed)...")

    driver = make_driver(download_dir)

    try:
        if args.wos:
            wos_login(driver, wos_email, wos_pass)
            wos_search_and_export(driver, download_dir)

        if args.scopus:
            scopus_login(driver, scopus_email, scopus_pass)
            scopus_search_and_export(driver, download_dir)

        if args.osf:
            check_osf(driver, "", "")

    finally:
        print("\n\nBrowser will close in 10 seconds. Press Ctrl+C to keep it open.")
        try:
            time.sleep(10)
        except KeyboardInterrupt:
            pass
        driver.quit()

    # Summary
    files = list(download_dir.glob("*"))
    print(f"\n{'='*55}")
    print(f"Done. {len(files)} file(s) in {download_dir}/")
    for f in files:
        print(f"  {f.name}")
    print()
    print("Next: upload exported files to the server and run:")
    print("  python3 p6/tools/01_parse_wos_export.py --input <exported_file>")
    print("  python3 p6/tools/03_deduplicate_merge.py")
    print(f"{'='*55}")


if __name__ == "__main__":
    main()
