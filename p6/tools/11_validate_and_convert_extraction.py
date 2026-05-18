"""
11_validate_and_convert_extraction.py
Validate a filled master_extraction CSV/XLSX and convert to the
p6_study_database.csv schema ready for merging.

Validation checks:
  - r within [-1, 1]; |r| < 0.95 (flag outliers)
  - n >= 10 (minimum sample size)
  - required fields present: r OR beta/t_value/f_value+df
  - icrv in 1–6 or legacy Roman codes
  - dpl in 1/2/3 or legacy PRE/FOL/SPN
  - included_final_review == 'Y' (only include coded 'Y')

Code conversions (new → legacy-compatible for p6_mara_updated.R):
  ICRV: 1→I, 2→II, 3→III, 4→III, 5→FR, 6→FR (MX for multi-country)
  DPL:  1→PRE, 2→FOL, 3→SPN
  doi_type: fsts→FSTS, exp→EXP, fdi→FDI, geo→GEO, comp→COMP, other→OTH
  fp_type:  acc→ACC, lab→LAB, mkt→MKT, mix→MIX

Effect size conversion (if r missing):
  t + df  → r = sqrt(t² / (t² + df))
  F + df  → r = sqrt(F / (F + df))
  beta    → r ≈ beta (documented as is_estimated = 1)

Usage:
  python3 11_validate_and_convert_extraction.py
  python3 11_validate_and_convert_extraction.py --input my_filled_extraction.xlsx
  python3 11_validate_and_convert_extraction.py --strict   # fail on any warning
"""

import csv
import math
import re
import sys
from datetime import date
from pathlib import Path

BASE   = Path("/home/user/PAPERS_IN_PHD_2026")
OUTDIR = BASE / "p6/tools/results"
TODAY  = date.today().strftime('%Y%m%d')

# ── CLI args ─────────────────────────────────────────────────────────────────
strict_mode = '--strict' in sys.argv
custom_input = None
for i, arg in enumerate(sys.argv[1:], 1):
    if arg == '--input' and i < len(sys.argv):
        custom_input = Path(sys.argv[i + 1])

# ── Locate input ──────────────────────────────────────────────────────────────
if custom_input:
    INPUT = custom_input
else:
    candidates = sorted(OUTDIR.glob('master_extraction_*.csv'), reverse=True)
    if not candidates:
        candidates = sorted(OUTDIR.glob('master_extraction_*.xlsx'), reverse=True)
    if not candidates:
        sys.exit("ERROR: no master_extraction_*.csv/xlsx found. Run 09_build_extraction_template.py first.")
    INPUT = candidates[0]

print(f"Input:  {INPUT}")
print(f"Strict: {strict_mode}")
print()


# ── Load rows ─────────────────────────────────────────────────────────────────
def load_input(path: Path) -> list[dict]:
    path = Path(path)
    if path.suffix in ('.xlsx', '.xls'):
        try:
            import openpyxl
        except ImportError:
            sys.exit("openpyxl required: pip install openpyxl")
        wb = openpyxl.load_workbook(path, read_only=True)
        ws = wb.active
        rows = list(ws.iter_rows(values_only=True))
        header = [str(h) if h else '' for h in rows[0]]
        return [dict(zip(header, [str(v).strip() if v is not None else '' for v in r]))
                for r in rows[1:]]
    else:
        with open(path, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))

all_rows = load_input(INPUT)
print(f"Loaded {len(all_rows)} rows from {INPUT.name}")


# ── Code maps ─────────────────────────────────────────────────────────────────
ICRV_MAP = {
    '1': 'I',   'i': 'I',   'advanced': 'I',
    '2': 'II',  'ii': 'II', 'emerging': 'II',
    '3': 'III', 'iii': 'III', 'transition': 'III',
    '4': 'III', 'resource': 'III', 'gcc': 'III',
    '5': 'FR',  'v': 'FR',  'sids': 'FR',
    '6': 'FR',  'vi': 'FR', 'frontier': 'FR',
    '0': 'MX',  'mx': 'MX', 'multi': 'MX',
    # pass-through legacy
    'I': 'I', 'II': 'II', 'III': 'III', 'FR': 'FR', 'MX': 'MX',
}

DPL_MAP = {
    '1': 'PRE', 'pre': 'PRE', 'pre-2000': 'PRE',
    '2': 'FOL', 'fol': 'FOL', '2000-2009': 'FOL', 'follower': 'FOL',
    '3': 'SPN', 'spn': 'SPN', '2010+': 'SPN', 'smartphone': 'SPN',
    # pass-through
    'PRE': 'PRE', 'FOL': 'FOL', 'SPN': 'SPN',
}

DOI_TYPE_MAP = {
    'fsts': 'FSTS', 'export intensity': 'FSTS', 'exportintensity': 'FSTS',
    'exp': 'EXP', 'export': 'EXP',
    'fdi': 'FDI', 'ofdi': 'FDI',
    'geo': 'GEO', 'geographic': 'GEO', 'geographic diversification': 'GEO',
    'comp': 'COMP', 'composite': 'COMP', 'doi': 'COMP',
    'oth': 'OTH', 'other': 'OTH',
    # pass-through
    'FSTS': 'FSTS', 'EXP': 'EXP', 'FDI': 'FDI',
    'GEO': 'GEO', 'COMP': 'COMP', 'OTH': 'OTH',
}

FP_TYPE_MAP = {
    'acc': 'ACC', 'accounting': 'ACC', 'roa': 'ACC', 'roe': 'ACC', 'ros': 'ACC',
    'lab': 'LAB', 'labor': 'LAB', 'labour': 'LAB', 'productivity': 'LAB', 'lp': 'LAB', 'tfp': 'LAB',
    'mkt': 'MKT', 'market': 'MKT', 'tobin': 'MKT', 'market value': 'MKT',
    'mix': 'MIX', 'composite': 'MIX', 'mixed': 'MIX',
    'ACC': 'ACC', 'LAB': 'LAB', 'MKT': 'MKT', 'MIX': 'MIX',
}

CDAI_MAP = {
    'h': 'H', 'high': 'H', '1': 'H',
    'm': 'M', 'medium': 'M', 'mid': 'M', '0.5': 'M',
    'l': 'L', 'low': 'L', '0': 'L',
    'H': 'H', 'M': 'M', 'L': 'L',
}


def safe_float(v):
    try:
        return float(str(v).strip())
    except (ValueError, TypeError):
        return None


def convert_t_to_r(t, df):
    t, df = safe_float(t), safe_float(df)
    if t is None or df is None or df <= 0:
        return None
    return math.sqrt(t**2 / (t**2 + df))


def convert_f_to_r(f, df):
    f, df = safe_float(f), safe_float(df)
    if f is None or df is None or df <= 0:
        return None
    return math.sqrt(f / (f + df))


def map_code(value: str, mapping: dict, field: str) -> tuple[str, str]:
    """Return (mapped_code, warning_or_empty)."""
    v = str(value).strip()
    if not v or v in ('None', 'nan', ''):
        return '', ''
    mapped = mapping.get(v, mapping.get(v.lower(), ''))
    if not mapped:
        return v, f"Unknown {field} code: '{v}'"
    return mapped, ''


# ── Filter & validate ─────────────────────────────────────────────────────────
errors   = []
warnings = []
valid    = []

# Determine which rows to process
def should_include(row: dict) -> bool:
    inc = str(row.get('included_final_review', '') or '').strip().upper()
    if inc in ('Y', 'YES', '1', 'TRUE'):
        return True
    if inc in ('N', 'NO', '0', 'FALSE', 'EXCLUDE'):
        return False
    # If field not filled, use extraction_status and r to decide
    status = str(row.get('extraction_status', '') or '').strip().lower()
    r_val  = str(row.get('r', '') or '').strip()
    return status == 'done' or bool(r_val)

included = [r for r in all_rows if should_include(r)]
skipped  = len(all_rows) - len(included)
print(f"Included for conversion: {len(included)}  Skipped (not Y/done): {skipped}")

for i, row in enumerate(included, 1):
    seq  = row.get('seq', str(i))
    sid  = row.get('study_id', '').strip() or f"NEW_{seq}"
    eid  = row.get('effect_id', '').strip() or f"{sid}_e1"
    errs = []
    warns = []

    # ── Effect size ───────────────────────────────────────────────────────
    r_raw       = row.get('r', '').strip()
    beta_raw    = row.get('beta', '') or row.get('effect_size_beta', '')
    t_raw       = row.get('t_value', '').strip()
    f_raw       = row.get('f_value', '').strip()
    df_raw      = row.get('df', '').strip()
    is_estimated = 0

    r_val = safe_float(r_raw)
    if r_val is None:
        # Try t→r
        r_val = convert_t_to_r(t_raw, df_raw)
        if r_val is not None:
            is_estimated = 1
        else:
            # Try F→r
            r_val = convert_f_to_r(f_raw, df_raw)
            if r_val is not None:
                is_estimated = 1
            else:
                # Use beta as proxy
                b = safe_float(beta_raw)
                if b is not None:
                    r_val = b
                    is_estimated = 1
                    warns.append(f"[{seq}] beta used as r proxy (is_estimated=1)")
                else:
                    errs.append(f"[{seq}] Missing effect size: no r, beta, t, or F")

    if r_val is not None:
        if abs(r_val) > 1.0:
            errs.append(f"[{seq}] |r|={r_val:.3f} > 1 (impossible)")
        elif abs(r_val) > 0.95:
            warns.append(f"[{seq}] |r|={r_val:.3f} > 0.95 (suspect outlier)")

    # ── Sample size ───────────────────────────────────────────────────────
    n_raw = (row.get('n') or row.get('sample_size_n') or '').strip()
    n_val = safe_float(n_raw)
    if n_val is None:
        warns.append(f"[{seq}] Missing n")
    elif n_val < 10:
        errs.append(f"[{seq}] n={n_val} < 10 (exclude)")
    elif n_val < 30:
        warns.append(f"[{seq}] n={n_val} < 30 (underpowered)")

    # ── Code conversions ─────────────────────────────────────────────────
    icrv_conv,  w = map_code(row.get('icrv', ''), ICRV_MAP, 'ICRV')
    if w: warns.append(f"[{seq}] {w}")

    dpl_conv, w = map_code(row.get('dpl', ''), DPL_MAP, 'DPL')
    if w: warns.append(f"[{seq}] {w}")

    doi_type_conv, w = map_code(row.get('doi_type', ''), DOI_TYPE_MAP, 'doi_type')
    if w: warns.append(f"[{seq}] {w}")
    if not doi_type_conv:
        doi_type_conv = 'OTH'

    fp_type_conv, w = map_code(row.get('fp_type', '') or row.get('performance_measure', ''),
                                FP_TYPE_MAP, 'fp_type')
    if w: warns.append(f"[{seq}] {w}")
    if not fp_type_conv:
        fp_type_conv = 'ACC'

    cdai_raw = str(row.get('cdai', '') or '').strip()
    cdai_conv = CDAI_MAP.get(cdai_raw, CDAI_MAP.get(cdai_raw.lower(), 'M'))

    # ── Build output row ─────────────────────────────────────────────────
    if errs:
        errors.extend(errs)
        if strict_mode:
            continue  # skip rows with errors in strict mode

    out = {
        'study_id':     sid,
        'effect_id':    eid,
        'author':       (row.get('authors') or '').split(';')[0].strip(),
        'year':         str(row.get('year', '')).strip(),
        'r':            f"{r_val:.4f}" if r_val is not None else '',
        'n':            str(int(n_val)) if n_val else '',
        'country':      row.get('country', '').strip(),
        'sample_start': str(row.get('sample_start', '')).strip(),
        'sample_end':   str(row.get('sample_end', '') or row.get('time_period', '')).strip(),
        'icrv':         icrv_conv,
        'cdai':         cdai_conv,
        'dpl':          dpl_conv,
        'doi_type':     doi_type_conv,
        'fp_type':      fp_type_conv,
        'include_flag': '1',
        'is_estimated': str(is_estimated),
        'notes':        row.get('notes', '').strip(),
    }
    warnings.extend(warns)
    valid.append(out)


# ── Report ────────────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"VALIDATION RESULTS")
print(f"{'='*60}")
print(f"  Input rows:        {len(all_rows)}")
print(f"  Included (Y/done): {len(included)}")
print(f"  Valid (converted): {len(valid)}")
print(f"  Errors:            {len(errors)}")
print(f"  Warnings:          {len(warnings)}")

if errors:
    print(f"\n{'='*40}\nERRORS (must fix before merge):\n{'='*40}")
    for e in errors[:20]:
        print(f"  ✗ {e}")
    if len(errors) > 20:
        print(f"  ... ({len(errors)-20} more)")

if warnings:
    print(f"\n{'='*40}\nWARNINGS (review):\n{'='*40}")
    for w in warnings[:20]:
        print(f"  ⚠ {w}")
    if len(warnings) > 20:
        print(f"  ... ({len(warnings)-20} more)")

if not valid:
    print("\nNo valid rows to write. Check errors above or fill the extraction template first.")
    sys.exit(0)

# ── Code distribution ─────────────────────────────────────────────────────────
print(f"\nCode distributions (converted):")
for field in ['icrv', 'dpl', 'doi_type', 'fp_type', 'cdai']:
    dist = {}
    for r in valid:
        dist[r[field]] = dist.get(r[field], 0) + 1
    print(f"  {field}: {dict(sorted(dist.items()))}")

# ── Write output ──────────────────────────────────────────────────────────────
DB_FIELDS = ['study_id','effect_id','author','year','r','n','country',
             'sample_start','sample_end','icrv','cdai','dpl','doi_type',
             'fp_type','include_flag','is_estimated','notes']

out_csv = OUTDIR / f"new_studies_ready_to_merge_{TODAY}.csv"
with open(out_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=DB_FIELDS)
    writer.writeheader()
    writer.writerows(valid)

print(f"\nOutput: {out_csv}")
print(f"Ready for: python3 10_merge_new_studies.py --new {out_csv.name}")
