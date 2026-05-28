---
name: deep-author-voice-transformation
description: Workflow command scaffold for deep-author-voice-transformation in MY_THESIS_PHD_CANDIDATE_26.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /deep-author-voice-transformation

Use this workflow when working on **deep-author-voice-transformation** in `MY_THESIS_PHD_CANDIDATE_26`.

## Goal

Transforms manuscript prose (EN/VI) to match the candidate's academic author voice, often using an AI-to-author-voice skill, with normalization of variable notation and Scopus/WoS symbols.

## Common Files

- `dist/manuscripts/en/source_md/*_en_clean.md`
- `dist/manuscripts/vi/source_md/*_vi.md`
- `manuscripts/*_en_clean.md`
- `manuscripts/*_vi_clean.md`
- `p*/p*_en_clean.md`
- `p*/submission/p*_vi.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Apply author-voice transformation skill to relevant manuscript files (EN and/or VI).
- Normalize variable notation and Scopus/WoS symbols as needed.
- Update both source manuscripts and distribution copies.
- Regenerate deliverables (docx/pdf) if required.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.