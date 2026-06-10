# M-AIDA v7.0 — Meta-Analysis Intelligent Data Assistant

Developed at Can Tho University by Do Thi Thuy Huong.  
Purpose-built for IB meta-analysis: semi-automated effect-size extraction from academic PDFs with human-in-the-loop PI verification and immutable data lock.

## System Architecture

```
frontend (React 18, :3000)
    └── calls ──→ backend (FastAPI, :8765)
                     ├── extractor.py   LLM-based PDF parsing
                     ├── notion_sync.py Notion database sync
                     └── models.py      Pydantic domain models
```

## Quick Start

```bash
# 1. Configure environment
cp backend/.env.example backend/.env
# Edit backend/.env: ANTHROPIC_API_KEY, NOTION_TOKEN, NOTION_DATABASE_ID

# 2. Start with Docker Compose
docker compose up

# 3. Open browser
open http://localhost:3000
```

## API Routes

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/extract` | Base64 PDF body → extracted effect size |
| POST | `/api/extract/upload` | Multipart PDF upload → extracted effect size |
| GET | `/api/studies` | List studies (filter: icrv, dpl, verified, locked) |
| GET | `/api/studies/{id}` | Single study detail |
| PATCH | `/api/studies/{id}/verify` | PI field overrides + approval |
| POST | `/api/studies/{id}/lock` | Irreversible PI data lock |
| GET | `/api/studies/export/csv` | Export locked studies as CSV |
| POST | `/api/notion/sync` | Push locked studies to Notion |
| GET | `/api/health` | Health check + service configuration flags |

## Extraction Workflow

1. **Parse** — PDF text extracted via MuPDF, segmented into statistical regions
2. **Identify** — LLM locates the focal I→P coefficient (not interactions/controls); moderators ICRV/DPL/cDAI are left blank for PI assignment from lookup tables
3. **Convert** — Hierarchy: direct *r* → *r* from *t* → *r*_partial from β (Peterson & Brown, 2005)
4. **Verify** — PI reviews each field; confidence < 0.70 is mandatory review
5. **Lock** — PI data lock is cryptographically timestamped and irreversible

## Citation

Do, T. H. (2025). *M-AIDA v7.0: Meta-Analysis Intelligent Data Assistant* [Software].  
Can Tho University. https://github.com/thuyhuongctu-cell/maida-core

---

## Authorship, license, and research-integrity note

**Author / copyright:** Đỗ Thùy Hương (Do Thuy Huong), College of Economics, Can Tho University.
M-AIDA was developed by the author to support effect-size extraction for Paper 6 of the doctoral
dissertation. It is the basis of a Vietnam Copyright Office (COV) software-copyright registration.

**Role of AI (research-integrity disclosure):** M-AIDA uses a large language model (Anthropic Claude)
to *propose* candidate effect sizes and statistical conversions from study text. It is a
**human-in-the-loop** tool: every proposed value must be independently verified, corrected if needed,
and permanently locked by the Principal Investigator (`pi_locked`) before it enters the analysis
database. The LLM does not select studies, decide eligibility, run the meta-analysis, or write any
interpretive content. This use is disclosed in the Paper 6 manuscript's AI-use statement, consistent
with MOST Circular guidance (Điều 16) and Emerald/Elsevier AI policies.

**Security:** copy `backend/.env.example` to `backend/.env` and supply your own keys; never commit a
real `.env` (it is git-ignored).

> Schema note (v7.0.1, 2026-06-10): the tool schema is aligned with the canonical P6 analysis
> database — ICRV = Institutional Context Regime Variation (I/II/III/FR/MX, WGI Rule of Law);
> cDAI = country Digital Adoption Index (0–1). ICRV, DPL, and cDAI are **PI-assigned from external
> lookup tables during verification**; the LLM extracts only statistics, the data-year window, and
> the two text-determinable classifications (DOI measure, performance measure).
