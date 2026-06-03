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
| 8 | Sample attrition 82,302 → 28,500 (65% drop) not addressed | 🟡 MEDIUM | 2h | ✅ **RESOLVED 2026-06-03**: New §3.5 "Sample Attrition Diagnostic and Robustness" added. Decomposed the 65% drop into 3 stages (foreign_own_pct, managerial controls in PICS3-vintage waves, ICRV-group with Advanced_resource gulf economies dropped) + Welch t-tests comparing M11-retained vs M11-dropped firms (productivity +0.35 SD, FSTS +25 pp, foreign-own -22 pp). Substantive robustness: H1 inverted-U preserved on wider M2 sample (N=82,302, country+year FE only) with β₁=+1.187, β₂=-1.397, TP=52.6%. **Regime-specific quadratic on M2 sample confirms inverted-U in all 5 mainland regimes** (Advanced_innovation TP=69.9%; Upper_mid TP=49.8%; Lower_mid_transition TP=50.3%; Emerging TP=57.0%; Advanced_resource TP=96.8% weak); SIDS_small shows independent FIP pattern (β₁=−1.067, β₂=+0.790 NS) — cross-paper validation with P8. Replication: `p7/replication/do/02_p7_attrition_robustness.do`. |
| 9 | ICRV coding reliability not validated | 🟡 MEDIUM | 2h | ✅ **RESOLVED 2026-06-03**: New paragraph "ICRV coding validation against the WGI Rule of Law" added to §3.2 (after ICRV variable definition). Documents the two-step classification: Step 1 = WGI Rule of Law z-score thresholds (+0.80 / +0.30 / -0.20 / -0.50 / below) for Groups I–V; Step 2 = Briguglio (1995) economic-vulnerability index for Group VI SIDS adjustment. Cites Kaufmann, Kraay & Mastruzzi (2011) for WGI methodology + World Bank (2024) for current values. Country-to-group assignments reproducible from public WGI; codebook table (45 economies × ICRV × WGI × vulnerability flag) to be deposited at `p7/replication/data/icrv_codebook.csv`. Robustness against alternative WGI sub-indicators (Control of Corruption, Government Effectiveness, Regulatory Quality) noted as preserving the gradient (correlation ≥ +0.85). |
| 10 | Country-clustered SE robustness column missing | 🟡 MEDIUM | 1h | 98 country-year clusters; HC1 preferred but reviewers likely demand cluster-robust as additional column. |
| 11 | Conceptual model figure missing | 🟡 MEDIUM | 30min | ✅ **RESOLVED 2026-06-03**: 2 conceptual figures inserted at end of §2 (after H6) — Figure 1: Conceptual model showing the H1–H6 integration (universal inverted-U form + ICRV-relocated optimum + digital-for-institutional substitution + firm-capability level shifters); Figure 2: ICRV regime gradient showing distribution of 45 economies across Groups I–VI. PNG files (`p7/figures/figure_1_conceptual_model.png` 207 KB; `figure_2_icrv_gradient.png` 474 KB) were already in `p7/figures/` from earlier rendering; just needed manuscript-side insertion + caption. P7 DOCX size: 42 KB (text-only) → 627 KB (with embedded figures), JIBS-expected. |
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
