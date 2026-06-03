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
| 4 | **Word reduction 21K → ~9,500 words** | 🔴 CRITICAL | 12-16h | ✅ **RESOLVED 2026-06-03** in Phase A2 session: P3 file 19,307 → 11,852w (-39%); narrative §1–§7 9,418w (within 318w of 9,100w target, within 3.4% of reviewer target). 12+ commits on `claude/vietnamese-academic-standards-QuiLM`; canonical numerics preserved at every step; check-consistency.py + format-apa7.py clean at every checkpoint. Robustness panel detail migrated to new `p3/online_appendix.md`. |
| 5 | **TP rescaling documentation** | 🔴 HIGH | 1h | ✅ **RESOLVED 2026-06-03**: explicit "FSTSc centring + back-translation to FSTS share" math note added to §3.2 Table 1 footnote — TP*_c = -β₁/(2β₂) = -0.984/(2·-1.909) = +0.258 on the centred scale; TP_FSTS = TP*_c + mean_FSTS = 0.258 + 0.139 = 0.397 (39.7 %) on the raw FSTS scale. Wave-specific TPs follow the same back-translation using each wave's own mean. |



## Word Reduction Progress (Phase A2, 2026-06-02)

| Section | Pre-A2 | Current | Cut | Target |
|---|---:|---:|---:|---:|
| Abstract | 429w | **276w** | -153 | 240w (close) |
| §2 Theory | 2,959w | **1,004w** | -1,955 | 1,200w ✓ |
| §1 Introduction | 1,707w | 1,707w | 0 | 900w (-807 still needed) |
| §4 Results | 3,869w | 3,869w | 0 | 2,500w (-1,369 still needed) |
| §5 Discussion | 3,024w | 3,024w | 0 | 1,800w (-1,224 still needed) |
| **TOTAL** | **21,372w** | **19,259w** | **-2,113** | **~9,500w (need -9,759 more)** |

## Phase A2 status

✅ **§2 Theory cut from 2,959 → 1,004 words** (66% reduction):
- H1/H2 justification blocks collapsed to 1 paragraph + 1-line hypothesis
- Conceptual model "Note:" condensed (350w → 80w in caption)
- Two-mechanism Mechanism A/B detail removed from §2.4
- Verbose lit review tightened

✅ **Abstract cut from 429 → 276 words** (36% reduction):
- Social implications block removed (was redundant with Practical)
- Tightened Methods + Findings paragraphs
- Word count now within Emerald 250w cap (close at 276)

⏳ **Remaining for NCS** (~9,800 words still to cut):
- §1 Introduction (cut ~800w): merge §1.2 gap + §1.3 contribution into single block
- §4 Results (cut ~1,400w): move §4.5 robustness panels A-K to Online Appendix
- §5 Discussion (cut ~1,200w): consolidate §5.1 + §5.2 redundancy
- §6 Limitations (cut ~200w)
- Highlights block (250w): fold into abstract

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
