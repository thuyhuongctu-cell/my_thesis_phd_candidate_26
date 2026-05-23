"""
P6 DOI Enrichment Script for 2_NO_DOI_MANUAL papers
=====================================================
Queries: Semantic Scholar → CrossRef → OpenAlex (in order)
Updates: fulltext_to_extraction_tracker_v2.csv with found DOIs

Usage:
    python3 p6/tools/11_doi_enrichment_nodoi.py [--dry-run] [--limit N] [--seq SEQ1,SEQ2]

Requirements:
    pip install requests difflib (stdlib: csv, time, re, json)
"""

import csv
import json
import re
import sys
import time
import argparse
from pathlib import Path
from difflib import SequenceMatcher

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except ImportError:
    print("ERROR: pip install requests")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
TRACKER = Path(__file__).parent / "results" / "fulltext_to_extraction_tracker_v2.csv"
RESULTS_FILE = Path(__file__).parent / "results" / "doi_enrichment_nodoi_results.csv"
EMAIL = "huongdt@vlute.edu.vn"

TITLE_MATCH_THRESHOLD = 0.82   # minimum fuzzy title similarity
YEAR_TOLERANCE = 1             # ±1 year allowed

# ---------------------------------------------------------------------------
# HTTP session with retry
# ---------------------------------------------------------------------------
def make_session():
    s = requests.Session()
    retry = Retry(total=3, backoff_factor=2, status_forcelist=[429, 500, 502, 503])
    s.mount("https://", HTTPAdapter(max_retries=retry))
    s.headers.update({
        "User-Agent": f"P6-MetaAnalysis-DOIEnrichment/1.0 (mailto:{EMAIL})"
    })
    return s

SESSION = make_session()

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def clean_title(t: str) -> str:
    return re.sub(r"[^\w\s]", " ", t.lower()).strip()

def title_sim(a: str, b: str) -> float:
    return SequenceMatcher(None, clean_title(a), clean_title(b)).ratio()

def year_ok(found_year, target_year, tol=YEAR_TOLERANCE) -> bool:
    try:
        return abs(int(found_year) - int(target_year)) <= tol
    except (TypeError, ValueError):
        return True  # unknown year — keep

def first_author_last(authors_str: str) -> str:
    """Extract last name of first author from 'Last, First; ...' format."""
    if not authors_str:
        return ""
    first = authors_str.split(";")[0].strip()
    return first.split(",")[0].strip().lower()

# ---------------------------------------------------------------------------
# Source 1: Semantic Scholar
# ---------------------------------------------------------------------------
def query_ss(title: str, authors: str, year: str) -> dict | None:
    """Returns {'doi', 'title', 'year', 'abstract', 'source'} or None."""
    query = f"{title[:100]}"
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "fields": "title,year,externalIds,abstract,authors",
        "limit": 5,
    }
    try:
        r = SESSION.get(url, params=params, timeout=15)
        if r.status_code != 200:
            return None
        data = r.json().get("data", [])
    except Exception:
        return None

    for p in data:
        pt = p.get("title", "")
        py = p.get("year") or ""
        sim = title_sim(title, pt)
        if sim >= TITLE_MATCH_THRESHOLD and year_ok(py, year):
            doi = p.get("externalIds", {}).get("DOI", "")
            return {
                "doi": doi,
                "title_found": pt,
                "year_found": str(py),
                "abstract": (p.get("abstract") or "")[:500],
                "source": "semantic_scholar",
                "sim": round(sim, 3),
            }
    return None

# ---------------------------------------------------------------------------
# Source 2: CrossRef
# ---------------------------------------------------------------------------
def query_crossref(title: str, authors: str, year: str) -> dict | None:
    fa = first_author_last(authors)
    query = f"{title[:120]} {fa}".strip()
    url = "https://api.crossref.org/works"
    params = {
        "query": query,
        "rows": 5,
        "select": "title,DOI,published,author,abstract",
        "mailto": EMAIL,
    }
    if year:
        params["filter"] = f"from-pub-date:{int(year)-1},until-pub-date:{int(year)+1}"
    try:
        r = SESSION.get(url, params=params, timeout=15)
        if r.status_code != 200:
            return None
        items = r.json()["message"]["items"]
    except Exception:
        return None

    for item in items:
        pt_list = item.get("title", [])
        pt = pt_list[0] if pt_list else ""
        py = ""
        dp = item.get("published", {}).get("date-parts", [[]])
        if dp and dp[0]:
            py = str(dp[0][0])
        sim = title_sim(title, pt)
        if sim >= TITLE_MATCH_THRESHOLD and year_ok(py, year):
            doi = item.get("DOI", "")
            abstract = item.get("abstract", "")
            return {
                "doi": doi,
                "title_found": pt,
                "year_found": py,
                "abstract": re.sub(r"<[^>]+>", "", abstract)[:500],
                "source": "crossref",
                "sim": round(sim, 3),
            }
    return None

# ---------------------------------------------------------------------------
# Source 3: OpenAlex
# ---------------------------------------------------------------------------
def query_openalex(title: str, authors: str, year: str) -> dict | None:
    url = "https://api.openalex.org/works"
    params = {
        "search": title[:120],
        "select": "title,doi,publication_year,abstract_inverted_index",
        "per-page": 5,
        "mailto": EMAIL,
    }
    if year:
        params["filter"] = f"publication_year:{int(year)-1}-{int(year)+1}"
    try:
        r = SESSION.get(url, params=params, timeout=15)
        if r.status_code != 200:
            return None
        items = r.json().get("results", [])
    except Exception:
        return None

    for item in items:
        pt = item.get("title") or ""
        py = item.get("publication_year") or ""
        sim = title_sim(title, pt)
        if sim >= TITLE_MATCH_THRESHOLD and year_ok(py, year):
            doi_raw = item.get("doi", "") or ""
            doi = doi_raw.replace("https://doi.org/", "")
            return {
                "doi": doi,
                "title_found": pt,
                "year_found": str(py),
                "abstract": "",
                "source": "openalex",
                "sim": round(sim, 3),
            }
    return None

# ---------------------------------------------------------------------------
# Main enrichment loop
# ---------------------------------------------------------------------------
def enrich_paper(row: dict) -> dict:
    title = row.get("title", "")
    authors = row.get("authors", "")
    year = row.get("year", "")
    seq = row.get("seq", "")

    result = {"seq": seq, "doi_found": "", "title_found": "", "year_found": "",
              "abstract": "", "source": "not_found", "sim": 0.0}

    for query_fn, label in [
        (query_ss, "SS"),
        (query_crossref, "CR"),
        (query_openalex, "OA"),
    ]:
        try:
            hit = query_fn(title, authors, year)
        except Exception as e:
            hit = None
        if hit and hit.get("doi"):
            result.update({
                "doi_found": hit["doi"],
                "title_found": hit.get("title_found", ""),
                "year_found": hit.get("year_found", ""),
                "abstract": hit.get("abstract", ""),
                "source": hit["source"],
                "sim": hit.get("sim", 0.0),
            })
            print(f"  [{label}] ✓ {hit['doi'][:40]}  sim={hit['sim']:.2f}")
            break
        time.sleep(0.5)  # polite rate limit

    return result

# ---------------------------------------------------------------------------
# Update tracker
# ---------------------------------------------------------------------------
def update_tracker(enrichment_map: dict[str, dict], dry_run: bool = False):
    """Write DOI + doi_link + abstract snippet to tracker."""
    with open(TRACKER, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fieldnames = list(rows[0].keys()) if rows else []

    updated = 0
    for row in rows:
        seq = row.get("seq", "")
        if seq in enrichment_map and enrichment_map[seq]["doi_found"]:
            e = enrichment_map[seq]
            doi = e["doi_found"]
            row["doi"] = doi
            row["doi_link"] = f"https://doi.org/{doi}"
            # Store abstract snippet in notes if no existing notes
            if e["abstract"] and not row.get("notes_for_extractor", "").strip():
                row["notes_for_extractor"] = f"[auto-abstract] {e['abstract'][:200]}"
            updated += 1

    if dry_run:
        print(f"\n[DRY RUN] Would update {updated} rows with DOIs")
        return

    with open(TRACKER, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"\n✓ Updated tracker: {updated} rows with DOIs")

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="DOI enrichment for 2_NO_DOI_MANUAL papers")
    parser.add_argument("--dry-run", action="store_true", help="Don't write to tracker")
    parser.add_argument("--limit", type=int, default=0, help="Process only N papers (0=all)")
    parser.add_argument("--seq", type=str, default="", help="Comma-separated seq IDs to process")
    parser.add_argument("--results-only", action="store_true", help="Only write results CSV, don't update tracker")
    args = parser.parse_args()

    with open(TRACKER, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    no_doi = [r for r in rows if r.get("extraction_priority", "") == "2_NO_DOI_MANUAL"]

    if args.seq:
        target_seqs = set(args.seq.split(","))
        no_doi = [r for r in no_doi if r.get("seq", "") in target_seqs]

    if args.limit:
        no_doi = no_doi[:args.limit]

    print(f"Processing {len(no_doi)} papers...")
    print("=" * 70)

    enrichment_map: dict[str, dict] = {}
    found = 0

    for i, row in enumerate(no_doi, 1):
        seq = row.get("seq", "")
        title = row.get("title", "")[:60]
        year = row.get("year", "")
        print(f"[{i:3}/{len(no_doi)}] seq={seq} ({year}) {title}...")

        result = enrich_paper(row)
        enrichment_map[seq] = result

        if result["doi_found"]:
            found += 1
        else:
            print(f"  ✗ not found")

        time.sleep(0.3)

    print(f"\n{'='*70}")
    print(f"Found: {found}/{len(no_doi)} ({found/len(no_doi)*100:.0f}%)")

    # Write results CSV
    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULTS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "seq", "doi_found", "title_found", "year_found", "source", "sim", "abstract"
        ])
        writer.writeheader()
        for v in enrichment_map.values():
            writer.writerow(v)
    print(f"Results saved to: {RESULTS_FILE}")

    if not args.dry_run and not args.results_only:
        update_tracker(enrichment_map, dry_run=False)
    elif args.dry_run:
        update_tracker(enrichment_map, dry_run=True)
    else:
        print("(--results-only: tracker not updated)")

if __name__ == "__main__":
    main()
