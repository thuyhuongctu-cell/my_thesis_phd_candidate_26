#!/usr/bin/env python3
"""
10_merge_new_studies.py — Merge newly coded studies into existing database.

After L2 screening, filter include_flag == Y from the extraction template
and append non-duplicate studies to the existing p6_study_database.csv.

Deduplication:
  1. Exact DOI match (doi_enriched vs existing doi column)
  2. Fuzzy title match (>90% similarity) + same year

Usage:
    python3 10_merge_new_studies.py \
        --new     p6/tools/results/l2_extraction_template.csv \
        --existing p6/data/p6_study_database.csv \
        --output  p6/data/p6_study_database_updated.csv
"""

import argparse
import csv
import sys
from pathlib import Path

try:
    from rapidfuzz import fuzz
    FUZZY_LIB = "rapidfuzz"
except ImportError:
    from difflib import SequenceMatcher
    FUZZY_LIB = "difflib"


# ── Code harmonization: legacy → new schema ───────────────────────────────────
# Legacy existing database codes → standardized numeric codes for metafor
#
# ICRV: Roman → integer 1-6
#   I   → 1 (Advanced: USA, UK, Germany, Japan, Korea, Taiwan)
#   II  → 1 (Smaller Advanced: Italy, Spain; some Transition: Poland → conservatively 1)
#   III → 2 (Emerging/Developing: China, India, Mexico, Brazil)
#   MX  → 0 (Multi-country mixed — kept separate; use as multi dummy in MARA)
#   FR  → 6 (Frontier/LDC)
ICRV_LEGACY = {"I": "1", "II": "1", "III": "2", "MX": "0", "FR": "6", "": ""}

# DPL: named phase → integer 1-3
#   PRE → 1 (pre-2000 publications)
#   SPN → 2 (2000-2009, digital spawn phase)
#   FOL → 3 (2010+, digital follow-on / platform maturity phase)
DPL_LEGACY = {"PRE": "1", "SPN": "2", "FOL": "3", "": ""}

# cDAI: categorical → midpoint continuous proxy (pending World Bank data lookup)
#   L → 0.25 (low digital adoption proxy)
#   M → 0.50 (medium)
#   H → 0.75 (high)
CDAI_LEGACY = {"L": "0.25", "M": "0.50", "H": "0.75", "": ""}

# doi_type: legacy → new
DOI_TYPE_LEGACY = {
    "FSTS": "FSTS", "EXP": "export_ratio", "GEO": "geographic_diversification",
    "COMP": "DOI", "FDI": "FDI", "OTH": "other", "": ""
}

# fp_type: legacy → new
FP_TYPE_LEGACY = {
    "ACC": "financial_perf", "MKT": "Tobin_Q", "MIX": "financial_perf",
    "LAB": "labor_productivity", "": ""
}


def harmonize_row(row: dict, source: str = "existing") -> dict:
    """Translate legacy codes to standardized schema. Adds _std columns."""
    if source == "existing":
        row["icrv_std"]     = ICRV_LEGACY.get(row.get("icrv", ""), row.get("icrv", ""))
        row["dpl_std"]      = DPL_LEGACY.get(row.get("dpl", ""), row.get("dpl", ""))
        row["cdai_std"]     = CDAI_LEGACY.get(row.get("cdai", ""), row.get("cdai", ""))
        row["doi_type_std"] = DOI_TYPE_LEGACY.get(row.get("doi_type", ""), row.get("doi_type", ""))
        row["fp_type_std"]  = FP_TYPE_LEGACY.get(row.get("fp_type", ""), row.get("fp_type", ""))
    else:
        # New template already uses standardized codes
        row["icrv_std"]     = row.get("icrv", "")
        row["dpl_std"]      = row.get("dpl", "")
        row["cdai_std"]     = row.get("cdai", "")
        row["doi_type_std"] = row.get("doi_type", "")
        row["fp_type_std"]  = row.get("fp_type", "")
    return row


def title_similarity(a: str, b: str) -> float:
    a = a.lower().strip()
    b = b.lower().strip()
    if not a or not b:
        return 0.0
    if FUZZY_LIB == "rapidfuzz":
        return fuzz.token_sort_ratio(a, b) / 100.0
    return SequenceMatcher(None, a, b).ratio()


def normalize_doi(doi: str) -> str:
    return doi.strip().lower().lstrip("https://doi.org/").lstrip("http://dx.doi.org/")


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--new",      required=True, help="L2 extraction template (post-screening)")
    p.add_argument("--existing", required=True, help="Existing study database CSV")
    p.add_argument("--output",   required=True)
    p.add_argument("--threshold", type=float, default=0.90, help="Title similarity threshold (default 0.90)")
    return p.parse_args()


def main():
    args = parse_args()

    existing_rows = list(csv.DictReader(open(args.existing, encoding="utf-8")))
    new_rows      = list(csv.DictReader(open(args.new,      encoding="utf-8")))

    # Harmonize legacy codes in existing database
    for r in existing_rows:
        harmonize_row(r, source="existing")

    # Build DOI index of existing studies
    existing_dois = set()
    for r in existing_rows:
        doi = r.get("doi", "") or r.get("doi_enriched", "")
        if doi.strip():
            existing_dois.add(normalize_doi(doi))

    # Filter: only INCLUDE from new
    candidates = [r for r in new_rows if r.get("include_flag", "").strip().upper() == "Y"]
    if not candidates:
        print("No included studies in new template. Exiting.", file=sys.stderr)
        sys.exit(1)

    accepted    = []
    dup_doi     = []
    dup_title   = []

    for row in candidates:
        new_doi   = normalize_doi(row.get("doi_enriched", "") or row.get("doi", ""))
        new_title = row.get("title", "").strip()
        new_year  = str(row.get("year", "")).strip()

        # Check 1: exact DOI
        if new_doi and new_doi in existing_dois:
            row["merge_status"] = "dup_doi"
            dup_doi.append(row)
            continue

        # Check 2: fuzzy title + year
        is_dup = False
        for ex in existing_rows:
            ex_title = ex.get("title", "").strip()
            ex_year  = str(ex.get("year", "") or ex.get("pub_year", "")).strip()
            if ex_year == new_year and title_similarity(new_title, ex_title) >= args.threshold:
                row["merge_status"] = "dup_title"
                dup_title.append(row)
                is_dup = True
                break

        if not is_dup:
            row["merge_status"] = "new"
            harmonize_row(row, source="new")
            accepted.append(row)

    # Append accepted to existing
    all_rows = existing_rows + accepted
    # Mark existing rows
    for r in existing_rows:
        r.setdefault("merge_status", "existing")

    # Write output — use union of all fieldnames
    all_fields = list(dict.fromkeys(
        list(existing_rows[0].keys()) + list(accepted[0].keys()) if accepted
        else list(existing_rows[0].keys())
    ))

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=all_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"Existing studies   : {len(existing_rows)}")
    print(f"New candidates (Y) : {len(candidates)}")
    print(f"  Duplicates (DOI) : {len(dup_doi)}")
    print(f"  Duplicates (title): {len(dup_title)}")
    print(f"  Accepted (new)   : {len(accepted)}")
    print(f"Updated database   : {len(all_rows)} total studies")
    print(f"Output             : {out}")
    print(f"Fuzzy library      : {FUZZY_LIB}")

    if accepted:
        print(f"\nNew k = {len(all_rows)} (was {len(existing_rows)})")
    else:
        print("\nNo new studies added — all candidates were duplicates.")

    print()
    print("NOTE: Legacy codes translated to *_std columns:")
    print("  icrv_std   : I→1, II→1, III→2, MX→0(multi), FR→6")
    print("  dpl_std    : PRE→1, SPN→2, FOL→3")
    print("  cdai_std   : L→0.25, M→0.50, H→0.75 (proxy; replace with WB DAI)")
    print("  doi_type_std, fp_type_std: see mapping in script header")
    print()
    print("Run MARA with icrv_std, dpl_std, cdai_std columns (not raw icrv/dpl/cdai)")


if __name__ == "__main__":
    main()
