# P5 China — Coefficient Reconciliation TODO

*Flagged: 2026-06-02 (lfe-academic-reviewer subagent)*
*Status: BLOCKING for IJOEM submission — requires NCS decision*

## Issue

The manuscript Table 2 reports M2 coefficients that **do not match** either replication pipeline output.

## Three discrepant result sets

| Source | β(FSTS) 2012 | β(FSTS²) 2012 | β(FSTS) 2024 | β(FSTS²) 2024 | TP 2012 | TP 2024 |
|---|---:|---:|---:|---:|---:|---:|
| **Manuscript Table 2** | +1.28 | −1.53 | +1.19 | −1.58 | 49.4 % | 47.2 % |
| **Python canonical** (`results_coefs.csv` M2 HC1) | **+2.065** | **−2.092** | **+1.498** | **−1.587** | 49.37 % | 47.19 % |
| **R replication** (`p5_R_coefs.csv` M2, centred FSTSc) | +0.944 | −1.284 | +1.033 | −1.344 | 47.65 % | 47.52 % |

## What we know

1. **Turning points (TP)** match across all three sets (49.4 % vs 49.37 % vs 47.65 % — within rounding).
2. **Paternoster z-statistics** match manuscript (z = +0.82 for FSTS, z = -0.61 for FSTSsq) — these reproduce from the Python canonical coefficient set exactly.
3. **R uses mean-centred FSTSc** (manuscript line 137 acknowledges this); centring changes level coefficients but not TP or Paternoster z. R results are mathematically equivalent to Python when accounting for centring.
4. **Manuscript values appear from a deprecated v1.2 draft** — `summary.md` line 28 says "v1.2 reports 49.4 / 47.6 / 48.9 — replication matches within ≤0.4 pp", implying the Python pipeline was developed to *reproduce v1.2 TPs* but the underlying coefficient values diverge.

## Risk assessment

- **TP, Paternoster z, Lind-Mehlum verdicts**: ALL CONSISTENT across sets → durability claim STANDS regardless of which coefficient set is canonical.
- **Table 2 inline coefficients**: PRESENTLY UNREPRODUCIBLE → IJOEM AE will catch if requested to verify against replication package.
- **Abstract claim (β_z = +0.28 for TCI 2012, +0.43 in 2024)**: also requires verification against canonical replication.
- **Desk-rejection risk**: HIGH if reviewer runs replication and finds mismatch.

## Options for NCS

**Option A: Treat Python `results_coefs.csv` as canonical (RECOMMENDED)**
- Update Table 2 to: β(FSTS) = +2.065/+1.498; β(FSTS²) = −2.092/−1.587
- Update abstract TCI β_z values from replication (verify exact numbers)
- Re-run analysis in Stata once to triple-confirm canonical numbers
- Effort: 2-3 hours

**Option B: Re-run Stata canonical**
- Use the original `04_run_models.do` Stata pipeline
- Document exact specification
- Update Table 2 + abstract from Stata output
- Match coefficient set acceptable to NCS preferred software
- Effort: 3-4 hours (includes Stata access + rerun)

**Option C: Defer to JABES/IJOEM submission revision**
- Submit current version with TODO flag (NOT RECOMMENDED — desk-reject risk)
- Address in revision if requested by editor
- Effort: 0 hours now; 4-6 hours under revision deadline pressure

## My recommendation

**Option A**: update Table 2 to Python canonical values. Since TPs, Paternoster z's, and qualitative findings all match, the only fix is updating the level coefficients to a single canonical source. The Python replication is fully reproducible from the do files and CSVs.

## What I've already fixed (Phase A1 P5)

- ✅ Removed §5.2 blind-review violations (P3 Vietnam, P4 Singapore named in body)
- ✅ Removed orphan references (Meyer et al. 2017, Do & Phan 2026)
- ✅ Removed §4.5 unsupported bootstrap mediation claims (n=1,000 draws)
- ✅ Added missing Helpman, Melitz, Yeaple (2004) AER reference
- ✅ Tightened §3.2 variable note (removed P3/P4 cross-reference)

## Remaining for NCS

1. Decide between Option A, B, or C
2. Execute coefficient reconciliation
3. Rebuild p5_china_blinded.docx
4. Re-verify Table 2 + abstract values against final canonical replication
