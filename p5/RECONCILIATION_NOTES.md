# P5 China — Reconciliation Notes

*Created: 2026-06-03 (retrospective; P5 had no per-paper RECONCILIATION until now)*

## Status: ✅ SUBMISSION-READY

P5 China has cleared all Phase A1 reviewer-flagged items. The paper passes blind-DOCX, APA7 cross-reference, and numerical-consistency checks. P5 is in the cleanest state of any paper in the portfolio.

## Items resolved across sessions

| # | Issue | Severity | Resolution |
|---|---|:-:|---|
| 1 | Table 2 coefficient mismatch (manuscript +1.28/+1.19 vs canonical Python CSV +2.065/+1.498) | 🔴 ERROR | Updated all 16 inline citations to canonical Python values; preserved unchanged TPs and Paternoster z (commit `62545d3`, 2026-06-02) |
| 2 | APJM → IJOEM retarget (5 places of stale APJM cruft: build script, replication notes EN+VI, legacy 7-part split folder, blinded DOCX, dist artifacts) | 🟡 WARN | Full purge in commit `0c823c9` (2026-06-02) + residual 3-file cleanup in commit `58ee98b` (2026-06-03) |
| 3 | P5 IJOEM submission folder README had stale "Running header (APJM)" checklist item | 🟡 WARN | Corrected to "Running header (IJOEM)" (commit `58ee98b`, 2026-06-03) |
| 4 | APA7 line 317 list-parenthetical citation: "(extended receivables, international logistics costs, currency risk, Manova, 2013)" parsed as phantom multi-author entry | 🟡 WARN | Restructured to "...payment terms such as extended receivables, international logistics costs, and currency risk (Manova, 2013)..." (commit `483e362`, 2026-06-03) |
| 5 | Blinded DOCX author-identifier leak (`thuyhuongctu@gmail.com`, `Can Tho University`, `Do Thuy Huong`) in word/document.xml | 🔴 ERROR | Fixed via build_paper_docx.py author-block stripper; rebuilt DOCX verified ✅ 0 author hits (commit `f1f5d38`, 2026-06-03) |

## Outstanding for NCS

None blocking. P5 is submission-ready for IJOEM (International Journal of Emerging Markets, Emerald).

## Verified UNCHANGED (canonical numerical alignment)

ALL Table 2 values verified to match canonical Python replication:
- Pooled M2 β(FSTS) = +2.065, β(FSTS²) = -2.146 ✓
- 2012 M2 TP = 49.4% ✓
- 2024 M2 TP = 47.2% ✓
- Pooled M2 TP = 48.8% ✓
- Pooled M8 β(TCI) = +0.169 ✓
- M5 β(TCI direct) = +0.158 ✓
- Paternoster z = +0.78 (FSTS), z = -0.61 (FSTS²) ✓
- N = 4,544 (pooled) = 2,610 (2012) + 1,934 (2024) ✓
- LM test p < .001 in both waves and pooled ✓

## Final session integrity checks

- `check-consistency.py`: ✅ 0 numerical inconsistencies
- `format-apa7.py`: ✅ all citations have entries in references
- Blind DOCX scan (9 author-identifier patterns): ✅ 0 hits
- IJOEM word cap = 10,000w; current = 7,331w (well under)
