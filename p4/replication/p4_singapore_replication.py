#!/usr/bin/env python3
"""DEPRECATED / DO NOT USE — mislabeled leftover.

This file historically contained a *Vietnam* (P3) replication body that read
WBES Vietnam waves from an ephemeral upload path. It was never a P4 Singapore
runner despite its name, and is kept only as a redirect to avoid breaking links
in older review notes (REPLICATION_STATUS.md, reviews/data_paper_reconciliation_2026-06.md).

Authoritative P4 Singapore replication (reproducible from committed raw data):

    python3 p4/replication/p4_singapore_figs_from_raw.py
        -> reads data_wbes/raw_dta/Singapore-2023-full-data.dta (WBES_RAW override)
        -> builds lnLP, FSTS, TCI(b8+e6+h1), DAI(c22b+k33+k38)
        -> estimates M0-M8 (incl. FSTS^2 x DAI interaction) + Lind-Mehlum turning point
        -> reproduces the headline: inverted-U (M2 FSTS_c +3.08, FSTS^2_c -1.90),
           TCI level +0.21, DAI level +0.17, FSTS^2 x DAI ~ +3.22 (manuscript +3.119),
           M2 turning point ~ 86% with CI exceeding the feasible FSTS range
           (i.e. not reliably located), N = 623 / 617.

Stata equivalent (authoritative for the candidate's licensed run):

    p4/replication/do/01_build_singapore.do
    p4/replication/do/02_run_models.do
"""
import sys

print(__doc__)
print("DEPRECATED. Run p4/replication/p4_singapore_figs_from_raw.py instead.")
sys.exit(1)
