---
name: markitdown
description: >
  Convert PDF, DOCX, XLSX, PPTX, HTML, images (EXIF + OCR), audio (transcription),
  CSV/JSON/XML, EPub, ZIP archives, and YouTube URLs to clean Markdown using
  Microsoft's markitdown library (v0.1.6+, MIT). Designed to feed LLM pipelines
  with structure-preserving text (headings, lists, tables, links). Use this skill
  when the user asks to read/extract/quote content from a non-Markdown file in
  the dissertation portfolio — for example: reviewer PDFs, supervisor feedback
  DOCX, WBES codebook XLSX, journal templates, OSF download bundles, or any
  Microsoft Office artifact. Complements the M-AIDA in-browser PDF reader
  (PDF.js + regex) by providing a CLI batch-conversion path that captures full
  prose plus tables for sustained text analysis. Output is plain Markdown
  printed to stdout; redirect to file as needed.
license: MIT
metadata:
  version: '0.1.6'
  source: 'https://github.com/microsoft/markitdown'
  upstream-package: 'markitdown[all] (pip)'
  installed: 2026-05-31
---

# Markitdown — File Conversion Skill (Microsoft)

## When to invoke this skill

Invoke when the user asks you to:

- Read a PDF/DOCX/XLSX/PPTX they uploaded or referenced by path
- Extract tables from an Excel codebook (e.g., WBES variable dictionary)
- Convert a journal's submission template DOCX so you can edit in Markdown
- Pull quotes from supervisor feedback documents
- Process a batch of reference manager exports
- Read OSF download bundles (ZIP)
- Transcribe an audio recording (lecture, meeting) — supports speech_recognition

Do NOT invoke for:
- Files already in `.md` / `.txt` / `.csv` (read directly with the Read tool)
- Files inside fenced code blocks or inline content (already text)
- Conversions where the user explicitly wants a different tool (e.g., pandoc)

## How to invoke

### Basic single-file conversion

```bash
markitdown <path-to-file>                  # prints Markdown to stdout
markitdown <path-to-file> > output.md      # save to file
```

### Single file with output flag

```bash
markitdown -o output.md <path-to-file>
```

### Stdin/pipe

```bash
cat document.pdf | markitdown
```

### Python API (preferred when batch-processing inside a script)

```python
from markitdown import MarkItDown
md = MarkItDown(enable_plugins=False)   # set True only if user has plugins
result = md.convert("path/to/file.pdf")
print(result.text_content)
```

## Common project workflows

### 1. Extract text from a reviewer PDF

```bash
markitdown reviews/jibs_review_round1.pdf > reviews/jibs_review_round1.md
```

Then Read the .md to quote reviewer comments back in your reply.

### 2. Extract WBES codebook table to inspect variable definitions

```bash
markitdown data/WBES_codebook_2024.xlsx > data/WBES_codebook_2024.md
```

The XLSX → MD conversion preserves table structure as Markdown tables.

### 3. Read supervisor's DOCX feedback with track-changes

```bash
markitdown supervisor_feedback/2026-05-15_chuong3_feedback.docx
```

Note: markitdown extracts the *final accepted* text only. To see track-changes,
the user needs to first accept/reject in Word, or use a different tool.

### 4. Batch convert a folder of journal templates

```bash
for f in templates/journal_*.docx; do
  markitdown "$f" > "${f%.docx}.md"
done
```

### 5. Process the OSF download bundle (ZIP)

```bash
markitdown osf_download_z37kn.zip > osf_contents.md
```

markitdown iterates ZIP contents and converts each supported file.

## Output characteristics

- Headings: preserved (H1-H6 → `#` to `######`)
- Lists: preserved (bullet + numbered)
- Tables: preserved as Markdown tables
- Links: preserved as `[text](url)`
- Footnotes: usually inlined
- Images: alt-text only by default; OCR available with `--use-llm` flag if LLM is configured
- Math equations: extracted as LaTeX source when present in source document
- Track-changes (Word): final-text only
- Hyperlinks in tables: preserved

## Performance notes

- Pure-Python PDFs: ~1-3 sec per page
- Scanned PDFs (image-only): markitdown falls back to OCR if available; slow (~10-30 sec/page)
- Large XLSX (>10K rows): ~5-15 sec; consider extracting specific sheets first
- DOCX with embedded media: media extracted as separate files unless `--no-extract-media` set

## Failure modes + diagnostics

| Symptom | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: _cffi_backend` | cffi/pycparser mismatch | `pip install cffi --upgrade --force-reinstall` |
| `Couldn't find ffmpeg` (audio files) | ffmpeg not installed | `apt-get install ffmpeg` |
| Empty output on PDF | Scanned (image-only) PDF without OCR | Install OCR: `pip install 'markitdown-ocr'` or use Read tool on PDF directly (Read supports OCR for images) |
| Garbled Vietnamese characters | Source encoding issue | Use `--charset utf-8` or open in pandoc fallback |
| Tables broken | Complex merged cells | Read directly with pandas + describe; markitdown is best-effort for tables |

## Security note (from upstream)

> MarkItDown performs I/O with the privileges of the current process. Like `open()` or `requests.get()`, it accesses any resource the process can access. In untrusted environments, sanitize inputs and use the narrowest `convert_*` function for your use case.

For this project: all inputs are author-controlled dissertation files, so the
security concern is low. Do NOT pipe arbitrary user-uploaded files to markitdown
without inspecting them first.

## Comparison with other project tools

| Tool | Best for | Limitation |
|---|---|---|
| **markitdown** (this skill) | PDF/DOCX/XLSX → MD for LLM analysis | Output is approximation; not high-fidelity for human reading |
| `pandoc` | MD → DOCX/PDF/TEX for *output* | Different direction (MD → other) |
| Read tool (PDF support) | Quick visual inspection, small PDFs (<20 pages) | Loses table structure; image content needs vision LLM |
| M-AIDA `MAIDA_intake.html` | In-browser effect-size extraction from IB papers | Domain-specific (P6 only) |

## Citation (if methodology is referenced)

> Microsoft Corporation. (2024). *MarkItDown: A Python utility for converting
> files to Markdown for LLMs* (v0.1.6) [Computer software]. GitHub.
> https://github.com/microsoft/markitdown
