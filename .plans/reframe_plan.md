# Plan — Narrative Reframing of the 6-Paper System + Dissertation (per Editor-in-Chief review)

## Context
An Editor-in-Chief-style peer review judges the econometrics/data as excellent but the **writing as
defensive**: the thesis apologizes for null findings and buries its bombshell results (53%
publication-bias inflation, the FIP, the export "cliff"/step-function) in sub-sections or as
"boundary cases." It asks for a shift from *defensive model-fitter* to *assertive theory-builder*,
**with a hard constraint: do NOT re-run any model — reframe language and argument structure only.**

User decisions: (1) plan first; (2) **"controlled boldness"** — keep methodological hedges so strong
claims survive real peer review. Calibration: several review actions are already partly done, so this
plan *elevates/sharpens* existing material and *adds missing theoretical mechanism labels* rather than
inventing claims. No numbers change anywhere.

## Guiding principles
1. Zero data/analysis change — prose, headings, ordering, framing only.
2. Controlled boldness with hedges. P6 "53%" → "trim-and-fill implies the pooled effect *may be*
   inflated ~53%" (Egger p=.057 borderline; Begg p=.0007). "Uppsala collapses" → "the Uppsala
   smooth-curve premise fails the boundary conditions tested here."
3. Bilingual parity — apply to both `_vi` and `_en`/`_clean`, consistent with dissertation chapters.
4. One unifying axis — **"Strategic Export Topography"**, **ICRV recast as an active *Transaction Cost
   Filter***, interacting with DAI.

## Per-target reframing (anchors verified)
- **Dissertation spine** (`thesis/chuong_1_gioi_thieu_vi.md`, `02_theoretical_framework_vi.md`,
  `chuong_2_tong_quan_tai_lieu_vi.md`, `chuong_5_ket_luan_de_xuat_vi.md`, `11_dissertation_positioning_vi.md`):
  vivid Asian export-heterogeneity hook; ICRV as Transaction Cost Filter; conclusion = ICRV governs
  where the I–P inflection sits; flagship contributions = FIP, cliff, 53% correction.
- **P6 meta** (`p6/21_p6_meta_vi.md`, `p6/p6_meta_manuscript_en.md`): elevate 53% to Intro headline
  (with Egger hedge); cDAI/DPL nulls → "Capability–Context Mismatch Theory".
- **P8 SIDS** (`p8/submission/world_development_package/p8_pacific_sids_vi.md`, `p8/p8_pacific_sids_en_clean.md`):
  add "Domestic Market Non-viability" + "Forced Survival Mandate"; negative slope = "Isolation
  Penalty" (TCE of isolation); DAI null via "Extreme Institutional Void".
- **P3 VN** (`p3/submission/p3_vietnam_vi.md`, `p3/p3_vietnam_en_clean.md`): promote "Digital Cliff
  Effect" step-function to central claim; DAI Tier-1 null → "Digital Saturation / Hygiene Factor".
- **P4 SG** (`p4/submission/p4_singapore_vi.md`, `p4/p4_singapore_en_clean.md`): "Fixed Transaction
  Cost Amortization" (TCE) explains TP≈82% (keep sparse-tail hedge); DAI = "Scale Lubricant";
  promote DAI×FSTS² (p=.005); Singapore = boundary stress-test.
- **P5 China** (`p5/submission/p5_china_vi.md`, `p5/p5_china_en_clean.md`): DICO stays a control
  (state crisply); 48% threshold = "Survival Constant" via Structural Over-embeddedness +
  Working-Capital Constraints; TCI = Level Shifter.
- **P7 capstone** (`p7/submission/jibs_package/p7_capstone_vi.md`, `p7/p7_capstone_en_clean.md`):
  female leadership = endogenous control (make explicit); "Institutional Slope" hook; four theories →
  one ICRV-centric architecture.

## Phasing (each phase = its own commit set)
- A: Dissertation spine. B: P6 + P8. C: P3 + P4 + P5. D: P7. E: rebuild all DOCX via
  `scripts/build_submission_package.sh` (pandoc 3.1.3), final commit + push.

## Verification
No-data-change gate (`git diff` prose-only); hedge check (grep 53/Uppsala/FIP/cliff); bilingual
parity; terminology consistency (FIP "gánh nặng…", ICRV crosswalk, new mechanism labels); Phase E
build + spot-check render.

## Out of scope
P4 Singapore replication data regen (no raw WBES); P4 76.4% vs ~82% (locked, keep 82% + TCE + hedge);
re-numbering P6 regimes to I–VI (declined; crosswalk note already added).
