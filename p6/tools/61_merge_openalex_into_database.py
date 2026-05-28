#!/usr/bin/env python3
"""
61_merge_openalex_into_database.py — Join VERIFIED OpenAlex metadata back into
the canonical k=238 study database to produce an OSF-publication CSV.

Integrity rule: only DOIs that OpenAlex actually verified are written
(verify_status in {verified, title_match}). doi_mismatch_check / author_year_guess
/ not_found rows are left with a blank DOI and an explicit oa_match_status, so the
public dataset never carries an unverified or fabricated DOI.

The join is by study_id, so every effect-size row of a multi-effect study
inherits that study's verified DOI/journal.

Usage:
  python3 61_merge_openalex_into_database.py \
      --db       ../data/p6_study_database.csv \
      --enriched ../data/p6_openalex_enriched.csv \
      --out      ../data/p6_study_database_osf.csv
"""

import argparse
import csv
from pathlib import Path

# Statuses whose DOI we trust enough to publish.
TRUSTED = {"verified", "title_match", "title_corrected"}
ADDED_COLS = ["oa_doi", "oa_journal", "oa_cited_by", "doi_verified", "oa_match_status"]


def load_enrichment(path: Path) -> dict[str, dict]:
    by_study: dict[str, dict] = {}
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            by_study[r["study_id"]] = r
    return by_study


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True, help="canonical p6_study_database.csv")
    ap.add_argument("--enriched", required=True, help="p6_openalex_enriched.csv")
    ap.add_argument("--out", required=True, help="OSF-publication CSV (db + verified metadata)")
    args = ap.parse_args()

    enr = load_enrichment(Path(args.enriched))

    with open(args.db, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    for c in ADDED_COLS:
        if c not in fieldnames:
            fieldnames.append(c)

    studies_verified: set[str] = set()
    studies_total: set[str] = set()
    rows_with_doi = 0

    for row in rows:
        sid = row["study_id"]
        studies_total.add(sid)
        e = enr.get(sid)

        # defaults
        row["oa_doi"] = ""
        row["oa_journal"] = ""
        row["oa_cited_by"] = ""
        row["doi_verified"] = "no"
        row["oa_match_status"] = e.get("verify_status", "") if e else "not_enriched"

        if not e:
            continue

        if row["oa_match_status"] in TRUSTED and (e.get("oa_doi") or "").strip():
            row["oa_doi"] = e["oa_doi"].strip()
            row["oa_journal"] = (e.get("oa_journal") or "").strip()
            row["oa_cited_by"] = (e.get("cited_by_count") or "").strip()
            row["doi_verified"] = "yes"
            rows_with_doi += 1
            studies_verified.add(sid)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    enriched_studies = len([s for s in studies_total if s in enr])
    print("OpenAlex -> database merge complete")
    print(f"  effect-size rows           : {len(rows)}")
    print(f"  unique studies             : {len(studies_total)}")
    print(f"  studies present in enrich  : {enriched_studies}")
    print(f"  studies with VERIFIED DOI  : {len(studies_verified)}")
    print(f"  effect rows carrying a DOI : {rows_with_doi}")
    print(f"\nOutput: {out_path}")
    print("Rows without a verified DOI keep oa_match_status (doi_mismatch_check / "
          "author_year_guess / not_found / not_enriched) for manual follow-up.")


if __name__ == "__main__":
    main()
