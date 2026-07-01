# P9 (India) — Pre-Submission Review

**Manuscript:** Threshold dissolution of the inverted-U I-P relationship in Indian firms, 2014–2025 (WBES 3 waves; UPI).
**Target:** Management International Review (Springer Nature).
**Source reviewed:** `p9_india/submission/mir_package/01_manuscript_blinded_full.md` (full), plus `03_cover_letter.md`, `02_title_page.md`, `README.md`.
**Date:** 2026-06-09.

## Summary

The paper is empirically strong, well-argued, and the headline numbers are internally consistent in the analytic-vs-raw N treatment (28,717 analytic / 29,136 raw, with per-wave raw and analytic Ns correctly distinguished — intentional, not an error). The threshold-dissolution story, Paternoster z-tests, robustness battery, and capability sign-flip are reported and supported. The em-dash scan is clean (0 in the manuscript). However, several MAJOR house-keeping defects would draw a desk-level or first-round reviewer flag: a **broken citation** (Hutzschenreuter et al. 2026 cited, absent from references), **~12 orphan references** never cited in the body, a **pooled-N discrepancy** (28,717 vs 28,742), a **title mismatch** between the manuscript and the cover letter/title page, an **abstract that vastly exceeds the claimed ≤250 words**, and a **contribution-count framing mismatch** (paper says "three contributions / H1–H3" but actually tests H1, H2a/b, H3a/b, H4a/b). One AI-tone word ("unprecedented") survives in the cover letter and README. None of these are fatal to the science; all are quick fixes.

## Severity Counts

| Severity | Count |
|---|---:|
| CRITICAL | 0 |
| MAJOR | 7 |
| MINOR | 6 |

## Top 3 Fixes (do first)

1. **Fix the broken Hutzschenreuter citation + reconcile the reference list.** Add Hutzschenreuter, Kleindienst, Sengupta and Verbeke (2026) to References (it is cited at line 77 but missing), and either cite or remove the ~12 orphan references (Ackerberg, Asher, Bharadwaj, De Loecker, Geleilate, Goldfarb, Haans, Hoskisson, Khanna, Melitz, Olley, Vial). Bidirectional citation↔reference integrity is the single most reviewer-visible defect.
2. **Reconcile the pooled-N discrepancy.** Body/abstract report pooled analytic N = 28,717 (= 8,941+9,300+10,476), but Section 4.4 reports the pooled 3-wave model at "N = 28,742." Resolve and state why (e.g., extra moderator deletions) or correct the typo.
3. **Unify the title and trim the abstract.** The manuscript title ("When Institutional Transformation Breaks the Threshold…") differs entirely from the cover-letter/title-page title ("Cross-Wave Stability of the Internationalisation–Performance Threshold…"). Pick one. Separately, the structured abstract runs ~600+ words against the ≤250 claimed in README/title page.

## Dimension 1 — Macro Logic

| ID | Sev | Location | Issue | Fix |
|---|---|---|---|---|
| M-1 | MAJOR | Intro Section 1 ("three contributions"); abstract Originality | Contribution/hypothesis count mismatch. Intro and prompt frame "three contributions" and the README implies H1–H3, but the paper actually tests **H1, H2a/H2b, H3a/H3b, H4a/H4b**. The digital-infrastructure (H4) result is one of the three headline contributions yet is not labelled in the H1–H3 numbering. | State explicitly that the three contributions map to H2 (threshold dissolution), H4 (public/private complement-not-substitute), and H3 (TCI sign-flip), with H1 as baseline. Make the H-numbering and contribution-numbering consistent. |
| M-2 | MINOR | Section 2.5 / Figure 1 caption | Conceptual model claims to integrate "H1 to H4b" but the three stated contributions in Section 1 do not name H4 as a contribution explicitly — chain is sound but the reader must reconstruct the mapping. | Add one sentence linking each contribution to its hypothesis number. |
| M-3 | MINOR | Abstract Findings ↔ Section 4.4 | Abstract reports "FSTS × wave_2025 = −1.63 (p<0.0001)"; body confirms. Consistent. (No fix — noted as verified.) | — |

Intro chain (institutional churn to untested scope condition to 3-wave test) is clear and the conclusions are supported by the results. H1–H4 are all tested and reported. Abstract is structured (Purpose/Design/Findings/etc.) — acceptable for MIR even though Emerald-style; flagged only for length.

## Dimension 2 — Writing / Structure

| ID | Sev | Location | Issue | Fix |
|---|---|---|---|---|
| W-1 | MAJOR | Abstract (lines 19–39) | Structured abstract is ~600+ words; README/title page state "≤250 words." Springer MIR typically wants a single unstructured paragraph ~150–250 words. | Condense to a single ≤250-word paragraph (or confirm MIR accepts structured); current six-subsection block is Emerald-formatted. |
| W-2 | MINOR | Section 4.4 and Section 5.1 | The linear-trend and wave-dummy results are restated almost verbatim in Results Section 4.4 and Discussion Section 5.1 (FSTS×wave_2025 = −1.63; FSTS×trend = −0.10). Mild redundancy. | Trim the Section 5.1 restatement to a back-reference. |
| W-3 | MINOR | Line 507 footer | Draft footer ("Section 4.6 robustness expansion … and Figure rendering pending") contradicts README's "finalised" status and would embarrass at submission. | Delete the draft-status footer before upload. |

Topic sentences and paragraph health are generally good. Highlights section is present and crisp.

## Dimension 3 — Grammar / Mechanics

| ID | Sev | Location | Issue | Fix |
|---|---|---|---|---|
| G-1 | MINOR | Section 5.2 line 351 heading | "a complementarity, not substitution" — parallelism off. | "a complementarity, not a substitution" or "complements, not substitutes." |
| G-2 | MINOR | Table 1, row "DAI Tier-2" and Title-page CRediT table | Stray placeholder commas in empty cells (`|, |, |`) render as literal commas in several tables. | Replace empty-cell `,` with blank or em-dash placeholder. |

No systematic article/agreement/tense/which-that or Chinglish problems found; prose is publication-grade.

## Dimension 4 — Numbers / Stats / Citations

| ID | Sev | Location | Issue | Fix |
|---|---|---|---|---|
| N-1 | MAJOR | Section 4.4 line 250 vs abstract/Section 3.1 | Pooled analytic N = **28,742** in Section 4.4 but **28,717** everywhere else (= sum of 8,941+9,300+10,476). | Reconcile; if the pooled model drops cases, state it, else fix to 28,717. |
| N-2 | MAJOR | Body line 77 vs References | **Hutzschenreuter, Kleindienst, Sengupta and Verbeke (2026)** cited in Section 2.1 but **not in the reference list** — broken citation. | Add full reference. |
| N-3 | MAJOR | References Section , lines 421–501 | **~12 orphan references** appear in the list but are never cited in the body: Ackerberg et al. (2015), Asher & Novosad (2017), Bharadwaj et al. (2013), De Loecker (2013), Geleilate et al. (2016), Goldfarb & Tucker (2019), Haans et al. (2016), Hoskisson et al. (2000), Khanna & Palepu (2010), Melitz (2003), Olley & Pakes (1996), Vial (2019). Sambharya (1996) is cited only in the cover letter, not the manuscript. | Cite each where relevant (e.g., Haans et al. 2016 for U-test methodology, Olley-Pakes/Ackerberg for productivity estimation) or delete from the list. |
| N-4 | MINOR | Verified numbers | TP 2014 = 61.8% and 2022 = 40.7%; 2025 β₂ = −0.16, p = 0.42; Paternoster z = −7.94 / +4.17; FSTS×DAI_epay = −4.02, p = 0.004; per-wave analytic N 8,941/9,300/10,476; raw 9,281/9,376/10,479; pooled raw 29,136 — all **consistent** across abstract, body, tables, README. Raw-vs-analytic dual reporting is intentional and correctly handled. | No fix — verified clean. |
| N-5 | MINOR | Prior-work disclosure | Do & Phan (2025) IntechOpen disclosure is present in abstract, Section 1, Section 6, acknowledgements, cover letter, and title page, in third person ("the authors' earlier work"). Compliant. | No fix — verified. |

## Dimension 5 — House Style / Declarations

| ID | Sev | Location | Issue | Fix |
|---|---|---|---|---|
| H-1 | MAJOR | Manuscript title (line 1) vs cover letter (line 9) / title page (line 7) | Two completely different titles. Desk editors cross-check. | Unify to one title across all package files. |
| H-2 | MINOR | Cover letter lines 25, 35; keyword list | Cover letter cites unsubmitted companion papers ("Author Citation P5 … P3") and the keyword "Conditional Digital Capability Moderation / CDCM" appears as a named framework in the abstract/title-page but the manuscript body uses "institutions-based view" as the lens — slight framing inconsistency between cover letter (CDCM) and manuscript (IBV). | Align the stated theoretical lens; ensure CDCM is defined in-text if kept as a keyword. |
| H-3 | MINOR | Declarations | Conflict-of-interest, funding, data-availability, GenAI-use statements all present and Springer-compliant. Prior-work disclosure in cover letter present. | No fix — verified. |

## Dimension 6 — Banned Vocab / Em-dash

| ID | Sev | Location | Issue | Fix |
|---|---|---|---|---|
| V-1 | MINOR | Cover letter line 13; README line 37 | "unprecedented" survives ("unprecedented institutional and digital transformation decade"). The manuscript body avoids it (uses "without obvious historical parallel," "no comparable historical precedent") — those are defensible. | Replace "unprecedented" in the cover letter/README for consistency with the cleaned manuscript. |
| V-2 | — | Manuscript full text | **Em-dash count = 0** (verified). En-dashes (–) used only for numeric ranges and Lind–Mehlum/Mizik–Jacobson compounds — correct. "transformative" count = 0. | No fix — verified clean. |

## Score

**7.0 / 10.** Science and analysis are 9-level; the deductions are entirely for submission-hygiene defects (broken/orphan citations, N discrepancy, title mismatch, abstract length, contribution-count framing) that a careful pass clears in under an hour.

## Recommendation

**Minor revision before submission.** No CRITICAL issues. Clear the 7 MAJOR items (citation integrity ×2, pooled-N, title unification, abstract length, contribution-numbering, CDCM-vs-IBV framing) and the manuscript is submission-ready for MIR.
