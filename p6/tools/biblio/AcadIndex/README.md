# Scholar Scraper

Automated academic paper scraper — fetches Google Scholar results, enriches metadata via Crossref, and verifies indexing in WOS and Scopus.

> Spanish documentation: [README-ES.md](README-ES.md)

## Pipeline

```
ScholarScraper (Firefox/Chrome) → queries/<folder>/page_N.html
       ↓
ParserScholarLite → Crossref (DOI) → Scopus API / WOS API
       ↓
output/<query>_output/<timestamp>/scraped_papers.xlsx
```

## Requirements

- Python 3.11+ and [uv](https://docs.astral.sh/uv/) (`pip install uv`)
- Firefox Portable (included in `browser/`) with a pre-configured user profile
- Institutional WOS access via Clarivate
- API keys for [Scopus Developer](https://dev.elsevier.com/) and Clarivate WOS

## Setup

1. Install dependencies:
   ```powershell
   uv venv
   uv pip install -r requirements.txt
   ```

2. Create a `.env` file at the project root:
   ```
   SCOPUS_API_KEY=your_scopus_api_key
   WOS_API_KEY=your_wos_api_key
   ```

## Usage

### Full pipeline (recommended)

`run_pipeline.py` runs scraping and parsing in a single command:

```powershell
# Scrape + parse (Firefox portable, 100 results)
uv run --with selenium run_pipeline.py "machine learning healthcare"

# More results with WOS/Scopus indexer verification
uv run --with selenium run_pipeline.py "deep learning NLP" --max 200 --indexers

# Chrome backend (better stealth, requires Chrome installed)
uv run --with nodriver run_pipeline.py "your query" --backend chrome --max 100

# Re-parse an existing folder without scraping again
uv run --with selenium run_pipeline.py "your query" --skip-scrape --out MyQuery
```

Output: `output/<query>_output/<timestamp>/scraped_papers.xlsx`

### Step by step

#### 1. Scrape Google Scholar

```powershell
uv run --with selenium scholar_scraper_test.py "your query" --max 100 --out MyQuery
```

HTML pages are saved to `queries/MyQuery/page_0.html`, `page_10.html`, etc.

#### 2. Authenticate WOS session

Open `browser/FirefoxPortable/FirefoxPortable.exe` (includes the institutional profile). Log in to the institutional library portal and access **Clarivate WOS**. The session may expire — renew it before each run if indexer verification is enabled.

#### 3. Parse saved HTMLs

```powershell
python main_scrape.py
```

Iterates over all subfolders in `queries/` and writes `scraped_papers.xlsx` to `output/`. Runtime can reach up to 3 hours depending on paper volume.

### Tampermonkey (manual alternative)

`tampermonkey/open_all_links.js` enables manual scraping directly from the browser:
- **Key K**: downloads the current page as HTML.
- **Mass-open button**: opens results in batches of 100.

Install via the Tampermonkey extension and import `open_all_links.js`. Place downloaded HTMLs inside `queries/<subfolder>/` before running `main_scrape.py`.

## Scraping backends

| Backend | Flag | Requirement | Notes |
|---|---|---|---|
| `firefox` (default) | `--with selenium` | Firefox Portable included | Uses pre-configured portable profile |
| `chrome` | `--with nodriver` | Chrome installed on the system | Better bot evasion — does not use CDP |

## Known issues

| Issue | Cause | Fix |
|---|---|---|
| CAPTCHA on Google Scholar | Too many requests in a short window | Scraper pauses for manual resolution; increase delays between sessions. |
| Crossref 504 error | Service timeout under high load | Scraper retries automatically; reduce query volume if it persists. |
| Excel file not generated | Excel is open during execution | Close Excel before running the scraper. |
| Disk full from Firefox temp files | Firefox does not clean up its temp folder automatically | Run `delete_trash.bat` to clear the temp directory. |
| High RAM usage from Firefox | Selenium + Firefox baseline behavior | Pending optimization. |
