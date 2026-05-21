"""
07_deep_title_screen.py
Deep title-based screening for UNSURE records using the full
research-screening-assistant PICOS framework.

Priority groups (from user workflow):
  P1: export intensity / FSTS → performance
  P2: multinationality / DOI → performance
  P3: FDI / OFDI → performance
  P4: international diversification → performance
  P5: generic internationalization → performance

For UNSURE records we apply stricter title rules to rescue
records that can be decided on title alone, and flag those
that genuinely need an abstract with a priority code.

Input : p6/tools/results/l2_screened_20260518.csv
Output: p6/tools/results/l2_deep_screened_YYYYMMDD.csv
        p6/tools/results/batch_screening_template_YYYYMMDD.txt  (for manual review)
"""

import csv, re
from datetime import date
from pathlib import Path

BASE_DIR = Path("/home/user/PAPERS_IN_PHD_2026")
INPUT    = BASE_DIR / "p6/tools/results/l2_screened_20260518.csv"
OUTDIR   = BASE_DIR / "p6/tools/results"
TODAY    = date.today().strftime('%Y%m%d')
OUT_CSV  = OUTDIR / f"l2_deep_screened_{TODAY}.csv"
OUT_TMPL = OUTDIR / f"batch_screening_template_{TODAY}.txt"

# ── EXCLUDE patterns (strong enough for title-only decision) ─────────────────
HARD_EXCL = [
    (r'\bcase stud(y|ies)\b',               'E2:qualitative-case-study'),
    (r'\bqualitative (study|research|anal)', 'E2:qualitative'),
    (r'\bbibliometric\b',                    'E2:bibliometric'),
    (r'\bmeta.analy',                        'E2:meta-analysis'),
    (r'\bsystematic review\b',               'E2:systematic-review'),
    (r'\bliterature review\b',               'E2:lit-review'),
    (r'\bconceptual (paper|model|framework)\b','E1:conceptual'),
    (r'\beditorial\b',                       'E1:editorial'),
    (r'\bbook review\b',                     'E1:book-review'),
    (r'\bco2 emission\b',                    'E6:non-IB-DV'),
    (r'\bcarbon (emission|footprint|tax)\b', 'E6:non-IB-DV'),
    (r'\bair pollution\b',                   'E6:non-IB-DV'),
    (r'\benvironmental (compliance|regulat)\b','E6:non-IB-DV'),
    (r'\bhealth (outcome|system|care)\b',    'E6:non-IB-DV'),
    (r'\bcountry.level (analysis|study)\b',  'E3:macro'),
    (r'\bnational (competitiveness|gdp)\b',  'E3:macro'),
]

# ── EXCLUDE: export as DV (not measuring firm performance) ───────────────────
EXPORT_DV_EXCL = [
    r'\bdeterminants? of export\b',
    r'\bexport decision\b',
    r'\bexport (propensit|particip|survival|entry|start)\b',
    r'\bwillingness to export\b',
    r'\bexport market (selection|choice|entry)\b',
    r'\bbarriers? to (export|internationaliz)\b',
    r'\bdrivers? of export\b',
    r'\bfactors? (affecting|influencing|determining) export\b',
    r'\bexport behavior\b',
    r'\bexport behaviour\b',
    r'\bgoing (international|global|abroad)\b',
    r'\binternationaliz(ation|ing) decision\b',
    r'\binternationaliz(ation|ing) intention\b',
    r'\bexport intent(ion)?\b',
    r'\bmotivations? (for|of) (export|internationaliz)\b',
]

# ── INCLUDE: P1 priority — explicit export intensity → performance ───────────
P1_INCL = [
    r'\bexport intensit(y|ies).{0,60}(performance|productivity|profit|roa|roe|tobin)',
    r'\bfsts.{0,60}(performance|productivity)',
    r'\bforeign sales.{0,60}(performance|productivity)',
    r'\b(performance|productivity|profit).{0,60}export intensit',
    r'\bexport.{0,30}firm performance\b',
    r'\bexport (and|&).{0,20}(firm|financial|operating) performance',
]

# ── INCLUDE: P2 — multinationality / DOI → performance ──────────────────────
P2_INCL = [
    r'\bmultinationalit(y|ies).{0,60}(performance|productivity)',
    r'\b(performance|productivity).{0,60}multinationalit',
    r'\bdegree of internationaliz.{0,60}(performance|productivity)',
    r'\binternational diversification.{0,60}(performance|productivity|value)',
    r'\b(performance|value).{0,60}international diversification',
    r'\binternational(iz|is)ation.{0,60}(firm|financial|operating) performance',
    r'\b(firm|financial|operating) performance.{0,60}international(iz|is)ation',
    r'\binternationali.{0,20}performance.{0,20}(relationship|link|nexus|effect)',
    r'\bperformance.{0,20}consequences? of internationaliz',
    r'\bperformance.{0,20}outcomes? of internationaliz',
    r'\bperformance effects? of.{0,30}multinational',
    r'\binternational expansion.{0,60}(performance|productivity)',
    r'\bglobal diversification.{0,60}(performance|productivity|value)',
]

# ── INCLUDE: P3 — FDI/OFDI → performance ────────────────────────────────────
P3_INCL = [
    r'\b(outward |o)fdi.{0,60}(performance|productivity)',
    r'\b(performance|productivity).{0,60}(outward |o)fdi',
    r'\bforeign direct invest.{0,60}(performance|productivity|profitab)',
    r'\b(performance|productivity).{0,60}foreign direct invest',
    r'\bsubsidiar(y|ies).{0,40}(performance|productivity)',
    r'\bentry mode.{0,60}(performance|productivity)',
    r'\b(performance|productivity).{0,40}entry mode',
]

# ── INCLUDE: P4/P5 — broader patterns ───────────────────────────────────────
P4_INCL = [
    r'\bcross.border (activit|operation|invest|expan).{0,40}(performance|productivity)',
    r'\bgeograph(ic|ical) diversification.{0,50}(performance|productivity|value)',
    r'\binternational scope.{0,50}(performance|productivity)',
    r'\bglobal (footprint|expansion|reach).{0,50}(performance|productivity)',
    r'\bliabilit(y|ies) of foreignness.{0,50}(performance|productivity)',
    r'\binternational business.{0,40}(performance|productivity)',
]


def t(text): return text.lower()


def check_excl(title):
    tl = t(title)
    for pat, reason in HARD_EXCL:
        if re.search(pat, tl):
            return reason
    n_edv = sum(1 for p in EXPORT_DV_EXCL if re.search(p, tl))
    if n_edv >= 1:
        # Also check for compensating P signal
        has_fp = bool(re.search(
            r'\b(firm|financial|operating) performance\b|\bproductivity\b|\broa\b|\broe\b|\btobin\b|\bprofitabilit',
            tl))
        if not has_fp:
            return 'E5:export-as-DV'
    return None


def check_incl(title):
    tl = t(title)
    for pat in P1_INCL:
        if re.search(pat, tl):
            return 'P1:export-intensity->perf', 'High'
    for pat in P2_INCL:
        if re.search(pat, tl):
            return 'P2:multinationality->perf', 'High'
    for pat in P3_INCL:
        if re.search(pat, tl):
            return 'P3:FDI->perf', 'Medium'
    for pat in P4_INCL:
        if re.search(pat, tl):
            return 'P4:broad-I->perf', 'Medium'
    return None, None


def priority_from_title(title):
    """Estimate effect-size extractability priority."""
    tl = t(title)
    if re.search(r'\bexport intensit|\bfsts|\bforeign sales (ratio|share)', tl):
        return 'High'
    if re.search(r'\bmultinationalit|\bdoi\b|\binternational diversif|\bgeograph.{0,10}diversif', tl):
        return 'High'
    if re.search(r'\bfdi|\bofdi|\bforeign direct', tl):
        return 'Medium'
    if re.search(r'\binternational(iz|is)', tl):
        return 'Medium'
    return 'Low'


# ── Main ──────────────────────────────────────────────────────────────────────
with open(INPUT, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames) + ['l2_deep_flag', 'l2_deep_reason', 'priority']
    rows = list(reader)

results = []
batch_lines = []
batch_count = 0

for row in rows:
    prev_flag = row['include_flag']
    title     = row.get('title', '') or ''
    seq       = row['seq']

    if prev_flag in ('Y', 'N'):
        # Keep existing decision; add priority for Y
        deep_flag   = prev_flag
        deep_reason = row.get('notes', '')
        priority    = priority_from_title(title) if prev_flag == 'Y' else ''
    else:
        # UNSURE — apply deep screening
        excl = check_excl(title)
        if excl:
            deep_flag   = 'N'
            deep_reason = excl
            priority    = ''
        else:
            incl_reason, incl_prio = check_incl(title)
            if incl_reason:
                deep_flag   = 'Y'
                deep_reason = incl_reason
                priority    = incl_prio
            else:
                deep_flag   = 'UNSURE'
                deep_reason = 'needs-abstract'
                priority    = priority_from_title(title)
                # Add to batch template
                batch_count += 1
                batch_lines.append(
                    f"ID: S{int(seq):04d}\n"
                    f"Title: {title}\n"
                    f"Authors: {row.get('authors','')}\n"
                    f"Year: {row.get('year','')}\n"
                    f"Journal: {row.get('journal','')}\n"
                    f"DOI: {row.get('doi_enriched','')}\n"
                    f"Abstract: [FETCH REQUIRED]\n"
                )

    row['l2_deep_flag']   = deep_flag
    row['l2_deep_reason'] = deep_reason
    row['priority']       = priority
    results.append(row)

# ── Write CSV ─────────────────────────────────────────────────────────────────
with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

# ── Write batch template ──────────────────────────────────────────────────────
with open(OUT_TMPL, 'w', encoding='utf-8') as f:
    f.write(f"# P6 Batch Screening Template — {TODAY}\n")
    f.write(f"# Records needing abstract for L2 decision: {batch_count}\n")
    f.write("# Fill in Abstract field, then submit to research-screening-assistant\n\n")
    f.write("---\n\n".join(batch_lines))

# ── Summary ───────────────────────────────────────────────────────────────────
deep_flags = {}
for r in results:
    deep_flags[r['l2_deep_flag']] = deep_flags.get(r['l2_deep_flag'], 0) + 1

print(f"Deep title screening complete")
print(f"Output CSV:      {OUT_CSV}")
print(f"Batch template:  {OUT_TMPL} ({batch_count} records)")
print()
print("Final l2_deep_flag distribution:")
for k in ['Y', 'N', 'UNSURE']:
    print(f"  {k}: {deep_flags.get(k,0)}")

# Breakdown of new Y from UNSURE
new_y = [r for r in results if r['include_flag']=='UNSURE' and r['l2_deep_flag']=='Y']
new_n = [r for r in results if r['include_flag']=='UNSURE' and r['l2_deep_flag']=='N']
print()
print(f"Rescued from UNSURE → Y: {len(new_y)}")
print(f"Resolved from UNSURE → N: {len(new_n)}")

# Priority distribution for Y
y_prio = {}
for r in results:
    if r['l2_deep_flag'] == 'Y':
        y_prio[r['priority']] = y_prio.get(r['priority'], 0) + 1
print()
print("Y records by priority:")
for k in ['High', 'Medium', 'Low', '']:
    if y_prio.get(k):
        print(f"  {k or 'unset'}: {y_prio[k]}")
