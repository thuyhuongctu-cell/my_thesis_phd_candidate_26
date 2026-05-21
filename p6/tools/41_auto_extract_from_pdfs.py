#!/usr/bin/env python3
"""
41_auto_extract_from_pdfs.py — Batch PDF extraction → pre-fill tracker
Run LOCALLY after downloading PDFs with 40_batch_download_pdfs.py.

Requires: pip install pdfplumber

For each PDF in p6/pdfs/:
  1. Matches to tracker row via seq number in filename
  2. Extracts: sample N, I→P coefficient, t-stat, p-value, conversion
  3. Computes converted_r
  4. Writes pre-filled values back to fulltext_to_extraction_tracker_v3.csv
     (only rows where converted_r is still empty — never overwrites manual work)

Output:
  - Updated tracker CSV
  - p6/tools/results/auto_extract_log_YYYYMMDD.csv  (extraction audit trail)
"""
import csv, re, math, sys, argparse
from pathlib import Path
from datetime import date

try:
    import pdfplumber
except ImportError:
    print("ERROR: pip install pdfplumber")
    sys.exit(1)

DEFAULT_PDF_DIR  = "p6/pdfs"
DEFAULT_TRACKER  = "p6/tools/results/fulltext_to_extraction_tracker_v3.csv"
DEFAULT_LOG      = f"p6/tools/results/auto_extract_log_{date.today().strftime('%Y%m%d')}.csv"

# ─── Internationalization variable keywords ───────────────────────────────────
# NOTE: "doi" removed — causes false positives on DOI strings in headers/references
I_KEYWORDS = [
    "fsts", "foreign sales", "export intensity", "export ratio",
    "internationalization", "internationalisation", "degree of int",
    "multinationality", "foreign revenue", "overseas sales",
    "export sales", "geographic diversif", "entropy", "n_countries",
    "number of countries", "foreign subsid",
]

# ─── Performance variable keywords ───────────────────────────────────────────
P_KEYWORDS = [
    "roa", "return on asset", "roe", "return on equity",
    "ros", "return on sales", "tobin", "profit margin",
    "sales growth", "revenue growth", "productivity", "performance",
    "financial performance", "firm performance",
]


def r_from_t(t: float, df: float) -> float:
    return t / math.sqrt(t**2 + df)


def r_from_beta(beta: float) -> float:
    return beta   # approximation when SD info unavailable


def extract_text(pdf_path: Path) -> str:
    try:
        with pdfplumber.open(pdf_path) as pdf:
            pages = []
            for p in pdf.pages:
                text = p.extract_text()
                if text:
                    pages.append(text)
        return "\n".join(pages)
    except Exception as e:
        return ""


def find_sample_size(text: str) -> int | None:
    patterns = [
        r'[Nn]\s*[=:]\s*(\d{1,3}(?:,\d{3})*|\d{2,6})',
        r'(\d{2,6})\s+(?:firm|compan|observ|enterprise)',
        r'sample\s+(?:of\s+)?(\d{2,6})',
        r'(\d{2,6})\s+(?:unique\s+)?(?:firm|observ)',
    ]
    sizes = []
    for pat in patterns:
        for m in re.finditer(pat, text, re.IGNORECASE):
            try:
                n = int(m.group(1).replace(',', ''))
                if 30 <= n <= 500_000:
                    sizes.append(n)
            except:
                pass
    if not sizes:
        return None
    # Modal value (most frequently mentioned)
    from collections import Counter
    return Counter(sizes).most_common(1)[0][0]


def find_ip_coefficient(text: str) -> dict | None:
    """
    Find the I→P main effect: look for lines containing both an I-keyword
    and a numeric coefficient (β or t-stat or p-value).
    Returns best candidate or None.
    """
    lines = text.split('\n')
    candidates = []

    for i, line in enumerate(lines):
        line_lower = line.lower()

        # Must contain an I-keyword
        if not any(kw in line_lower for kw in I_KEYWORDS):
            continue

        # Extract numeric values from the line and ±2 surrounding lines
        context = '\n'.join(lines[max(0,i-2):i+3])

        # t-statistic
        t_match = re.search(r'\bt\s*[=\(]\s*(-?\d+\.\d+)', context)
        # beta
        b_match = re.search(r'β\s*=?\s*(-?0?\.\d{2,4})|[Bb]eta\s*=\s*(-?0?\.\d{2,4})', context)
        # p-value
        p_match = re.search(r'p\s*[=<]\s*(0?\.\d{2,4})', context, re.IGNORECASE)
        # r value
        r_match = re.search(r'\br\s*=\s*(-?0?\.\d{2,4})', context)

        # Require at least one numeric stat
        if not any([t_match, b_match, p_match, r_match]):
            continue

        entry = {
            "line": line.strip()[:100],
            "t": float(t_match.group(1)) if t_match else None,
            "beta": float((b_match.group(1) or b_match.group(2))) if b_match else None,
            "p": float(p_match.group(1)) if p_match else None,
            "r": float(r_match.group(1)) if r_match else None,
        }
        candidates.append(entry)

    if not candidates:
        return None

    # Prefer candidates that have a t-stat (most reliable conversion)
    with_t = [c for c in candidates if c["t"] is not None]
    if with_t:
        return with_t[0]
    return candidates[0]


def compute_r(cand: dict, n: int | None) -> tuple[float | None, str]:
    """Returns (converted_r, formula)"""
    if cand.get("r") is not None:
        return round(cand["r"], 4), "direct"

    if cand.get("t") is not None and n is not None:
        df = n - 2
        if df > 0:
            return round(r_from_t(cand["t"], df), 4), "t_to_r"

    if cand.get("beta") is not None:
        return round(r_from_beta(cand["beta"]), 4), "beta"

    return None, ""


def effect_direction(r: float | None, beta: float | None, t: float | None) -> str:
    v = r if r is not None else (beta if beta is not None else t)
    if v is None:
        return ""
    return "+" if v >= 0 else "-"


def seq_from_filename(name: str) -> str | None:
    m = re.match(r'^(\d+)_', name)
    return m.group(1) if m else None


def process_pdf(pdf_path: Path) -> dict:
    seq = seq_from_filename(pdf_path.name)
    result = {
        "seq": seq or "", "pdf": pdf_path.name,
        "sample_size_n": "", "converted_r": "", "conversion_formula": "",
        "effect_direction": "", "t_value": "", "p_value": "",
        "table_or_page": "", "notes": "", "status": ""
    }

    text = extract_text(pdf_path)
    if not text.strip():
        result["status"] = "NO_TEXT"
        return result

    n = find_sample_size(text)
    cand = find_ip_coefficient(text)

    if n:
        result["sample_size_n"] = str(n)

    if cand:
        r, formula = compute_r(cand, n)
        result["converted_r"]       = str(r) if r is not None else ""
        result["conversion_formula"] = formula
        result["effect_direction"]  = effect_direction(r, cand.get("beta"), cand.get("t"))
        result["t_value"]           = str(cand["t"]) if cand.get("t") else ""
        result["p_value"]           = str(cand["p"]) if cand.get("p") else ""
        result["notes"]             = f"AUTO: {cand['line'][:80]}"
        result["status"]            = "EXTRACTED" if r else "PARTIAL"
    else:
        result["status"] = "NO_IP_COEFF_FOUND"

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-dir",  default=DEFAULT_PDF_DIR)
    parser.add_argument("--tracker",  default=DEFAULT_TRACKER)
    parser.add_argument("--log",      default=DEFAULT_LOG)
    parser.add_argument("--dry-run",  action="store_true",
                        help="Show what would be written without modifying tracker")
    args = parser.parse_args()

    pdf_dir = Path(args.pdf_dir)
    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs found in {pdf_dir} — run 40_batch_download_pdfs.py first.")
        return

    print(f"Processing {len(pdfs)} PDFs from {pdf_dir}...", flush=True)

    # Load tracker
    with open(args.tracker, newline="", encoding="utf-8") as f:
        tracker_rows = list(csv.DictReader(f))
    fieldnames = list(tracker_rows[0].keys())
    seq_to_row = {r["seq"]: r for r in tracker_rows}

    extractions = []
    updated = 0
    skipped_manual = 0
    no_seq = 0

    for i, pdf_path in enumerate(pdfs, 1):
        ex = process_pdf(pdf_path)
        extractions.append(ex)

        seq = ex["seq"]
        if not seq or seq not in seq_to_row:
            no_seq += 1
            continue

        row = seq_to_row[seq]

        # Never overwrite manually filled data
        if row.get("converted_r", "").strip():
            skipped_manual += 1
            ex["status"] = "SKIP_MANUAL_FILLED"
            continue

        if not args.dry_run and ex["converted_r"]:
            row["converted_r"]        = ex["converted_r"]
            row["conversion_formula"] = ex["conversion_formula"]
            row["effect_direction"]   = ex["effect_direction"]
            row["t_value"]            = ex["t_value"]
            row["p_value"]            = ex["p_value"]
            if ex["sample_size_n"] and not row.get("sample_size_n", "").strip():
                row["sample_size_n"]  = ex["sample_size_n"]
            # Append to notes rather than overwrite
            existing_notes = row.get("notes_for_extractor", "")
            row["notes_for_extractor"] = (existing_notes + " | " + ex["notes"]).strip(" |")
            updated += 1

        if i % 20 == 0:
            print(f"  {i}/{len(pdfs)} | extracted={updated} skip_manual={skipped_manual}",
                  flush=True)

    # Write updated tracker
    if not args.dry_run:
        with open(args.tracker, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(tracker_rows)

    # Write extraction log
    log_cols = ["seq", "pdf", "sample_size_n", "converted_r", "conversion_formula",
                "effect_direction", "t_value", "p_value", "notes", "status"]
    Path(args.log).parent.mkdir(parents=True, exist_ok=True)
    with open(args.log, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=log_cols)
        w.writeheader()
        w.writerows(extractions)

    print(f"\n=== AUTO-EXTRACTION SUMMARY ===")
    print(f"PDFs processed:    {len(pdfs)}")
    print(f"r extracted:       {updated}" + (" (DRY RUN — tracker NOT modified)" if args.dry_run else ""))
    print(f"Skipped (manual):  {skipped_manual}")
    print(f"No seq match:      {no_seq}")
    no_coeff = sum(1 for e in extractions if e["status"] == "NO_IP_COEFF_FOUND")
    no_text  = sum(1 for e in extractions if e["status"] == "NO_TEXT")
    print(f"No I→P coeff:      {no_coeff}")
    print(f"No text (scan):    {no_text}")
    print(f"Log:               {args.log}")
    if not args.dry_run and updated:
        print(f"Tracker updated:   {args.tracker}")
        print("\nNEXT: Verify AUTO extractions manually (check 'AUTO:' in notes_for_extractor)")
        print("      Set ready_for_r=1 only after human verification")


if __name__ == "__main__":
    main()
