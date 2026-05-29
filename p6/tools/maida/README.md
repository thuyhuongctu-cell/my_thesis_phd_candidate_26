# M-AIDA v7.0 — Meta-Analysis Intelligent Data Assistant

Developed at the College of Economics, Can Tho University, by Đỗ Thị Thúy Hương (PI) and
Phan Anh Tú. Purpose-built for IB meta-analysis: semi-automated effect-size extraction from
academic PDFs with human-in-the-loop PI verification and an immutable data lock.

## System Architecture

Single-file web application (`MAIDA_intake.html`) — runs entirely client-side in the browser,
no server, no external database, no API key embedded in source.

```
MAIDA_intake.html  (HTML5 + JavaScript ES2017+, no build step)
    ├── PDF.js 3.11 (CDN)         → readPdf: extract text from PDF
    ├── ruleExtract (offline)      → regex extraction of N, r, t(df), F(1,df2), β
    ├── aiExtract (window.claude)  → Claude artifact API draft extraction (claude.ai)
    ├── conversion: t2r / beta2r / f2r / clampR / z (Fisher z)
    ├── renderCands / accept       → PI verify → LOCK (audit trail)
    └── exportCSV / JSON           → locked records only
```

## Quick Start

Open `MAIDA_intake.html` in any modern browser. No install, no server.

- **Nạp PDF / .txt** or paste text into the textarea.
- **Trích xuất (AI)** uses Claude inside a claude.ai artifact (no API key); outside claude.ai it
  automatically falls back to **Trích xuất theo quy tắc** (offline regex).
- Verify each candidate (edit N / df / r / p / measure), then **Kiểm chứng ✓** to lock it.
- **Kết xuất CSV / JSON** exports only verified-and-locked records.

## Effect-size conversion hierarchy (dissertation §3.3.1)

When Pearson's *r* is not reported directly, conversions are applied in order of statistical
precision:

1. *r* from *t*: `r = √(t² / (t² + df))` (Cohen, 1988) — sign preserved.
2. *r*_partial from standardized β: `r = 0.98 × β` (Peterson & Brown, 2005).
3. *r* from *F* (df₁ = 1): `r = √(F / (F + df₂))` (Rosenthal, 1994).

All *r* are then Fisher-transformed `z = ½·ln[(1+r)/(1−r)]`; any |r| ≥ 1 is rejected.

## Export fields (CSV)

`study_id, effect_id, author, year, country, r, n, fisher_z, measure, moderator, p, source`

## Citation

Đỗ, T. T. H., & Phan, A. T. (2026). *M-AIDA v7.0: Meta-Analysis Intelligent Data Assistant*
[Computer software]. Can Tho University. See `CITATION.cff`.
