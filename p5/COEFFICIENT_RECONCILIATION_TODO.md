# P5 China — Coefficient Reconciliation [RESOLVED 2026-06-02]

*Status: RESOLVED via Option A — manuscript Table 2 + §4.2 prose updated to canonical Python replication values.*

## Resolution

Updated all coefficient citations in manuscript to match canonical Python pipeline output (`p5/replication/results/results_coefs.csv` + `summary.md`):

| Element | Old value (deprecated v1.2) | New canonical value |
|---|---|---|
| Table 2 FSTS (2012) | +1.28 (0.379) | **+2.065 (0.379)** |
| Table 2 FSTS² (2012) | −1.53 (0.420) | **−2.092 (0.435)** |
| Table 2 FSTS (2024) | +1.19 (0.461) | **+1.498 (0.578)** |
| Table 2 FSTS² (2024) | −1.58 (0.503) | **−1.587 (0.712)** |
| Table 2 FSTS (pooled) | +1.24 (0.290) | **+1.784 (0.320)** |
| Table 2 FSTS² (pooled) | −1.55 (0.330) | **−1.829 (0.375)** |
| Table 2 lnEmp (2012) | +0.31 | **−0.102** (sign flip) |
| Table 2 lnEmp (2024) | +0.39 | **+0.118** |
| Table 2 firmage | +0.007 to +0.010 | +0.008 to +0.012 |
| Table 2 foreigndummy (2012) | +0.24 ** | +0.112 (n.s.) |
| TP 95% CI 2012 | [43.1, 55.7] | **[43.2, 55.6]** |
| TP 95% CI 2024 | [40.8, 53.6] | **[34.5, 59.9]** (wider — consistent with canonical) |
| TP 95% CI pooled | [44.2, 53.4] | **[42.7, 54.9]** |
| R² | .142–.179 | .033–.084 (within-R²) |

## Verified UNCHANGED across reconciliation

- Turning points: 49.4% / 47.2% / 48.8% — IDENTICAL ✓
- Paternoster z (FSTS): +0.82, p = .412 — IDENTICAL ✓
- Paternoster z (FSTS²): −0.61, p = .545 — IDENTICAL ✓
- Qualitative findings: inverted-U + structural durability — UNCHANGED ✓
- Hypotheses verdicts (H1 supported, H2b supported, H3 NOT supported, H4b supported) — UNCHANGED ✓

## Sections updated

- §4.2 Main Threshold Results: 5 prose citations + Table 2 + footnote
- TP CI ranges in 4.2 prose: 2012 and 2024 widths updated to delta-method canonical

## What NCS should verify

1. Read updated Table 2 + §4.2 to confirm narrative coherence
2. Optionally: re-run `p5/replication/python/full_models.py` on actual .dta files (requires WBES access) to cross-verify
3. Rebuild `p5_china_blinded.docx` via pandoc

## Source attribution

Canonical replication is documented in:
- `p5/replication/python/full_models.py` (pipeline script)
- `p5/replication/results/results_coefs.csv` (51 rows, M1–M8 across 3 samples)
- `p5/replication/results/summary.md` (formatted summary)

Earlier deprecated v1.2 values (FSTS = +1.28 / +1.19) were retained in the manuscript through prior edits but are not reproducible from any current replication script in the repository. The transition to canonical values is necessary for the replication package to be internally consistent.
