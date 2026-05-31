# markitdown skill

Claude skill wrapper for Microsoft's `markitdown` Python library — converts PDF/DOCX/XLSX/PPTX/HTML/image/audio files to Markdown.

## Installation status

- **Upstream package:** installed via `pip install 'markitdown[all]'` (v0.1.6)
- **CLI:** `markitdown <file>` available system-wide
- **Python API:** `from markitdown import MarkItDown`
- **Skill wrapper:** `.claude/skills/markitdown/SKILL.md` (this folder)

## Reinstallation (if needed)

```bash
pip install 'markitdown[all]' --upgrade
pip install cffi --upgrade --force-reinstall   # if _cffi_backend error
```

## Optional: ffmpeg for audio transcription

```bash
apt-get install -y ffmpeg
```

## Why a wrapper skill?

The Python package is a *tool*; this skill tells Claude *when* and *how* to invoke it in the context of the dissertation portfolio (P3–P8 papers, CD1/CD2, 5 thesis chapters, OSF bundles, WBES codebooks, supervisor feedback DOCX, etc.).

## License

MIT (matches upstream Microsoft markitdown).
