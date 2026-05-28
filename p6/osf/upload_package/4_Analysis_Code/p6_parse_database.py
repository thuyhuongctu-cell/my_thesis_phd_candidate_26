#!/usr/bin/env python3
"""
Parse p6_study_database_coded.md → p6/data/p6_study_database.csv

Extraction script for three-level MARA with metafor R.
Follows the meta-analysis-extraction-workflow pattern:
  python p6_parse_database.py --input ../p6_study_database_coded.md
                               --output ../data/p6_study_database.csv

Output columns (metafor-compatible):
  study_id, effect_id, author, year, r, n, country,
  sample_start, sample_end, icrv, cdai, dpl,
  doi_type, fp_type, include_flag, is_estimated, notes
"""

import re
import csv
import sys
import argparse
from pathlib import Path


# ── Unicode normalisation ────────────────────────────────────────────────────

def _norm(s: str) -> str:
    """Replace Unicode minus (U+2212) and en/em dash with ASCII hyphen."""
    return (
        s.replace("−", "-")
         .replace("–", "-")
         .replace("—", "-")
    )


# ── Effect-size / n parsing ──────────────────────────────────────────────────

def parse_r_values(r_str: str):
    """
    Parse r column → (list[float], is_estimated: bool).

    Handles:
      • Single:              "0.15"  / "−0.197"
      • Slash-separated:     "0.145/0.163/0.107/−0.036"
      • 'to' range:          "−0.02 to 0.03"   → midpoint
      • Dash range:          "0.037–0.85"       → midpoint
      • '+' prefix or est:   "+0.07 (est.)"
    """
    s = _norm(r_str.strip())
    is_est = bool(re.search(r"\(est\.?\)", s, re.IGNORECASE))
    s = re.sub(r"\(est\.?\)", "", s, flags=re.IGNORECASE).strip()
    s = s.replace("+", "")

    # Slash-separated
    if "/" in s:
        parts = [p.strip() for p in s.split("/") if p.strip()]
        return [float(p) for p in parts], is_est

    # Explicit " to " range
    if " to " in s:
        lo_s, hi_s = s.split(" to ", 1)
        lo, hi = float(lo_s.strip()), float(hi_s.strip())
        return [(lo + hi) / 2], is_est

    # Dash range: "0.037-0.85" or "−0.065-−0.22"
    # Requires both sides to have at least one digit after any leading minus
    range_m = re.fullmatch(r"(-?\d+\.?\d*)-(\d+\.?\d*)", s)
    if range_m:
        lo, hi = float(range_m.group(1)), float(range_m.group(2))
        return [(lo + hi) / 2], is_est

    # Single value
    return [float(s)], is_est


def parse_n_values(n_str: str, num_effects: int) -> list:
    """
    Parse n column → list[int] of length num_effects.

    • Slash-separated, same count as effects → use each value.
    • Slash-separated, different count → use integer average for all.
    • Dash range "47-81" → midpoint for all.
    • Single or "~1,200" → same value for all.
    """
    s = _norm(str(n_str).strip()).lstrip("~").replace(",", "").replace(" ", "")

    if "/" in s:
        parts = [int(p) for p in s.split("/") if p.strip()]
        if len(parts) == num_effects:
            return parts
        avg = sum(parts) // len(parts)
        return [avg] * num_effects

    range_m = re.fullmatch(r"(\d+)-(\d+)", s)
    if range_m:
        lo, hi = int(range_m.group(1)), int(range_m.group(2))
        return [(lo + hi) // 2] * num_effects

    return [int(s)] * num_effects


# ── Period parsing ───────────────────────────────────────────────────────────

def parse_period(period_str: str):
    """
    Parse "~1978-81", "2003-17", "~2014-22", "1992-17" etc.
    Returns (start_year: int, end_year: int) or (None, None).
    2-digit suffix rule: if end_year < start_year, add 100 (cross-century).
    """
    s = _norm(period_str.strip()).lstrip("~")
    m = re.fullmatch(r"(\d{4})-(\d{2,4})", s)
    if m:
        start = int(m.group(1))
        suffix = m.group(2)
        if len(suffix) == 4:
            end = int(suffix)
        else:
            century = (start // 100) * 100
            end = century + int(suffix)
            if end < start:
                end += 100
        return start, end
    single = re.fullmatch(r"(\d{4})", s)
    if single:
        y = int(single.group(1))
        return y, y
    return None, None


# ── Author / year parsing ────────────────────────────────────────────────────

def parse_author_year(ay_str: str):
    """Parse 'Author (YYYY) **TAG**' → (author: str, year: int)."""
    s = re.sub(r"\*+\w+\*+", "", ay_str)   # strip **NEW**, **AUTHOR** etc.
    s = re.sub(r"[†*]", "", s).strip()
    m = re.match(r"^(.*?)\s*\((\d{4})\)", s)
    if m:
        return m.group(1).strip(), int(m.group(2))
    return s, None


# ── ICRV normalisation ───────────────────────────────────────────────────────

_ICRV_MAP = {
    "I": "I", "II": "II", "III": "III",
    "FR": "FR", "FRONTIER": "FR",
    "MX": "MX", "SIDS": "SIDS",
}

def norm_icrv(s: str) -> str:
    return _ICRV_MAP.get(s.strip().upper(), s.strip())


# ── Markdown table helpers ───────────────────────────────────────────────────

def is_data_header(line: str) -> bool:
    return "| ID |" in line and "Author-Year" in line and "ICRV" in line

def is_separator(line: str) -> bool:
    return bool(re.match(r"^\|[-| :]+\|$", line.strip()))

def split_row(line: str):
    """Split '| a | b | c |' → ['a', 'b', 'c']."""
    parts = line.strip().split("|")
    return [p.strip() for p in parts[1:-1]]


# ── Main ─────────────────────────────────────────────────────────────────────

def parse(db_path: Path) -> list:
    text = db_path.read_text(encoding="utf-8")
    records = []
    in_table = False

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if is_data_header(line):
            in_table = True
            continue

        if is_separator(line):
            continue

        if not line.startswith("|"):
            if in_table:
                in_table = False
            continue

        if not in_table:
            continue

        cells = split_row(line)
        if len(cells) < 11:
            continue

        sid_raw   = cells[0]
        ay_raw    = cells[1]
        r_raw     = cells[2]
        n_raw     = cells[3]
        country   = cells[4]
        period    = cells[5]
        icrv_raw  = cells[6]
        cdai_raw  = cells[7]
        dpl_raw   = cells[8]
        doi_type  = cells[9]
        fp_type   = cells[10]
        notes_raw = cells[11] if len(cells) > 11 else ""

        # Validate study ID (must start with S + digits)
        sid = sid_raw.split()[0]
        if not re.match(r"^S\d+$", sid):
            continue

        author, year = parse_author_year(ay_raw)

        try:
            r_vals, is_est = parse_r_values(r_raw)
        except (ValueError, TypeError) as exc:
            print(f"WARN [{sid}] r='{r_raw}': {exc}", file=sys.stderr)
            continue

        k = len(r_vals)

        try:
            n_vals = parse_n_values(n_raw, k)
        except (ValueError, TypeError) as exc:
            print(f"WARN [{sid}] n='{n_raw}': {exc}", file=sys.stderr)
            n_vals = [None] * k

        sample_start, sample_end = parse_period(period)

        icrv  = norm_icrv(icrv_raw)
        cdai  = cdai_raw.strip().upper()
        if cdai not in ("H", "M", "L"):
            cdai = "L"
        dpl = dpl_raw.strip().upper()
        if dpl not in ("PRE", "SPN", "FOL"):
            dpl = "SPN"

        doi_type = doi_type.strip()
        fp_type  = fp_type.strip()
        notes    = re.sub(r"[†*]", "", notes_raw).strip()

        for i, (r_val, n_val) in enumerate(zip(r_vals, n_vals)):
            effect_id = f"{sid}_e{i + 1}" if k > 1 else sid
            include   = 0 if (n_val is not None and n_val < 15) else 1
            records.append({
                "study_id":     sid,
                "effect_id":    effect_id,
                "author":       author,
                "year":         year,
                "r":            round(r_val, 6),
                "n":            n_val,
                "country":      country,
                "sample_start": sample_start,
                "sample_end":   sample_end,
                "icrv":         icrv,
                "cdai":         cdai,
                "dpl":          dpl,
                "doi_type":     doi_type,
                "fp_type":      fp_type,
                "include_flag": include,
                "is_estimated": int(is_est),
                "notes":        notes,
            })

    return records


def write_csv(records: list, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "study_id", "effect_id", "author", "year",
        "r", "n", "country", "sample_start", "sample_end",
        "icrv", "cdai", "dpl", "doi_type", "fp_type",
        "include_flag", "is_estimated", "notes",
    ]
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(records)


def main():
    ap = argparse.ArgumentParser(description="Parse P6 study database → CSV")
    ap.add_argument("--input",  default=None, help="Path to p6_study_database_coded.md")
    ap.add_argument("--output", default=None, help="Path for output CSV")
    args = ap.parse_args()

    here   = Path(__file__).parent
    db     = Path(args.input)  if args.input  else here.parent / "p6_study_database_coded.md"
    out    = Path(args.output) if args.output else here.parent / "data" / "p6_study_database.csv"

    if not db.exists():
        sys.exit(f"ERROR: Database not found: {db}")

    records = parse(db)
    write_csv(records, out)

    studies = len({r["study_id"] for r in records})
    effects = len(records)
    incl    = sum(1 for r in records if r["include_flag"] == 1)
    est     = sum(1 for r in records if r["is_estimated"] == 1)

    print(f"Parsed  : {studies} studies  →  {effects} effect rows")
    print(f"Included: {incl}/{effects}  (excluded: n < 15)")
    print(f"Estimated r: {est} rows flagged (is_estimated=1)")
    print(f"Output  : {out}")

    # Quick distribution check
    from collections import Counter
    icrv_dist = Counter(r["icrv"] for r in records if r["include_flag"] == 1)
    dpl_dist  = Counter(r["dpl"]  for r in records if r["include_flag"] == 1)
    cdai_dist = Counter(r["cdai"] for r in records if r["include_flag"] == 1)
    print(f"\nICRV distribution : {dict(sorted(icrv_dist.items()))}")
    print(f"DPL  distribution : {dict(sorted(dpl_dist.items()))}")
    print(f"cDAI distribution : {dict(sorted(cdai_dist.items()))}")


if __name__ == "__main__":
    main()
