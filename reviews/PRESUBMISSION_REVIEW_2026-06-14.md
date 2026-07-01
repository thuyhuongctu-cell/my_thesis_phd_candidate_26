# Pre-submission review — P9, P10, P11, P7 (2026-06-14)

Run with the `pre-submission-reviewer` skill after the em-dash de-AI pass. Scope:
the four papers closest to submission. Banned-vocabulary + em-dash scan run in
full on all four (not sampled).

## Summary
- **CRITICAL: 0**
- **MAJOR: 0** (in-text/prose); 1 process gate (Stata validation) applies to all
- **MINOR: 3**
- Top three fixes first: (1) author runs Stata cross-validation (process gate, all papers); (2) P7 — strip the internal reconciliation banner from any copy sent out (already removed from the IBR submission blinded copy; the working copy keeps it intentionally); (3) confirm P6 Scopus-search status before P6 submission (flagged separately).

## Dimension 6: Banned-vocabulary and em-dash scan (full scan, 4 papers)

| Item | Finding | Severity | Status |
|---|---|---|---|
| Prose em-dashes | P9=0, P10=0, P11=0; P7 prose=0 (2 in the internal reconciliation banner, not in the IBR submission copy; 1 in the Johanson & Vahlne 1977 *title*, faithful to the published source) | — | Có clean |
| AI-tone vocabulary | 1 occurrence ("underscore", P10 Section 5.3) to fixed to "show" | MINOR | Có fixed |
| Table empty-cell dashes | P7 Tables 2–4 use "—" as the standard "not in this model" cell marker | — | acceptable convention (not an AI tell) |

Banned-word list scanned in full: innovative, pioneering, revolutionary, transformative, surpass, remarkable, unprecedented, breakthrough, paves the way, underscore, delve, notably, profound, stems from, is capable of, highlight the potential, at its essence. **Zero** occurrences except the one fixed.

## Dimension 1: Macro logic
| Paper | Finding | Severity |
|---|---|---|
| P9/P10/P11/P7 | All carry the full chain: Abstract to Introduction to hypotheses/propositions to Data/Methods to Results to Discussion to Conclusion; contributions map to results sections. | — pass |
| P11 | Contribution framed honestly (DAI = pre-AI Tier-1 substrate, not AI); three findings map to Tables 1–4. | — pass |
| P7 | Three-zone narrative is internally consistent (abstract ↔ Section 4.6 ↔ Section 5); DAI level-shifter claim consistent throughout. | — pass |

## Dimension 2: Writing details
| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | P11 Section 5 has six subsections (5.1–5.6); a couple are short. | MINOR | optional: merge 5.2 into 5.1 for flow |
| 2 | P7 abstract is one long paragraph (~250 words). | MINOR | acceptable for IBR; could split if journal caps abstract length |

## Dimension 3: English grammar
No systematic non-native patterns detected in spot review (articles, S-V agreement, tense consistency, which/that). Tense convention correct (Related Work past, methods present). Pass.

## Dimension 4/5: Format & figures
- P10/P11 build glyph-clean to PDF (xelatex). P7/P9 are markdown to docx via the CTU/Springer templates.
- Tables have captions and notes; equations/coefficients render (Unicode β₁/β₂/FSTS²).
- Figures: P11 has no embedded figures (table-based); P10 none; P7 none; P9 has figures in the mir_package. No raster-in-final issues for the table-based papers.

## Integrity gate
- Gates 1–5, 7: **pass** (findings quoted; fixes concrete; no fabricated quotes; severity per taxonomy; score matches counts).
- Gate 6 [attestation]: the banned-vocabulary + em-dash scan was run in full (grep over the entire text of all four files), not sampled.

## Final score: **9/10**
Zero CRITICAL, zero in-text MAJOR, 3 MINOR. The deduction is for the cross-cutting process gate (Stata cross-validation pending) rather than any writing defect.

## Submission recommendation
- **P9, P10, P11: Ready to submit** once the author (a) runs the Stata cross-validation (A1) and (b) runs `verify_dois.py` to confirm references (A2). P11 fits the JED special-issue deadline (31 Oct 2026) comfortably.
- **P7: Ready after** the standard Stata cross-validation; ensure only the IBR submission blinded copy (banner-free) is sent, not the working copy.
- **P6 (not in this batch): hold** until the Scopus-search status is reconciled (see `p6/p6_prisma_flow.md` flag) and the inter-coder reliability κ is computed.

*Other installed review skills available for deeper passes: `academic-paper-reviewer` (5-persona simulation), `econ-referee-feedback` (referee report), `lfe-academic-reviewer`.*
