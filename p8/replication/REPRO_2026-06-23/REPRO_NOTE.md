# P8 (Pacific SIDS) — Reproduction Note, 2026-06-23

Independent re-run from raw WBES `.dta`, hardening reproducibility of the **redesigned**
(dissolution-framing) P8 study. This run regenerates the analytic dataset and estimates
from source; it does not rely on any pinned intermediate.

## Command

```bash
python3 p8/replication/build_and_run_p8_7pacific.py
```

Environment: pandas / numpy / pyreadstat / statsmodels / scipy. No `linearmodels`; the
runner uses a pure-Python wild-cluster restricted bootstrap (Cameron–Gelbach–Miller 2008,
Rademacher weights, null imposed via FWL residualisation), B = 9,999, seed 20260619.
Inference: two-way FE (economy + year), CRV1 cluster by economy (7 clusters), plus the
wild-cluster bootstrap appropriate for the 7-cluster design.

## Sample

- **N = 1,450** firms, **7 clusters** (genuine Pacific SIDS): Fiji, Kiribati, Papua New
  Guinea, Samoa, Solomon Islands, Tonga, Vanuatu. **Timor-Leste EXCLUDED** (not a World
  Bank Pacific Island Country / not a UN Pacific SIDS).
- Exporters (FSTS > 0): 212 (14.6%); mean FSTS = 0.054.
- Per-economy N: Fiji 175, Kiribati 149, PNG 155, Samoa 228, Solomon 257, Tonga 297,
  Vanuatu 189.
- Estimation subsamples after listwise deletion: M1/M2 N = 1,434; M3 N = 1,389.

## Headline finding — the inverted-U DISSOLVES (N = 1,450)

| Model | Term | β | SE (CRV1) | p (CRV1) | p (wild) |
|---|---|--:|--:|--:|--:|
| M1 (linear) | FSTS_c | **−0.085** | 0.151 | 0.572 | **0.656** |
| M2 (quadratic) | FSTS_c | −0.567 | 0.281 | 0.044 | **0.088** |
| M2 (quadratic) | FSTS_c² | **+0.696** | 0.357 | 0.051 | **0.082** |
| M3 (+capability) | FSTS_c | −0.852 | 0.248 | 0.001 | 0.024 |
| M3 (+capability) | FSTS_c² | +1.051 | 0.341 | 0.002 | 0.056 |
| M3 (+capability) | TCI_z | +0.064 | 0.027 | 0.018 | 0.036 |
| M3 (+capability) | DAI | +0.157 | 0.089 | 0.076 | 0.102 |

Interpretation (the headline): across the full sample the export-intensity slope is
statistically indistinguishable from zero (wild-cluster p ≈ .66), and the curvature term
is only marginally significant and **positive** (convex), not concave (wild-cluster p ≈ .082).
The canonical inverted-U **dissolves** via sign reversal that is not significant. M3 hints
at a more strongly positive (convex) curvature once capability is held constant, presented
cautiously, not as a confirmed reversal. Technological capability raises the productivity
*level* (p ≈ .036) but does not restore the inverted-U.

## Match vs CANONICAL_NUMBERS.md

`data_wbes/analysis/CANONICAL_NUMBERS.md` (locked 2026-06-13, Timor scope updated 2026-06-19):
SIDS_small / P8 7-Pacific — N = 1,450; linear slope −0.085 (p_wild = .66); curvature
+0.696 (p_wild = .082).

| Quantity | Canonical | Reproduced | Match |
|---|---|---|:--:|
| N | 1,450 | 1,450 | **Y** |
| Clusters | 7 | 7 | **Y** |
| Linear FSTS_c slope | −0.085 | −0.085 | **Y** |
| Linear p_wild | ≈ .656 | 0.656 | **Y** |
| Quadratic FSTS_c | −0.567 | −0.567 | **Y** |
| Quadratic FSTS_c² | +0.696 | +0.696 | **Y** |
| Quadratic p_wild (FSTS_c / FSTS_c²) | ≈ .088 / .082 | 0.088 / 0.082 | **Y** |

**All canonical targets reproduced exactly. No discrepancies.**

## Important — β = −1.339 is SUPERSEDED (limiting case only)

The β = −1.339 "Forced Internationalization Penalty" (SE 0.386, p < .001; PPP-level spec,
N = 209 complete cases / full sample N ≈ 959) is the **OLD / fragile** estimate. It survives
only on a handful of island economies with complete firm-level data (≈ 3 exporting economies,
N ≈ 209) and is sensitive to that small set. It must be treated **ONLY as a theoretical
limiting case** (the FIP bounding concept), **NEVER as the headline**. The headline for P8
is the **dissolution** of the inverted-U at **N = 1,450** (slope ≈ 0, curvature positive and
only marginal). Any package, manuscript, or verify note that presents −1.339 / N = 959 as the
P8 result is superseded and must be replaced by the redesign (dissolution) framing.

## Cross-reference

- Redesign manuscript: `p8/p8_pacific_sids_redesigned_en.md`
- Live submission target: `p8/submission/world_development_redesign/`
- Design + verification: `p8/P8_REDESIGN_2026-06.md`
- Prior cross-check: `reviews/REPLICATION_CROSSCHECK_2026-06-23.md`
- Pinned analytic dataset (this run): `p8/replication/data/p8_7pacific_pinned.csv`
- Model CSV (this run): `p8/replication/reanalysis_7pacific/p8_7pacific_models.csv`
