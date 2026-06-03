# P7 Capstone — Reconciliation Notes

*Created: 2026-06-02 (after lfe-academic-reviewer Phase A1 review)*

## Status: PARTIALLY RESOLVED

4 of 12 reviewer-flagged issues addressed. **CRITICAL coefficient verification required by NCS before JIBS submission.**

## Fixed in this session

| # | Issue | Severity | Action |
|---|---|:-:|---|
| 1 | Subject-verb agreement: "this study advance/test/show" | 🟡 WARNING | → "advances/tests/shows" (multiple instances) |
| 2 | 49 vs 45 economies inconsistency | 🟡 WARNING | Standardised to 45 (per audit JSON: 48 entries, 3 panel duplicates removed = 45) |
| 3 | Missing Meyer, van Witteloostuijn & Beugelsdijk (2017) reference | 🔴 ERROR | Added APA7 entry: *JIBS* 48(5) "What's in a p?" |
| 4 | 3 orphan references removed (Aiken & West 1991, Hayes 2018, Dawson 2014) | 🟡 WARNING | Removed (methodological boilerplate, never cited in body) |

## Outstanding for NCS — CRITICAL BLOCKING [✅ RESOLVED 2026-06-02]

| # | Issue | Severity | Status | Notes |
|---|---|:-:|:-:|---|
| 5 | **DAI×ICRV coefficient verification** | 🔴 CRITICAL | ✅ **VERIFIED** | Coefficient FOUND in `p7_coefs_all_models.csv` M11 row: `M11,dai_x_icrv,0.0524,0.0266,1.967,0.0492,*,28500`. β=0.0524 (rounds to +0.052 ✓), p=0.0492 (rounds to .049 ✓), SE=0.0266, t=1.967, N=28,500. Reviewer scan missed this row during inspection. Manuscript claim VERIFIED. No retraction needed. Desk-reject risk REMOVED. |

## Outstanding for NCS — HIGH

| # | Issue | Severity | Effort | Notes |
|---|---|:-:|---:|---|
| 6 | ICRV typology not differentiated from existing | 🔴 HIGH | 1d | ✅ **RESOLVED 2026-06-03**: ~270w "ICRV vs prior institutional typologies" passage added to P7 §2 after the ICRV definition paragraph. Explicitly positions ICRV against Hoskisson, Eden, Lau & Wright (2000) AMR four-region typology; Peng (2003) + Wright, Filatotchev, Hoskisson & Peng (2005) institution-based view; Whitley (1999) *Divergent Capitalisms*; Hoskisson, Wright, Filatotchev & Peng (2013) mid-range emerging multinationals; Cuervo-Cazurra, Ciravegna, Melgarejo & Lopez (2017) uncertainty-management capability. Framing positions ICRV as nested/complementary rather than competing. 4 missing refs added to thesis/04_references_apa7.md. |
| 7 | CIMT (Capability-Institution Mismatch Theory) absent | 🟡 MEDIUM | 1-2h | Portfolio claim names CIMT but manuscript has 0 hits. Decide with PGS.TS. Phan Anh Tú: (a) name CIMT in §5.1 contribution list, or (b) confirm CIMT retired in favor of "relocated-optimum + digital-for-institutional substitution" framing. |
| 8 | Sample attrition 82,302 → 28,500 (65% drop) not addressed | 🟡 MEDIUM | 2h | Add comparison table of dropped vs retained firm characteristics OR Heckman lambda from Vietnam companion (P3). |
| 9 | ICRV coding reliability not validated | 🟡 MEDIUM | 2h | Provide WGI correlation OR codebook reference. Limitations honestly flags as future work. |
| 10 | Country-clustered SE robustness column missing | 🟡 MEDIUM | 1h | 98 country-year clusters; HC1 preferred but reviewers likely demand cluster-robust as additional column. |
| 11 | Conceptual model figure missing | 🟡 MEDIUM | 30min | JIBS typically expects 1-2 conceptual figures; need "relocated-optimum logic" diagram. |
| 12 | Abstract conversion to structured Purpose/Design/Findings/Originality | 🟡 LOW | 30min | JIBS doesn't mandate structured, but most accepted papers use it. README claims structured. |

## 10 orphan references (4 cleaned in this session, 6 remaining)

Removed: Aiken & West (1991), Hayes (2018), Dawson (2014) — methodological boilerplate.

Still orphan (NCS to remove or cite):
- Cuervo-Cazurra et al. (2018)
- Contractor, Kumar & Kundu (2007)
- World Bank (2025a) DPI
- World Bank (2025b) VN economic update
- World Bank (2025c)
- World Bank (2026a) ID4D
- World Bank (2024) Justice

Several World Bank entries (2024-2026) are likely meant as macro evidence in §3 or §5; NCS should either add inline cites or remove from references.

## Verified UNCHANGED (canonical numerical alignment)

ALL M2/M5/M7/M8/M9/M10/M11 coefficients verified against `p7_coefs_all_models.csv`:
- M2: TP=37.1%, LM p<.001 ✓
- M5: TP=39.5%, adjR²=.671 ✓
- M11: TP=25.7%, LM p=.026 ✓
- M11 three-way FSTS×DAI×ICRV: −0.016, NS p=.910 ✓

**ONLY DAI×ICRV main-interaction coefficient β=+0.052/p=.049 unverifiable** (ISSUE #5 above).

## Publishability ceiling estimate

| Journal | After Top 3 Fixes | After All 12 Fixes |
|---|:-:|:-:|
| JIBS (ABS-4*, target) | 5-15% | 15-25% |
| **MIR (ABS-3, backup)** | 35-50% | **40-55%** |
| IBR (ABS-3, alt) | 30-45% | 35-50% |
| IJOEM (ABS-2) | 60-75% | 70-80% |

**Strategic recommendation per reviewer**: Conditional push to JIBS after CRITICAL coefficient verification (ISSUE #5). Prepare MIR + IBR fallback simultaneously. Do NOT submit to JIBS until ISSUE #5 is bulletproof.
