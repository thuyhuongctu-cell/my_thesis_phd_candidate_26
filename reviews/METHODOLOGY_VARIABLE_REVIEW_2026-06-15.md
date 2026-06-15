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

## Open — needs author reconciliation against the estimation code (NOT guessed)
**TCI item set is described inconsistently across documents.** The exact set
should be reconciled to whatever the do-files/replication actually estimated:
- P7 replication (`p7/replication/00_prep_prebuilt_data.py`): comment says
  TCI_full is a **5-component** composite (cert + foreign-tech + product-innov +
  process-innov + R&D), `tci_z = zscore(TCI_full)`; but the cleaned pool
  (`data_wbes/p7/p7_pooled_clean.csv`) exposes only `tci_cert` + `tci_foreign_tech`.
- P7 manuscript variable table: "TCI_z = R&D (h8) + ISO certification (b8)" (**2-item**).
- Thesis §3.4.5.4 (P7): TCI_z = z-std(b8, e6) (**2-item, different pair**).
These three do not agree. Likewise the 2-item TCI differs across papers (P7/CĐ1
use h8+b8 = R&D+ISO; P8/§3.4.5.x use b8+e6 = cert+foreign-tech). Recommendation:
pick the authoritative item set from the actual estimation, then make §3.3.4,
§3.4.5.x, each paper's variable table, and the data dictionary agree.

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
