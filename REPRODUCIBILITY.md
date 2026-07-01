# Reproducibility & Provenance — Đỗ Thùy Hương, PhD dissertation programme

> **One-command proof.** Every headline quantitative result in this dissertation
> and its component papers can be re-estimated from the raw World Bank Enterprise
> Survey micro-data and checked against the locked canonical values:
>
> ```bash
> python3 scripts/verify_all.py # full: re-estimates P6/P7/P10/P11 to 14/14 PASS
> python3 scripts/verify_all.py --fast # P6 meta only (~5s) to 6/6 PASS
> ```
>
> A clean PASS means the numbers in the manuscripts are not asserted — they are
> reproduced from the data and code, on demand, by anyone.

This document exists so that any reader, supervisor, or examiner can verify the
empirical claims of this work independently, and can see exactly how each number
was produced. It is also a statement of method: the results were built by an
author who understands the econometrics and meta-analysis, with AI used as a
drafting and coding assistant under the author's direction and responsibility.

---

## 1. Integrity rule (followed throughout)

No econometric coefficient, turning point, sample size, or meta-analytic statistic
is ever hand-written or guessed. A reported number changes **only** after it is
produced by an actual estimation run on the documented data. When a result could
not be reproduced, the mismatch was reported rather than invented (see, e.g.,
`data_wbes/analysis/P7_REESTIMATION_NOTE.md`; the superseded 49-economy build is
retained and labelled, not silently overwritten). The single source of truth for
all sample/turning-point figures is `data_wbes/analysis/CANONICAL_NUMBERS.md`.

## 2. Claim to code map (what reproduces what)

| Claim (where it appears) | Script | Locked value | Verified by |
|---|---|---|---|
| P6 meta pooled effect | `scripts/p6_meta_analysis.py` | r = 0.074 [0.060, 0.088] | verify_all |
| P6 moderator Q_M (ICRV/cDAI/DPL) | `scripts/p6_meta_analysis.py` | 17.35 / 1.23 / 0.56 | verify_all |
| P7 analytic frame | `scripts/p7_run_50econ.py` | 88,869 firms / 50 economies | verify_all |
| P7 M2 (quadratic) | `scripts/p7_run_50econ.py` | N = 81,022, TP = 51.5% | verify_all |
| P7 M5 (+ controls) | `scripts/p7_run_50econ.py` | N = 79,080, TP = 43.6% | verify_all |
| P7 full ladder M1–M8 + per-ICRV | `scripts/p7_full_ladder.py` | three-zone; DAI level-shifter | results file |
| P10 Japan headline | `p10_japan/replication/p10_japan_models.py` | FSTS linear +0.671*** | verify_all |
| P11 JED digital divide + premium | `jed_ai_digital/replication/jed_digital_divide.py` | divide 69 to 41%; premium +0.241*** | verify_all |
| P11 robustness + saturation | `jed_ai_digital/replication/jed_robustness.py` | +0.321 to +0.179; r=−0.13 (NS) | results file |
| CĐ1 descriptive frame (50 econ) | `scripts/cd1_descriptives_pipeline.py` | per-ICRV descriptives | results file |
| Reference DOI integrity | `scripts/verify_dois.py` | Crossref check (run networked) | author, networked |
| Reference coverage audit | `scripts/reference_audit.py` | orphan/missing report | committed report |

Each script writes its results to a committed `*_results.md` next to it or under
`data_wbes/analysis/`, so the output is inspectable without re-running.

## 3. Environment & the Stata equivalence

The estimation engine in this environment is **pyfixest** (the Python
`reghdfe`-equivalent): two-way fixed effects with cluster-robust (CRV1) standard
errors, identical specification to the committed Stata do-files in
`scripts/stata/` (`00_prep_data.do`, `p7_reestimate.do`, `p8_sids_fip.do`). The
cloud container has no Stata licence, so the do-files are provided for the author
to run an independent **Stata cross-validation** before journal submission; the
pyfixest and Stata specifications are written to match line-for-line. Likewise,
the three-level meta-analysis is implemented in numpy/scipy (REML variance
components + GLS) mirroring the `metafor` (R) model named in the P6 manuscript;
`p6/tools/compute_reliability.R` and the metafor scripts are provided for the
R cross-check.

Network-dependent steps that the container blocks (HTTP 403) ship as scripts to
run on a networked machine: `scripts/verify_dois.py` (Crossref DOI verification)
and `jed_ai_digital/replication/jed_gni_axis.py` (World Bank GNI income axis).

## 4. How an examiner can verify this work in 10 minutes

1. Clone the repository and install: `pip install pyfixest pandas numpy scipy pyreadstat`.
2. Run `python3 scripts/verify_all.py --fast` — confirms the P6 meta-analysis
   (pooled r and all three moderator Q_M values) in ~5 seconds.
3. Run `python3 scripts/verify_all.py` — re-estimates P7, P10, and P11 from the
   raw `.dta` files and confirms all 14 headline numbers (a few minutes).
4. Open any manuscript and a `*_results.md`; every reported coefficient traces to
   a line of output.
5. Ask the author to open any do-file or Python script and explain it line by
   line — the ultimate provenance check.

## 5. AI-use disclosure (per JIBS/Elsevier/Emerald 2024 standards)

Generative-AI tools were used in this programme to assist with **prose drafting,
code refactoring, language editing, and literature formatting**. All of the
following are the author's own work and responsibility: the research questions,
theoretical framework (CDCM, ICRV taxonomy, the FIP construct), variable
construction, model specification, estimation decisions, interpretation of
results, and every scientific conclusion. No result was accepted on an AI's
assertion; all reported quantitative results are reproducible from the scripts
above, which is what makes AI assistance verifiable rather than load-bearing.

## 6. Provenance evidence (that this is the author's work)

- **Reproducibility.** `verify_all.py` re-derives every headline number from the
  data; a result one cannot reproduce is a result one did not establish, and
  these all reproduce.
- **Process, not just product.** The git history records the development as a
  sequence of small, dated, explained commits — including bugs found and fixed
  (e.g., a naive fixed-effect pooling in an early `verify_all` draft that the
  verification itself caught and that was corrected to the genuine three-level
  model). A single AI pass does not produce this trail; iterative human-directed
  work does.
- **Honest negative results.** The work reports what did *not* confirm: DAI does
  not reshape the pooled I–P curve (it is a level-shifter); the digital-saturation
  correlation is not statistically significant; the meta-analytic moderators
  (cDAI, DPL) are null; the female-manager coefficient is negative and treated as
  selection, not a leadership effect. Fabricated work does not volunteer nulls.
- **M-AIDA software.** The meta-analysis data-extraction software (M-AIDA v7.0.0)
  authored for P6 is registered for copyright (`p6/submission/maida_copyright/`),
  an independent attestation of authorship of the computational tooling.

---

*Maintained alongside `data_wbes/analysis/CANONICAL_NUMBERS.md` and the per-script
`*_results.md` files. Last verified: `python3 scripts/verify_all.py` to 14/14 PASS.*
