#!/usr/bin/env python3
"""
Script 24: Fetch abstracts and OA PDF URLs from the OpenAlex API.

Two passes:
  Pass A — 87 still-UNSURE papers (unsure_still_round4_20260518.csv):
            fetch abstract for Round-5 resolution (script 25).
  Pass B — 520 v6 pool (extraction_worklist_v6_20260518.csv):
            fetch OA PDF URL for download prioritisation.

OpenAlex API is free; no API key required.  Adding ?mailto= enables the
"polite pool" with higher rate limits (10 req/s, 100 k/day).

DOI lookup :  GET https://api.openalex.org/works/https://doi.org/{doi}
Title search: GET https://api.openalex.org/works?search={title}&per-page=1
Rate limit : polite pool ≈ 10 req/s → default sleep = 0.12 s between requests.
Results are cached in openalex_cache_YYYYMMDD.json so interrupted runs resume
without hitting the API again.

Usage
-----
    python3 24_fetch_openalex_abstracts_pdfs.py
    python3 24_fetch_openalex_abstracts_pdfs.py --email you@uni.edu --delay 0.2
"""

import argparse, csv, json, pathlib, time, urllib.parse, urllib.request, urllib.error
from collections import defaultdict

# ── paths ──────────────────────────────────────────────────────────────────────
BASE    = pathlib.Path(__file__).parent
RES     = BASE / "results"
TODAY   = "20260519"

UNSURE_INPUT  = RES / "unsure_still_round4_20260518.csv"
POOL_INPUT    = RES / "extraction_worklist_v6_20260518.csv"
CACHE_FILE    = RES / f"openalex_cache_{TODAY}.json"

OUTPUT_UNSURE = RES / f"openalex_unsure_r4_abstracts_{TODAY}.csv"
OUTPUT_POOL   = RES / f"openalex_v6_pool_enriched_{TODAY}.csv"

# OpenAlex fields to select (minimises payload)
FIELDS = "id,doi,display_name,abstract_inverted_index,best_oa_location,open_access,locations"
OA_BASE = "https://api.openalex.org/works"

# ── CLI ────────────────────────────────────────────────────────────────────────
ap = argparse.ArgumentParser()
ap.add_argument("--email", default="Thuyhuongctu@gmail.com",
                help="Polite-pool email (OpenAlex identifies your requests)")
ap.add_argument("--delay", type=float, default=0.12,
                help="Seconds between API calls (default 0.12 ≈ 8 req/s)")
args = ap.parse_args()
EMAIL = args.email
DELAY = args.delay


# ── helpers ───────────────────────────────────────────────────────────────────

def reconstruct_abstract(inv_idx: dict) -> str:
    """Reconstruct plain text from OpenAlex abstract_inverted_index."""
    if not inv_idx:
        return ""
    pos_word: dict[int, str] = {}
    for word, positions in inv_idx.items():
        for pos in positions:
            pos_word[pos] = word
    return " ".join(pos_word[k] for k in sorted(pos_word))


def best_pdf_url(work: dict) -> str:
    """Return best OA PDF URL from a work record (empty string if none)."""
    bol = work.get("best_oa_location") or {}
    if bol.get("pdf_url"):
        return bol["pdf_url"]
    for loc in (work.get("locations") or []):
        if loc.get("pdf_url"):
            return loc["pdf_url"]
    return ""


def _get(url: str) -> dict | None:
    """HTTP GET → parsed JSON, or None on error."""
    try:
        time.sleep(DELAY)
        req = urllib.request.Request(url, headers={"User-Agent": "P6-MetaAnalysis/1.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        if e.code == 429:          # rate-limit: back off and retry once
            time.sleep(5)
            try:
                with urllib.request.urlopen(url, timeout=20) as resp:
                    return json.loads(resp.read())
            except Exception:
                return None
        return None
    except Exception:
        return None


def fetch_by_doi(doi: str) -> dict | None:
    doi_enc = urllib.parse.quote(doi.strip(), safe="")
    url = f"{OA_BASE}/https://doi.org/{doi_enc}?select={FIELDS}&mailto={EMAIL}"
    return _get(url)


def fetch_by_title(title: str) -> dict | None:
    q = urllib.parse.quote(title.strip()[:200])
    url = f"{OA_BASE}?search={q}&per-page=1&select={FIELDS}&mailto={EMAIL}"
    data = _get(url)
    if data is None:
        return None
    results = data.get("results", [])
    return results[0] if results else None


def enrich(doi: str, title: str, cache: dict) -> dict:
    """Return enrichment dict; consult / update cache in-place."""
    key = doi.strip().lower() if doi.strip() else f"TITLE::{title[:100]}"
    if key in cache:
        return cache[key]

    work = fetch_by_doi(doi) if doi.strip() else None
    if work is None:
        work = fetch_by_title(title)

    if work is None:
        result = {"abstract": "", "oa_status": "", "oa_pdf_url": "", "openalex_id": "NOT_FOUND"}
    else:
        result = {
            "abstract":    reconstruct_abstract(work.get("abstract_inverted_index") or {}),
            "oa_status":   (work.get("open_access") or {}).get("oa_status", ""),
            "oa_pdf_url":  best_pdf_url(work),
            "openalex_id": work.get("id", ""),
        }
    cache[key] = result
    return result


# ── load / save cache ─────────────────────────────────────────────────────────

def load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, encoding="utf-8") as f:
                c = json.load(f)
            print(f"  Cache loaded: {len(c)} entries from {CACHE_FILE.name}")
            return c
        except Exception:
            pass
    return {}


def save_cache(cache: dict) -> None:
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


# ── Pass A: 87 still-UNSURE ───────────────────────────────────────────────────

def pass_a(cache: dict) -> None:
    print("\n=== Pass A: 87 still-UNSURE papers (abstract fetch for R5 resolution) ===")
    with open(UNSURE_INPUT, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print(f"  Input rows: {len(rows)}")

    out_cols = list(rows[0].keys()) + ["abstract", "oa_status", "oa_pdf_url", "openalex_id"]
    found = missing = 0

    with open(OUTPUT_UNSURE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_cols, extrasaction="ignore")
        w.writeheader()
        for i, r in enumerate(rows, 1):
            doi   = r.get("doi", "").strip()
            title = r.get("title", "").strip()
            enr = enrich(doi, title, cache)
            r.update(enr)
            w.writerow(r)
            status = "✓ abstract" if enr["abstract"] else "✗ no abstract"
            pdf    = "✓ OA PDF"   if enr["oa_pdf_url"] else "  no PDF"
            print(f"  [{i:3d}/87] {status}  {pdf}  {title[:55]}")
            if enr["abstract"]:
                found += 1
            else:
                missing += 1
            if i % 20 == 0:
                save_cache(cache)       # checkpoint every 20

    save_cache(cache)
    print(f"\n  Pass A done — abstracts found: {found}  missing: {missing}")
    print(f"  Output → {OUTPUT_UNSURE.name}")


# ── Pass B: 520 v6 pool ───────────────────────────────────────────────────────

def pass_b(cache: dict) -> None:
    print("\n=== Pass B: 520 v6 pool (OA PDF URL + abstract enrichment) ===")
    with open(POOL_INPUT, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print(f"  Input rows: {len(rows)}")

    existing_cols = list(rows[0].keys())
    new_cols      = [c for c in ["abstract", "oa_status", "oa_pdf_url", "openalex_id"]
                     if c not in existing_cols]
    out_cols = existing_cols + new_cols

    oa_pdf_count = abstract_count = 0

    with open(OUTPUT_POOL, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_cols, extrasaction="ignore")
        w.writeheader()
        for i, r in enumerate(rows, 1):
            doi   = str(r.get("doi", "") or "").strip()
            title = str(r.get("title", "") or "").strip()
            enr = enrich(doi, title, cache)
            for k, v in enr.items():
                r[k] = v
            w.writerow(r)
            if enr["oa_pdf_url"]:
                oa_pdf_count += 1
            if enr["abstract"]:
                abstract_count += 1
            if i % 50 == 0:
                pct = i / len(rows) * 100
                print(f"  [{i:3d}/{len(rows)}] {pct:.0f}%  "
                      f"OA PDFs so far: {oa_pdf_count}  abstracts: {abstract_count}")
                save_cache(cache)

    save_cache(cache)
    pct_pdf = oa_pdf_count / len(rows) * 100
    pct_abs = abstract_count / len(rows) * 100
    print(f"\n  Pass B done:")
    print(f"    OA PDF URL found : {oa_pdf_count}/{len(rows)} ({pct_pdf:.1f}%)")
    print(f"    Abstract found   : {abstract_count}/{len(rows)} ({pct_abs:.1f}%)")
    print(f"  Output → {OUTPUT_POOL.name}")


# ── main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    print(f"Script 24 — OpenAlex abstract + OA-PDF enrichment")
    print(f"  Email (polite pool) : {EMAIL}")
    print(f"  Delay between calls : {DELAY}s (~{1/DELAY:.0f} req/s)")
    print(f"  Cache file          : {CACHE_FILE.name}")
    print(f"  Estimated runtime   : ~{(87 + 520) * DELAY / 60:.1f} min (607 calls)")

    RES.mkdir(exist_ok=True)
    cache = load_cache()

    pass_a(cache)
    pass_b(cache)

    print("\n=== Summary ===")
    print(f"  Total cache entries : {len(cache)}")
    print(f"  Pass A output       : {OUTPUT_UNSURE.name}")
    print(f"  Pass B output       : {OUTPUT_POOL.name}")
    print("\nNext step: run script 25 on the Pass A output to resolve UNSURE papers.")


if __name__ == "__main__":
    main()
