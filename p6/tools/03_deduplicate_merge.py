#!/usr/bin/env python3
"""
03_deduplicate_merge.py — Merge multiple parsed CSVs and remove duplicates.

Deduplication logic (in order):
  1. Exact DOI match (case-insensitive, normalised)
  2. Fuzzy title match (≥85% similarity, SequenceMatcher) within ±1 year

Sources are labelled wos / scopus / openalex; duplicates get source "multi".

PRISMA counts are printed to stdout.

Usage:
  python3 03_deduplicate_merge.py \\
      --inputs results/wos_parsed_20260517.csv results/scopus_parsed_20260517.csv \\
      --output results/merged_unique_20260517.csv

  # With optional OpenAlex CSV (same column schema):
  python3 03_deduplicate_merge.py \\
      --inputs results/wos_parsed.csv results/scopus_parsed.csv results/openalex_parsed.csv
"""

import argparse
import csv
import difflib
import re
import sys
from datetime import datetime
from pathlib import Path


SIMILARITY_THRESHOLD = 0.85


def load_csv(filepath: Path) -> list[dict]:
    with open(filepath, encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def normalise_doi(doi: str) -> str:
    doi = doi.strip().lower()
    doi = re.sub(r"^https?://doi\.org/", "", doi)
    return doi


def normalise_title(title: str) -> str:
    """Lowercase, collapse whitespace, strip punctuation for fuzzy compare."""
    t = title.lower().strip()
    t = re.sub(r"[^\w\s]", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t


def title_similarity(a: str, b: str) -> float:
    na, nb = normalise_title(a), normalise_title(b)
    if not na or not nb:
        return 0.0
    return difflib.SequenceMatcher(None, na, nb).ratio()


def safe_year(record: dict) -> int | None:
    try:
        return int(str(record.get("year", "")).strip()[:4])
    except (ValueError, TypeError):
        return None


def merge_records(inputs: list[Path]) -> list[dict]:
    """Load all CSVs, count per-source, then deduplicate."""
    all_records: list[dict] = []
    source_counts: dict[str, int] = {}

    for path in inputs:
        rows = load_csv(path)
        for r in rows:
            source = r.get("source", "unknown").strip().lower()
            source_counts[source] = source_counts.get(source, 0) + 1
            # Normalise DOI in-place for comparison
            r["_doi_norm"] = normalise_doi(r.get("doi", ""))
        all_records.extend(rows)

    print(f"\nPRISMA counts (before deduplication):")
    for src, n in sorted(source_counts.items()):
        print(f"  {src:<12}: {n:>5}")
    print(f"  {'TOTAL':<12}: {len(all_records):>5}")

    return all_records, source_counts


def deduplicate(records: list[dict]) -> tuple[list[dict], int]:
    """
    Return (unique_records, n_duplicates).
    Each unique record gets a 'source' field reflecting all sources it appeared in.
    Duplicates get 'duplicate_of' = source_id of canonical record.
    """
    canonical: list[dict] = []  # deduplicated output
    n_dupes = 0

    for rec in records:
        doi = rec.get("_doi_norm", "")
        year = safe_year(rec)
        title = rec.get("title", "")
        matched_idx = None

        # Pass 1: exact DOI match
        if doi:
            for i, canon in enumerate(canonical):
                if canon.get("_doi_norm") and canon["_doi_norm"] == doi:
                    matched_idx = i
                    break

        # Pass 2: fuzzy title match (only when no DOI hit)
        if matched_idx is None and title:
            for i, canon in enumerate(canonical):
                canon_year = safe_year(canon)
                # Year guard: within 1 year or either year is missing
                if year is not None and canon_year is not None:
                    if abs(year - canon_year) > 1:
                        continue
                sim = title_similarity(title, canon.get("title", ""))
                if sim >= SIMILARITY_THRESHOLD:
                    matched_idx = i
                    break

        if matched_idx is not None:
            # Merge source labels
            existing_source = canonical[matched_idx].get("source", "")
            new_source = rec.get("source", "")
            if new_source and new_source not in existing_source:
                canonical[matched_idx]["source"] = "multi"
            n_dupes += 1
        else:
            # New unique record — include it
            new_rec = {k: v for k, v in rec.items() if not k.startswith("_")}
            new_rec["duplicate_of"] = ""
            canonical.append(new_rec)

    return canonical, n_dupes


def write_csv(records: list[dict], output_path: Path) -> None:
    columns = [
        "source", "source_id", "authors", "year", "title",
        "journal", "doi", "abstract", "duplicate_of",
    ]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Merge and deduplicate parsed WoS/Scopus/OpenAlex CSVs."
    )
    parser.add_argument(
        "--inputs",
        nargs="+",
        required=True,
        help="One or more parsed CSV files (wos_parsed, scopus_parsed, openalex_parsed)",
    )
    parser.add_argument(
        "--output",
        default="",
        help="Output CSV path (default: results/merged_unique_YYYYMMDD.csv)",
    )
    args = parser.parse_args()

    input_paths = [Path(p) for p in args.inputs]
    missing = [p for p in input_paths if not p.exists()]
    if missing:
        for m in missing:
            print(f"ERROR: file not found: {m}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        output_path = Path(args.output)
    else:
        datestamp = datetime.today().strftime("%Y%m%d")
        output_path = Path(__file__).parent / "results" / f"merged_unique_{datestamp}.csv"

    all_records, source_counts = merge_records(input_paths)
    unique, n_dupes = deduplicate(all_records)

    print(f"\n  Duplicates removed : {n_dupes:>5}")
    print(f"  Unique records     : {len(unique):>5}")

    # Source breakdown of uniques
    src_breakdown: dict[str, int] = {}
    for r in unique:
        s = r.get("source", "unknown")
        src_breakdown[s] = src_breakdown.get(s, 0) + 1
    print(f"\nUnique records by source:")
    for src, n in sorted(src_breakdown.items()):
        print(f"  {src:<12}: {n:>5}")

    write_csv(unique, output_path)
    print(f"\nOutput written: {output_path}")
    print(f"\nPaste into PRISMA flow:")
    for src, n in sorted(source_counts.items()):
        label = {"wos": "WoS Core Collection", "scopus": "Scopus", "openalex": "OpenAlex"}.get(
            src, src
        )
        print(f"  {label}: n = {n}")
    print(f"  Total before dedup : n = {len(all_records)}")
    print(f"  Duplicates removed : n = {n_dupes}")
    print(f"  After dedup        : n = {len(unique)}")


if __name__ == "__main__":
    main()
