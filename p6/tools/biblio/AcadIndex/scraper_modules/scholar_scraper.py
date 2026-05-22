"""
ScholarScraper — automated Google Scholar page scraper.

Replaces the Tampermonkey open_all_links.js workflow:
  - Navigates Scholar results page by page (start=0, 10, 20, ...)
  - Detects CAPTCHA and pauses for manual resolution
  - Saves page_0.html, page_10.html, ... compatible with ParserScholarLite
  - Random delays to avoid bot detection (mirrors Tampermonkey 1-3s delay)

Two backends — same external interface:
  backend="firefox"  →  Selenium + Firefox Portable (default, consistent with rest of project)
  backend="chrome"   →  nodriver (Chrome, no CDP — best stealth option)

Usage:
    scraper = ScholarScraper(output_dir=Path("queries/MyQuery"), max_results=100)
    saved = scraper.run("machine learning healthcare")
"""

import asyncio
import random
import time
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).parent.parent  # project root
FIREFOX_BINARY = BASE_DIR / "browser" / "FirefoxPortable" / "App" / "Firefox64" / "firefox.exe"
FIREFOX_PROFILE = BASE_DIR / "browser" / "FirefoxPortable" / "Data" / "profile"

SCHOLAR_BASE = "https://scholar.google.com/scholar"
RESULTS_PER_PAGE = 10
MAX_PAGES = 990  # mirrors Tampermonkey MAX_EXPLORED_PAGES

# JS injected after every navigation to suppress navigator.webdriver
_STEALTH_JS = """
Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3]});
"""


def _build_url(query: str, start: int = 0) -> str:
    return f"{SCHOLAR_BASE}?q={quote_plus(query)}&hl=en&start={start}"


# ---------------------------------------------------------------------------
# Firefox backend (Selenium + Firefox Portable)
# ---------------------------------------------------------------------------

def _make_firefox_driver(headless: bool = False):
    from selenium import webdriver

    profile = webdriver.FirefoxProfile(str(FIREFOX_PROFILE))
    # Tampermonkey runs in a real browser — mirror that by disabling automation flags
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference("useAutomationExtension", False)
    profile.set_preference(
        "general.useragent.override",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    )

    options = webdriver.FirefoxOptions()
    options.profile = profile
    options.binary_location = str(FIREFOX_BINARY)
    if headless:
        options.add_argument("--headless")

    return webdriver.Firefox(options=options)


class _FirefoxBackend:
    def __init__(self, headless: bool):
        self.headless = headless

    def run(self, query: str, output_dir: Path, max_results: int) -> list[Path]:
        driver = _make_firefox_driver(self.headless)
        saved: list[Path] = []

        try:
            url = _build_url(query, 0)
            print(f"[firefox] opening  : {url}")
            driver.get(url)
            driver.execute_script(_STEALTH_JS)
            time.sleep(random.uniform(3.0, 5.0))

            start = 0
            batch = 1
            total = max_results // RESULTS_PER_PAGE

            while start < max_results:
                print(f"[page {batch}/{total}] start={start}")

                # --- CAPTCHA (mirrors Tampermonkey captchaExists check) ---
                try:
                    driver.find_element("id", "gs_captcha_c")
                    print("\n[!] CAPTCHA detected — solve it in the browser and press Enter here.")
                    input("Press Enter to continue...")
                    time.sleep(2)
                except Exception:
                    pass

                # --- data-lid check (mirrors proxy.document.querySelector('[data-lid]')) ---
                results = driver.find_elements("css selector", "[data-lid]")
                if not results:
                    print("  [stop] No [data-lid] results, stopping.")
                    break

                # --- save (mirrors downloadButton.click() logic) ---
                html = driver.page_source
                filepath = output_dir / f"page_{start}.html"
                filepath.write_text(
                    f"<!DOCTYPE html><html>{html}</html>", encoding="utf-8"
                )
                saved.append(filepath)
                print(f"  [saved] {filepath.name}  ({filepath.stat().st_size // 1024} KB)")

                next_start = start + RESULTS_PER_PAGE
                if next_start >= max_results:
                    break

                # --- random delay (mirrors Math.random() * 3000 + 1000) ---
                delay = random.uniform(1.5, 3.0)
                print(f"  [delay] {delay:.1f}s")
                time.sleep(delay)

                driver.get(_build_url(query, next_start))
                driver.execute_script(_STEALTH_JS)
                time.sleep(random.uniform(1.0, 2.5))

                start = next_start
                batch += 1

        finally:
            driver.quit()

        return saved


# ---------------------------------------------------------------------------
# Chrome backend (nodriver — no CDP, best stealth option)
# ---------------------------------------------------------------------------

class _ChromeBackend:
    def __init__(self, headless: bool):
        self.headless = headless

    def run(self, query: str, output_dir: Path, max_results: int) -> list[Path]:
        return asyncio.run(self._async_run(query, output_dir, max_results))

    async def _async_run(self, query: str, output_dir: Path, max_results: int) -> list[Path]:
        try:
            import nodriver as uc
        except ImportError as e:
            raise ImportError("nodriver required for chrome backend: pip install nodriver") from e

        browser = await uc.start(
            headless=self.headless,
            browser_args=["--window-size=1280,900"],
        )
        saved: list[Path] = []

        try:
            tab = await browser.get(_build_url(query, 0))
            await asyncio.sleep(random.uniform(3.0, 5.0))

            start = 0
            batch = 1
            total = max_results // RESULTS_PER_PAGE

            while start < max_results:
                print(f"[page {batch}/{total}] start={start}")

                try:
                    el = await tab.select("#gs_captcha_c", timeout=2)
                    if el:
                        print("\n[!] CAPTCHA detected — solve it in the browser and press Enter here.")
                        input("Press Enter to continue...")
                        await asyncio.sleep(2)
                except Exception:
                    pass

                try:
                    results = await tab.select("[data-lid]", timeout=5)
                    if not results:
                        print("  [stop] No [data-lid] results, stopping.")
                        break
                except Exception:
                    print("  [stop] No [data-lid] results, stopping.")
                    break

                html = await tab.get_content()
                filepath = output_dir / f"page_{start}.html"
                filepath.write_text(
                    f"<!DOCTYPE html><html>{html}</html>", encoding="utf-8"
                )
                saved.append(filepath)
                print(f"  [saved] {filepath.name}  ({filepath.stat().st_size // 1024} KB)")

                next_start = start + RESULTS_PER_PAGE
                if next_start >= max_results:
                    break

                delay = random.uniform(1.5, 4.0)
                print(f"  [delay] {delay:.1f}s")
                await asyncio.sleep(delay)

                await tab.get(_build_url(query, next_start))
                await asyncio.sleep(random.uniform(1.0, 2.5))

                start = next_start
                batch += 1

        finally:
            browser.stop()

        return saved


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------

class ScholarScraper:
    """
    Scrapes Google Scholar result pages and saves them as HTML files.

    Parameters
    ----------
    output_dir : Path
        Where to save page_0.html, page_10.html, ...
    max_results : int
        Upper bound on results to fetch (snapped to multiple of 10).
    backend : "firefox" | "chrome"
        "firefox" uses Selenium + Firefox Portable (default).
        "chrome"  uses nodriver (no CDP, better stealth — requires: pip install nodriver).
    headless : bool
        Run browser without a visible window. Not recommended for Scholar.
    """

    def __init__(
        self,
        output_dir: Path,
        max_results: int = 100,
        backend: str = "firefox",
        headless: bool = False,
    ):
        self.output_dir = Path(output_dir)
        self.max_results = max(
            RESULTS_PER_PAGE,
            (max_results // RESULTS_PER_PAGE) * RESULTS_PER_PAGE,
        )

        if backend == "chrome":
            self._backend = _ChromeBackend(headless)
        else:
            self._backend = _FirefoxBackend(headless)

    def run(self, query: str) -> list[Path]:
        """Navigate Scholar for *query* and return list of saved HTML Paths."""
        self.output_dir.mkdir(parents=True, exist_ok=True)

        print(f"[scholar] query      : {query}")
        print(f"[scholar] max results: {self.max_results}")
        print(f"[scholar] output     : {self.output_dir}\n")

        saved = self._backend.run(query, self.output_dir, self.max_results)

        print(f"\n[scholar] done — {len(saved)} pages saved to {self.output_dir}")
        print("[scholar] next step  : python main_scrape.py")
        return saved
