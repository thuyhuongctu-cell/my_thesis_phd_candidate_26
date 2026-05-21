#!/usr/bin/env python3
"""
45_export_extraction_queue.py — Export prioritized extraction queue for 538 Y papers

Creates a work-ready CSV showing all Y papers with:
  - What's already filled (icrv, dpl, fp_type)
  - What still needs filling (converted_r, sample_size_n, icrv if blank)
  - Direct links (doi_link, google_scholar, source_url_or_pdf_path)
  - PDF status and auto-extract flag

Sort order: (1) has PDF local, (2) has repo URL, (3) icrv filled, (4) priority_rank

Usage:
  python3 p6/tools/45_export_extraction_queue.py
  python3 p6/tools/45_export_extraction_queue.py --output p6/tools/results/my_batch.csv
  python3 p6/tools/45_export_extraction_queue.py --icrv 1,2   # filter by ICRV
  python3 p6/tools/45_export_extraction_queue.py --no-pdf-only  # only papers without PDFs
"""
import csv, argparse
from pathlib import Path
from datetime import date

DEFAULT_TRACKER = "p6/tools/results/fulltext_to_extraction_tracker_v3.csv"
DEFAULT_OUTPUT  = f"p6/tools/results/extraction_queue_y_{date.today().strftime('%Y%m%d')}.csv"

OUT_COLS = [
    "priority_rank", "seq", "year", "journal", "title",
    "doi", "doi_link", "google_scholar",
    "icrv", "dpl", "fp_type", "country_guess",
    "pdf_status", "source_url_or_pdf_path", "pdf_filename",
    "extraction_note",
    # fields to fill
    "sample_size_n", "converted_r", "conversion_formula",
    "reported_coefficient", "t_value", "p_value",
    "effect_direction", "model_type", "study_period_start", "study_period_end",
    "notes_for_extractor", "ready_for_r",
]


def pdf_status(row: dict) -> str:
    found = row.get("pdf_found", "").strip()
    if found == "Y":
        return "LOCAL_PDF"
    if found == "URL":
        return "REPO_URL"
    if row.get("source_url_or_pdf_path", "").strip():
        return "HAS_URL"
    return "NO_PDF"


def extraction_note(row: dict) -> str:
    notes = []
    if not row.get("converted_r", "").strip():
        notes.append("NEED_R")
    if not row.get("sample_size_n", "").strip():
        notes.append("NEED_N")
    if not row.get("icrv", "").strip():
        notes.append("NEED_ICRV")
    if not row.get("fp_type", "").strip():
        notes.append("NEED_FP")
    status = pdf_status(row)
    if status == "LOCAL_PDF":
        notes.append("AUTO_EXTRACT_READY")
    elif status == "NO_PDF":
        notes.append("FIND_PDF_FIRST")
    return " | ".join(notes)


def sort_key(row: dict) -> tuple:
    status = pdf_status(row)
    pdf_order = {"LOCAL_PDF": 0, "REPO_URL": 1, "HAS_URL": 2, "NO_PDF": 3}[status]
    icrv_order = 0 if row.get("icrv", "").strip() else 1
    try:
        rank = int(row.get("priority_rank", "9999") or "9999")
    except:
        rank = 9999
    return (pdf_order, icrv_order, rank)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tracker",      default=DEFAULT_TRACKER)
    parser.add_argument("--output",       default=DEFAULT_OUTPUT)
    parser.add_argument("--icrv",         default="",  help="Comma-separated ICRV codes to include (e.g. 1,2,3)")
    parser.add_argument("--no-pdf-only",  action="store_true", help="Export only papers without PDFs")
    parser.add_argument("--limit",        type=int, default=0, help="Max rows to export (0=all)")
    args = parser.parse_args()

    with open(args.tracker, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # Filter to Y papers only
    y_rows = [r for r in rows if r.get("fulltext_screening_decision", "") == "Y"]
    print(f"Y papers total: {len(y_rows)}", flush=True)

    # Apply filters
    if args.icrv:
        keep = set(args.icrv.split(","))
        y_rows = [r for r in y_rows if r.get("icrv", "").strip() in keep]
        print(f"  After ICRV filter ({args.icrv}): {len(y_rows)}", flush=True)

    if args.no_pdf_only:
        y_rows = [r for r in y_rows if pdf_status(r) == "NO_PDF"]
        print(f"  After no-PDF filter: {len(y_rows)}", flush=True)

    # Sort
    y_rows.sort(key=sort_key)

    if args.limit:
        y_rows = y_rows[:args.limit]

    # Build output rows
    out_rows = []
    for row in y_rows:
        out = {}
        for col in OUT_COLS:
            out[col] = row.get(col, "")
        out["pdf_status"] = pdf_status(row)
        out["extraction_note"] = extraction_note(row)
        out_rows.append(out)

    # Write
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS)
        w.writeheader()
        w.writerows(out_rows)

    # Summary
    statuses = {}
    for r in out_rows:
        s = r["pdf_status"]
        statuses[s] = statuses.get(s, 0) + 1

    need_r = sum(1 for r in out_rows if "NEED_R" in r["extraction_note"])
    need_icrv = sum(1 for r in out_rows if "NEED_ICRV" in r["extraction_note"])

    print(f"\n=== EXTRACTION QUEUE EXPORT ===")
    print(f"Exported:          {len(out_rows)} papers")
    print(f"  LOCAL_PDF:       {statuses.get('LOCAL_PDF', 0)}")
    print(f"  REPO_URL:        {statuses.get('REPO_URL', 0)}")
    print(f"  HAS_URL:         {statuses.get('HAS_URL', 0)}")
    print(f"  NO_PDF:          {statuses.get('NO_PDF', 0)}")
    print(f"Need converted_r:  {need_r}")
    print(f"Need ICRV code:    {need_icrv}")
    print(f"\nOutput: {args.output}")
    print(f"\nWORKFLOW:")
    print(f"  1. Open {args.output} in Excel/Google Sheets")
    print(f"  2. Start with LOCAL_PDF rows — run 41_auto_extract_from_pdfs.py first")
    print(f"  3. Fill: converted_r, sample_size_n, icrv (if blank)")
    print(f"  4. Set ready_for_r=1 after verifying each row")
    print(f"  5. When ≥50 rows have ready_for_r=1: run 42_merge_tracker_to_database.py")


if __name__ == "__main__":
    main()
