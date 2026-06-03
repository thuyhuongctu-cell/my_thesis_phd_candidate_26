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
| 6 | **3-journal target confusion (CRITICAL)** | 🔴 CRITICAL | 2h | ✅ **RESOLVED 2026-06-03 (final)**: NCS confirmed target = **Asia Pacific Journal of Management (APJM, Springer Nature, Q1, ABS-3)**. Rationale: (i) perfect geographic fit for the 45-economy Asia-Pacific corpus and the ICRV taxonomy; (ii) Q1 status within the user-specified Q1–Q2 range (MRQ Q3–Q4 excluded; IBR excluded by user; MIR harder + slower review; APJM is the optimum); (iii) APJM editorial board includes institutional-theory experts (Peng 2003 IBV anchor) welcoming the integrated capability-institution mechanism contribution; (iv) 6–8 month review timeline vs MIR 8–12 months; (v) Springer EM portal NCS already familiar. **Implementation:** manuscript header line 5 + footer updated to APJM; new `p6/submission/apjm_package/` created with title page + APJM-specific cover letter + README; OSF DOI z37kn unchanged (preregistration body is journal-agnostic — no retro-edit). Build script updated to emit APJM package. Submit with current k = 238 (Path A); Path B WoS/Scopus expansion to k ≈ 600–700 pre-registered as follow-up replication. EN cover letter only (per NCS choice). **Subsequent revision 2026-06-03:** "CIMT" theory name removed from §2.2 + cover letter + keywords per scholar-review feedback; section retitled "An Integrated Capability–Institution Mechanism" and framed as a synthesis of established channels rather than a novel named theory. |
| 7 | Single-coder extraction (PRISMA Item 9 violation) | 🔴 HIGH | 1h | Disclosed transparently as pre-reg deviation #4. Mitigations (double-entry, pilot) help but don't substitute for κ. Re-framing or hire second coder. |
| 8 | Schwens et al. (2018) reference verification | 🟡 MED | 30min | ⚠ **NCS verification required (2026-06-03)**: P6 ref entry (line 473) is "Schwens et al. (2018) *Limits to outsourcing*. JIBS 49(6) 682-703" — confirmed to be the outsourcing meta-analysis, not an I-P meta-analysis. The inline citations at §1 (line 30 "six major meta-analyses") and §3 (line 100 "five anchor meta-analyses") treat this as an I-P meta-analysis used for backward/forward citation tracking. NCS to decide: (a) verify Schwens 2018 *outsourcing* meta-analysis was in fact used as an anchor for I-P backward tracking (then keep but document overlap), or (b) replace inline with a real Schwens et al. I-P meta-analysis if intended, or (c) remove Schwens from the "anchor meta-analyses" list (drops anchor count from 5 to 4). |
| 9 | Wu et al. (2022) reference verification | 🟡 MED | 30min | ✅ **RESOLVED 2026-06-03**: P6 ref entry corrected from Wu, Wang, Hong, Piperopoulos & Zhuo (2022) JWB on *innovation* performance (primary study, not meta-analysis) to **Wu, Wood & Khan (2022) IBR 31(2) 101920** — the canonical I-P meta-analysis. Inline citations "Wu et al., 2022" at §1 line 30 and elsewhere now point to the correct meta-analysis. |
| 10 | 5+ orphan in-text citations (Vernon 1971, Rugman 1976, Hitt 1997/2006, Scott 1995, Johanson & Vahlne 2009) | 🟡 MED | 1h | ✅ **RESOLVED 2026-06-03**: Audit of current P6 shows: Vernon 1971 (line 121, 1 inline) + Rugman 1976 (line 121, 1 inline) + Hitt et al. 2006 (line 30, 1 inline) had no central refs → added 3 canonical entries to thesis/04_references_apa7.md. Scott 1995 already had a ref (false positive). Hitt 1997 and Johanson & Vahlne 2009 have zero actual inline occurrences in current P6 (likely removed during earlier editing) — no action needed. |
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
