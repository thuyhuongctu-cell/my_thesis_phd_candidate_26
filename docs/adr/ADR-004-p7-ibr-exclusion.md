# ADR-004: IBR explicitly excluded as target for P6 and P7

**Status:** ACCEPTED
**Date:** 2026-06-02
**Scope:** Portfolio-wide journal-target policy
**Triggering decision:** NCS choice in plan-mode session "do not submit to IBR"

## Context

When evaluating Q1/Q2 IB journals for the dissertation portfolio, **International Business Review (IBR, Elsevier, ABS-3)** is a natural candidate for:
- P6 (meta-analysis on I-P relationship)
- P7 (capstone multi-country empirical paper)

IBR has comparable ABS rating to APJM/MIR (ABS-3), publishes meta-analyses regularly, and has Asia-Pacific editorial-board representation.

However, NCS explicitly excluded IBR from the target set during the plan-mode session. The decision was made on **administrative and operational grounds**, not theoretical fit grounds:

1. **PRISMA single-coder tolerance:** IBR's methodological reviewer pool tends to flag PRISMA Item 9 (single-coder data extraction) more strictly than APJM/MIR. P6 used a single-coder extraction protocol with mitigations (double-entry verification, pilot calibration) but cannot report a second coder's κ. This is disclosed transparently as PRE-REGISTERED deviation #4 on OSF z37kn, but desk-editor risk at IBR is materially higher than at APJM.

2. **Abstract format preference:** IBR prefers an unstructured abstract; APJM and MIR allow the Emerald 7-section structured format that the dissertation portfolio standardised on. Switching abstract format for IBR specifically would create cross-portfolio inconsistency.

3. **Submission portal familiarity:** NCS has prior experience with Springer Editorial Manager (APJM, MIR) but no prior submission to Elsevier portals. Operational risk of unfamiliar portal during a tight defense-deadline window.

4. **Review-cycle uncertainty:** IBR review times in 2024-2025 reported as more variable than APJM's published average; predictability matters for defense-timing planning.

## Decision

**Exclude IBR from the target set for P6 and P7.**

- P6 → APJM primary (ADR-002), MIR backup
- P7 → JIBS primary, MIR backup (NOT IBR)

This is a **soft exclusion**: if APJM and MIR both desk-reject for non-substantive reasons, IBR can be reconsidered as a third-line option. The exclusion is not based on quality concerns about IBR.

## Consequences

**Positive:**
- Simplified portfolio submission strategy: 2 Springer venues (APJM for P6, JIBS-or-MIR for P7) + Emerald cluster for P3/P4/P5/P8/P9'
- Consistent abstract format (Emerald 7-section) across all 7 papers
- Predictable submission portal interactions (Springer + Emerald only)
- κ-extraction-coder concern (P6 PRISMA Item 9) routed to a more tolerant venue

**Trade-offs:**
- One fewer Q1/Q2 ABS-3 fallback in the target set
- Cannot leverage IBR's strong Asia-Pacific reach for the meta-analysis

**Mitigation:** If both APJM (P6) and JIBS (P7) desk-reject, the soft exclusion can be revisited. ADR will be superseded if that happens.

## Verification

- P6 submission package: `p6/submission/apjm_package/` (no IBR variant exists)
- P7 submission package: `dist/SUBMISSION_FINAL/P7_Capstone_JIBS/` (no IBR variant exists)
- No `ibr_package/` directory anywhere in the repo

## Related

- [ADR-002](./ADR-002-p6-mbr-mir-apjm.md) — P6 final target (APJM, not IBR)
- [ADR-003](./ADR-003-p9-thailand-to-india.md) — P9' target (MIR, not IBR)
- `p6/RECONCILIATION_NOTES.md` issue #6 — full target-journal decision matrix MIR/IBR/MRQ
