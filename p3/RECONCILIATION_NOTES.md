# P3 Vietnam — Reconciliation Notes

*Created: 2026-06-02 (after lfe-academic-reviewer Phase A1 review)*

## Status: PARTIALLY RESOLVED

3 of 5 reviewer-flagged items addressed in this session. **Critical word-reduction work deferred to NCS (12-16h estimated effort).**

## Fixed in this session

| # | Issue | Severity | Action |
|---|---|:-:|---|
| 1 | Word count declared 6,800 vs actual 21,372 | 🔴 CRITICAL | Updated to "~16,800 words (reduction to ~9,500 pending)" |
| 2 | Inline journal acronyms "(2020, SMJ)" / "(2022, MIR)" | 🟡 WARNING | Removed all inline journal tags |
| 3 | Coefficient discrepancies: β=-0.587 vs CSV -0.573; +0.640 vs +0.627 | 🟡 WARNING | Updated to canonical CSV values |

## Outstanding for NCS — MAJOR

| # | Issue | Severity | Effort | Notes |
|---|---|:-:|---:|---|
| 4 | **Word reduction 21K → ~9,500 words** | 🔴 CRITICAL | 12-16h | Section budgets per reviewer recommendation below |
| 5 | **TP rescaling documentation** | 🔴 HIGH | 1h | TP=39.7% claim vs mechanical β=−0.984/(2×−1.909)=25.8%; need explicit "FSTSc centring + back-translation to FSTS share" math note in §3.5 |

## Word reduction plan (per reviewer)

| Section | Current narrative | TARGET | Cut |
|---|---:|---:|---:|
| Abstract | 411 | 240 | −171 |
| §1 Introduction | 1,595 | **900** | −695 |
| §2 Theory & Hypotheses | 2,676 | **1,200** | −1,476 |
| §3 Methods | 1,659 | **1,100** | −559 |
| §4 Results | 3,869 | **2,500** | −1,369 |
| §5 Discussion | 2,731 | **1,800** | −931 |
| §6 Limitations | 564 | **350** | −214 |
| §7 Conclusion | 253 | 250 | 0 |
| **Total narrative** | **~15,500** | **~9,500** | **~−6,000** |

**Top reduction targets** (per reviewer):
1. **§2 Theory** (cut ~1,500w): Collapse H1/H2/H3/H4 justification blocks to 1 paragraph + 1-line formal hypothesis each. Move conceptual model "Note:" (350w) to figure caption.
2. **§4 Results** (cut ~1,400w): Move §4.5 robustness panels A-K to Online Appendix; keep summary table only.
3. **§5 Discussion** (cut ~900w): Consolidate §5.1 (DAI obsolescence) + §5.2 (TCI-DAI distinction) - heavy redundancy.
4. **§1 Introduction** (cut ~700w): Merge §1.2 (gap) + §1.3 (contribution) into single 600w block.
5. **Highlights** (250w): JED doesn't use Emerald structured highlights — fold into abstract.

## Verified UNCHANGED

ALL coefficient values match canonical `p3/replication/coefs_main_models.csv`:
- Pooled M2 FSTSc: +0.984 ✓ matches CSV 0.9843
- Pooled M2 FSTSc²: −1.909 ✓ matches CSV −1.9091
- Pooled M7 TCI_z: +0.179 ✓ matches CSV 0.1792
- Pooled M8 FSTSc²: −1.650 ✓ matches CSV −1.6497
- 2023 M8 FSTSc×DAI_z: −0.912 ✓ matches CSV −0.9121
- Paternoster z = 3.353 ✓
- N=2,958 = 989+956+1,013 ✓

Step-function decomposition: Panel H exporter-only quadratic β = −0.200, p=.660 (unverified in main CSV; confirm via supplementary).

## Theoretical defensibility

Reviewer assessment: "defensible. Step-function reading is empirically sharp." Genuine novelty:
- Within-country temporal durability of TP band (39-46%) across 14 years through WTO/GFC/CPTPP/EVFTA/COVID shocks
- Tier-1 digital proxy obsolescence framing (positive→null→negative trajectory)

Recommended tightening: "contribution is empirical decomposition, not mechanism discovery."

## Publishability ceiling at JED

After fixes: realistic MAJOR REVISE accept. Empirical core (step-function + temporal durability + digital obsolescence) is JED-grade. Vietnam-WBES portfolio role (lower-middle ICRV IV baseline) well-justified.
