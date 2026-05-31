# Humanizer Full-Portfolio Pass — Completion Report

**Date:** 2026-05-31
**Skill:** `.claude/skills/humanizer/` v2.7.0 (22+ pattern categories)
**Scope:** All 17 documents — 6 papers EN, 4 papers VI, 2 chuyên đề VI, 5 thesis chapters VI

---

## 1. Approach

1. **Built `scripts/humanizer_scan.py`** to detect AI-writing patterns across EN + VI prose. Patterns from `humanizer` skill (§3 -ing tells, §4 promotional, §7 AI vocab, §8 copula avoidance, §9 negative parallelism, §14 em-dash, §23 filler, §27 persuasive authority) + Vietnamese-specific patterns from `phd-academic-writing-humanizer`.
2. **Two refinement iterations** to remove false positives:
   - Excluded markdown tables (em-dash used as "no data" placeholder)
   - Excluded en-dash `–` (legitimate in compound terms: I–P, Levinsohn–Petrin, Lind–Mehlum, number ranges 5–10)
   - Excluded "significantly" (standard statistical reporting language, not an AI tell)
   - Excluded Vietnamese "đáng kể"/"đáng chú ý" (legitimate academic qualifiers, ≈ "substantial"/"notable")
3. **Surgical-mode fixes** — only edited clear AI tells, preserved all academic register and substantive content.

## 2. Surgical edits applied (9 total)

| File | Pattern | Before | After |
|---|---|---|---|
| `manuscripts/p3_vietnam_en_clean.md` L61 | §27 persuasive | `This tension lies at the heart of the I–P literature.` | `This tension is central to the I–P literature.` |
| `manuscripts/p4_singapore_en_clean.md` L62 | §23 filler | `mean-centered before squaring in order to mitigate` | `mean-centered before squaring to mitigate` |
| `manuscripts/p4_singapore_en_clean.md` L101 | §23 filler | `TCI interaction terms in order to assess` | `TCI interaction terms to assess` |
| `manuscripts/p4_singapore_en_clean.md` L198 | §7 AI vocab | `A formal power analysis underscores the implication` | `A formal power analysis quantifies the implication` |
| `manuscripts/p4_singapore_en_clean.md` L220 | §7 AI vocab | `it also underscores that the evidence is concentrated` | `it also signals that the evidence is concentrated` |
| `manuscripts/p5_china_en_clean.md` L55 | §7 AI vocab | `one of the most enduring questions` | `one of the longest-standing questions` |
| `manuscripts/p5_china_en_clean.md` L85 | §7 AI vocab | `rather than an enduring structural trade-off` | `rather than a stable structural trade-off` |
| `manuscripts/p5_china_en_clean.md` L409 | §7 AI vocab | `It is an enduring structural feature` | `It is a stable structural feature` |
| `manuscripts/p5_china_en_clean.md` L271 | §27 persuasive | `the bounded-optimum logic at the heart of H1` | `the bounded-optimum logic central to H1` |

## 3. Items NOT edited (and why)

### 3.1 Em-dashes (90 remaining)
The vast majority of remaining em-dashes (90/110 = 82%) are **intentional formatting**:

- **Citation venue tags** `(Author Citation, 2026 — JFAR)` / `(Author Citation, 2026 — VEFR)` — the candidate uses this format to disambiguate multiple 2026 self-citations while preserving blind-review status. Changing to APA7 letter suffix (2026a/b/c) would un-blind by revealing the author has multiple 2026 papers.
- **Acronym definitions** `Resource-Based View — RBV` / `liability of foreignness — LOF` — standard academic inline-definition convention.
- **Block headers in lists** `**Block C — Financing Structure:**` — typographic separator, not prose.
- **Edit-history notes** in document front-matter (intentional, functional).

These are not AI tells; replacing them en masse would degrade rather than improve the prose.

### 3.2 ", reflecting" -ing endings (12 remaining)
All 12 instances examined are **substantive causal/descriptive links**, not decorative wrap-ups:

- Hypothesis statements (P5 H2a/H2b): explain mechanism behind predicted pattern
- Descriptive statistics: attach substantive cause to observed trends
- Sample composition notes: explain why a metric has a particular value

Removing them would weaken the prose. Example: `"shifted toward machinery and electronics, reflecting a structural upgrade"` — the participle attaches a substantive interpretation; rephrasing as a separate sentence would add a sentence break without information gain.

### 3.3 Negative parallelism (4 remaining)
- P3 L951 `"not merely a"` — substantive contrast with prior literature claim
- P4 L19 `"is not whether"` — legitimate framing of unresolved question
- P7 L47 `"not just a parallel upward shift"` — substantive analytical distinction (TCI's effect goes beyond level shift)
- P7 L233 `"not merely a proxy for firm governance quality"` — substantive rejection of alternative interpretation

All 4 are real academic argumentation using a common rhetorical device, not decorative AI patterns.

### 3.4 "Serves as a" copula avoidance (1 remaining)
P3 L337: `"c22b alone serves as a harmonised cross-wave proxy"` — "serves as a proxy" is standard methodology vocabulary for instrumental variables and measurement constructs. Not an AI tell.

### 3.5 Vietnamese AI vocab (1 remaining)
P3 VI L617: `"bối cảnh thay đổi"` — appears in a substantive Discussion-section caveat about generalisability scope. Legitimate Vietnamese phrasing.

## 4. Final state

| Document | Words | Total hits | Density/1000w | Verdict |
|---|---:|---:|---:|---|
| P3 Vietnam (EN, APJM) | 16,864 | 8 | 0.47 | ✅ Clean |
| P4 Singapore (EN, MIR) | 9,618 | 3 | 0.31 | ✅ Clean |
| P5 China (EN, IJOEM) | 14,614 | 23 | 1.57 | ✅ Clean (em-dashes are venue tags) |
| P6 Meta (EN, MIR) | 8,355 | 6 | 0.72 | ✅ Clean |
| P7 Capstone (EN, JIBS) | 8,838 | 4 | 0.45 | ✅ Clean |
| P8 SIDS (EN, World Dev) | 5,762 | 1 | 0.17 | ✅ Clean |
| P3/P4/P5/P6 (VI) | 70,164 | 49 | 0.70 | ✅ Clean (mostly venue tags) |
| CĐ1 | 11,891 | 0 | 0.00 | ✅ Spotless |
| CĐ2 | 18,909 | 5 | 0.26 | ✅ Clean |
| Ch1 Giới thiệu | 5,649 | 0 | 0.00 | ✅ Spotless |
| Ch2 Tổng quan | 13,450 | 2 | 0.15 | ✅ Clean |
| Ch3 Phương pháp | 6,903 | 5 | 0.72 | ✅ Clean |
| Ch4 Kết quả | 10,380 | 7 | 0.67 | ✅ Clean |
| Ch5 Kết luận | 8,058 | 0 | 0.00 | ✅ Spotless |

**Total residual hits: 110** (down from ~565 in initial raw scan)
- 90 = em-dashes in citation venue tags / acronym definitions / block headers (intentional)
- 20 = substantive ", reflecting" / negative parallelism / methodology phrasing (legitimate)

## 5. Submission readiness

| Paper | Journal | Checklist | Status |
|---|---|---|---|
| P3 Vietnam | APJM | 12/12 | ✅ SẴN SÀNG NỘP |
| P4 Singapore | MIR | 12/12 | ✅ SẴN SÀNG NỘP |
| P5 China | IJOEM | 12/12 | ✅ SẴN SÀNG NỘP |
| P6 Meta | MIR | 10/12 (0 critical) | ✅ Submission-ready (2 WB warnings are FP for meta-analysis) |
| P7 Capstone | JIBS | 11/12 (1 FP "affiliation" in Cho et al. ref title) | ✅ Submission-ready |
| P8 SIDS | World Development | N/A (no template) | ✅ Submission-ready |

## 6. Rebuilt deliverables

- `p3/submission/apjm_package/01_manuscript_blinded.docx` + `p3/submission/p3_vietnam_manuscript_blinded.docx`
- `p4/submission/mir_package/01_manuscript_blinded.docx` + `p4/submission/p4_singapore_manuscript_blinded.docx`
- `p5/submission/ijoem_package/01_manuscript_blinded.docx` + `p5/submission/p5_china_manuscript_blinded.docx`

## 7. Methodology note

The scanner and audit are reproducible: `python3 scripts/humanizer_scan.py` regenerates `reports/humanizer_audit.{md,json}` from current source. Any reviewer can verify the pattern coverage independently.

---

*Generated 2026-05-31 after applying `/humanizer` skill (surgical mode) across all 17 portfolio documents.*
