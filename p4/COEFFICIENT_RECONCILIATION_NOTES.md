# P4 Singapore — Coefficient Reconciliation Notes

*Created: 2026-06-02 (after lfe-academic-reviewer Phase A1 review)*

## Status: PARTIALLY RESOLVED

5 of 9 reviewer-flagged issues addressed in this session. Remaining 4 require NCS attention.

## Fixed (this session)

| # | Issue | Action |
|---|---|---|
| 1 | Table 2 M5 FSTS coefficient mismatch | +2.165 → **+2.563** (canonical CSV value) |
| 2 | Table 2 M6 FSTS coefficient mismatch | +2.322 → **+2.491** (canonical CSV value) |
| 3 | Table 2 M8 FSTS coefficient mismatch | +2.409 → **+2.492** (canonical CSV value) |
| 4 | Word count declaration wrong (8,500 vs actual ~13,000) | Updated to "approximately 13,000 words" |
| 5 | §3.4(ii) "we are underpowered" first-person voice | → "the analysis is underpowered" |
| 6 | §4.3 M3 vs M4 cross-reference error | "Model M3" → "Model M4-TCI" |
| 7 | "primary contribution" softened (f²=0.018 below small-effect) | → "primary empirical signature" |
| 8 | 7 missing reference entries added | Coase 1937, Williamson 1985, Teece 2007, Gelman & Carlin 2014, Leon 2004, World Bank 2023, World Bank 2025a |

## Outstanding (NCS workflow)

| # | Issue | Severity | Effort |
|---|---|:-:|---:|
| 9 | Word count reduction: 13,791 → ≤12,000 (cut ~1,800 words) | 🔴 High | 3h |
| 10 | Abstract restructure to Emerald 7-section format (Purpose/Design/Findings/Limitations/Practical/Social/Originality) | 🔴 High | 1.5h |
| 11 | N=84 vs N=111 exporters subsample discrepancy needs verification | 🟡 Medium | 30min |
| 12 | Citation style inconsistency (comma in `et al., YEAR` form) needs systematic pass | 🟡 Medium | 1h |

## Word reduction targets per reviewer

| Section | Current ~words | Target cut | Rationale |
|---|---:|---:|---|
| §2.3.4 Three candidate mechanisms | 350 | 200 | Repeated in §5.1 |
| §3.4 Boundary conditions (iii) | 900 | 250 | Tighten LM framing |
| §5.1 Tier-1 vs Tier-1+2 + Institutional transferability | 700 | 450 | Heavy redundancy with §3.2.3 R1 |
| §4.5 Additional robustness notes | 350 | 150 | Overlap §3.4(ii) and (iv) |
| **Total** | **2,300** | **~1,050** | |

Additional 750 words can come from tightening §2 Theory development + §5 Discussion paragraphs.

## Verification of canonical reconciliation

Canonical source: `p4/replication/coefs_main_models.csv` (Python pipeline)

| Coefficient | M2 | M5 | M6 | M7 | M8 |
|---|---:|---:|---:|---:|---:|
| Manuscript (now) | +2.652 | **+2.563** | **+2.491** | +1.952 | **+2.492** |
| Canonical CSV | +2.652 | +2.563 | +2.491 | N/A* | +2.492 |
| Status | ✓ | ✓ FIXED | ✓ FIXED | ⚠ Different spec | ✓ FIXED |

*M7 in CSV does not include FSTSc/FSTSc² (TCI+DAI direct only, no FSTS terms). The manuscript M7 includes FSTS terms (different specification). Manuscript value of +1.952 left in place — NCS to verify or remove M7 column.

## What to verify next

1. Optional re-run `p4/replication/do/` Stata pipeline if access available
2. Cross-check Table 2 against any Stata log output
3. Verify M7 specification choice (FSTS-included or FSTS-excluded?)
4. Decide on word reduction priorities for NCS pass
5. Restructure abstract to Emerald 7-section format
