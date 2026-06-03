# ADR-003: P9 scope switch (Thailand → India) + journal target (MIR)

**Status:** ACCEPTED
**Date:** 2026-05-30
**Paper:** P9 (renamed P9') — Cross-wave threshold-stability study, now centred on India
**Triggering commits:** `172dcdd` (P9 Thailand infrastructure), `ac8dbbc` (P9' India infrastructure)

## Context

P9 was initially scoped as a Thailand cross-wave WBES paper (2016 + 2025 waves) targeting JED, parallel to the P3/P8 JED submission strategy.

After scoping work in commit `172dcdd`, three constraints emerged:

1. **WBES Thailand wave coverage limits:** Thailand has WBES waves in 2016 and 2025, but the 2016 wave uses the older PICS3 schema and the digital-capability items are sparse; the cross-wave threshold-stability test required at least three waves of harmonisable data with consistent digital-capability coverage, which Thailand cannot provide.

2. **India offers a stronger natural experiment:** India has three usable WBES waves (2014 PICS3, 2022 BEE, 2025 BREADY) covering the demonetisation (2016) + GST (2017) + IBC (2016) + UPI launch (2016) + UPI saturation (2024) + PLI (2020) + COVID-19 (2020-2022) + Atmanirbhar Bharat (2020) policy sequence. This is a far richer institutional-transformation laboratory than Thailand's relatively stable period.

3. **Tier-1 vs Tier-2 digital decomposition feasibility:** the India 2025 BREADY wave includes the e-payment percentage item (k33) that maps onto UPI public infrastructure utilisation, enabling a Tier-1 (private website) vs Tier-2 (public-infrastructure-mediated UPI) decomposition that is theoretically novel and policy-relevant. Thailand has no equivalent public digital infrastructure programme at the WBES-observable resolution.

The scope switch turns a planned descriptive cross-wave paper into a policy-relevant quasi-experiment.

## Decision

**Stage 1 — Scope switch (Thailand → India):**
- Drop the Thailand-only scope.
- Adopt India 3-wave WBES design (2014 / 2022 / 2025) with cumulative N ≈ 29,000 firm-observations.
- Rename paper internally P9 → P9' to reflect the scope reset.
- Delete `p9_thailand/` infrastructure (commit history preserved in `172dcdd` for archival).
- Build new `p9_india/` infrastructure (commit `ac8dbbc`).

**Stage 2 — Journal target:**
- Target **Management International Review (MIR, Springer Nature, ABS-3, Q1)** as primary.
- Backup target: IJOEM (Emerald, Q1) if MIR desk-rejects.
- Rationale:
  - MIR fits the IB-theoretical contribution (institutions-based view + capability-institution moderation)
  - MIR welcomes South Asian institutional-transformation studies
  - 8,424w manuscript fits MIR's ~9-10,000w guidance with -1,576w buffer
  - The UPI quasi-experiment frame speaks to a current MIR conversation on state-provisioned infrastructure vs private capability accumulation

## Consequences

**Positive:**
- Stronger theoretical contribution (threshold dynamics under institutional shift, not just stability)
- Policy-relevant Tier-1 vs Tier-2 digital decomposition
- Three-wave panel-equivalent identification through repeated cross-sections
- Cross-paper validation of CIMT mechanism in South Asian regime context (complements East Asian + SIDS evidence)

**Trade-offs:**
- Overlap with prior author book chapter (Do & Phan, 2025, IntechOpen, DOI 10.5772/intechopen.1011012) on Indian firms required full **Declaration of Distinctiveness** in cover letter (7-dimension comparison table) — see PROJECT_SELF_CRITIQUE Group C.1
- Sample-relationship disclosure required in P9' manuscript §3 (lines 55, 69) + §5/§6 (lines 285, 293)
- All disclosure mechanisms in place; the risk is **mitigated, not eliminated** — if the journal flags the overlap as inadequate disclosure, NCS may need to expand the differentiation memo

**Negative outcome path (if MIR desk-rejects):** IJOEM (Emerald) as backup, requires no rewrite — the 8,424w manuscript fits IJOEM's 10,000w cap with comfortable buffer.

## Verification

- `p9_india/p9_india_en_clean.md` clean (current word count 8,424w)
- `p9_india/submission/mir_package/03_cover_letter.md` includes 7-dimension distinctiveness table
- Self-citation Do & Phan (2025) explicit in §3, §5/§6, references list
- `p9_thailand/` legacy folder removed per ADR scope switch
- Cross-validated CIMT signature (P9' India regime III/IV) against P3 Vietnam (IV) + P5 China (III) + P4 Singapore (I) + P8 SIDS (VI)

## Related

- [ADR-002](./ADR-002-p6-mbr-mir-apjm.md) — MIR was P6's earlier intended target; the MIR slot is now P9'
- [ADR-004](./ADR-004-p7-ibr-exclusion.md) — IBR not considered for P9' (consistent with portfolio exclusion)
- PROJECT_SELF_CRITIQUE Group C — book chapter overlap disclosure
- Book chapter: Do, T. H., & Phan, A. T. (2025). *Internationalization and firm performance of firms in India: the role of top management*. IntechOpen. DOI: 10.5772/intechopen.1011012
