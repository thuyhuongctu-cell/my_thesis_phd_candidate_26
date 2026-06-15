# Heavy pre-submission review — 2026-06-15

Full-corpus citation-integrity and consistency pass requested before submission
("review heavily, fix all errors"), applying the installed review skills
(`pre-submission-reviewer`, `academic-paper-reviewer`, `econ-referee-feedback`,
`lfe-academic-reviewer`, `kiem-tra-meta-analysis`, `academic-variable-formatter`).
This pass went deeper than the 2026-06-14 run and used automated two-way
citation checking (every in-text author-year vs. every reference entry, in both
directions) on each manuscript.

## What was found and fixed

### P7 (capstone working source + IBR submission blinded copy)
- **CRITICAL — broken cite:** `Stallkamp & Schotter (2021)` was cited in §2 but
  had no reference entry. Added.
- **Orphans removed** (listed, never cited): Hayes (2018), Long & Ervin (2000),
  Wu et al. (2022) — the Wu entry also had an internally impossible volume
  (JWB vol. 54 for a 2022 article) — and World Bank policy notes 2025a/b/c,
  2026a, 2024.
- **Orphans resolved by anchoring** (kept and given an accurate in-text home):
  World Bank (2025) on the WBES data sentence; Aiken & West (1991) + Dawson
  (2014) on the interaction-terms method; IFC (2022) + Buchhave et al. (2026) on
  the negative female-management finding; Cuervo-Cazurra et al. (2018) on the
  institutional-theory sentence.
- World Bank `2026b` renumbered to `2026` (now the sole 2026 entry).
- Result: zero orphans, zero broken cites. DOCX rebuilt.

### P6 (working source + JWB submission blinded copy)
- **Broken cites fixed by adding entries** (cited in text, absent from list):
  Dunning (2000), Dickersin (1990), Lu & Beamish (2004), Rugman (1976),
  Scott (1995), Vernon (1971), Sahay et al. (2020), Valentine et al. (2010).
  `Kafouros et al., 2012` was aligned to the project's verified Kafouros et al.
  (2023) entry (the 2012 paper was not in the vetted bibliography; the 2023
  entry is topically appropriate and DOI-verified). **Author check:** if the
  2012 knowledge-reservoirs paper was specifically intended, restore it instead.
- **`Perryy, M. Z.` → `Perryman, A. A.`** in Kirca et al. (2012) — the same typo
  fixed earlier in P10; the JOM 2012 meta-analysis author is Alexa A. Perryman.
- **Wrong Wu (2022) entry replaced:** the list carried an empirical JWB study
  (Wu, Wang, Hong, Piperopoulos & Zhuo) with an impossible volume (52/2022),
  but the in-text cite is to Wu as one of the "six major meta-analyses," i.e.
  Wu, Wood & Khan (2022, IBR). Replaced with the correct meta-analysis.
- **Orphans removed** (working source only; the JWB copy did not contain these):
  Jensen & Meckling (1976), Lakens (2020), Paternoster (1998).
- Table 4.1 Regime I counts `140/108 → 139/107` (column sums now reconcile to
  K=288 / k=238). Stallkamp reordered before Stanley.
- Result: zero orphans, zero broken cites in both files. DOCX rebuilt.
- **Pouresmaeili et al. (2018)** is a named *included primary study* (the FR-group
  outlier, study S86 in `forest_data.csv`), not a methods/theory reference. It is
  documented in the supplementary coded database, not the main list. No entry was
  fabricated. If the target journal requires asterisk-marked included studies, the
  author should add it (full citation is in the author's reference manager).

## Open items the author must resolve before P6 is submission-ready

1. **P6 detailed-statistics reconciliation (BLOCKER).** The two P6 manuscript
   versions disagree on the detailed publication-bias and subgroup numbers, and
   *neither* matches the current analysis script:
   - Q_M(DPL): working source = **0.56, p=.755** (matches `verify_all.py` and
     `CANONICAL_NUMBERS.md`); JWB copy still shows the old **0.62, p=.734**.
   - Egger: working source b=0.475, p=.057; JWB p=.052; script slope p=.007.
   - Trim-and-fill: working source k=58; JWB k=57; script ~10 (L0 estimator).
   - Group III r̄: working source 0.069; JWB 0.068; script subgroup r=−0.007.
   `verify_all.py` validates only the headline figures (pooled r, k/K, the three
   Q_M values — all 14/14 pass). The detailed pub-bias/subgroup numbers in the
   manuscripts come from an R/`metafor` run not reproduced by the Python verifier.
   **No numbers were changed** (integrity rule: coefficients change only after a
   real estimation run). The author should re-run the R/`metafor` analysis,
   confirm the authoritative values, and sync both P6 copies to them.
2. **P6 search-status framing.** The working source says "WoS + Scopus confirmed
   (20 May 2026)"; the JWB copy frames it more conservatively as
   "citation-anchored systematic searching." This was already flagged in
   `p6/p6_prisma_flow.md` / the 2026-06-14 review as the Scopus-search
   reconciliation item. Pick one consistent, accurate description before submission.
3. **P6 ICR κ** for the 20% double-coded subsample is still pending (κ ≥ 0.70 target).

## Reproducibility
`scripts/verify_all.py`: **14/14 pass** after all edits (P6 6/6, P7 4/4, P10, P11).
No econometric coefficients were fabricated or altered.

## Standing author-only items (unchanged)
Stata cross-validation; `verify_dois.py` over the full reference set (the newly
added classics — Dunning 2000, Vernon 1971, Rugman 1976, Dickersin 1990,
Valentine 2010 — were added without DOIs and should be confirmed in that pass);
GVHD name + final thesis title placeholders.
