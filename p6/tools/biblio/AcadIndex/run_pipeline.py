"""
Full pipeline: scrape Google Scholar → parse → Excel output.

Steps:
  1. ScholarScraper   navigates Scholar and saves page_N.html to queries/<folder>/
  2. ParserScholarLite reads those HTMLs, fetches metadata via Crossref,
     optionally verifies against WOS/Scopus, and writes scraped_papers.xlsx
     to output/<query>_output/<timestamp>/

Usage
-----
# Default (Firefox portable, 100 results, WOS/Scopus disabled for speed)
python run_pipeline.py "machine learning healthcare"

# More results, enable indexer verification (WOS + Scopus APIs required)
python run_pipeline.py "deep learning NLP" --max 200 --indexers

# Chrome backend
python run_pipeline.py "tu query" --backend chrome --max 50

# Skip scraping (re-parse an existing folder)
python run_pipeline.py "tu query" --skip-scrape --out Query13
"""

import argparse
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

from scraper_modules.scholar_scraper import ScholarScraper
from scraper_modules.parser_scholar_singlethread import ParserScholarLite

QUERIES_DIR = ROOT / "queries"


def scrape(query: str, folder: str, max_results: int, backend: str) -> Path:
    output_dir = QUERIES_DIR / folder
    scraper = ScholarScraper(
        output_dir=output_dir,
        max_results=max_results,
        backend=backend,
    )
    saved = scraper.run(query)
    if not saved:
        print("[pipeline] No pages were saved — aborting parse step.")
        sys.exit(1)
    return output_dir


def parse(folder_path: Path, use_indexers: bool):
    print(f"\n[pipeline] Parsing HTML files in {folder_path} ...")
    t0 = time.time()
    parser = ParserScholarLite(use_wos_api=True, use_indexers=use_indexers)
    parser.read_htmls(to_excel=True, path=str(folder_path))
    print(f"[pipeline] Parse done in {time.time() - t0:.1f}s")


def main():
    ap = argparse.ArgumentParser(description="Scholar scrape + parse pipeline")
    ap.add_argument("query", nargs="?", default="machine learning healthcare",
                    help="Google Scholar search query")
    ap.add_argument("--max", type=int, default=100,
                    help="Max results to scrape (multiple of 10, default: 100)")
    ap.add_argument("--backend", choices=["firefox", "chrome"], default="firefox",
                    help="Browser backend (default: firefox)")
    ap.add_argument("--out", type=str, default=None,
                    help="Output subfolder name inside queries/ (default: sanitized query)")
    ap.add_argument("--indexers", action="store_true",
                    help="Enable WOS + Scopus indexer verification (requires API keys)")
    ap.add_argument("--skip-scrape", action="store_true",
                    help="Skip scraping and only (re-)parse an existing folder")
    args = ap.parse_args()

    folder = args.out or args.query.replace(" ", "_")[:40]

    t_total = time.time()

    if not args.skip_scrape:
        folder_path = scrape(args.query, folder, args.max, args.backend)
    else:
        folder_path = QUERIES_DIR / folder
        if not folder_path.exists():
            print(f"[pipeline] Folder not found: {folder_path}")
            sys.exit(1)
        print(f"[pipeline] Skipping scrape, using existing folder: {folder_path}")

    parse(folder_path, use_indexers=args.indexers)

    print(f"\n[pipeline] Total time: {time.time() - t_total:.1f}s")
    print(f"[pipeline] Results saved to output/<query>_output/<timestamp>/scraped_papers.xlsx")


if __name__ == "__main__":
    main()
