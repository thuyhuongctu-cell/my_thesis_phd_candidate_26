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

---

## Filter search for the N=209 sample (option a, exhausted 2026-06-19)

The committed P8 coefficients show **all models at N≈209** (M1=209, M3=205), so −1.339 is the
control-and-capability-complete sample, not a basic-controls sample. Testing every plausible
required-complete set on the **current** 7-Pacific SIDS data:

| Required-complete set | M1 β(FSTS_c) | N |
|---|--:|--:|
| basic controls only | +0.022 | 515 |
| + tci_z | +0.095 | 500 |
| + dai_z | +0.028 | 513 |
| + tci_z + dai_z (capability-complete) | +0.102 | 498 |
| **Paper** | **−1.339** | **209** |

**Conclusion.** No subset of the current data reproduces N=209, and every subset yields a
**positive** FSTS coefficient. The current raw SIDS `.dta` contains ~2.5× more complete firms
than the paper's sample (current ≈498–515 vs paper 209 for the same 7 economies and control set),
so the −1.339 result derives from a **data version not present in the repository** — the raw SIDS
`.dta` files themselves appear to have grown/changed since P8 was estimated. The N=209 sample
cannot be reconstructed here.

**Required from the candidate (only she can resolve this):** locate and commit the **exact P8
analytic `.dta`** (the ~209-firm capability-complete SIDS sample that yields β=−1.339), or the
exact raw SIDS `.dta` snapshot used. Until then the FIP result is not reproducible from the repo,
and a referee reproducing on current data obtains a positive coefficient. This blocks a credible
P8 submission and should be reconciled against thesis §4.7.

---

## Full re-estimation on current raw .dta (per candidate request, 2026-06-19)

7 Pacific SIDS built directly from the raw WBES `.dta` now in the repo; FSTS=(d3b+d3c)/100;
ln_labor_prod=ln(sales/l1); country+year FE; CRV1 cluster by economy.

| Model | β(FSTS_c) | p (cluster) | N |
|---|--:|--:|--:|
| M1 FIP (FE + controls) | **+0.352** | 0.322 | 610 |
| M2 quadratic | −0.688 | 0.472 | 610 |
| M3 + TCI + DAI | −0.915 | 0.405 | 588 |
| Year-FE only | +0.099 | 0.869 | 610 |
| Bivariate (no FE) | +0.480 | 0.433 | 1,471 |
| Exporters-only | +0.182 | 0.690 | 98 |
| **Paper (older data)** | **−1.339** | **<.001** | **209** |

**Definitive finding.** On the current data the FSTS–productivity coefficient is **non-significant
in every specification** (all p>0.30) and **sign-unstable** (M1 positive; M2/M3 negative). The
strong, highly significant FIP (−1.339, p<.001) **does not survive** — the relationship is
effectively null on the fuller current sample (N≈610–1,471 vs the paper's 209–959).

**Decision required (candidate).** The FIP contribution as stated (a *robust, significant* monotone
negative penalty) is not supported by the current repository data. Options:
1. **Locate & commit the original P8 `.dta`** (the ~209/959-firm version that yields −1.339) and
   treat the current larger `.dta` as a different/expanded download — then the paper stands on the
   pinned data and the discrepancy is a data-versioning note.
2. **Adopt the current data** and substantially revise P8 (and thesis §4.7): the SIDS I–P relation
   is *null/weak*, not a strong FIP — which is a different (weaker) contribution.
This is a substantive call for the candidate; no paper/thesis text was rewritten.

---

## Country-composition sensitivity (2026-06-19)

Re-ran the FIP under different SIDS economy sets on current raw .dta (FE + CRV1 by economy):

| Set | M1 β(FSTS) | p | N | #econ |
|---|--:|--:|--:|--:|
| 7 Pacific (Kiribati has no old wave → 6 in M1) | +0.352 | 0.32 | 610 | 6 |
| 8 econ: 7 Pacific + Timor-Leste (Comoros dropped) | +0.118 | 0.58 | 844 | 7 |

Note: **Kiribati has only the 2025 wave** (no foreign-ownership control → 0 firms in M1), so the
7-Pacific FIP is effectively estimated on 6 economies. Adding Timor-Leste (2009/2015/2021) raises
it to 7 economies / N=844. In every configuration the FSTS coefficient is **non-significant**
(M1 positive, M2/M3 weakly negative). Country composition does **not** recover the −1.339: the
root cause is the firm-count gap (current ≈610–844 vs paper 209), i.e., the current raw `.dta`
contain substantially more firms than the version the paper was estimated on.
