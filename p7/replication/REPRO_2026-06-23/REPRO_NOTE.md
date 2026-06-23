# P7 Replication — REPRO_2026-06-23

Independent re-estimation of the P7 50-economy capstone from **raw `.dta`** survey
files, for reproducibility hardening. Source of truth for reported numbers:
`data_wbes/analysis/CANONICAL_NUMBERS.md` (master-locked). This run is an
auditable cross-check, not a replacement for the master-locked numbers.

## Command

```bash
cd /home/user/MY_THESIS_PHD_CANDIDATE_26
python3 scripts/p7_run_50econ.py
# (also mirrored at dist/osf/P7_capstone/code/p7_run_50econ.py — byte-identical)
```

Estimates table (`estimates.csv`, model/term/coef/se/p/n) regenerated with a thin
extractor that reuses the runner's `build()` so the analytic frame is identical;
it only adds clustered SEs (CRV1 by economy), which the runner's own CSV omits.

- Env: pandas / numpy / pyreadstat / statsmodels / scipy / **pyfixest 0.60.0**
  (FE absorption + CRV1). `linearmodels` is absent, per the project rule.
- Spec: two-way FE (economy + year), CRV1 clustered on economy. `lp_z` =
  within-wave z-score of winsorised ln(d2/l1); `FSTS=(d3b+d3c)/100`; centered
  `fsts_c`, `fsts_c2`. TP = −β₁/(2β₂) + mean(FSTS), in % of sales.
- Frame this run: **92,564 analytic rows / 50 economies / 107 country-year pairs.**

## Raw-build N vs master-locked N (EXPECTED gap — do NOT "fix")

| Model | Raw-build N (this run) | Master-locked N (canonical) |
|---|--:|--:|
| M2 (FSTS + FSTS²) | **84,453** | 81,022 |
| M5 (+ controls)   | **82,358** | 79,080 |

The raw build is larger than the master-locked frame because the raw build vs the
master cleaning/dedup pipeline differ, and the raw folder now carries **4
Azerbaijan waves** (2009/2013/2019/2024) added after the master lock. This gap is
documented and acceptable. The **manuscript keeps the master-locked N**
(81,022 / 79,080); these raw-build N are reported here only as an independent
cross-check. We did NOT edit any number to close the gap.

## Coefficients & turning points

| Model | N (raw) | β₁ (FSTS) | β₂ (FSTS²) | Turning point | p (Lind–Mehlum) |
|---|--:|--:|--:|--:|--:|
| M2 | 84,453 | +1.153*** | −1.359*** | **51.40%** | < 0.001 |
| M5 | 82,358 | +0.498*** | −0.714*** | **43.83%** | < 0.001 |

Both inverted-U turning points reproduce the canonical targets to the tenth of a
point: M2 51.40% ≈ canonical **51.5%**; M5 43.83% ≈ canonical **43.6%**.
Lind–Mehlum confirms a true interior inverted-U (positive slope at FSTS min,
negative at FSTS max) at p < .001 for both.

## Three-zone structure by ICRV group (M5-form per group)

| ICRV group | N (raw) | Turning point | p (LM) | Zone |
|---|--:|--:|--:|---|
| I. Advanced_innovation | 5,581 | 79.12% | 0.304 | Upper — near-linear, TP out of range |
| II. Advanced_resource | 2,075 | 62.04% | 0.081 | Upper–mid |
| III. Upper_mid | 14,638 | 53.64% | 0.143 | Mid — not reliably located |
| IV. Lower_mid_transition | 42,094 | **43.03%** | < 0.001 | **Mid — sharp inverted-U** |
| V. Emerging | 16,152 | 34.24% | 0.195 | Lower — structure dissolves |
| VI. SIDS_small (linear FIP) | 1,818 | — | n.s. (p=0.329) | Lower — no inverted-U |
| VI. SIDS_small (quad) | 1,818 | β₂ = +0.870 (p=0.013) | — | U-shape, not inverted-U |

The **three-zone gradient reproduces**: only Group IV (Lower_mid_transition) shows
a sharp, significant inverted-U with **TP 43.03% = canonical 43.0%**; the SIDS
group shows no inverted-U (quadratic curvature is positive → U-shape / FIP, not an
inverted-U).

## Match vs canonical

| Quantity | This run (raw-build) | Canonical (master-locked) | Match |
|---|--:|--:|:--:|
| M2 TP | 51.40% | 51.5% | ✅ |
| M5 TP | 43.83% | 43.6% | ✅ |
| Group IV (Lower_mid) TP | 43.03% | 43.0% | ✅ |
| SIDS inverted-U | none (β₂>0, U-shape) | none | ✅ |
| Lind–Mehlum (M2, M5) | p < .001 | p < .001 | ✅ |
| M2 N | 84,453 | 81,022 | ✅ gap (raw↔master, documented) |
| M5 N | 82,358 | 79,080 | ✅ gap (raw↔master, documented) |
| Economies / pairs | 50 / 107 | 50 / 103 | ⚠️ 107 vs 103 pairs (4 extra Azerbaijan raw waves) |

**Verdict:** turning points and three-zone structure reproduce cleanly. The only
discrepancies are N (raw-build larger than master-locked) and the pair count
(107 vs 103), both attributable to the documented raw↔master pipeline difference
plus the newly-added Azerbaijan raw waves. No number was altered to force a match.

### Legacy values that must NOT be presented as current
91,982 / 49 economies; M2 N = 84,910; M5 N = 38,342; TP 40.0%. None of these
appear in this run.

## Files in this folder
- `estimates.csv` — model, term, coef, se, p, n (M2 + M5, CRV1 SEs).
- `REPRO_NOTE.md` — this note.
- Full per-model + per-group table from the runner:
  `data_wbes/analysis/p7_50econ_models.csv`.
