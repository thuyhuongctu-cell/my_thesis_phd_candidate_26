# P6 — Three-Level Meta-Analysis: OSF Materials

**Institutional Context, Digital Adoption, and the Internationalization–Performance Relationship: A Three-Level Meta-Analysis**

- **Authors:** Đỗ Thùy Hương (corresponding) · Phan Anh Tú — Can Tho University, Vietnam
- **OSF project:** https://osf.io/z37kn · **Registration DOI:** 10.17605/OSF.IO/Z37KN
- **Preregistered:** 2026-05-18 · **Target journal:** *Management Review Quarterly* (Springer)

---

## ⚠️ Status of these materials

These files correspond to the **registered baseline pool**: **k = 238 studies / K = 288 effect
sizes** (1982–2026), with the full three-level meta-analytic model already estimated
(pooled r̄ = 0.074, 95% CI [0.060, 0.088]; total I² = 62.4%).

A **formal WoS + Scopus search** to expand the pool to the preregistered target (**k ≥ 250**)
is **in progress**; the final expanded dataset and the manuscript preprint will be added to
this project once complete. The registered 20% double-coded inter-coder reliability protocol
was **not executed** — coding was single-coder (no second coder available), so no κ/ICC
statistics are reported; this is disclosed as a deviation in the manuscript, and a dual-coded
check is planned for the expansion. Treat the data and results here as the **baseline
snapshot**, not the final analysis.

---

## Folder structure

| Folder | Contents |
|--------|----------|
| `1_Preregistration/` | The preregistration record (study design, hypotheses H1–H3, analysis plan) — mirrors the registered version. |
| `2_Search_and_Screening/` | WoS + Scopus search strategy; PRISMA 2020 flow diagram; PRISMA 2020 checklist; screening template. |
| `3_Data/` | `p6_study_database_baseline.csv` (288 effect sizes, one row per effect); `codebook.md` (variable definitions + coding rules); `primary_studies_APA7.md` (references of included studies). |
| `4_Analysis_Code/` | `p6_parse_database.py` (builds the analysis CSV) → `p6_real_mara.R` (three-level MARA via **metafor**) → `generate_p6_figures.py` (forest + moderator plots). |
| `5_Results/` | `table1_baseline.csv` … `table5_sensitivity.csv` and `forest_data.csv` — the outputs reported in the manuscript baseline. |

## Reproducing the baseline analysis

```bash
# 1) Build the analysis dataset
python3 4_Analysis_Code/p6_parse_database.py        # → 3_Data/p6_study_database_baseline.csv

# 2) Run the three-level meta-analysis (R + metafor)
Rscript 4_Analysis_Code/p6_real_mara.R              # → 5_Results/*.csv

# 3) Render figures
python3 4_Analysis_Code/generate_p6_figures.py
```

**Data dictionary (key columns of the database):** `study_id`, `effect_id`, `author`, `year`,
`r` (effect size), `n` (sample size), `country`, `icrv`/`icrv_std` (institutional context-regime
vulnerability), `cdai` (country Digital Adoption Index, 0–1), `dpl` (Digital Platform Lifecycle
phase), `fp_type` (firm-performance measure), `include_flag`, `is_estimated`. Full definitions
in `3_Data/codebook.md`.

## How to cite

> Đỗ, T. H., & Phan, A. T. (2026). *Institutional context, digital adoption, and the
> internationalization–performance relationship: A three-level meta-analysis* [Preregistration].
> OSF. https://doi.org/10.17605/OSF.IO/Z37KN

## License

Recommended: **CC-BY 4.0** for documents/code and **CC0** for the coded dataset (effect-size
metadata only — no copyrighted full texts are redistributed). Contact: huongp1323001@gstudent.ctu.edu.vn
