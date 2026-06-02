---
name: wos-review-matrix
description: Convert Web of Science BibTeX exports into thematic literature review matrices (Markdown + CSV) and Word DOCX literature reviews with GB/T 7714-2015 references. Use when the user asks to convert WoS exports, create a literature review matrix, annotated review table, Markdown matrix, CSV export, Word literature review, docx 文献综述, or research synthesis table from Web of Science metadata.
---

# WoS Review Matrix

Use this skill to turn a Web of Science BibTeX export into a thematic literature review package. The default output is a readable Markdown matrix, a UTF-8 CSV matrix, and a Word `.docx` literature review with GB/T 7714-2015 references.

## Required Reference

Before extracting fields or writing outputs, read these references:

- `references/review-matrix-schema.md` for matrix columns, evidence priority, uncertainty labels, and Markdown/CSV output rules.
- `references/literature-review-docx.md` for the DOCX literature review structure and synthesis writing rules.
- `references/gbt7714-2015.md` for reference list formatting and sorting rules.

## Workflow

### Phase 1: Read and Parse Input

1. Locate the input file.
   - The user provides a path to a WoS-exported BibTeX `.bib` file.
   - If no path is given, search the current working directory for `.bib` files and ask the user which one to use.

2. Count total entries.
   - Read the entire BibTeX file.
   - Count the number of `@` entries (e.g., `@article`, `@inproceedings`, `@book`, etc.).
   - Report the count to the user: "找到 N 篇文献，开始处理..."

3. Deduplicate entries.
   - Deduplicate by DOI first. If two entries share the same DOI, keep the one with more complete metadata.
   - Deduplicate by title (case-insensitive, normalised whitespace) when DOI is absent.
   - Report the final deduplicated count: "去重后共 N 篇文献"

### Phase 2: Extract Matrix Fields (Batch Processing)

**IMPORTANT: Process ALL entries. Do not stop early or skip entries.**

4. For each deduplicated entry, extract the 13 matrix columns defined in the schema reference.
   - Use the BibTeX `abstract` field as the primary evidence source.
   - Use `keywords` as a secondary source for theoretical concepts and themes.
   - Use other BibTeX fields (title, author, year, journal, pages) for metadata columns.
   - Apply evidence discipline: use `未提及`, `待补充`, `推断:` labels per the schema rules.

5. Batch processing for large files.
   - If the file contains more than 20 entries, process in batches of 15-20 entries.
   - After each batch, report progress: "已处理 M/N 篇 (batch X/Y)"
   - Continue until all entries are processed.
   - After the final batch, report: "全部 N/N 篇处理完成"

6. If the user provides a separate notes file.
   - Read the notes file and match entries by DOI or title.
   - Merge user notes into the `我的笔记/批注` column.
   - If no notes file is provided, fill this column with `暂无笔记`.

### Phase 3: Generate Matrix Outputs

7. Generate Markdown matrix.
   - For fewer than 15 entries: produce a single Markdown table with all 13 columns.
   - For 15 or more entries: produce a compact summary table plus per-entry detail sections.
   - Display the Markdown matrix in the conversation.

8. Generate CSV file.
   - Save a UTF-8 CSV file to the current working directory.
   - Use the filename: `wos-review-matrix-<topic>.csv` (infer topic from keywords or user input).
   - Include one row per deduplicated entry with all 13 columns.
   - Use semicolons instead of line breaks inside cells.

### Phase 4: Write Literature Review DOCX

9. Write the DOCX literature review.
   - Use the completed matrix as the factual substrate.
   - Organize the review by arguments, themes, mechanisms, methods, debates, and research gaps, not by entry order.
   - Follow the DOCX structure and writing rules from the reference.
   - Detect review language from the user's instructions (Chinese or English).

10. Generate references.
    - Format all entries as GB/T 7714-2015.
    - Chinese references before English references.
    - Sort by first author surname within each language group.

11. Save the DOCX file.
    - Save to the current working directory.
    - Use the filename: `wos-literature-review-<topic>.docx`

## Output Guidance

Name generated files clearly, for example:

```text
wos-review-matrix-system-justification.csv
wos-review-matrix-system-justification.md
wos-literature-review-system-justification.docx
```

## Supported Input Formats

| Format | Support | Notes |
|---|---|---|
| BibTeX (.bib) | Full support | Recommended. Contains abstract, keywords, DOI. |
| RIS (.ris) | Supported | Field mapping may lose some detail. |
| EndNote XML (.xml) | Supported | Requires field mapping. |

If the user provides a non-BibTeX format, map fields to the BibTeX equivalents before processing.

## Evidence Discipline

Treat the BibTeX abstract and keywords as primary evidence, not decoration. Preserve the user's own synthesis points when they are present in a notes file.

If a field is absent from the available material, write `未提及`. If the field is important but needs additional manual reading, write `待补充`. If you infer a relationship from keywords or abstract context, prefix it with `推断:`.

When using direct excerpts from abstracts, keep them short and tied to the BibTeX entry that supports them.

Do not let the DOCX literature review exceed the evidence. If the abstracts are thin, write a more cautious review and make the weak evidence points explicit.

## Progress and Verification

At the end of processing, report a summary:

```
--- 处理完成 ---
总条目数: N
去重后: M (删除 K 个重复)
矩阵行数: M
CSV: wos-review-matrix-<topic>.csv
DOCX: wos-literature-review-<topic>.docx
```

The user can verify that the entry count matches their WoS export. If any entries were skipped or produced errors, list them explicitly.
