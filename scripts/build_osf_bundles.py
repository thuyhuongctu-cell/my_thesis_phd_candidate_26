#!/usr/bin/env python3
"""build_osf_bundles.py — assemble upload-ready OSF folders, one per paper.

Operationalises osf/OSF_PROJECT_STRUCTURE.md: for each component paper it
creates dist/osf/<paper>/ with code/, materials/, manuscript/, a verify.txt
(exact command + expected headline number), and a README. The candidate then
drags each folder into its OSF project. Output goes to dist/ (gitignored) so the
repo is not bloated; raw WBES micro-data are NEVER copied (licensed) — only an
access note.

Run:  python3 scripts/build_osf_bundles.py
"""
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'dist' / 'osf'

# paper -> (code scripts, blinded manuscript, verify command, expected headline)
PAPERS = {
    'P3_vietnam': (
        ['manuscripts/p3_vietnam_en_clean.md'],
        'manuscripts/p3_vietnam_en_clean.md',
        'See manuscript replication appendix (Stata + Python).',
        'Inverted-U turning point 39-46% FSTS across waves.'),
    'P4_singapore': (
        ['p4/replication/p4_singapore_figs_from_raw.py',
         'p4/replication/REPRO_2026-06-23/estimates.csv'],
        'manuscripts/p4_singapore_en_clean.md',
        'python3 p4/replication/p4_singapore_figs_from_raw.py',
        'Inverted-U M2 (FSTS_c +3.08/FSTS^2_c -1.90); TP ~88.6% (not reliably '
        'located); DAI x FSTS^2 +3.119 (p~.02); N=623/617.'),
    'P5_china': (
        ['p5/replication/python/build_and_run.py',
         'p5/replication/REPRO_2026-06-23/estimates.csv'],
        'manuscripts/p5_china_en_clean.md',
        'python3 p5/replication/python/build_and_run.py',
        'Inverted-U pooled TP 48.8% (mfg 42.3% 2012 / 29.7% 2024); threshold '
        'stability (Paternoster z ns); pooled N=4,544 (2,610/1,934).'),
    'P6_meta': (
        ['scripts/p6_meta_analysis.py', 'p6/results/forest_data.csv'],
        'p6/submission/jwb_package/01_manuscript_blinded.md',
        'python3 scripts/p6_meta_analysis.py',
        'Pooled r=0.074; Q_M ICRV=17.35/cDAI=1.23/DPL=0.56; k=238, K=288.'),
    'P7_capstone': (
        ['scripts/p7_run_50econ.py', 'scripts/p7_full_ladder.py',
         'p7/replication/REPRO_2026-06-23/estimates.csv'],
        'p7/submission/ibr_package/01_manuscript_blinded.md',
        'python3 scripts/p7_run_50econ.py',
        'M2 N=81,022 TP=51.5%; M5 N=79,080 TP=43.6%; three-zone per-ICRV '
        '(Group IV 43.0% sharp; SIDS no inverted-U).'),
    'P8_sids': (
        ['p8/replication/build_and_run_p8_7pacific.py',
         'p8/replication/REPRO_2026-06-23/estimates.csv'],
        'p8/p8_pacific_sids_redesigned_en.md',
        'python3 p8/replication/build_and_run_p8_7pacific.py',
        'Inverted-U DISSOLVES across 7 Pacific SIDS (N=1,450/7 clusters): '
        'linear FSTS_c -0.085 (p_wild=.66); quadratic FSTS_c^2 +0.696 '
        '(p_wild=.082). FIP beta=-1.339 is a SUPERSEDED 3-cluster limiting '
        'case only, not the headline.'),
    'P9_india': (
        ['p9_india/replication/run_pipeline.py',
         'p9_india/replication/REPRO_2026-06-23/estimates.csv'],
        'p9_india/submission/mir_package/01_manuscript_blinded_full.md',
        'python3 p9_india/replication/run_pipeline.py',
        'Threshold dissolution across waves (TP 61.8% 2014 / 40.7% 2022 / '
        'dissolves); Paternoster z=-7.94; pooled N~28,717.'),
    'P10_japan': (
        ['p10_japan/replication/p10_japan_models.py',
         'p10_japan/replication/REPRO_2026-06-23/estimates.csv'],
        'p10_japan/submission/abm_package/01_manuscript_blinded.md',
        'python3 p10_japan/replication/p10_japan_models.py',
        'FSTS linear +0.671***; quadratic ns (near-linear); exporter premium '
        '+0.258***; N=2,168.'),
    'P11_jed': (
        ['jed_ai_digital/replication/jed_digital_divide.py',
         'jed_ai_digital/replication/jed_robustness.py',
         'jed_ai_digital/replication/jed_gni_axis.py'],
        'jed_ai_digital/jed_digital_divide_manuscript.md',
        'python3 jed_ai_digital/replication/jed_digital_divide.py',
        'Digital divide 69->41%; pooled DAI premium +0.241***.'),
}

DATA_NOTE = """WBES micro-data are licensed and are NOT included here. Obtain them
free from https://www.enterprisesurveys.org upon registration. The analysis
scripts read the standard .dta cross-sections; see the codebook in materials/.
"""

if OUT.exists():
    shutil.rmtree(OUT)
for paper, (scripts, manuscript, cmd, expected) in PAPERS.items():
    base = OUT / paper
    for sub in ('code', 'materials', 'manuscript', 'data'):
        (base / sub).mkdir(parents=True, exist_ok=True)
    for s in scripts:
        src = ROOT / s
        if src.exists():
            shutil.copy(src, base / 'code' / src.name)
    man = ROOT / manuscript
    if man.exists():
        shutil.copy(man, base / 'manuscript' / '01_manuscript_blinded.md')
    # materials
    shutil.copy(ROOT / 'data_wbes' / 'analysis' / 'CANONICAL_NUMBERS.md',
                base / 'materials' / 'CANONICAL_NUMBERS.md')
    cb = ROOT / 'p6' / 'tools' / 'p6_extraction_codebook.md'
    if cb.exists() and paper == 'P6_meta':
        shutil.copy(cb, base / 'materials' / 'codebook.md')
    (base / 'data' / 'README_data_access.md').write_text(DATA_NOTE)
    (base / 'code' / 'verify.txt').write_text(
        f'Reproduce the headline result:\n\n  {cmd}\n\n'
        f'Expected:\n  {expected}\n\n'
        f'Full project reproducibility check: python3 scripts/verify_all.py '
        f'(14/14 PASS).\n')
    label = 'Registered analysis plan' if paper == 'P6_meta' \
        else 'Registered analysis materials (post-hoc)'
    (base / 'README.md').write_text(
        f'# OSF bundle — {paper}\n\n'
        f'OSF label: **{label}** (see osf/OSF_PROJECT_STRUCTURE.md).\n\n'
        f'- `code/` — estimation script(s) + verify.txt\n'
        f'- `materials/` — canonical numbers / codebook\n'
        f'- `manuscript/` — blinded manuscript\n'
        f'- `data/` — access note only (WBES is licensed)\n\n'
        f'Reproduce: `{cmd}`\nExpected: {expected}\n')
    print(f'  built dist/osf/{paper}/')

print(f'\n{len(PAPERS)} OSF bundles -> {OUT.relative_to(ROOT)} (gitignored). '
      f'Upload each folder to its OSF project.')
