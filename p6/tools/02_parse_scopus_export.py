#!/usr/bin/env python3
"""
02_parse_scopus_export.py — Parse Scopus CSV export to standard parsed CSV.

Scopus standard CSV export column names (common variants handled):
  Title, Authors, Year, Source title, DOI, Abstract, EID, Link

Usage:
  python3 02_parse_scopus_export.py --input exports/scopus_export.csv
  python3 02_parse_scopus_export.py --input exports/scopus_export.csv --output results/scopus_parsed_20260517.csv
"""

import argparse
import csv
import re
import sys
from datetime import datetime
from pathlib import Path


# Scopus uses different column name variants across export versions — map them all
COLUMN_MAP = {
    # Title
    "Title": "title",
    "Document Title": "title",
    # Authors
    "Authors": "authors",
    "Author Names": "authors",
    # Year
    "Year": "year",
    "Publication Year": "year",
    "Publish Year": "year",
    # Source/Journal
    "Source title": "journal",
    "Source Title": "journal",
    "Journal": "journal",
    "Publication Name": "journal",
    # DOI
    "DOI": "doi",
    # Abstract
    "Abstract": "abstract",
    # EID (unique Scopus identifier)
    "EID": "source_id",
    "Scopus EID": "source_id",
    # Link
    "Link": "link",
    "URL": "link",
}


def parse_scopus_file(filepath: Path) -> list[dict]:
    """Parse a Scopus CSV export into a list of canonical record dicts."""
    records = []

    with open(filepath, encoding="utf-8-sig", errors="replace", newline="") as fh:
        # Detect dialect
        sample = fh.read(4096)
        fh.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
        except csv.Error:
            dialect = csv.excel

        reader = csv.DictReader(fh, dialect=dialect)
        if reader.fieldnames is None:
            print("ERROR: CSV has no header row.", file=sys.stderr)
            sys.exit(1)

        # Build a mapping from actual column name → canonical name
        col_mapping: dict[str, str] = {}
        for col in reader.fieldnames:
            if col in COLUMN_MAP:
                col_mapping[col] = COLUMN_MAP[col]

        for row in reader:
            rec = _build_record(row, col_mapping)
            records.append(rec)

    return records


def _build_record(row: dict, col_mapping: dict[str, str]) -> dict:
    """Build a canonical record from a Scopus CSV row."""
    # Flatten: pick first matching column for each canonical field
    flat: dict[str, str] = {}
    for col, canonical in col_mapping.items():
        if canonical not in flat:
            val = (row.get(col) or "").strip()
            if val:
                flat[canonical] = val

    # Normalise DOI
    doi = flat.get("doi", "").lower()
    doi = re.sub(r"^https?://doi\.org/", "", doi)
    doi = doi.strip()

    # Normalise source_id: strip "2-s2.0-" prefix sometimes present
    source_id = flat.get("source_id", "").strip()

    # Year: strip whitespace and non-numeric suffixes
    year = re.sub(r"[^\d].*$", "", flat.get("year", "").strip())

    return {
        "source": "scopus",
        "source_id": source_id,
        "authors": flat.get("authors", ""),
        "year": year,
        "title": flat.get("title", ""),
        "journal": flat.get("journal", ""),
        "doi": doi,
        "abstract": flat.get("abstract", ""),
    }


def write_csv(records: list[dict], output_path: Path) -> None:
    columns = ["source", "source_id", "authors", "year", "title", "journal", "doi", "abstract"]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse Scopus CSV export to standard CSV.")
    parser.add_argument("--input", required=True, help="Scopus export .csv file")
    parser.add_argument(
        "--output",
        default="",
        help="Output CSV path (default: results/scopus_parsed_YYYYMMDD.csv)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERROR: input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        output_path = Path(args.output)
    else:
        datestamp = datetime.today().strftime("%Y%m%d")
        output_path = Path(__file__).parent / "results" / f"scopus_parsed_{datestamp}.csv"

    records = parse_scopus_file(input_path)

    n_no_doi = sum(1 for r in records if not r.get("doi"))
    print(f"Parsed {len(records)} records from {input_path.name}")
    print(f"  Missing DOI : {n_no_doi}")

    write_csv(records, output_path)
    print(f"Output written: {output_path}")


if __name__ == "__main__":
    main()
