# Installed Skills Catalog

*Updated: 2026-06-02 — added 5 skills from Auto-Empirical-Research-Skills (AERS) repo*

## Total: 26 skills (21 existing + 5 newly added)

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

## Sources
- All 5 new skills from https://github.com/thuyhuongctu-cell/Auto-Empirical-Research-Skills (AERS, 50+ skills repo)
- License: CC BY-SA 4.0 (preserved)
