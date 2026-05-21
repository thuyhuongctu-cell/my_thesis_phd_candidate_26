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
2. **Identify** — LLM locates the focal I→P coefficient (not interactions/controls)
3. **Convert** — Hierarchy: direct *r* → *r* from *t* → *r*_partial from β (Peterson & Brown, 2005)
4. **Verify** — PI reviews each field; confidence < 0.70 is mandatory review
5. **Lock** — PI data lock is cryptographically timestamped and irreversible

## Citation

Do, T. H. (2025). *M-AIDA v7.0: Meta-Analysis Intelligent Data Assistant* [Software].  
Can Tho University. https://github.com/thuyhuongctu-cell/maida-core
