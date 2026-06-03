# P9' India — Reconciliation Notes

*Created: 2026-06-03 (retrospective; P9' India had no per-paper RECONCILIATION until now)*

## Status: ✅ SUBMISSION-READY

P9' India is the newest paper in the portfolio (created in the Phase A/B/C arc after the original Thailand-targeted P9 was abandoned). It has cleared all integrity checks and informs both Chapter 4 §4.4.4 and Chapter 5 §5.1 of the dissertation.

## Items resolved across sessions

| # | Issue | Severity | Resolution |
|---|---|:-:|---|
| 1 | APA7 cross-reference missing 4 econometric refs (Cameron-Gelbach-Miller 2008 wild bootstrap; Chodorow-Reich et al. 2020 India demonetization; MacKinnon & Webb 2017 wild bootstrap; Mizik & Jacobson 2003 strategic-emphasis trade-off) | 🟡 WARN | Added 4 canonical entries to thesis/04_references_apa7.md (commit `e6761b4`, 2026-06-03) |
| 2 | P9_Thailand_JED legacy submission folder (from when P9 was Thailand → JED) | 🟡 housekeeping | Replaced with `dist/SUBMISSION_FINAL/P9_India_MIR/` containing rebuilt blinded DOCX; legacy folder removed (commit `f1f5d38` + cleanup 2026-06-03) |

## Outstanding for NCS

None blocking. P9' India is submission-ready for MIR (Management International Review, Springer) or IJOEM (alternative target).

## Verified UNCHANGED (canonical numerical alignment)

ALL key findings verified to match canonical R + Python replication:
- WBES India 3 waves:
  - 2014 PICS3: N_raw = 9,281; analytic = 8,941 ✓
  - 2022 BEE: N_raw = 9,376; analytic = 9,300 ✓
  - 2025 BREADY: N_raw = 10,479; analytic = 10,476 ✓
  - Pooled raw N = 29,136; pooled analytic = 28,717 ✓
- Wave 2014: TP = 61.8% (inverted-U present) ✓
- Wave 2022: TP = 40.7% (inverted-U migrating) ✓
- Wave 2025: TP undefined (curvature collapse; FSTS slope = -0.10/yr trend) ✓
- Paternoster z = -7.94 (HC1) and z = -3.50 (cluster G=24 states) ✓
- DAI Tier-2 UPI quasi-experiment: β = -4.02 (p = 0.004) — confirmed in §4 ✓
- TCI cross-wave shift: β = +0.12 → +0.19 → -0.08 ✓
- Pooled 3-wave model: FSTS × wave_2025 = -1.63 (p < 0.0001) ✓
- DAI Tier-1 (website) trajectory: 52.7% (2014) → 60.6% (2022) → 41.8% (2025) ✓
- DAI Tier-2 (UPI e-payment, 2025 only): 65.8% ✓

## Phase C integration

P9' findings are integrated into the dissertation chapters:
- **Chapter 4 §4.4.4 Ấn Độ** (1,070 Vietnamese words; commit `11cdefb`, 2026-06-02): full reporting of all wave-specific findings, Paternoster z-tests, UPI quasi-experiment, TCI sign flip, and Table 4.7 (Điểm uốn theo đợt khảo sát Ấn Độ).
- **Chapter 5 §5.1 India synthesis** (212 Vietnamese words): India as BOUNDARY CONDITION for CDCM framework. Refutation of Tier-2 universal substitution hypothesis. Purpose-aligned public infrastructure principle.

## Final session integrity checks

- `check-consistency.py`: ✅ 0 numerical inconsistencies across all 60 files
- `format-apa7.py`: ✅ all citations have entries in references
- Blind DOCX scan: ✅ 0 author-identifier hits (rebuilt to dist/SUBMISSION_FINAL/P9_India_MIR/, commit `f1f5d38`)
- Target journal options: MIR (primary) or IJOEM (alternative)
