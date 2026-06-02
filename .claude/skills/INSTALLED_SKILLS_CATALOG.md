# Installed Skills Catalog

*Updated: 2026-06-02 — added 9 WoS/PRISMA skills (literature review + systematic review)*

## Total: 35 skills (26 prior + 9 newly added)

## Existing skills (21)

### Vietnamese-specific academic
- chinh-sua-tai-lieu-latex-khoa-hoc — LaTeX scientific docs
- chinh-sua-van-ban-hoc-thuat-scopus-wos — Scopus/WoS text cleanup
- chuyen-doi-van-ban-ai-sang-giong-tac-gia — AI text → natural author voice
- chuyen-doi-van-ban-ai-theo-giong-tac-gia — AI text → specific author voice (uses publications)
- phd-academic-writing-humanizer — PhD writing humanizer (em-dash focus)
- academic-translation-vietnamese — EN→VI academic translation
- academic-variable-formatter — Variable notation Scopus/WoS

### Conceptual model
- academic-conceptual-model-diagram — Box/arrow diagrams
- conceptual-model-international-business — IB conceptual models
- conceptual-model-scopus-wos — Scopus/WoS frameworks

### Review + writing
- dissertation-theoretical-framework-reviewer — Theory framework review
- humanizer — 22+ AI pattern detection (Wikipedia methodology)
- stop-slop — AI tells removal

### Utility
- deploy, fix-issue, review (slash commands)
- session-start-hook, handoff, retrospective
- security-review, skill-management
- markitdown, p6-openalex-enrich, github-actions-workflow

## NEW skills installed from AERS (5)

### 1. academic-proofreader-multi-pass
**Source**: AERS skill 38 (peternka)
**Purpose**: Multi-pass elite proofreader for AER/QJE/top-economics journals. Spawns specialist subagents (copyeditor, econometrics checker, citation verifier, table/figure verifier).
**Use for**: P3 Vietnam, P7 JIBS Capstone — high-quality forensic proofread before submission.
**Trigger**: "proofread", "AER proofread", "forensic proofread", "submission ready check"

### 2. humanizer-academic-medical
**Source**: AERS skill 44 (matsuikentaro1)
**Purpose**: AI-tells removal for academic medical/scientific papers (more aggressive than our existing humanizer). Detects inflated significance, superficial -ing, vague attributions, copula avoidance, etc.
**Use for**: All papers — second-pass humanization beyond existing humanizer skill.
**Trigger**: "humanize medical", "academic AI removal"

### 3. empirical-analysis-R-pipeline
**Source**: AERS skill 00.3
**Purpose**: Full R-based empirical pipeline (AER/QJE style) — dplyr + fixest + did + bacondecomp + HonestDiD + rdrobust + Synth + MatchIt + grf + DoubleML + modelsummary + kableExtra + gt.
**Use for**: P6 meta-analysis re-run verification, P3/P5/P9 robustness checks in R.
**Trigger**: "R pipeline", "fixest", "modelsummary R", "DID R", "metafor"

### 4. deslop-academic
**Source**: AERS skill 45 (stephenturner)
**Purpose**: De-slop with scientific writing focus (manuscripts, abstracts, cover letters, grant narratives, discussion sections, peer review responses).
**Use for**: Pre-submission cleanup pass on P3-P9 manuscripts.
**Trigger**: "deslop", "de-AI", "make it sound human"

### 5. avoid-ai-writing
**Source**: AERS skill 47 (conorbronsdon)
**Purpose**: Audit + rewrite for AI-isms with detection-only mode option.
**Use for**: Pre-flight check before iThenticate / AI detector submission.
**Trigger**: "remove AI-isms", "audit AI patterns", "AI detection check"

## Workflow integration

For each paper in Phase A1, recommended skill sequence:

1. **lfe-academic-reviewer** (subagent) — comprehensive review
2. **academic-proofreader-multi-pass** (NEW) — forensic multi-pass for high-stakes papers (P3 JED, P7 JIBS)
3. **chuyen-doi-van-ban-ai-theo-giong-tac-gia** — voice transfer to Do & Phan book chapter style
4. **humanizer** + **humanizer-academic-medical** (NEW combined) — AI-tell removal
5. **deslop-academic** (NEW) — final pre-submission cleanup
6. **avoid-ai-writing** (NEW) — pre-flight detection check
7. **scripts/build_paper_docx.py** — rebuild submission DOCX

For empirical pipeline:
- **empirical-analysis-R-pipeline** (NEW) — useful for P6 meta-analysis verification or any R-based work

## NEW: WoS / PRISMA literature-review skills (9, installed 2026-06-02)

These 9 skills cover Web of Science search, paper detail extraction, BibTeX → literature matrix conversion, chart generation, and full PRISMA 2020 systematic-review automation. They support the **CĐ1 Tổng luận tài liệu** and **P6 meta-analysis** workflows.

### Search + paper-detail layer (5 skills)
- **wos-search** — Search WoS by topic / author / title / DOI; supports edition + database filtering. Requires Chrome DevTools MCP + WoS institutional login.
- **wos-paper-detail** — Get full metadata for a paper by WoS ID (e.g., WOS:000779183600001).
- **wos-parse-results** — Internal helper used by other WoS skills to parse results pages / API responses.
- **wos-navigate-pages** — Navigate / paginate / "load more" on the WoS results page.
- **wos-export** — Export citations from a WoS result set (BibTeX / RIS / CSV).
- **wos-download** — Download PDFs of WoS hits where the institution has access.

### Literature-matrix + chart layer (2 skills)
- **wos-review-matrix** — Convert WoS BibTeX exports to thematic literature-review matrix (Markdown + CSV) + Word DOCX literature review with GB/T 7714-2015 references. *Caveat for our portfolio: outputs GB/T 7714 references; project uses APA7 (thesis/04_references_apa7.md). Use the matrix output but regenerate the reference list via scripts/format-apa7.py.*
- **wos-review-workflow** — Self-contained chart-generation workflow with bundled Python + map shapefiles. 7 chart types (yearly bar, collaboration bar, chord, world map, keyword bar, keyword pie, wordcloud) from a WoS Excel export. Useful for the P6 meta-analysis descriptive figures and the CĐ1 Tổng luận tài liệu visualisation block.

### Full-pipeline layer (1 skill)
- **systematic-review** — PRISMA 2020 systematic review pipeline. Heavily automated: search strategy, multi-source consolidation (PubMed + Semantic Scholar + OpenAlex + Consensus + WoS/Embase), CrossRef DOI verification, dedup, two-pass screening, RoB, meta-analysis with R metafor, PRISMA 2020 diagram, PROSPERO draft, PRISMA-trAIce checklist. Requires multiple MCPs (PubMed, Consensus, Zotero) for full automation.

## Where each WoS/PRISMA skill applies in the portfolio

| Skill | CĐ1 Tổng luận | P6 Meta | P3–P9 | Notes |
|---|:-:|:-:|:-:|---|
| wos-search | ✅ | ✅ | — | Needs Chrome + WoS login (local env) |
| wos-paper-detail / parse / navigate / export / download | ✅ | ✅ | — | Companion to wos-search |
| wos-review-matrix | ✅ | ✅ | — | Needs a large WoS BibTeX export (200–500+ hits); the existing `references/p*.bib` are small *cited-references* exports, not search exports |
| wos-review-workflow | — | ✅ | — | Needs a WoS Excel export; could regenerate P6 yearly / collaboration / world-map figures |
| systematic-review | — | ✅ | — | Heaviest dependency footprint; useful if redoing P6 with PRISMA-trAIce AI-disclosure checklist |

## Skills NOT installed from this upload batch

- **ECC (Everything Claude Code)** — 30 agents / 135 skills / 60 commands mega-plugin. Too broad and generic for the dissertation context; would clutter `.claude/skills/` with non-academic dev tools.
- **VoxCPM** — Voice TTS library; not relevant for dissertation text work.
- **WBES-DATA-VIEWER** — Mislabelled despite the alluring name; this is for "Web-Based Energy Scheduling" (power-grid data), NOT World Bank Enterprise Survey.
- **global-reports** — Documentation repo (README + CODE_OF_CONDUCT + CONTRIBUTING only); no skill artifacts.
- **awesome-resources** — Community awesome-list; not a skill.

## Why none of the 9 new skills could be auto-applied to the repo in this session

The dissertation portfolio repo does not contain the inputs these skills expect:

- No WoS-export `.xls(x)` files in `p6/` (wos-review-workflow input)
- The existing `references/p*.bib` files are post-writing cited-references exports (~10–50 entries each), not raw WoS search exports (200–500+) that wos-review-matrix is designed to process
- This remote container does not have Chrome DevTools MCP + WoS institutional login (CTU credentials), nor PubMed / Consensus / Zotero MCPs that systematic-review's full automation requires

To actually use any of these skills, the NCS should run them locally on the laptop where Chrome + the CTU WoS institutional login + Zotero are available. The skills are installed and registered; the moment the appropriate inputs (WoS BibTeX or Excel exports) appear in the repo, they become applicable.

## Sources
- 5 AERS skills (2026-06-02 prior session): https://github.com/thuyhuongctu-cell/Auto-Empirical-Research-Skills
- 9 WoS/PRISMA skills (this session): wos-search-skill, wos-review-skill, wos-review-matrix-skill, systematic-review-skill, wos-skills (bundle) — all user-uploaded zips
- Licenses: MIT (wos-* + systematic-review), CC BY-SA 4.0 (AERS) — all preserved.
