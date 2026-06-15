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

## EMPIRICAL VERIFICATION (2026-06-15) — real .dta, in the Claude Code container
Ran the P7 builder + estimator on the actual WBES `.dta` files in `data_wbes/raw_dta/`
(146 files) to verify the TCI construction directly, not just from code comments:

- **P7 analytical file exposes only `tci_cert`, `tci_foreign_tech`, `tci_z`** — no
  innovation/R&D columns. So `tci_z` is unambiguously the **2-item b8+e6** composite.
- **Japan-2025.dta** (339 vars, 2,168 firms) carries b8 and e6; on rebuild Japan enters
  the pool with a valid `tci_z` (27.7% certified, 3.1% foreign-tech). Japan IS eligible
  and IS included once the build is re-run.
- **Substantive result stable with Japan**: on the real-data rebuild, `tci_z` is positive
  and significant in every model (b = +0.31 … +0.55, p < .001); the baseline quadratic
  (M2) is inverted-U (turning point ~42%). The TCI-positive + inverted-U story holds.

### Reproducibility gap found (author's call — NOT auto-fixed)
The committed analytical file `data_wbes/p7/p7_pooled_clean.csv` is **stale**: 106,765
rows, 55 country labels, **no Japan**. A fresh build from the current `raw_dta/` gives
145,034 rows but only 42 countries (incl. Japan). Neither exactly matches the thesis's
reported P7 frame (88,869 firms / 103 economy-year pairs / 50 economies / M2 N=81,022),
and the country counts diverge (42 rebuild vs 55 committed), so the `raw_dta/` set in
this container is likely **not the full canonical set** the thesis numbers were locked
against. Recommendation: re-run build→estimate from the definitive raw set, refresh the
committed `p7_pooled_clean.csv`, and re-lock the P7 numbers so the package reproduces the
"incl. Japan 2025" claim. Nothing was overwritten here (doing so would desync the package
from the thesis's reported results). TCI construction (b8+e6) itself is confirmed.

### UPDATE — gap resolved by two build/run fixes + spec reconciliation
1. **Builder filename bug** (`01_build_p7_dataset.py`): the country/year regex could not
   parse hyphenated names, silently dropping 11 economies (Brunei-Darussalam, Hong-Kong,
   Korea-Republic, Kyrgyz-Republic, Lao-PDR, Papua-New-Guinea, Saudi-Arabia,
   Solomon-Islands, Sri-Lanka, Taiwan-China, Timor-Leste) and the Viet-Nam-2023 wave; the
   dedup/panel/skip logic only ran in the uploads branch. Fixed (parse_stem = first
   19xx/20xx token + letters-only country key; logic unified). Rebuild now yields **51
   economies incl. Japan-2025, 115 economy-year pairs, 2006–2026, complete-N 78,507**.
2. **Estimator control bug** (`02_run_p7_models.py`): the default control set included
   `foreign_own_pct` (b6a), only ~41% populated, which halved the controlled-model sample
   (≈79k → ≈32k) and made the FSTS curvature look "not confirmed". Removed from defaults.
3. **Reconciliation result (incl. Japan, thesis-consistent controls):** the fully-specified
   two-way-FE models reproduce the thesis: **M5 N=77,486 inverted-U TP 33.4% (p<.001);
   M10 N=74,398 inverted-U TP 34.4% (p<.001); TCI_z positive p<.001 in every model
   (+0.19…+0.26).** N is within ~2% of the thesis's M5 N=79,080; TPs sit in the thesis's
   reported range. ⟹ The thesis's substantive P7 claims (inverted-U + TCI-positive) **hold
   with Japan included**; the earlier apparent weakening was purely the two script bugs.
   Refreshed data + Japan-inclusive results are committed (`data_wbes/p7/`,
   `p7/replication/results_incl_japan/`). Thesis chapter numbers left as locked pending an
   author decision to formally re-lock to the Japan-inclusive figures.

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
