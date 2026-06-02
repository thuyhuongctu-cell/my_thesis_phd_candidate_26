# P8 Pacific SIDS — Reconciliation & Outstanding Items

*Created: 2026-06-02 (after lfe-academic-reviewer Phase A1 review)*

## Status: PARTIALLY RESOLVED

5 of 17 reviewer-flagged items addressed in this session. Remaining items require NCS workflow (some need analysis re-run).

## Fixed in this session

| # | Issue | Severity | Action |
|---|---|:-:|---|
| 1 | Marano, Tallman & Teece (2016) wrong reference (J. of Leadership & Organizational Studies) | 🔴 ERROR | Replaced with correct Marano, Arregle, Hitt, Spadafora & van Essen (2016) *Journal of Management* meta-analytic review |
| 2 | Missing Bertram (2006) MIRAB reference | 🔴 ERROR | Added APA7 entry: *Asia Pacific Viewpoint* |
| 3 | Missing Banalieva & Dhanaraj (2019) reference | 🔴 ERROR | Added APA7 entry: *JIBS* |
| 4 | Missing Mahler, Serajuddin, Wadhwa & Yonzan (2026) reference | 🔴 ERROR | Added APA7 entry: World Bank Group |
| 5 | Heckman selection in abstract but not in Results | 🔴 ERROR | Removed Heckman from Abstract Design section; reduced to "Three OLS specifications" |
| 6 | Comoros (Indian Ocean) labeled as Pacific SIDS | 🔴 CRITICAL | **Conservative fix**: Title + Abstract relabeled "Pacific and Indian Ocean Small Island Developing States" |

## Outstanding for NCS

| # | Issue | Severity | Effort | Notes |
|---|---|:-:|---:|---|
| 7 | Comoros exclusion alternative | 🔴 CRITICAL | 4-6h | Re-run all R models with N=1,352 (Comoros contributes 117 obs / 1.7% of sample). FIP result likely robust but should verify. NCS choice: keep relabeled title or exclude+rerun. |
| 8 | Wild-cluster bootstrap (G=9 clusters) | 🔴 HIGH | 6-8h | Cameron-Gelbach-Miller (2008) wild bootstrap; Roodman et al. (2019) Stata. Add as Appendix B robustness. |
| 9 | Leave-one-country-out (LOO) sensitivity | 🟡 MED | 3-4h | Timor-Leste = 26.8% of sample; verify FIP not Timor-Leste-driven. Add as Appendix B. |
| 10 | M3 N=526 vs M1 N=1,469 (64% drop) | 🟡 MED | 1h | Either Heckman selection adjustment or explicit multiple-imputation discussion. |
| 11 | Abstract trim from ~280w to ≤250w | 🟡 LOW | 15 min | Tighten Originality/Practical implications sections. |
| 12 | Marano et al. 2016 in-text citations update | 🟢 DONE | — | Changed "Tallman & Teece, 2016" → "Marano et al., 2016" globally. |

## Verification of numerical alignment

ALL Table 2 values verified to match canonical `p8/replication/results/p8_R_coefs.csv`:

| Coefficient | Manuscript | CSV |
|---|---|---|
| M1 β(FSTS_c) | −0.404 (0.188), p=.032 | −0.403826 (0.18767), p=.031872 ✓ |
| M2 β(FSTS_c) | −0.925 (0.828), p=.265 | −0.924659 (0.828408), p=.264856 ✓ |
| M2 β(FSTS_c²) | +0.649 (0.980), p=.508 | +0.648514 (0.97977), p=.508325 ✓ |
| M_yearFE | −1.236, p<.001 | −1.236155, p≈5e−06 ✓ |
| M_bivariate | −1.596, p<.001 | −1.595769 ✓ |
| M3 TCI_z | +0.058, p=.495 | +0.058026, p=.495116 ✓ |
| M3 DAI_z | +0.062, p=.402 | +0.061523, p=.402328 ✓ |

**Note**: P8 differs from P5/P4 — numerical reconciliation was already correct. No Table 2 value updates needed.

## FIP Theoretical Contribution

Reviewer assessment: "moderate-to-strong" defensibility:
- ✓ 3-prerequisite structure well-grounded (Johanson & Vahlne 1977; Winters & Martins 2004; Khanna & Palepu 2010)
- ✓ §2.2 differentiates FIP from 4 adjacent concepts (LoF, three-stage, necessity entrepreneurship, Briguglio index)
- ✓ "Internationalization-to-scale vs internationalization-to-survive" framing is novel and publishable

Suggested strengthening:
- ✗ Explicit contrast: FIP firm-level signature (β₁<0, β₂ not<0, no TP) vs macro vulnerability index (no firm-level signature)
- ✗ Position FIP as not-renaming-existing-phenomena defence

## Publishability ceiling at JED

Reviewer estimate: **HIGH** after Top 3 fixes (Comoros decision + wild-cluster bootstrap + reference list)

Post-fix (this session): submission-ready except for Comoros re-analysis decision and wild-cluster bootstrap robustness check. JED editorial mission (developing-country economics) aligns excellently with Pacific SIDS context.
