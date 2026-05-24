#!/usr/bin/env python3
"""
42_merge_tracker_to_database.py — Merge extraction tracker v3 → study database

Maps fulltext_to_extraction_tracker_v3.csv (58 cols) to p6_study_database_v2.csv (22 cols).
Only merges rows where:
  - fulltext_screening_decision == 'Y'
  - ready_for_r == '1'
  - converted_r is filled

Deduplication against existing k=288:
  1. Exact DOI match
  2. Fuzzy title match (>90%) + same year

Usage:
  python3 p6/tools/42_merge_tracker_to_database.py
  python3 p6/tools/42_merge_tracker_to_database.py --dry-run
  python3 p6/tools/42_merge_tracker_to_database.py --min-ready 10  # lower threshold for testing
"""
import csv, re, math, argparse, sys
from pathlib import Path
from datetime import date

try:
    from rapidfuzz import fuzz as _fuzz
    def fuzzy_ratio(a, b): return _fuzz.token_sort_ratio(a, b)
except ImportError:
    from difflib import SequenceMatcher
    def fuzzy_ratio(a, b): return 100 * SequenceMatcher(None, a.lower(), b.lower()).ratio()

DEFAULT_TRACKER  = "p6/tools/results/fulltext_to_extraction_tracker_v3.csv"
DEFAULT_DATABASE = "p6/data/p6_study_database_v2.csv"
DEFAULT_OUTPUT   = "p6/data/p6_study_database_v2.csv"   # canonical merged DB (22 cols)
DEFAULT_BACKUP   = f"p6/data/p6_study_database_v2_backup_{date.today().strftime('%Y%m%d')}.csv"
MIN_READY        = 50   # minimum ready_for_r=1 before allowing merge

# ── Column mappings ──────────────────────────────────────────────────────────

# icrv integer → legacy letter code (for icrv col) and icrv_std (int)
ICRV_INT_TO_LETTER = {
    "1": "I", "2": "II", "3": "III", "4": "IV", "5": "V", "6": "VI", "0": "MX"
}
ICRV_INT_TO_STD = {
    "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "0": "0"
}

# dpl integer → v2 label scheme (PRE / SPN / FOL), matching p6_study_database_v2
DPL_TO_LEGACY = {"1": "PRE", "2": "SPN", "3": "FOL"}

# fp_type → database ACC / MKT / PROD / COMP
FP_MAP = {
    "roa": "ACC", "roe": "ACC", "ros": "ACC",
    "tobin_q": "MKT", "market_return": "MKT",
    "sales_growth": "GROWTH", "productivity": "PROD",
    "composite": "COMP",
}

# doi_type (internationalization measure) passthrough mapping
DOI_TYPE_MAP = {
    "fsts": "FSTS", "entropy": "ENTROPY", "n_countries": "GEO",
    "fdi_stock": "FDI", "export_dummy": "EXP_DUM", "composite": "COMP",
    "other": "OTHER",
}

# conversion_formula → is_estimated
IS_ESTIMATED = {
    "direct": "0", "beta": "1", "t_to_r": "1",
    "F_to_r": "1", "p_to_r": "1",
}


def fisher_z(r: float) -> float:
    r = max(-0.9999, min(0.9999, r))
    return 0.5 * math.log((1 + r) / (1 - r))


def make_study_id(author: str, year: str, existing_ids: set) -> str:
    parts = re.split(r'[,;&]|\band\b', author, maxsplit=1)
    first = parts[0].strip()
    last = first.split()[-1] if first else "Unknown"
    last = re.sub(r'[^\w]', '', last)
    base = f"{last}{year}"
    sid = base
    suffix = 2
    while sid in existing_ids:
        sid = f"{base}_{suffix}"
        suffix += 1
    return sid


def first_author_slug(authors: str) -> str:
    parts = re.split(r'[,;&]|\band\b', authors, maxsplit=1)
    first = parts[0].strip()
    return first.split()[-1] if first else "Unknown"


def is_duplicate(row: dict, existing_rows: list, doi_index: dict) -> bool:
    doi = row.get("doi", "").strip().lower()
    title = row.get("title", "").strip().lower()
    year = row.get("year", "").strip()

    if doi and doi in doi_index:
        return True

    for ex in existing_rows:
        ex_title = ex.get("notes", "").lower()[:80]  # notes has title fragment sometimes
        # fuzzy on study_id author+year as proxy
        if ex.get("year") == year:
            ratio = fuzzy_ratio(title[:60], ex.get("_title_key", "")[:60])
            if ratio > 90:
                return True
    return False


def tracker_row_to_db(row: dict, study_id: str, effect_idx: int) -> dict:
    r_val = float(row["converted_r"])
    n_val = int(row.get("sample_size_n", "0") or "0")
    year  = row.get("year", "").strip()

    icrv_int = str(row.get("icrv", "")).strip()
    dpl_int  = str(row.get("dpl", "")).strip()
    fp_raw   = str(row.get("fp_type", "")).strip().lower()
    doi_raw  = str(row.get("internationalization_measure_guess", "")).strip().lower()
    formula  = str(row.get("conversion_formula", "")).strip().lower()

    effect_id = study_id if effect_idx == 1 else f"{study_id}_e{effect_idx}"

    author = first_author_slug(row.get("authors", "Unknown"))
    country = row.get("country_guess", "").strip() or row.get("region_guess", "").strip()

    # cdai: assign 'L' (low) for pre-2010, 'H' (high) for 2010+
    # Will be updated properly when cDAI moderator data is available
    try:
        cdai = "H" if int(year) >= 2010 else "M" if int(year) >= 2000 else "L"
    except:
        cdai = ""

    # Derived effect-size columns required by p6_study_database_v2 (metafor inputs)
    z_val = fisher_z(r_val)
    vi_val = 1.0 / (n_val - 3) if n_val > 3 else ""

    return {
        "study_id":   study_id,
        "effect_id":  effect_id,
        "author":     author,
        "year":       year,
        "r":          str(round(r_val, 4)),
        "n":          str(n_val) if n_val > 0 else "",
        "country":    country,
        "sample_start": row.get("study_period_start", "").strip(),
        "sample_end":   row.get("study_period_end", "").strip(),
        "icrv":       ICRV_INT_TO_LETTER.get(icrv_int, icrv_int),
        "icrv_std":   ICRV_INT_TO_STD.get(icrv_int, ""),
        "cdai":       cdai,
        "dpl":        DPL_TO_LEGACY.get(dpl_int, dpl_int),
        "doi_type":   DOI_TYPE_MAP.get(doi_raw, doi_raw.upper() or "OTHER"),
        "fp_type":    FP_MAP.get(fp_raw, "OTHER"),
        "include_flag": "1",
        "is_estimated": IS_ESTIMATED.get(formula, "1"),
        "notes":      row.get("notes_for_extractor", "")[:80],
        "fisher_z":   str(round(z_val, 5)),
        "vi":         str(round(vi_val, 6)) if vi_val != "" else "",
        "dpl_std":    dpl_int,
        "doi":        row.get("doi", "").strip(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tracker",    default=DEFAULT_TRACKER)
    parser.add_argument("--database",   default=DEFAULT_DATABASE)
    parser.add_argument("--output",     default=DEFAULT_OUTPUT)
    parser.add_argument("--backup",     default=DEFAULT_BACKUP)
    parser.add_argument("--min-ready",  type=int, default=MIN_READY)
    parser.add_argument("--dry-run",    action="store_true")
    args = parser.parse_args()

    # Load tracker
    with open(args.tracker, newline="", encoding="utf-8") as f:
        tracker = list(csv.DictReader(f))

    # Filter to ready rows
    ready = [
        r for r in tracker
        if r.get("fulltext_screening_decision") == "Y"
        and r.get("ready_for_r", "").strip() == "1"
        and r.get("converted_r", "").strip()
        and int(r.get("seq", "0")) > 435   # new candidates only (seq > 435)
    ]

    print(f"Tracker rows ready_for_r=1 (new, seq>435): {len(ready)}")

    if len(ready) < args.min_ready:
        print(f"ERROR: Only {len(ready)} ready rows — need at least {args.min_ready}.")
        print("Continue manual extraction; re-run when more papers are coded.")
        sys.exit(1)

    # Load existing database
    with open(args.database, newline="", encoding="utf-8") as f:
        db_rows = list(csv.DictReader(f))
    db_fieldnames = list(db_rows[0].keys())

    # Build DOI index from existing (v2 `doi` column + legacy "doi:" in notes)
    doi_index = {
        r["doi"].strip().lower()
        for r in db_rows
        if r.get("doi", "").strip()
    } | {
        r.get("notes", "").split("doi:")[1].strip().lower()
        for r in db_rows
        if "doi:" in r.get("notes", "").lower()
    }
    # Also from tracker DOIs that match existing
    existing_study_ids = {r["study_id"] for r in db_rows}
    existing_years_authors = {
        (r.get("author", "").lower()[:10], r.get("year", ""))
        for r in db_rows
    }

    # Build title key index for fuzzy matching
    for r in db_rows:
        r["_title_key"] = r.get("author", "") + r.get("year", "")

    # Process new rows
    new_db_rows = []
    duplicates = []
    study_id_map = {}   # (author, year) → study_id, for same-study multi-effects

    for row in ready:
        doi = row.get("doi", "").strip().lower()
        author_slug = first_author_slug(row.get("authors", "")).lower()
        year = row.get("year", "").strip()
        key = (author_slug[:10], year)

        # Check duplicate against existing
        if doi and (doi in doi_index):
            duplicates.append(row)
            continue
        if key in existing_years_authors:
            duplicates.append(row)
            continue

        # Get or create study_id
        if key not in study_id_map:
            sid = make_study_id(row.get("authors", ""), year, existing_study_ids)
            existing_study_ids.add(sid)
            study_id_map[key] = {"id": sid, "effect_count": 0}
        study_id_map[key]["effect_count"] += 1
        eidx = study_id_map[key]["effect_count"]

        try:
            db_row = tracker_row_to_db(row, study_id_map[key]["id"], eidx)
            new_db_rows.append(db_row)
        except Exception as e:
            print(f"  WARNING seq={row.get('seq')}: {e}")

    print(f"New effects to add:  {len(new_db_rows)}")
    print(f"Duplicates skipped:  {len(duplicates)}")
    print(f"Existing k:          {len(set(r['study_id'] for r in db_rows))}")
    new_studies = len(set(r["study_id"] for r in new_db_rows))
    print(f"New studies:         {new_studies}")
    print(f"Updated k:           {len(set(r['study_id'] for r in db_rows)) + new_studies}")

    if args.dry_run:
        print("\n[DRY RUN] No files modified.")
        if new_db_rows:
            print("Sample new rows:")
            for r in new_db_rows[:3]:
                print(f"  {r}")
        return

    # Backup existing database
    import shutil
    shutil.copy(args.database, args.backup)
    print(f"Backup: {args.backup}")

    # Write merged database (strip _title_key helper col)
    all_rows = db_rows + new_db_rows
    for r in all_rows:
        r.pop("_title_key", None)

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=db_fieldnames)
        w.writeheader()
        w.writerows(all_rows)

    print(f"Written: {args.output}  ({len(all_rows)} total effect sizes)")
    print(f"\nNEXT: Rscript p6/tools/meta_r_scripts/00_mara_starter_20260520.R")


if __name__ == "__main__":
    main()
