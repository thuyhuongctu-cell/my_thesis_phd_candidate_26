# WoS Review Matrix Skill

A Claude Code skill for turning Web of Science BibTeX exports into:

- a thematic Markdown literature review matrix
- a UTF-8 CSV review matrix
- a Word `.docx` literature review with GB/T 7714-2015 references

Adapted from [zotero-review-matrix-skill](https://github.com/kasabulanka2019/zotero-review-matrix-skill), originally built for Zotero/Codex workflows.

## Features

- Reads WoS-exported BibTeX `.bib` files (also supports RIS and EndNote XML)
- Deduplicates entries by DOI and title
- Batch processing with progress reporting for large exports
- Extracts 13-column thematic review matrix from abstracts and keywords
- Generates Markdown and CSV matrices
- Writes structured DOCX literature review with GB/T 7714-2015 references
- Chinese references before English, sorted by first author surname

## Requirements

- Claude Code with custom skills support

## Install

```bash
git clone https://github.com/qijialiao/wos-review-matrix-skill.git
cp -R wos-review-matrix-skill ~/.claude/skills/wos-review-matrix
```

Then register in `~/.claude/skills/marketplace.json`:

```json
{
  "name": "wos-review-matrix",
  "description": "Literature review matrix and DOCX synthesis from Web of Science metadata exports",
  "source": {
    "source": "directory",
    "path": "./wos-review-matrix"
  }
}
```

Restart Claude Code or open a new conversation to refresh the skill list.

## Usage

In Claude Code:

```
Use $wos-review-matrix to convert my WoS BibTeX export into a review matrix
```

In Chinese:

```
用 wos-review-matrix 把我的 WoS BibTeX 文件整理成文献综述矩阵和 docx
```

## Output

- `wos-review-matrix-<topic>.md` — Markdown matrix
- `wos-review-matrix-<topic>.csv` — CSV matrix (UTF-8)
- `wos-literature-review-<topic>.docx` — DOCX literature review

## Credits

Based on [kasabulanka2019/zotero-review-matrix-skill](https://github.com/kasabulanka2019/zotero-review-matrix-skill). Rewritten for Claude Code and Web of Science metadata.
