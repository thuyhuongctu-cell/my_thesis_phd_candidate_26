# ADR Index — Journal-Target Decisions for the 7-Paper Portfolio

This directory records the rationale for each journal-target decision across the dissertation portfolio. The records use a lightweight MADR-inspired format (Context → Decision → Consequences). They exist for three reasons:

1. **Committee defense preparation.** Reviewers and committee members will ask "why did you switch from X to Y?" — these ADRs are the documented answer.
2. **Submission traceability.** Each ADR cites the commit where the switch was executed, so reviewers can audit what changed and when.
3. **PROJECT_SELF_CRITIQUE Group I resolution.** Documents the strategic positioning decisions flagged as undocumented.

## Decisions on record

| # | Paper | Switch | Status | Date | Triggering commit |
|---|---|---|:-:|---|---|
| [ADR-001](./ADR-001-p5-apjm-to-ijoem.md) | P5 China | APJM → IJOEM | ACCEPTED | 2026-05-29 | retroactive in plan-mode session |
| [ADR-002](./ADR-002-p6-mbr-mir-apjm.md) | P6 Meta-analysis | MBR → MIR → APJM | ACCEPTED | 2026-06-03 | `6db49d6`, `1061efa` |
| [ADR-003](./ADR-003-p9-thailand-to-india.md) | P9 / P9' | Thailand → India scope; → MIR | ACCEPTED | 2026-05-30 | `172dcdd`, `ac8dbbc` |
| [ADR-004](./ADR-004-p7-ibr-exclusion.md) | P7 Capstone | IBR explicitly excluded; JIBS primary | ACCEPTED | 2026-06-02 | NCS decision |

## Decisions not on record (within scope, no switch)

| Paper | Target | Rationale |
|---|---|---|
| P3 Vietnam | JED (Emerald) | NEU partnership; faster local review; commit `50856bf` |
| P4 Singapore | JABES (Emerald/UEH) | UEH partnership; commit `530ad77` |
| P8 SIDS | JED (Emerald) | Parallel-submission with P3 to JED; commit `50856bf` |

## Reviewing this index

When NCS adds new ADRs, update the table above. Decisions marked `ACCEPTED` are operational. To supersede a decision, write a new ADR referencing the prior one and mark the prior `SUPERSEDED-BY-ADR-NNN`.
