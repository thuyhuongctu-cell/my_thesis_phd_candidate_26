# ADR-001: Retarget P5 (China) from APJM to IJOEM

**Status:** ACCEPTED
**Date:** 2026-05-29
**Paper:** P5 — Chinese private manufacturing firms; export-intensity ↔ performance
**Triggering commit(s):** plan-mode `peaceful-bubbling-kahn.md` at session start

## Context

P5 was initially drafted for **Asia Pacific Journal of Management (APJM)** when the dissertation portfolio was conceptualised. After completing the analysis (two WBES waves, 2012 + 2024; N ≈ 8,000 firms), the paper word-count grew to ~16,000w pre-trim, well above APJM's ~12,000w guidance, and beyond the ~10,000w upper bound where empirical IB papers comfortably fit the typical APJM revision cycle.

Additionally:
- **APJM's editorial focus** is on multi-country Asia-Pacific empirical research with strong theoretical contribution; P5's single-country (China) scope was a marginal fit.
- The portfolio had **another paper (P6 meta-analysis) more naturally positioned for APJM** — see ADR-002.
- **International Journal of Emerging Markets (IJOEM, Emerald)** Q1, fits China focus, accepts ~10,000w empirical papers, has faster review cycles (~3–4 months vs APJM ~6–8 months), and a Vietnam-based NCS has a more established submission workflow with Emerald than with Springer Nature.

## Decision

Retarget P5 to **IJOEM**. Execute systematic cleanup of APJM-specific cruft:
- Rename `manuscripts/p5_china/apjm/` → `manuscripts/p5_china/ijoem/`
- Update `scripts/build_submission_package.sh` to emit `p5_china_IJOEM.{docx,tex,pdf}`
- Replicate-note paths across EN + VI `p5_china_*_clean.md` files
- Rebuild blinded DOCX into `p5/submission/ijoem_package/`
- Verify zero `apjm`/`APJM` residuals in P5 scope (`grep` audit)

## Consequences

**Positive:**
- P5 word-count (9,491w post-trim) comfortably within IJOEM's 10,000w cap with ~500w buffer
- Faster expected review cycle (~3–4 months)
- Cleaner separation: APJM slot freed for P6 meta-analysis (ADR-002)
- Emerald submission portal already familiar to NCS

**Trade-offs:**
- IJOEM impact factor and citation reach lower than APJM (ABS-3); P5 contribution accordingly more "incremental empirical" framing rather than "theory-extending"
- ABS rating: IJOEM ABS-2 vs APJM ABS-3 (small step down)

**Mitigation:** P5 is one of seven papers in the dissertation portfolio; the highest-prestige slot is allocated to P7 (JIBS, ABS-4*). Portfolio-wide ABS distribution remains strong (1 × ABS-4*, 3 × ABS-3, 3 × ABS-2/Q1).

## Verification

- `grep -rniE "apjm|APJM" p5/ manuscripts/p5_china* scripts/build_submission_package.sh` returns only the line-170 P3→APJM echo (which is correct; P3 still targets APJM-equivalent Emerald journals via JED).
- `p5_china_IJOEM.*` artifacts present in `dist/submission/`; mislabeled `p5_china_APJM.*` removed.
- Blinded DOCX zero author-identifier hits.

## Related

- [ADR-002](./ADR-002-p6-mbr-mir-apjm.md) — P6 takes the APJM slot freed by this decision
- PR #12 body updated: "P5 (APJM)" → "P5 (IJOEM)"
