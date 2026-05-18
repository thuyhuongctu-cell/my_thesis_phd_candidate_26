"""
05_l2_screen_titles.py
Title-based L2 screening for P6 meta-analysis candidates.
Input : l2_prescreened.csv (782 rows, prescreen_flag = Y/N/UNSURE)
Output: l2_screened_YYYYMMDD.csv  — include_flag filled for all rows

Criteria (title-only; no abstracts from WoS Starter API):
  INCLUDE (Y): firm-level I→P study, quantitative, financial/operational performance as DV
  EXCLUDE (N): qualitative/case-study, macro/country-level, no I→P relationship, non-business field
  UNSURE    : insufficient information from title alone → needs full-text
"""

import csv
import re
from datetime import date
from pathlib import Path

INPUT  = Path("/root/.claude/uploads/8dca9eb8-5333-42aa-a4e9-a67af768cec6/de8984aa-l2_prescreened.csv")
OUTDIR = Path("/home/user/PAPERS_IN_PHD_2026/p6/tools/results")
OUTDIR.mkdir(parents=True, exist_ok=True)
OUTPUT = OUTDIR / f"l2_screened_{date.today().strftime('%Y%m%d')}.csv"

# ── Signal dictionaries ──────────────────────────────────────────────────────

# Hard EXCLUDE — title alone is sufficient to exclude
EXCL_PATTERNS = [
    (r'\bcase stud(y|ies)\b',           'EXCL:qualitative-case-study'),
    (r'\bqualitative\b',                 'EXCL:qualitative'),
    (r'\bethnograph',                    'EXCL:qualitative-ethnographic'),
    (r'\bsystematic review\b',           'EXCL:review-only'),
    (r'\bmeta.analy',                    'EXCL:meta-analysis'),
    (r'\bbibliometric',                  'EXCL:bibliometric'),
    (r'\bliterature review\b',           'EXCL:review-only'),
    (r'\bconceptual (framework|model|paper)\b', 'EXCL:conceptual'),
    (r'\bcarbon emission',               'EXCL:env-DV'),
    (r'\bco2 emission',                  'EXCL:env-DV'),
    (r'\bgreenhous',                     'EXCL:env-DV'),
    (r'\benvironmental (pollution|degradation|footprint)\b', 'EXCL:env-DV'),
    (r'\bhealth (outcome|performance)\b','EXCL:non-business'),
    (r'\bmedical\b',                     'EXCL:non-business'),
    (r'\bhospital\b',                    'EXCL:non-business'),
    (r'\bcountry.level (analysis|study|evidence)\b', 'EXCL:macro'),
    (r'\bmacroeconomic\b',               'EXCL:macro'),
    (r'\bgdp growth\b',                  'EXCL:macro'),
    (r'\bnational competitiveness\b',    'EXCL:macro'),
    (r'\bhistoric(al)? (case|account)\b','EXCL:historical-narrative'),
    (r'\b(1946|1947|1948|1949|1950|1951|1952|1953|1954|1955|1956|1957|1958|1959|1960)[-–]', 'EXCL:historical-pre1970'),
    (r'\bdissertation\b',                'EXCL:dissertation'),
    (r'\bthesis\b',                      'EXCL:dissertation'),
]

# Strong INCLUDE signals — pair: (i_signal, p_signal)
INCL_I_PATTERNS = [
    r'\binternational(iz|is)',          # covers -ation/-ing/-ed/-e/-es
    r'\bmultinational(ity)?\b',
    r'\bfsts\b',
    r'\bforeign sales\b',
    r'\bexport intensit(y|ies)\b',
    r'\bdegree of internationali',
    r'\boutward fdi\b',
    r'\bofdi\b',
    r'\bcross.border (expansion|operations|activit)',
    r'\bglobal (expansion|diversification|spread)',
    r'\bgeographic(al)? diversification\b',
    r'\bforeign market (entry|expansion)',
    r'\bentry mode\b',
    r'\bforeign direct invest',
    r'\bsubsidiar(y|ies)\b.*\bperformance\b',
    r'\bexporting firm',
    r'\bexporter.*performance',
]

INCL_P_PATTERNS = [
    r'\bfirm performance\b',
    r'\bfinancial performance\b',
    r'\blabor productivity\b',
    r'\blabour productivity\b',
    r'\bproductivity\b',
    r'\broa\b',
    r'\broe\b',
    r'\btobin',
    r'\breturn on (asset|equity|sales|invest)',
    r'\boperating performance\b',
    r'\beconomic performance\b',
    r'\bprofitabilit(y|ies)\b',
    r'\bsales growth\b',
    r'\brevenue growth\b',
    r'\bmarket value\b',
    r'\bfirm value\b',
    r'\bcompetitive advantage\b',
    r'\bperformance\b',          # broad — catches "performance outcomes", "performance effects" etc.
    r'\befficienc(y|ies)\b',
    r'\bsurvivor?\b',
]

# DV-as-IV signals: when "export performance" likely means export is the DV (not I→P)
EXPORT_PERF_AS_DV = [
    r'\b(export|international|exporting) (behavior|behaviour|performance|decision|propensit|intensit|particip)',
    r'\bdeterminants? of export\b',
    r'\bexport (entry|survival|intensity|growth|propensit)',
    r'\bwillingness to (export|internationaliz)',
    r'\bgoing (international|global|abroad)',
]

# Signals that suggest innovation/CSR/ESG as SOLE performance, not financial
INNOVATION_CSR_SOLE = [
    r'\binnovation performance\b(?!.*\bfirm performance)',
    r'\bcsr performance\b(?!.*\bfirm|financial)',
    r'\besg (performance|score)\b(?!.*\bfirm|financial)',
    r'\benvironmental performance\b(?!.*\bfirm|financial)',
]


def t(text: str) -> str:
    return text.lower()


def matches(text: str, patterns: list) -> tuple:
    tl = t(text)
    for pat in patterns:
        if isinstance(pat, tuple):
            pat, reason = pat
        else:
            reason = pat
        if re.search(pat, tl):
            return True, reason
    return False, None


def screen_title(row: dict) -> tuple:
    """Returns (include_flag, notes)"""
    title  = row.get('title', '') or ''
    journal = row.get('journal', '') or ''
    pre    = row.get('prescreen_flag', '') or ''
    pre_reason = row.get('prescreen_reason', '') or ''
    tl = t(title + ' ' + journal)

    # ── 1. Hard exclusions (pre-N stays N) ──────────────────────────────────
    if pre == 'N':
        return 'N', row.get('notes', '') or 'prescreen:N'

    for pat, reason in EXCL_PATTERNS:
        if re.search(pat, tl):
            return 'N', reason

    # ── 2. Export-as-DV: very strong signal that this studies EXPORT not PERFORMANCE ─
    n_export_dv = sum(1 for pat in EXPORT_PERF_AS_DV if re.search(pat, tl))
    has_fp = bool(re.search(r'|'.join(INCL_P_PATTERNS), tl))
    has_i  = bool(re.search(r'|'.join(INCL_I_PATTERNS), tl))

    if n_export_dv >= 2 and not has_fp:
        return 'N', 'EXCL:export-as-DV'

    # ── 3. Strong INCLUDE: explicit I + P in title ───────────────────────────
    if has_i and has_fp:
        return 'Y', 'L2:title-I+P-confirmed'

    # ── 4. Pre-Y with a clear performance signal (fp_type coded) ────────────
    if pre == 'Y' and row.get('prescreen_fp_type'):
        return 'Y', f"L2:prescreen-Y+fp={row['prescreen_fp_type']}"

    # ── 5. Pre-Y with DOI/FDI signal but no explicit P → UNSURE ─────────────
    if pre == 'Y' and has_i:
        # Has internationalization signal but no clear performance DV in title
        return 'UNSURE', 'L2:has-I-no-P-in-title'

    # ── 6. WEAK-INCL:exporter ───────────────────────────────────────────────
    if 'WEAK-INCL:exporter' in pre_reason:
        if has_fp:
            return 'Y', 'L2:exporter+fp-confirmed'
        return 'UNSURE', 'L2:exporter-no-fp-in-title'

    # ── 7. WEAK-INCL:financial-perf ─────────────────────────────────────────
    if 'WEAK-INCL:financial-perf' in pre_reason:
        if has_i:
            return 'Y', 'L2:financial-perf+I-confirmed'
        return 'UNSURE', 'L2:financial-perf-no-I'

    # ── 8. WEAK-INCL:subsidiaries ───────────────────────────────────────────
    if 'WEAK-INCL:subsidiaries' in pre_reason:
        if has_fp:
            return 'Y', 'L2:subsidiaries+fp'
        return 'UNSURE', 'L2:subsidiaries-no-fp'

    # ── 9. NO-CLEAR-SIGNAL: apply conservative UNSURE ───────────────────────
    if pre == 'UNSURE':
        return 'UNSURE', f'L2:no-clear-signal({pre_reason})'

    # ── 10. Pre-Y with no strong I or P → UNSURE ────────────────────────────
    if pre == 'Y':
        return 'UNSURE', 'L2:prescreen-Y-but-weak-title'

    return 'UNSURE', 'L2:unclassified'


# ── Run screening ────────────────────────────────────────────────────────────
with open(INPUT, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

results = []
for row in rows:
    flag, note = screen_title(row)
    row['include_flag'] = flag
    row['notes'] = note
    results.append(row)

# ── Write output ─────────────────────────────────────────────────────────────
with open(OUTPUT, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

# ── Summary ──────────────────────────────────────────────────────────────────
counts = {}
for r in results:
    counts[r['include_flag']] = counts.get(r['include_flag'], 0) + 1

print(f"L2 title-screening complete → {OUTPUT}")
print(f"Total: {len(results)}")
for k in ['Y', 'N', 'UNSURE']:
    print(f"  {k}: {counts.get(k,0)}")

# Show N reasons
n_reasons = {}
for r in results:
    if r['include_flag'] == 'N':
        n_reasons[r['notes']] = n_reasons.get(r['notes'], 0) + 1
print("\nExclusion reasons:")
for k, v in sorted(n_reasons.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
