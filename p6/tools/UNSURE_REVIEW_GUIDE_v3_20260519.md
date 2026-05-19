# UNSURE Review Guide — L2 Manual Screening (v3, 19/05/2026)

## Summary

After v3 rule-based prescreening of 535 extraction candidates:
- **Pre-Y**: 394 (73.6%) — probable INCLUDE, proceed to effect-size extraction
- **Pre-N**: 45 (8.4%) — probable EXCLUDE, verify then dismiss
- **UNSURE**: 96 (17.9%) — require manual review (this guide)

Use: `p6/tools/results/extraction_worklist_v10_20260519.csv`  
Sort by `prescreen_flag` → review N first, then UNSURE.

---

## UNSURE Breakdown (96 papers)

| Category | Count | Action |
|----------|-------|--------|
| `WEAK-INCL:exporter` | 11 | Likely INCLUDE if exports → firm performance; EXCLUDE if exports is DV |
| `WEAK-INCL:financial-perf` | 6 | Likely INCLUDE if I→financial performance clear; check direction |
| `WEAK-INCL:subsidiaries` | 2 | Likely INCLUDE if FDI/subsidiary → firm performance; EXCLUDE if DV is entry decision |
| `NO-CLEAR-SIGNAL` | 77 | Need abstract to determine direction; see batched list below |

---

## Batch 1: WEAK-INCL Cases (19) — Quick Review (~30 min)

These have a weak INCLUDE signal. Read title + abstract. The key question:
> **Is this measuring how internationalization (FSTS/exports/FDI/multinationality) affects firm financial performance (ROA/productivity/revenue growth)?**

**YES → Y** | **NO → N** | **Abstract inconclusive → get full text**

WEAK-INCL papers (priority sort):
| seq | Title (truncated) | Signal | Suggested |
|-----|-------------------|--------|-----------|
| 463 | Finding the sweet spot: effects of exporting on the relationship between... | WEAK-INCL:exporter | Likely Y |
| 466 | Exporting is a team sport: the link between management training and performance | WEAK-INCL:exporter | Likely Y |
| 187 | The Joint Effects of Firm's Globalization and ESG Rating on Financial performance | WEAK-INCL:financial-perf | Likely Y |
| 6 | Overseas Business and Ethnic Ties, Slack Resources... | WEAK-INCL:exporter | UNSURE — check DV |
| 30 | The inefficiency of exporting SMEs: Evidence from manufacturing | WEAK-INCL:exporter | Likely Y |
| 275 | From domestic to exporter, what happens? Evidence for Spanish manufacturers | WEAK-INCL:exporter | Likely Y (learning-by-exporting) |
| 395 | Antecedents to differentiation strategy in the exporting SME | WEAK-INCL:exporter | Likely N (strategy as DV) |
| 404 | Effects of the use of competitiveness as a strategy on exporting companies | WEAK-INCL:exporter | UNSURE — check DV |
| 208 | Home country adverse political shocks and cross-border M&A... | WEAK-INCL:financial-perf | UNSURE — check if I→P |
| 38 | How does offshore outsourcing of knowledge-intensive activities affect... | WEAK-INCL:financial-perf | UNSURE — check DV |

---

## Batch 2: NO-CLEAR-SIGNAL — "Export Intensity / ESG / Tax" Group (~20 papers)

These often have export intensity mentioned but not clearly as I measure → firm performance.

Key papers to prioritize:
| seq | Title | Likely verdict |
|-----|-------|---------------|
| 1 | Corporate ESG Performance, Ownership Structure and **Export Intensity** | Likely Y if ESG→export intensity, but **check if export intensity is DV** |
| 37 | Does Corporate ESG Performance Improve **Export Intensity**? | Likely N (ESG→export intensity wrong direction) |
| 39 | Does environmental disclosure increase firm exports? | Likely N (disclosure→exports wrong direction) |
| 10 | The impact of enterprise income tax on firm export | Likely N (tax→exports wrong direction) |
| 43 | CEO gender, institutional context and **firm exports** | UNSURE — if exports→performance then Y; if CEO→exports then N |
| 32 | ICT Investment, ISO 14000, and Export Performance in India | Likely N (ICT→export perf wrong direction) |
| 35 | R&D and export performance: heterogeneity along export intensity | BORDERLINE — "export intensity" is I measure, need to check DV |
| 57 | Bank credit, public incentives, tax incentives and export performance | Likely N (credit/incentives→export perf wrong direction) |
| 68 | Export Performance and Stock Return: Case of Fishery Firms | BORDERLINE — could be I→P if exports→stock return |

---

## Batch 3: NO-CLEAR-SIGNAL — Internationalization → Performance Group (~20 papers)

These are genuine ambiguous cases. Need abstract to determine if I→P relationship measured.

| seq | Title | Priority | DOI |
|-----|-------|----------|-----|
| 27 | A vicarious learning perspective on home-peer-firm... | High | Yes |
| 28 | Configuring foreign market knowledge and opportunity recognition... | High | Yes |
| 40 | Impact of sourcing from informal economy on export likelihood... | High | Yes |
| 69 | Product Newness, Low Competition, Recent Technology, and Export Orientation | High | Yes |
| 99 | Effects of board composition, board size and CEO duality on export performance | High | Yes |
| 98 | Effects of top management team composition on SME export performance | High | Yes |
| 102 | What Determines Small Champions' Export Performance? Evidence from Korea | High | Yes |
| 104 | Foreign market experience, learning by hiring and firm export performance | High | Yes |

---

## Eligibility Decision Rules (Quick Reference)

```
INCLUDE (Y) if:
  ✓ IV = export intensity/FSTS/multinationality/DOI/FDI
  ✓ DV = firm financial performance (ROA, ROE, productivity, Tobin's Q, sales growth)
  ✓ Quantitative r or beta reported (or computable from t/F)
  ✓ Firm-level unit of analysis

EXCLUDE (N) if:
  ✗ IV = capability/strategy/resources, DV = export performance → WRONG DIRECTION
  ✗ Export participation/propensity is the DV (who exports, not how they perform)
  ✗ Country-level macro analysis
  ✗ Qualitative, conceptual, case study
  ✗ No quantitative effect size (survey results without r/beta)
  ✗ Health, education, environment-only journals
```

---

## After Manual Review

1. Update `prescreen_flag` → `include_flag` for reviewed rows (Y/N confirmed)
2. For Y papers: fill `r`, `n`, `icrv`, `doi_type`, `fp_type` from full text
3. Run `python3 p6/tools/10_merge_new_studies.py` to merge new Y papers into k=238 database
4. For the remaining ~394 Pre-Y cases: same extraction process for r and n
5. Run `p6/tools/compute_reliability.R` after 20% subsample double-coded

## Claude API Batch Screener (Optional)

For the 77 NO-CLEAR-SIGNAL cases, you can use the Claude API screener
to get AI-based recommendations before manual review:

```bash
python3 p6/tools/29_claude_api_batch_screener.py \
  --input p6/tools/results/extraction_worklist_v10_20260519.csv \
  --output p6/tools/results/l2_ai_screened_20260519.csv \
  --api-key sk-ant-YOUR_API_KEY \
  --mode unsure
```

Cost estimate: ~77 papers × $0.00025 ≈ **< $0.02**
