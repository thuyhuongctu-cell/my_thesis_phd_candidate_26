# P6 Meta-Analysis — Submission-Readiness Checklist (PRISMA · ICR · OSF)

**Purpose:** close the gaps that currently block journal submission of P6 (JIM first target).
**Status legend:** ✅ done · ⏳ author action required · 🤖 tooling ready in repo

The meta-analytic *results* are final and consistent (k = 238 studies, K = 288 effects; pooled r = 0.074; `p6/data/p6_study_database.csv` + `p6/results/`). What remains are the **reporting-standard artefacts** that a reviewer will require. None can be fabricated; each needs the author to run a provided tool and paste the outputs.

---

## 1. Formal PRISMA database search  ⏳ (🤖 tool ready)
The manuscript currently rests on a pre-formal-search working database and leaves the PRISMA flow intermediates as `[TBD]` (29 per package). To convert this into a defensible systematic review:

- [ ] Run the formal WoS + Scopus search **on a networked machine** using `p6/tools/28_extract_wos_scopus_locally.py` (instructions: `p6/tools/HOW_TO_EXTRACT_DATA.md`). The exact search strings are pre-registered in `p6/osf/P6_OSF_Preregistration_Template.md` §6.
- [ ] Record counts at each PRISMA stage: identified → deduplicated → title/abstract screened → excluded (by reason) → full-text assessed → excluded (by reason) → **included (k = 238, K = 288, already known)**.
- [ ] Paste these numbers into the PRISMA flow (replaces every `[n = TBD]`) in all P6 packages (`jim`, `ibr`, `jwb`, `apjm`) and the PRISMA appendix.
- [ ] Reconcile: if the formal search yields a different included k/K than 238/288, update the analysis and all downstream numbers. If it confirms 238/288, state that the working database equals the formal-search yield.

> If a full formal search is not feasible before the target submission date, the honest fallback is to **reframe** §3.1 as a systematic-but-bounded search (backward/forward citation from named anchor meta-analyses + database supplement) and drop language implying an exhaustive WoS/Scopus census. Do **not** leave `[TBD]` placeholders in a submitted manuscript.

## 2. Inter-coder reliability (ICR)  ⏳ (🤖 protocol + R code ready)
Table 3.1 reports κ/ICC as `[TBD]`. A meta-analysis claiming reliable moderator coding must report actual agreement.

- [ ] Draw the pre-specified 20% stratified subsample (`p6/tools/09_select_reliability_subsample.py`).
- [ ] Have a second coder independently code that subsample (ICRV regime, DPL phase, industry, DOI type, performance type; continuous cDAI).
- [ ] Compute Cohen's κ (categorical) and ICC(2,1) (cDAI) using the R snippet in `p6/tools/p6_extraction_codebook.md` §7.
- [ ] Paste the values into Table 3.1 and confirm each meets threshold (κ ≥ 0.70; ICC ≥ 0.80).

## 3. OSF pre-registration  ⏳ (✅ template ready — only 3 placeholders)
`p6/osf/P6_OSF_Preregistration_Template.md` is complete except 3 placeholders.

- [ ] Create the OSF project, upload the protocol, the analysis code, and the (locked) data dictionary.
- [ ] Fill the 3 placeholders (authors/affiliation, registration date, project DOI).
- [ ] Replace the manuscript's "registration identifier will be inserted at acceptance" with the **actual OSF DOI/URL** (Methods §3 and the data-availability statement).
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
P6's *analysis* is done and internally consistent. The blockers are **PRISMA flow + ICR reporting** (items 1–2) and the **OSF DOI** (item 3) — all have tooling in the repo and require the author to run them and paste outputs. The AI disclosure (item 4) is fixed pending a one-line scope confirmation. Do not submit P6 with `[TBD]` placeholders.
