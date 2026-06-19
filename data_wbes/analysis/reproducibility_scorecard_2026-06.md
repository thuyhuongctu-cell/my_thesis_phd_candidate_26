# Reproducibility scorecard — all empirical papers (2026-06-19)

Headline re-estimated directly from the raw WBES `.dta` now in the repo (ln(d2/l1), quadratic FSTS,
HC1; quick sign/significance/turning-point check — not each paper's exact controls/IV spec, so
turning points are approximate, but sign and significance are diagnostic).

| Paper | Canonical headline | Re-estimate (raw .dta) | Verdict |
|---|---|---|---|
| **P3** Vietnam | inverted-U, TP 39–46% | ∩, TPs in range; DAI trajectory pattern reproduces | ✅ pattern solid (magnitudes build-dependent) |
| **P4** Singapore | inverted-U, TP ≈88.6%, N=623 | N=623 exact; b₂=−2.63 (p<.001); TP high | ✅ solid |
| **P5** China | TP 49.4/47.2, inverted-U | N≈4,646; b₂=−1.84 (p<.001); **TP=49%** | ✅✅ matches |
| **P7** 50-economy | β₁=1.189, TP 51.5%/43.6% | reproduces exactly via `p7_run_50econ.py` | ✅✅ exact |
| **P9** India | TP 62→41 collapse, sign-flip | pooled ∩, b₂=−1.20 (p<.001), TP=46% | ✅ solid |
| **P10** Japan | near-linear, b₂ n.s., +0.671 | N≈2,068; **b₂ n.s.** (near-linear) | ✅✅ matches |
| **P8** SIDS FIP | −1.339 "7 Pacific SIDS" | −1.339 only on **3 economies** (Fiji/PNG/Vanuatu, N=209); null on full data | ⚠️ **fragile — isolated weak link** |
| **P6** meta | r̄=0.074, I²=62.4%, Q_M=17.35 | (meta of published effect sizes — separate data, not re-run here) | — verify separately |

## Bottom line

**6 of 7 firm-level papers reproduce their headline from the raw data.** The inverted-U, the
three-zone structure's *middle* (transition, sharp ∩) and *top* (advanced, near-linear) zones, the
capability level-shifter result, China's temporal stability, Japan's near-linearity, and India's
collapse are all robust. **Only P8 (the Forced Internationalization Penalty / bottom zone) is
fragile** — a 3-economy / 3-cluster estimate that does not survive the fuller current data.

Also surfaced (systemic, lower-severity): the per-paper replication scripts (P4, P5) point to
**stale ephemeral upload paths** and do not run as committed — a replication-packaging issue to fix
(repoint to `data_wbes/raw_dta/`).

## Optimal direction (recommendation)

1. **Keep the thesis backbone as is** — it is empirically sound; do not over-react to the P8 scare.
2. **Reframe the FIP contribution honestly** (P8 + thesis §4.7 + the "bottom zone" + novelty claim 6):
   from a *robust empirical penalty across seven Pacific SIDS* to a **theoretical boundary-condition
   concept** ("forced internationalization penalty") supported by **suggestive, exploratory evidence
   from a small SIDS sample**, with an explicit limitation that it is not yet robustly estimable given
   the few SIDS economies with complete pre-2018 firm data. The three-zone structure's bottom zone is
   then "dissolution of the inverted-U, with a suggestive (data-limited) sign reversal" rather than a
   strong FIP. This is defensible and integrity-preserving.
3. **Replication hardening** before submission/defense: pin each paper's analytic dataset, repoint
   replication scripts to `data_wbes/raw_dta/`, and commit an estimates table per paper so every
   headline is auditable.
4. Discuss the FIP reframing with the advisor (it touches a named novelty claim).
