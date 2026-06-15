# Methodology & variable-description robustness review — 2026-06-15

Referee-lens audit of variable measurement (Chương 3 §3.3) and methodology
(§3.4–3.5), in response to the question of whether the variable descriptions and
methods are solid.

## Verdict
Design and variable measurement are **largely solid and publication-grade**. The
main weaknesses are **measurement-consistency / documentation** issues around the
TCI (and to a lesser extent DAI) construct, plus inherent observational-data
bounds that the thesis already handles honestly.

## Strengths (sound as written)
- DV (labour productivity) well-justified over ROA/ROE; cross-currency
  comparability handled correctly (z within country–year; PPP; ROS for levels).
- TCI vs DAI construct-purity logic (non-overlapping, formative-composite criteria
  per Coltman et al. 2008; Bharadwaj 2013; Verhoef 2021).
- Identification (§3.5.6): two-way FE + IV (first-stage F, over-id) + Oster (2019)
  δ-bounds + honest "inferential bounds" framing + triangulation of institutional
  moderation. Best practice for repeated cross-sections.
- Nonlinearity via Lind–Mehlum U-test (+ Haans et al. 2016), not just quadratic sign.
- Comprehensive robustness (measure swaps, subsamples, winsorization, VIF,
  Breusch–Pagan, leave-one-out, trim-and-fill).

## Fixed in this pass
1. **TCI item-code error (P5 China, §3.4.5.3 + its variable table):** TCI_full was
   written as mean(b8, e6, **b4, b7a**), but b4 (% female ownership) and b7a
   (manager experience) are **not** technological-capability items. Corrected to
   mean(b8, e6, **h1, h8**) = quality cert + foreign-tech + product innovation +
   R&D, matching P5's own manuscript definition (≥3 of {b8, e6, h1, h8}).
2. **§3.3.4** now states the TCI thin/full operationalization explicitly and notes
   that each component study's exact item set (and the schema-availability reason
   for differences) is given in its own data table.
3. **§3.5.6** measurement-invariance limitation across the 3 WBES questionnaire
   generations is now acknowledged; self-praising phrasing neutralised.

## RESOLVED (2026-06-15) — P7 TCI item set confirmed against real-data pipeline
The author confirmed P7 uses the real WBES data (50 economies, incl. Japan 2025).
Tracing the canonical pipeline settles the earlier ambiguity:
- `01_build_p7_dataset.py` (raw WBES .dta → `p7_pooled_clean.csv`, 50 economies)
  builds `tci_z` = standardized mean of **2 components: b8 (quality cert) + e6
  (foreign-licensed tech)**. `02_run_p7_models.py` reads exactly this file.
- `00_prep_prebuilt_data.py` (the "5-component" comment) is a **legacy 3-country
  (VNM/CHN/SGP) demo converter**, NOT in the thesis pipeline. Its header has been
  annotated as legacy/non-canonical.
- ⟹ Thesis §3.4.5.4 (P7: b8 + e6, 2-item thin) is **correct**; no estimate change.
  §3.3.4 reconciliation note updated from "needs checking" to "confirmed".

Remaining tidy-up (cosmetic, author's call, no numbers affected): some companion
**paper** variable tables phrase the 2-item TCI as "R&D (h8) + ISO (b8)" rather
than "cert (b8) + foreign-tech (e6)". Align each paper's prose to the b8+e6 pair
used by the estimation so the wording matches across documents.

## Other referee-sensitive points (design-inherent; already disclosed)
- Repeated cross-sections → firm-level causal inference is bounded (handled via
  FE/IV/Oster/bounds framing).
- IV exclusion restriction (industry-mean instrument for capability) is the usual
  vulnerability; first-stage F and over-id are reported.
- DAI is largely a Tier-1 binary (website), which saturates in Advanced economies
  (Digital Saturation Paradox); DAI_rich only for the 2024+ subset.

## Standing reproducibility items (execution, not design)
P6 detailed publication-bias/subgroup numbers need an R/`metafor` re-run to match
the script; inter-coder reliability κ pending; Stata cross-validation pending.
