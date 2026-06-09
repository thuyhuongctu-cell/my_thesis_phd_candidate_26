# P6 Meta-Analysis — Submission-Readiness Checklist (PRISMA · ICR · OSF)

**Purpose:** close the gaps that currently block journal submission of P6 (JIM first target).
**Status legend:** ✅ done · ⏳ author action required · 🤖 tooling ready in repo

The meta-analytic *results* are final and consistent (k = 238 studies, K = 288 effects; pooled r = 0.074; `p6/data/p6_study_database.csv` + `p6/results/`). What remains are the **reporting-standard artefacts** that a reviewer will require. None can be fabricated; each needs the author to run a provided tool and paste the outputs.

---

## 1. PRISMA flow  ✅ RESOLVED via honest reframe (2026-06-09)
All four submission packages (jim/ibr/jwb/apjm + apjm supplementary) were reframed from an exhaustive-WoS/Scopus-census narrative (with `[TBD]` intermediates) to a **systematic-but-bounded, citation-anchored search** (backward/forward citation from 5 anchor meta-analyses + database supplement), reported under the PRISMA 2020 "studies identified via other methods" variant. The synthesized set is the data-backed **k = 238 / K = 288**; **no `[TBD]` placeholders remain**. The ibr/jwb stale **237/287** totals were also corrected to 238/288 throughout.

> Optional upgrade (author): if a full formal WoS/Scopus census is run later, the flow can be re-expressed with stage-level counts (tooling: `p6/tools/28_extract_wos_scopus_locally.py`; search strings in `p6/osf/P6_OSF_Preregistration_Template.md` §6). This is **no longer a submission blocker**.

## 2. Inter-coder reliability (ICR)  ⏳ table reframed; κ/ICC still author-only
Table 3.1 was reframed (2026-06-09) into an honest **reliability protocol**: it now states the PI single-coded the full corpus against the documented codebook (Appendix B) and that an independent **20% double-coding pass (k = 47)** to compute κ/ICC is the one remaining pre-submission reliability step. The Limitations section was reconciled to match (no longer claims ICR "was assessed"). The actual κ/ICC values still require a second coder and cannot be fabricated:

- [ ] Draw the pre-specified 20% stratified subsample (`p6/tools/09_select_reliability_subsample.py`).
- [ ] Have a second coder independently code that subsample (ICRV regime, DPL phase, industry, DOI type, performance type; continuous cDAI).
- [ ] Compute Cohen's κ (categorical) and ICC(2,1) (cDAI) using the R snippet in `p6/tools/p6_extraction_codebook.md` §7.
- [ ] Add the computed values to Table 3.1 (the threshold/protocol scaffold is already in place) and confirm each meets threshold (κ ≥ 0.70; ICC ≥ 0.80).

## 3. OSF pre-registration  ⏳ (✅ template ready — only 3 placeholders)
`p6/osf/P6_OSF_Preregistration_Template.md` is complete except 3 placeholders.

- [ ] Create the OSF project, upload the protocol, the analysis code, and the (locked) data dictionary.
- [ ] Fill the 3 placeholders (authors/affiliation, registration date, project DOI).
- [ ] Replace the `[insert OSF DOI at submission]` placeholder (already in all four packages) with the **actual OSF DOI/URL** (Methods §3 and the data-availability statement).
- [ ] Because effect-size extraction is already complete, register honestly as a **retrospective/transparency registration** (or "registered after data collection"); do not imply a priori timing that did not occur.

## 4. AI-use disclosure (M-AIDA)  ✅ done — author to confirm scope
- [x] Manuscript AI-use statement updated in all four P6 packages to disclose the LLM-assisted extraction tool (M-AIDA, Anthropic Claude) with **100% PI verification + data lock**; Grammarly for language only; no GenAI for selection/analysis/interpretation.
- [x] "extracted manually" → "extracted" in Methods (the false absolute removed).
- [ ] **Author to confirm scope wording.** The repo shows M-AIDA was built for P6 and an auto-extraction log exists, but the final database is consistent with PI manual coding (codebook = manual; human-style notes; tool's `cdai` label differs from the manuscript). Choose the accurate variant:
      (a) *current wording* — "used to assist extraction, all PI-verified" (if the tool's proposals were used at all); or
      (b) downgrade to — "developed and trialed; the final database was coded and verified by the PI" (if the tool's output did **not** enter the final dataset).
- [ ] Align M-AIDA's `cdai_score` label (currently "Cultural Distance Asymmetry Index") to "country Digital Adoption Index" before publishing the code, so the tool matches the manuscript construct.

## 5. Honest reframing of the contribution (reviewer-facing)  ⏳
Per the audit (B2): publication bias halves the pooled effect (r 0.074 → 0.035), and two of three novel moderators are null (the ICRV result is driven by a k = 3 Frontier cell). Before submission:
- [ ] Foreground the **publication-bias** finding as a primary contribution; present the moderator nulls as informative bounds rather than failures.
- [ ] Ensure the title/abstract/positioning do not over-promise confirmed moderator effects.

## 6. Standard pre-submission items  ⏳
- [ ] Confirm reference style per target (JIM = APA 7; Emerald fallbacks = Harvard — already applied to Emerald packages).
- [ ] Run the institutional similarity check (CTU / journal Crossref Similarity Check).
- [ ] Verify figure files are high-resolution at upload.

---

### Bottom line
P6's *analysis* is done and internally consistent, and **all `[TBD]` placeholders are now removed** from the four submission packages. The **PRISMA flow is resolved** via an honest citation-anchored reframe (item 1), and the **ICR table is reframed honestly** (item 2) — only the actual κ/ICC computation (a 20% second-coder pass) and the **OSF DOI** (item 3) remain as genuine author-only steps. The AI disclosure (item 4) is fixed pending a one-line scope confirmation. P6 no longer contains submission-blocking placeholders.

- [x] **Manuscript OSF wording corrected (integrity):** removed the false claim that pre-registration *preceded* extraction; all four packages now state an honest **transparency registration** of the analysis plan with a `[insert OSF DOI at submission]` placeholder, and 'pre-registered robustness checks' → 'pre-specified'. The full ready-to-submit OSF content is `p6/osf/P6_OSF_Preregistration_Template.md` (+ .docx).
