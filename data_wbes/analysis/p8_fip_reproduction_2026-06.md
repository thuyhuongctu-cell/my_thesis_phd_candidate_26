# P8 FIP (−1.339) — reproduction check from raw .dta (2026-06-19)

**Task.** Verify whether the P8 headline result — Forced Internationalization Penalty,
M1 β(FSTS) = **−1.339** (p<.001), N=209, 7 Pacific SIDS — reproduces on the current
canonical data (option a, after the committed `p7_pooled_clean.csv` was found to give +0.022).

**Method.** Built the 7 Pacific SIDS directly from the raw WBES `.dta` files now in the repo,
using the documented P7/P8 construction (`ln_labor_prod = ln(sales/l1)`; FSTS variants
`(d3b+d3c)/100` and `d3c/100`; controls `ln_size, firm_age (year−b5), foreign_own (b6a)`;
country + year FE; OLS). Same estimator as `run_p8_7pacific.py`.

**Result — the FIP does NOT reproduce; the sign is positive on the current data:**

| Source / construction | M1 β(FSTS_c) | N |
|---|--:|--:|
| Committed result CSV (paper) | **−1.339** (p<.001) | 209 |
| Re-run of `run_p8_7pacific.py` on current `p7_pooled_clean.csv` | **+0.022** (p=.96) | 515 |
| Raw `.dta`, FSTS = (d3b+d3c)/100 | **+0.352** | 610 |
| Raw `.dta`, FSTS = d3c/100 | **+0.437** | 610 |
| (cross-ref) P7 canonical z-spec SIDS linear (`p7_run_50econ.py`) | −0.098 (ns) | 1,818 |

Restricting to pre-2023 waves does not change this (the complete-control sample is already
pre-2023; the 2023–2025 SIDS waves lack the foreign-ownership control).

**Reading.** The strongly negative FIP coefficient (−1.339, N=209) does **not** survive on the
current data under any faithful construction: the level-spec coefficient is **positive**
(+0.02 to +0.44) on the larger N=515–610 sample, and only weakly negative and non-significant
(−0.098) in the within-economy-year z-spec. The sign of the SIDS FSTS–productivity slope is
therefore **sample/construction-dependent**, and the paper's −1.339 appears specific to the
smaller N=209 sample whose exact definition cannot be reconstructed from the current files.

**Implication (high priority, candidate action).** Before submitting P8 (World Development) or
defending the FIP contribution:
1. **Identify and pin** the exact analytic sample (and variable construction) that yields
   β=−1.339 / N=209, and commit that `.dta` as the P8 replication data.
2. **Re-examine robustness:** if the FSTS coefficient is positive on the fuller current sample,
   the FIP claim needs either a justified sample restriction (why N=209, not N≈610) or a
   reconsideration. A referee who reproduces on the committed data currently obtains a *positive*
   coefficient.
3. The thesis §4.7 FIP and the few-cluster note added to the P8 manuscript both rest on −1.339
   and should be revisited once (1)–(2) are resolved.

**No thesis/manuscript number was changed** — this is a reproduction diagnostic for the candidate.
