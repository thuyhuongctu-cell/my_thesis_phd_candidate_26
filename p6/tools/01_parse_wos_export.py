#!/usr/bin/env python3
"""
01_parse_wos_export.py — Parse WoS Full Record Tab-delimited export (.txt)

WoS format:
  - Each record starts with "PT J" (journal article)
  - Fields: FN/VR header, then field-code + space + value (e.g. "TI Title of paper")
  - Multi-line values are continued on indented lines (spaces, no field code)
  - Records separated by "ER" on its own line
  - File ends with "EF"

Usage:
  python3 01_parse_wos_export.py --input exports/wos_export.txt
  python3 01_parse_wos_export.py --input exports/wos_export.txt --output results/wos_parsed_20260517.csv
"""

import argparse
import csv
import re
import sys
from datetime import datetime
from pathlib import Path


FIELDS_OF_INTEREST = {
    "AU": "authors",
    "TI": "title",
    "SO": "journal",
    "PY": "year",
    "DI": "doi",
    "AB": "abstract",
    "UT": "source_id",
}


def parse_wos_file(filepath: Path) -> list[dict]:
    """Parse a WoS Full Record export file into a list of record dicts."""
    records = []
    current: dict[str, list[str]] = {}
    current_field = None

    with open(filepath, encoding="utf-8-sig", errors="replace") as fh:
        for raw_line in fh:
            line = raw_line.rstrip("\n").rstrip("\r")

            # End of record
            if line.strip() == "ER":
                if current:
                    records.append(_finalise(current))
                current = {}
                current_field = None
                continue

            # End of file marker
            if line.strip() == "EF":
                break

            # Skip file header lines (FN / VR)
            if line.startswith(("FN ", "VR ")):
                continue

            # Detect field code: exactly 2 upper-case chars + space at position 0-2
            if len(line) >= 3 and line[2] == " " and line[:2].isupper():
                field_code = line[:2]
                value = line[3:].strip()
                current_field = field_code
                if field_code not in current:
                    current[field_code] = []
                if value:
                    current[field_code].append(value)
            elif current_field and line.startswith("   "):
                # Continuation of previous field (indented)
                value = line.strip()
                if value:
                    current.setdefault(current_field, []).append(value)

    # Flush any trailing record (no ER at end)
    if current:
        records.append(_finalise(current))

    return records


def _finalise(raw: dict[str, list[str]]) -> dict:
    """Convert raw field lists into a flat record dict with canonical columns."""
    rec: dict = {"source": "wos"}

    # source_id: strip leading "WOS:" prefix if present
    source_id_parts = raw.get("UT", [])
    source_id = " ".join(source_id_parts).strip()
    if source_id.upper().startswith("WOS:"):
        source_id = source_id[4:]
    rec["source_id"] = source_id

    # Authors: join semicolon-separated list
    rec["authors"] = "; ".join(raw.get("AU", [])).strip()

    # Year: first value
    year_parts = raw.get("PY", [])
    rec["year"] = year_parts[0].strip() if year_parts else ""

    # Title: join continuation lines with space
    rec["title"] = " ".join(raw.get("TI", [])).strip()

    # Journal
    rec["journal"] = " ".join(raw.get("SO", [])).strip()

    # DOI: normalise to lowercase, strip "https://doi.org/" prefix
    doi_parts = raw.get("DI", [])
    doi = " ".join(doi_parts).strip().lower()
    doi = re.sub(r"^https?://doi\.org/", "", doi)
    rec["doi"] = doi

    # Abstract: join continuation lines with space
    rec["abstract"] = " ".join(raw.get("AB", [])).strip()

    return rec


def write_csv(records: list[dict], output_path: Path) -> None:
    columns = ["source", "source_id", "authors", "year", "title", "journal", "doi", "abstract"]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse WoS Full Record export to CSV.")
    parser.add_argument("--input", required=True, help="WoS export .txt file")
    parser.add_argument(
        "--output",
        default="",
        help="Output CSV path (default: results/wos_parsed_YYYYMMDD.csv)",
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
        output_path = Path(__file__).parent / "results" / f"wos_parsed_{datestamp}.csv"

    records = parse_wos_file(input_path)

    # Report
    n_journal = sum(1 for r in records if r.get("source_id"))
    n_no_doi = sum(1 for r in records if not r.get("doi"))
    print(f"Parsed {len(records)} records from {input_path.name}")
    print(f"  With source_id : {n_journal}")
    print(f"  Missing DOI    : {n_no_doi}")

    write_csv(records, output_path)
    print(f"Output written   : {output_path}")


if __name__ == "__main__":
    main()
