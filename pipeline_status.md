# Dissertation Pipeline Status

> LFE Academic Workflow — adapted from Library-First Engineering v2
> Project: PhD Dissertation — Đỗ Thùy Hương (VLUTE), supervised by PGS.TS. Phan Anh Tú (CTU)
> Branch: `claude/edit-vietnamese-academic-standards-xcAmn`
> Last updated: 2026-05-16

---

## Integrity Score: 🟢 GREEN

## Active Persona
**Archivist** (maintenance / inter-mission period)

## Session Count
**45** (hygiene audit due — completed this session)

---

## Paper Status

| Paper | Target Journal | Status | Last Action |
|-------|---------------|--------|-------------|
| P3 — Vietnam | JABS (Emerald) | ✅ Submission ready | IBR rejected → retargeted to JABS; lifecycle language fixed; Wu+Pisani §5 positioning added |
| P4 — Singapore | MIR (Springer) | ✅ Submission ready | Institutional transferability §5.1 added; P4 v8 integrated |
| P5 — China | IJOEM (Emerald) | ✅ Submission ready | Companion paper (P2 JFAR) disclosed in §6; v9 integrated |
| P6 — Meta-analysis | IBR (Elsevier) | 🟡 In progress | 9/11 Part 2 candidates confirmed in forest_data.csv (S204,S232,S210,S212,S222,S220,S108/223,S198,S126/216); S-116/117 (Barłożewski) still need r; S-62 citation wrong |
| P7 — Multi-country capstone | JIBS (Palgrave) | ✅ Submission ready | jibs_package built; §4.5.4 methodology added; H2 partial-confirmation corrected; dist/ synced |
| P8 — Pacific SIDS boundary | World Development (Elsevier) | ✅ Submission ready | world_development_package built; FIP theory; 9 SIDS economies |
| CĐ2 — Chuyên đề 2 | PhD Committee (VI) | ✅ Submitted v2.1 | APJM→JABS updated 2026-05-12 |
| CĐ1 — Chuyên đề 1 | PhD Committee (VI) | ✅ Complete | |

## Thesis Chapters

| Chapter | Status |
|---------|--------|
| `thesis/04_references_apa7.md` | ✅ 651 lines, v2.9 — all 110 primary studies present |
| `writing_guides/` | ✅ Author voice guide, academic standards, LFE framework |

---

## Pipeline Phase
**Between missions** — all active papers at submission-ready state. P6 manuscript in-progress pending manual r-value extraction.

## Completed This Session (2026-05-15)
- dist/ chapters (chuong_1/4/5) synced with thesis/ master; docx rebuilt via pandoc
- H2 hypothesis table corrected: "Xác nhận một phần" (TCI curvature moderation NS in P7 49-economy sample)
- server-anthropic: model IDs updated (claude-3-opus-20240229 → claude-sonnet-4-6 default)
- P6 manuscript end note: target journal corrected APJM → IBR
- thesis/00_optimal_plan_vi.md: P6/P7 status already updated (prior session)
- thesis/03_methodology_vi.md: §4.5.4 P7 already present (prior session)
- p7/submission/jibs_package/: all 4 files present (prior session)
- check-consistency.py: 0 issues confirmed

## Completed This Session (2026-05-16)
- p6/p6_wos_search_guide.md: WoS+Scopus queries updated to use wildcards (`internationaliz*`, `internationalis*`) — captures internationalized, internationalising, internationalizations (per user's WordHippo review of word forms)
- Repository-wide scan: 107→108 country-year fix (4 files, committed prior), ~172→K=288/k=238 fix (5 files), P3/P4 inversion in writing_guides/09 fixed — all confirmed clean
- I²=62.5% figure: consistent across all files (only ICBEF baseline 87.92% appears in correct context)
- pipeline_status.md: updated — S-62 and S-116/S-117 already resolved in forest_data.csv (both still listed as pending — now corrected)
- chuyen_de/20_cd1_cd2_review_report_vi.md: errata note added — historical 101.035/107 values preserved; correct values 101.185/108 noted (committed bf25711)
- thesis/11_dissertation_positioning_vi.md: 4 stale markers fixed — P5 🔄→✅, P5 "đang chạy"→"bản thảo hoàn chỉnh", P7 "MIR/JIBS"→"JIBS", P7 "đang thiết kế"→"bản thảo hoàn chỉnh" (committed 0788689)
- P3 abstract: trimmed from 304 to exactly 250 words for JABS structured-abstract limit (removed 40-word parenthetical, density sentence, minor cuts); JABS README word count updated "247→250"; blinded docx rebuilt via pandoc (committed 151a44b, 5ba7445)
- P5: Haans, Pieters & He (2016) 4-condition LM block added to §4.2 (C1–C4 for 2012, 2024, and pooled waves) + APA7 reference added (committed 5ba7445, 4ad334f)
- P7: TP formula corrected in §3.3 — removed erroneous `× SD(FSTS)` term (applies only to z-standardized FSTS; P7 uses mean-centering only); Haans (2016) 4-condition LM block added to §4.2 + APA7 reference added (committed 5ba7445, 4ad334f)
- thesis/11_dissertation_positioning_vi.md §7.4: P6 entry added (was missing); P8 garbled UTF-8 "bu1ea3n thu1ea3o..." fixed to "bản thảo hoàn chỉnh"; P3/P4 "vừa xong"→"hoàn chỉnh"; P7 "target JIBS"→"JIBS under revision"; timeline corrected 2026 H2/2027 H1 (committed 34fd730)
- P8 Haans et al. (2016) DOI added — all 5 papers P3–P8 now consistently have `smj.2399` DOI (committed ff28030)
- All 6 submission blinded docx rebuilt: P4 (5 commits stale), P5, P6 (k=238/K=288 stale), P7, P8 (committed 1558bea, ff28030, 66862e2, f0f4e4b)
- dist/ full rebuild: 7 thesis docx + 5 CTU chapters + 6 English manuscripts (P3–P8, P8 newly added) all rebuilt from current sources (committed af50029)
- dist/manuscripts/vi/: P3/P4/P5 vi docx rebuilt — were stale (dist built at 39287bc; sources updated in fa2142e table-numbering fix and 068c193 citation additions) (committed 955c8e6)
- writing_guides/09: stale target journals updated — P3 JFAR→JABS, P4 IBR→MIR, P5 APJM→IJOEM, P6 TBD→IBR (committed 7a0fc97)
- p6/21_p6_meta_vi.md: P3 self-citation journal corrected APJM→Journal of Asia-Pacific Business (committed 7a0fc97)
- P4: APA7 journal/volume italic format standardized across all 30 references (*Journal*, *Vol* → *Journal, Vol*); internal process notes removed from §4.4 body (committed a3eeabd, cb25e7c, 9e7cc55); MIR blinded docx and dist/en/ rebuilt
- P6 §3.1 search strategy: WoS/Scopus search string expanded — Asia-Pacific geographic filter removed; added FATA, geographic diversification, export ratio, foreign subsidiaries; added ABI/INFORM, Business Source Complete, ScienceDirect, SpringerLink, Emerald Insight to database coverage; ProQuest Dissertations removed
- P6 §3.2 eligibility criteria: "Publication type" row added — main corpus restricted to peer-reviewed journal articles + articles in press with DOI; dissertations/theses/working papers/conference papers excluded from primary analysis
- P6 §3.2: peer-review restriction paragraph inserted after eligibility table (exact text per user specification)
- p6/p6_wos_search_guide.md: WoS and Scopus queries expanded to match manuscript §3.1; supplementary databases section added (Phần 3); "Non-peer-reviewed publication" exclusion reason added to Level 1 screening table; section headers renumbered (4→5, 5→6)
- P6 IBR blinded docx rebuilt from updated manuscript source
- p6/p6_prisma_flow.md v2.2: IDENTIFICATION box updated (5 supplementary DBs added, scite.ai→Google Scholar); Level 1 screening: "Non-peer-reviewed publication" exclusion added; §2 WoS+Scopus queries updated to expanded global strings; §3 exclusion criterion 6 expanded; INCLUDED breakdown updated; version history logged (committed eccd3d8)
- p6/21_p6_meta_vi.md v1.6: §3.1 supplementary search rewritten (5 databases + Google Scholar forward citation, 5 anchor metas); footer updated — scite.ai→forward/supplementary screen; peer-reviewed-only corpus note added (committed 7dc2e48)
- dist/manuscripts/en/p6_meta_en_clean.docx rebuilt — was stale since search protocol expansion (committed 28cb442)
- p6/p6_study_database_coded.md: S236/S237/S238 table rows added; S85/S195/S196 notes corrected; all 238 studies now documented in markdown (committed cfb97ab)
- dist/chuyen_de_1/: CĐ1 docx (57KB) and CĐ2 docx (790KB with figures) first-ever built from source files (committed 39ac92b)
- dist/submission_packages/CD1+CD2 rebuilt — stale since 01aad57 (committed 09cdcd3)
- p4/submission/mir_package/01_manuscript_blinded.docx rebuilt — 3 commits stale: APA7 refs, §4.4 process notes removed (committed 6e8bb98)
- build_ctu_docx.sh: P8 entry added; P3 and P6 fixed to use --resource-path=. from their own dir (figures were being silently dropped in root-level builds); P3 dist and JABS blinded docx rebuilt with all 6 figures (1.6MB); P6 dist and IBR blinded already had correct sizes (committed 1676f1b, 50b74ab, 7282d4c)
- P3 Haans ref title: "inverted-U-shaped"→"inverted U-shaped" to match canonical form in thesis/04_references_apa7.md and P4/P5/P7/P8 (committed 1676f1b)
- CĐ2 B.1: H3 split into H3a/H3b (CDCM regime-contingent moderation) + H3c discriminant validity — section heading, hypothesis text, abstract VI+EN, narrative summary, theory table all updated (committed 53fd628)
- CĐ2 B.2: Bảng 2.13 framework comparison inserted (7 frameworks × 8 dimensions; CĐ2 only framework with all 8 ✓; JFAR row added); DANH MỤC BẢNG updated (committed dbdf466)
- CĐ2 B.6: H4 split into H4a/H4b/H4c (experience, education, gender) — heading, variable table, M5 description, model table, both abstracts updated (committed 1fccdc0, 591ec06)
- CĐ2 B.8: Phụ lục D Stata cluster SE code block added — Cameron & Miller (2015) citation; 235 clusters; HC1 vs cluster SE note; M2–M5 and H4a/H4b/H4c runs (committed 1fccdc0)
- Khatua et al. (2024): APA7 format corrected to advance online publication in thesis/04_references_apa7.md (committed 53fd628)
- thesis/04_references_apa7.md v2.8: Pirlea et al. (2026) "Global Progress" chapter entry added (Section P); version header updated (committed 7a821ce)
- P8 §1: Pirlea et al. (2026) in-text citation added — SIDS development lag context ("progress slowest on record in 15/26 benchmarks; SIDS disproportionately affected") (committed 7a821ce)
- P8 §3.2: Mahler, Wang & Weber (2026) in-text citation added — DAI null context ("5% LIC basic digital skills; 77% HIC data center capacity") (committed 7a821ce)
- P8 references: Mahler et al. (2026) AI atlas + Pirlea et al. (2026) global-progress added alphabetically (committed 7a821ce)
- dist: P8 docx + source_md snapshot + world_development_package/01_manuscript_blinded.docx rebuilt (committed 38c3fac)
- **11 PDFs uploaded by user assessed for dissertation relevance** (16/05/2026 session continuation):
  - 5 applicable: Agarwal+Barattieri+Mattoo WPS11352 (P3); Barattieri+Mattoo+Signoret WPS11354 (P3); Mahler+Serajuddin+Wadhwa+Yonzan WPS11350 (P8); Kim+Kumar+Ramalho+Russell WPS11279 (CD2); Geginat+Ramalho WPS7460 (P8/CD1)
  - 4 not cited: Gould et al. 2013 (South Asia FDI); Barattieri et al. 2014 (M&A services); de Nicola et al. 2026 (robots+FDI); WBG Annual Report 2025 (general)
  - 2 moderate: Kee et al. 2025 (P5 optional); WBG Annual Report 2025 (general background)
- thesis/04_references_apa7.md v2.9: Section T added (5 new entries); Mahler disambiguation note; usage guide updated
- p3/p3_vietnam_en_clean.md §5 Discussion: Agarwal et al. (2026) ascending-limb corroboration added; Barattieri et al. (2026) trade liberalization macro evidence added in §5.5
- p8/p8_pacific_sids_en_clean.md §1: Mahler, Serajuddin, Wadhwa & Yonzan (2026) slowest development pace added (as Mahler et al. 2026b to disambiguate from Mahler, Wang & Weber 2026 Atlas chapter)
- chuyen_de/cd2/00_cd2_ctu_final_vi.md §3.3 Tầng 3: Kim et al. (2026) institutional capacity framework added after North (1990) definition
- Rebuilt: dist/manuscripts/en/p3_vietnam_en_clean.docx, p8_pacific_sids_en_clean.docx, dist/submission_packages/cd2/CD2_submission_final.docx
- **P6 S238/S85 duplicate resolved** (16/05/2026): S238 = Cho & Lee (2018) confirmed duplicate of S85 (same r=−0.029, same n=232, Korea family firms); S238 row removed from forest_data.csv + p6_study_database_coded.md; S85 cDAI corrected M→H; k=237, K=287 updated across p6_meta_manuscript_en.md, 21_p6_meta_vi.md, p6_prisma_flow.md, p6_study_database_coded.md; dist/manuscripts/en/p6_meta_en_clean.docx rebuilt (1.25MB); submission/ibr_package/01_manuscript_blinded.docx rebuilt (1.2MB); p3/submission/jabs_package/01_manuscript_blinded.docx rebuilt (1.6MB, stale since Agarwal+Barattieri citations added)

## Coordination Files
None active in `.plans/` (clean state).

---

## Pending (external data required)
1. P6: PRISMA formal search (WoS+Scopus) — fill in `p6/p6_wos_search_guide.md` [TBD] counts after manual search
2. P6: Part 5 Nhóm A studies [S-140]–[S-144] — PDFs needed to extract r values before assigning S239–S243

~~P3: Lind-Mehlum 4-condition full report~~ ✅ RESOLVED (§4.2, C1–C4 per Haans et al. 2016, commit 5f8ac68)  
~~P3: Cubic FSTS³ test with AIC/BIC~~ ✅ RESOLVED (§4.5, β=-1.763 p=.287, AIC/BIC favour quadratic)  
~~P3: Marginal effects table 10/30/50/70%~~ ✅ RESOLVED (Table 4b in §4.2, β1=0.984 β2=-1.909)  
New skill installed: `stata-khong-license-giai-phap` (16/05/2026) — Python/R econometrics alternatives

~~P6: r-values for S-116/S-117~~ ✅ RESOLVED (S236: r=−0.10; S237: r=−0.04)  
~~P6: S-62 citation correction~~ ✅ RESOLVED (Lee et al. 2014, IJCHM, US hotels, fp_type=MKT)  
~~P6: S236/S237/S238 missing from study database coded.md~~ ✅ RESOLVED (commit cfb97ab — rows added; S85 cDAI M→H corrected; S195/S196 cross-referenced to their subsample counterparts)  
~~P6: S238 vs S85 duplicate review~~ ✅ RESOLVED (16/05/2026 — S238 confirmed duplicate of S85 [Cho & Lee 2018, same r=−0.029, same n=232]; S238 removed from forest_data.csv + study_database_coded.md; S85 cDAI corrected M→H; k=237, K=287; all P6 files + dist docx updated)

## Logic Sovereignty Anchors (locked — never change without full grill phase)
- P3: TP pooled = 39.7% (range 39–46%) | TCI β = 0.179 | DAI IV β = 0.018 | N = 2,958
- P4: DAI×FSTS² = +3.119 (p=.005) | TP ≈ 88.6% | N = 623
- P5: TP 2012 = 49.4% | TP 2024 = 47.2% | Paternoster p = .545 | N = 4,559
- P7: TP ≈ 36% (pooled M2, N=84,910) | DAI β=+0.155 (p<.001) | ICRV gradient TP 28%→55% | N=84,910–38,342
- P8: FIP β = −0.404 (p=.032, country FE) | no quadratic turning point | N=1,469 (9 Pacific SIDS)
- CĐ2: N = 101,185 | 47 economies | 108 country-year pairs | 14 waves

---

## LFE Skill Reference
| Skill | When to invoke |
|-------|---------------|
| `lfe-research-architect` | New paper design, section restructuring, peer review response planning |
| `lfe-paper-writer` | Executing an approved writing plan (reads `.plans/active_plan.md`) |
| `lfe-academic-reviewer` | Verifying manuscript against language rules, APA7, journal compliance |
| `lfe-reference-archivist` | Post-review: sync bibliography, regenerate docx, commit+push |
| `lfe-quick-fixer` | Typos, minor edits, date updates (max 3 files, max ~50 words) |

