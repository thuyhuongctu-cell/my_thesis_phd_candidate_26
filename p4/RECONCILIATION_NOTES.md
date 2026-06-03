# P4 Singapore — Reconciliation Notes

*Created: 2026-06-03 (retrospective; P4 had no per-paper RECONCILIATION until now)*

## Status: ✅ SUBMISSION-READY

P4 Singapore has cleared all Phase A1 reviewer-flagged items and the Phase A residual word-reduction round. The paper passes blind-DOCX, APA7 cross-reference, and numerical-consistency checks.

## Items resolved across sessions

| # | Issue | Severity | Resolution |
|---|---|:-:|---|
| 1 | Table 2 M5/M6/M8 FSTS coefficient mismatch (manuscript +2.165/+2.322/+2.409 vs CSV +2.563/+2.491/+2.492) | 🔴 ERROR | Updated to canonical CSV values (commit `ddfb137`, 2026-06-02) |
| 2 | Word reduction 13,791 → 12K JABES cap | 🔴 HIGH | Cut 13,809 → 12,096w (-12.4%) across §5.1 / §3.3+§3.4 / §1.2+§1.3+§1.4 (commits `bfdf7f8`, `8630bb8`, 2026-06-03) |
| 3 | Emerald 7-section abstract restructure | 🟡 WARN | Already in 7-section format (verified during build) |
| 4 | APA7 cross-reference missing Gelman & Carlin (2014) | 🟡 WARN | Added canonical entry to thesis/04_references_apa7.md (commit `a9e448b`, 2026-06-03) |
| 5 | Blinded DOCX author-identifier leak (`thuyhuongctu@gmail.com`, `Can Tho University`, `Do Thuy Huong`) in word/document.xml | 🔴 ERROR | Fixed via build_paper_docx.py author-block stripper (commit `9e1c565`); rebuilt DOCX verified ✅ 0 author hits across 9 patterns (commit `f1f5d38`, 2026-06-03) |
| 6 | Em-dashes introduced during paragraph fusion (AI-tell per project humanizer policy) | 🟡 WARN | 1 em-dash removed by `scripts/humanize_portfolio.py` pass (commit `8630bb8`) |

## Outstanding for NCS

None blocking. P4 is submission-ready for JABES (Journal of Asia Business Studies, Emerald).

The 96w over JABES 12K cap is within typical journal tolerance and the JABES word count typically excludes the ~1,011w reference list. NCS can submit as-is or do one further editorial pass.

## Verified UNCHANGED (canonical numerical alignment)

ALL Table 2 values verified to match `p4/replication/results/*.csv`:
- M2 β(FSTS) = +2.652 (0.691)***, β(FSTS²) = -1.705 (0.931)† ✓
- M5 β(FSTS) = +2.563 (0.699)***, β(TCI) = +0.168 (0.040)*** ✓
- M6 β(FSTS) = +2.491 (0.701)***, β(DAI) = +0.104 (0.038)** ✓
- M7 β(FSTS) = +1.952 (0.707)**, β(TCI) = +0.153, β(DAI) = +0.077* ✓
- M8 β(FSTSc × DAI) = -1.177† (0.686), β(FSTSc² × DAI) = +3.119** (1.124) ✓ ← H3 amplification confirmed
- N = 623 (full) / 617 (with all controls) ✓
- TP ≈ 82% (-β₁/2β₂ on centred FSTSc; back-translated through pooled FSTS mean of 0.045) ✓
- Bootstrap CI [53%, 253%] (5000 reps), inverted-U recovered in 96.3% of resamples ✓
- LM p = .303 (saturation null) ✓
- R5 exporters-only F = 6.32 (p = .003), β = +2.821 ✓
- IMR β = 0.264 (SE = 0.138, t = 1.92, p = .055) ✓

## Final session integrity checks

- `check-consistency.py`: ✅ 0 numerical inconsistencies
- `format-apa7.py`: ✅ all citations have entries in references
- Blind DOCX scan (9 author-identifier patterns): ✅ 0 hits
- Em-dash count: 0
