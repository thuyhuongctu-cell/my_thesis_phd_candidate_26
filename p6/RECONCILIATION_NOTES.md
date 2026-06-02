# P6 Meta-analysis — Reconciliation Notes

*Created: 2026-06-02 (after lfe-academic-reviewer Phase A1 review)*

## Status: PARTIALLY RESOLVED

5 of 12 reviewer-flagged items addressed in this session. Critical target-journal decision pending NCS.

## Fixed in this session

| # | Issue | Severity | Action |
|---|---|:-:|---|
| 1 | Submission README stale numbers (word count, r, I²) | 🔴 ERROR | Updated: 9K→11,129w; r=0.075→0.074; I²=62.4%→87.8% |
| 2 | Missing Hunter & Schmidt (2015) methodological ref | 🟡 WARNING | Added APA7 entry: *Methods of meta-analysis* (3rd ed.) Sage |
| 3 | Missing Geyskens et al. (2009) methodological ref | 🟡 WARNING | Added APA7 entry: *Journal of Management* IB meta-analysis review |
| 4 | §5.2 "We intend" voice slip | 🟡 WARNING | → "This paper intends" |
| 5 | §5.1 "our wider primary-study programme" voice | 🟡 WARNING | → "the authors' wider primary-study programme" |

## Outstanding for NCS

| # | Issue | Severity | Effort | Notes |
|---|---|:-:|---:|---|
| 6 | **3-journal target confusion (CRITICAL)** | 🔴 CRITICAL | 2h | Header=MIR, README/folder=IBR, PRISMA checklist=MRQ. **User intent (2026-06-02): NOT IBR.** Likely MIR (matches manuscript header) or MRQ. Decision affects abstract format, cover letter, submission URL. |
| 7 | Single-coder extraction (PRISMA Item 9 violation) | 🔴 HIGH | 1h | Disclosed transparently as pre-reg deviation #4. Mitigations (double-entry, pilot) help but don't substitute for κ. Re-framing or hire second coder. |
| 8 | Schwens et al. (2018) reference verification | 🟡 MED | 30min | Reviewer flagged: title in references is "Limits to outsourcing" (outsourcing meta-analysis, not I-P). Verify intent. |
| 9 | Wu et al. (2022) reference verification | 🟡 MED | 30min | Reviewer flagged: appears to be primary study, not I-P meta-analysis. Verify. |
| 10 | 5+ orphan in-text citations (Vernon 1971, Rugman 1976, Hitt 1997/2006, Scott 1995, Johanson & Vahlne 2009) | 🟡 MED | 1h | Add reference entries or remove in-text citations. |
| 11 | Abstract structure: Emerald 7-section → IBR unstructured (if IBR retained) | 🟡 MED | 1h | MIR allows Emerald format; MRQ allows structured; IBR prefers unstructured. |
| 12 | PRISMA Item 15 (GRADE/certainty) missing | 🟢 LOW | 30min | Acceptable at IBR/MIR; add brief paragraph if MRQ pursued. |

## Verified UNCHANGED

ALL numerical claims match canonical CSVs (table1-table5):
- Pooled r = 0.074 [.060, .088], Q_total = 1,909.42 (df=287) ✓
- I²_total = 87.8%, I²₍₂₎ = 76.1%, I²₍₃₎ = 11.8% ✓
- ICRV Q_M = 17.35, p=.002 (full); 1.49 (df=3, p=.68) Drop-FR sensitivity ✓
- cDAI Q_M = 1.23, p=.541 ✓
- DPL Q_M = 0.56, p=.755 ✓
- Vevea-Hedges step-function selection model — methodologically sophisticated ✓

## Three-Way Target Journal Decision Matrix

| Criterion | MIR (Springer) | IBR (Elsevier) | MRQ (Springer) |
|---|---|---|---|
| ABS rating | 3 | 3 | 1 |
| Acceptance prob | ~50% | ~40% | ~60% |
| Abstract format | Emerald structured OK | Unstructured preferred | Structured OK |
| PRISMA single-coder tolerance | Moderate | Low | High |
| Manuscript header (line 5) | ✓ matches | ✗ | ✗ |
| Submission package folder | ✗ named `ibr_package` | ✓ matches | ✗ |
| PRISMA checklist | ✗ | ✗ | ✓ "retargeted from IBR" |

**Recommendation per NCS preference (NOT IBR)**: MIR primary (matches header + ABS-3 highest) OR MRQ (highest accept probability).

## Submission Package Status

Current state: `p6/submission/ibr_package/` — name no longer accurate.

When NCS decides target:
1. Rename folder to `mir_package/` or `mrq_package/`
2. Update cover letter Salutation + EiC + journal
3. Update abstract format if needed
4. Rebuild submission DOCX via `scripts/build_paper_docx.py --paper p6`
   - May need to update PAPERS dict path in script
