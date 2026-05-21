#!/usr/bin/env python3
"""
08_prepare_l2_template.py — Build L2 extraction template from DOI-enriched candidates.

Reads new_candidates_doi_enriched.csv (output of 07_enrich_doi_crossref.py)
and produces a pre-populated extraction sheet with blank columns for effect
sizes and moderator codes, ready for manual L2 coding.

Usage:
  python3 08_prepare_l2_template.py \
      --input  p6/tools/results/new_candidates_doi_enriched.csv \
      --output p6/tools/results/l2_extraction_template.csv
"""

import argparse
import csv
import re
from datetime import datetime
from pathlib import Path

# Columns that come from the candidates file (carry-over)
CARRY_COLS = ["title", "authors", "year", "journal", "doi_enriched", "doi_source"]

# Blank columns the coder fills in (see p6_extraction_codebook.md)
BLANK_COLS = [
    # Study identifiers
    "study_id",        # Author_Year (e.g., Smith_2020); add a/b for same author-year
    "effect_id",       # study_id + _E1, _E2 etc.
    # Sample descriptors
    "country",         # ISO-3; multiple: semicolon-separated
    "sample_start",    # First year of data
    "sample_end",      # Last year of data
    "n",               # Total firm-level observations
    # Effect size
    "r",               # Pearson r (or estimated from β / t / F)
    "r_quadratic",     # β of DOI² if curvilinear study; else blank
    "turning_point",   # Turning point % if reported; else blank
    # Moderators
    "icrv",            # 1=Advanced 2=Emerging 3=Transition 4=Resource-Rich 5=SIDS 6=Frontier
    "cdai",            # Country Digital Adoption Index 0–1 (ITU/WB mean for sample period)
    "cdai_source",     # "ITU_2023" or "WB_DAI"
    "cdai_missing",    # 1 if cdai unavailable
    "dpl",             # 1=pre-2000 2=2000-2009 3=2010-2026 (based on data midpoint)
    "doi_type",        # fsts / entropy / n_countries / fdi_stock / export_dummy / composite / other
    "fp_type",         # roa / roe / ros / tobin_q / sales_growth / productivity / market_return / composite
    # Quality flags
    "is_estimated",    # 1 = r estimated from β or t/F
    "is_partial",      # 1 = partial correlation
    "is_panel",        # 1 = panel/longitudinal data
    "endogeneity_corrected",  # 1 = IV/Heckman/GMM/DID used
    "include_flag",    # 1 = include; 0 = exclude after L2
    "notes",           # Any coding notes or uncertainties
]


def make_study_id(row: dict) -> str:
    """Generate a candidate study_id from first author last name + year."""
    authors = row.get("authors", "").strip()
    year    = row.get("year", "").strip()
    if not authors:
        return ""
    first_author = authors.split(";")[0].split(",")[0].strip()
    last_name    = first_author.split()[-1] if first_author else "Unknown"
    last_name    = re.sub(r"[^A-Za-z]", "", last_name)
    return f"{last_name}_{year}" if last_name and year else ""


def infer_dpl(row: dict) -> str:
    """Infer DPL phase from year as a starting hint (coder should verify)."""
    year = row.get("year", "")
    try:
        y = int(year)
        if y < 2000:
            return "1"   # pre-digital
        elif y < 2010:
            return "2"   # early digital
        else:
            return "3"   # platform era
    except ValueError:
        return ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",  default="p6/tools/results/new_candidates_doi_enriched.csv")
    parser.add_argument("--output", default="p6/tools/results/l2_extraction_template.csv")
    args = parser.parse_args()

    in_path  = Path(args.input)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not in_path.exists():
        # Fall back to non-enriched candidates if enrichment hasn't run yet
        fallback = in_path.parent / "new_candidates_20260518.csv"
        if fallback.exists():
            print(f"[warn] {in_path.name} not found — using {fallback.name} instead")
            in_path = fallback
        else:
            raise FileNotFoundError(f"Input not found: {in_path}")

    rows = []
    with open(in_path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            rows.append(row)

    # Build output fieldnames: seq + carry-over + blank coding columns
    out_fields = ["seq"] + CARRY_COLS + BLANK_COLS

    out_rows = []
    for i, row in enumerate(rows, start=1):
        out_row = {"seq": i}

        # Carry over available columns
        for col in CARRY_COLS:
            # doi_enriched falls back to doi if enrichment not run
            if col == "doi_enriched":
                out_row[col] = row.get("doi_enriched") or row.get("doi") or ""
            else:
                out_row[col] = row.get(col, "")

        # Pre-fill blanks where inference is safe
        for col in BLANK_COLS:
            if col == "study_id":
                out_row[col] = make_study_id(row)
            elif col == "dpl":
                out_row[col] = infer_dpl(row)
            else:
                out_row[col] = ""

        out_rows.append(out_row)

    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=out_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out_rows)

    enriched_count = sum(1 for r in out_rows if r.get("doi_enriched", "").strip())
    print(f"L2 extraction template ready:")
    print(f"  Records         : {len(out_rows):,}")
    print(f"  With DOI        : {enriched_count:,} ({enriched_count/len(out_rows)*100:.1f}%)")
    print(f"  Blank columns   : {len(BLANK_COLS)} fields for manual coding")
    print(f"  DPL pre-filled  : from publication year (verify against data period)")
    print(f"  study_id        : auto-generated candidate (check duplicates!)")
    print(f"\nOutput: {out_path}")
    print(f"\nNext step: open in Excel/LibreOffice, sort by year, code L2 inclusion")
    print(f"  Codebook: p6/tools/p6_extraction_codebook.md")


if __name__ == "__main__":
    main()
