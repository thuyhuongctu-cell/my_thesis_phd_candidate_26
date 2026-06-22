# P6 → Journal of World Business (JWB) — Submission Gate-Checklist

**Decision (Quyết ④):** submit **now at the locked corpus k = 238 / K = 288**.
The submission is gated on **author-only reporting items**, *not* on pool size.
Expanding the Frontier/SIDS cell is **future work / a revision lever**, not a
pre-submission requirement (see `p6/P6_FRONTIER_SIDS_TARGETED_SEARCH_PROTOCOL.md`).

> **Status legend:** [x] done · [ ] author action required · 🔒 hard blocker (do not submit until cleared)

---

## 0. Analysis state (no action — for confidence)
- [x] Canonical numbers locked (R `metafor` three-level MARA): r = 0.074, 95% CI [0.060, 0.088]; K = 288, k = 238; I² = 62.4%; trim-and-fill k = 57 imputed, adj. r = 0.035. Source: `p6/results/CANONICAL_NUMBERS_P6.md`.
- [x] JWB / JIM / APJM manuscripts mutually consistent on every headline number.
- [x] SIDS k = 0 made symmetric in Method (Table 4.1 note) and the k≈5↔k=0 contradiction in Limitations (a) resolved across all live packages (commit 7fea871).
- [x] No `[TBD]` placeholders; PRISMA reframed honestly (citation-anchored "other methods" variant).

---

## 1. 🔒 HARD BLOCKER — Inter-coder reliability (ICR) κ / ICC
Six cells in **Table 3.1** are still `[insert after dual-coding]`
(`01_manuscript_blinded.md` lines **873–878**; same in `04_manuscript_latex.tex`).
This is the **only** item that genuinely blocks submission. Steps:

- [ ] Draw the pre-specified 20% stratified subsample, k = 47 (`p6/tools/09_select_reliability_subsample.py`).
- [ ] **Author 2 (Phan Anh Tú)** independently codes the subsample **blind** to Author 1: ICRV regime, DPL phase, industry, DOI type, performance type (categorical) + cDAI (continuous).
- [ ] Compute Cohen's κ (5 categorical moderators) and ICC(2,1) (cDAI) — R snippet in `p6/tools/p6_extraction_codebook.md` §7. *(R is not installed in this environment; run on the author's machine.)*
- [ ] Replace the 6 cells with computed values; confirm each meets threshold (κ ≥ 0.70; ICC ≥ 0.80).
- [ ] If any value < threshold: reconcile codes, document the resolution, re-compute — do **not** report a sub-threshold value silently.

---

## 2. OSF registration — confirm (DOI already present)
- [x] OSF DOI present in JWB Methods §3.1: `10.17605/OSF.IO/Z37KN` (line 573) and data-availability statement.
- [ ] **Confirm the OSF project at Z37KN is actually created and public** (or embargoed-but-registered), and that the uploaded protocol/data dictionary matches the submitted manuscript. Do not submit citing a DOI that resolves to nothing.
- [x] Honest framing: registered as a **transparency / retrospective** registration (corpus already assembled) — no false a-priori-timing claim.

## 3. AI-use disclosure — one-line scope confirmation
- [x] M-AIDA + Grammarly disclosure present (line 1341), variant **(a)**: "tool used to assist extraction, every value PI-verified and locked."
- [ ] **Author confirms variant (a) is accurate.** If the tool's proposals did **not** enter the final dataset, downgrade to variant (b): "developed and trialed; the final database was coded and verified by the PI." (Readiness checklist item 4.)

## 4. Standard pre-submission items
- [ ] Reference style = **APA 7** (JWB / Elsevier). Confirm bibliography + in-text formatting.
- [ ] Run institutional similarity check (CTU / Crossref Similarity Check); confirm no unintended overlap with the published ICBEF 2025 conference paper (state lineage / "what's new vs. Do & Phan 2025").
- [ ] Figures uploaded at high resolution (forest plot, funnel plot) — vector or ≥ 300 dpi.
- [ ] Title/abstract foreground **publication bias** as the primary contribution; moderator nulls framed as informative bounds, not confirmed effects (no over-claim of ICRV/cDAI/DPL).
- [ ] Cover letter (`03_cover_letter.md`) updated with current framing.

## 5. Cross-reference note (verify before submit)
- [ ] The SIDS/Frontier sentences cite **"Appendix B"** for *targeted search strings* (lines ~914, 1236, 1312), but Appendix B in this manuscript is the **Coding Protocol** (line 1577); the actual supplementary search strings live in **OSF §6**. Either (i) change those three cross-refs to "OSF §6 / future-work protocol," or (ii) add a short "targeted Frontier/SIDS search strings" sub-section to an appendix. Recommended: (i) — minimal, accurate. *(Pre-existing wording; flagged here, not silently edited.)*

---

## 6. Downstream (JIM, APJM — next rungs of the ladder)
Same ICR gate (6 unfilled cells each). Additional:
- [ ] **APJM** manuscript states OSF registration but **omits the DOI** — add `10.17605/OSF.IO/Z37KN` to APJM Methods + data-availability before its turn.
- [ ] JIM = APA 7; APJM (Emerald) = Harvard — confirm per-journal reference style (already applied per readiness checklist).

---

### Bottom line
**One hard blocker (ICR κ/ICC, §1) + four quick author confirmations (§2–§5).**
None depends on adding studies. Once §1 is filled and §2–§5 ticked, JWB is ready to submit at k = 238.
