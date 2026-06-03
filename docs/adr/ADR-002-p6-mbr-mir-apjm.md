# ADR-002: P6 (Meta-analysis) journey — MBR → MIR → APJM

**Status:** ACCEPTED (final: APJM)
**Date:** 2026-06-03 (final retarget)
**Paper:** P6 — Three-level meta-analysis of I-P relationship in Asia-Pacific
**Triggering commits:** `6db49d6` (MBR→MIR), `1061efa` (MIR→APJM)

## Context

P6 underwent two journal-target switches, each driven by a different constraint. Documenting both as one ADR to keep the rationale chain intact.

**Stage 1 — Original target: MBR (Multinational Business Review, Emerald, ABS-2).**
- Selected initially as a low-cycle-time IB journal with strong Asia-Pacific reach.
- After analysis completion (k = 238 studies; pooled r = 0.074; I² = 87.8%; OSF preregistration z37kn), the contribution profile turned out stronger than initially expected — the three-level MARA + publication-bias bounding + ICRV moderation test together constitute a methodologically novel contribution, not merely an incremental Asia-Pacific replication.
- MBR's ABS-2 rating did not match the methodological ambition.

**Stage 2 — Intermediate target: MIR (Management International Review, Springer Nature, ABS-3, Q1).**
- Retargeted from MBR to MIR (commit `6db49d6`) after word-count audit + contribution-profile review.
- Word-count trimmed from ~17k → ~11.6w to fit MIR's ~12,000w guidance.
- MIR fits Asia-Pacific multi-country meta-analysis well; ABS-3 / Q1 status matches the contribution.

**Stage 3 — Final target: APJM (Asia Pacific Journal of Management, Springer Nature, ABS-3, Q1).**
- After scholar-review of v1.4 manuscript flagged geographic-fit concerns + theoretical-fit concerns (CIMT institutional-gradient mechanism is sharpest in Asia-Pacific specifically, less so for general MIR readership), and after P5 retargeted away from APJM (ADR-001), the APJM slot became available.
- Retargeted from MIR to APJM (commit `1061efa`).
- APJM editorial board includes institutional-theory experts (Peng 2003 IBV anchor) welcoming the CIMT contribution.
- APJM Q1 status within the user-specified Q1–Q2 range; IBR explicitly excluded (ADR-004).

## Decision

**Final target: APJM (Asia Pacific Journal of Management, Springer Nature, Scopus Q1, ABS-3).**

Rationale for the chain:
1. **MBR → MIR**: contribution profile + ABS rating mismatch; need ABS-3 / Q1
2. **MIR → APJM**: geographic + theoretical fit (Asia-Pacific 45-economy corpus + ICRV taxonomy + CIMT mechanism); APJM slot freed by ADR-001; APJM faster review than MIR (~6-8 months vs 8-12); APJM editorial board institutional-theory composition

## Consequences

**Positive:**
- Submission target stabilised at APJM Q1 / ABS-3
- Better editorial-board fit for CIMT institutional mechanism
- Faster expected review cycle vs MIR
- Springer Nature submission portal already familiar via prior planned MIR target

**Trade-offs:**
- Submission package folder structure required renames: `mir_package/` → `apjm_package/`
- Cover letter, title page, and README all updated for APJM-specific framing
- OSF preregistration z37kn was originally registered targeting MIR; preregistration body is journal-agnostic so **no retroactive edit needed** (the deviation note in `p6/RECONCILIATION_NOTES.md` documents this transparently).

**Path B (preregistered follow-up):** OSF z37kn pre-registers a formal-search expansion from k = 238 to k ≈ 600–700 as a follow-up replication, which would target the same APJM venue or a backup (per ADR-002 chain experience, MIR remains the natural backup).

## Verification

- Manuscript header line 5 + footer updated to APJM
- New `p6/submission/apjm_package/` created with title page + APJM-specific cover letter + README
- OSF DOI z37kn unchanged
- Build script `scripts/build_paper_docx.py` updated to emit APJM package
- See `p6/RECONCILIATION_NOTES.md` issue #6 for full file-level audit

## Related

- [ADR-001](./ADR-001-p5-apjm-to-ijoem.md) — P5 freed the APJM slot
- [ADR-004](./ADR-004-p7-ibr-exclusion.md) — IBR excluded as a target for both P6 and P7
- `thesis/CIMT_REALITY_AND_TOP_1PCT_SCHOLAR_REVIEW.md` — scholar-review that triggered MIR → APJM retarget
- OSF z37kn: https://osf.io/z37kn (DOI: 10.17605/OSF.IO/Z37KN)
