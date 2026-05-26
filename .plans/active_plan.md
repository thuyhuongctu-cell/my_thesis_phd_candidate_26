# Active Plan — Remove unpublished P3–P8 self-citations & labels; full integration

USER DECISION: (1) Full integration — remove BOTH the "P3/P4/.../P8" labels AND the
"(Đỗ & Phan, 2026x)" self-citations; present everything as the dissertation's OWN seamless
analysis by economy/topic. (2) Scope: dissertation chapters + CĐ1 + CĐ2.

WHY: P3–P8 are unpublished (under review/revision) — cannot be cited as published sources.

## CRITICAL: what to KEEP vs REMOVE
KEEP (published — do NOT touch these citations):
- **P1** = Đỗ & Phan (2026a) — Vietnam Economic & Financial Review (đã công bố)
- **P2** = Đỗ & Phan (2026g) — Journal of Finance & Accounting Research (đã công bố)

REMOVE / INTEGRATE (unpublished P3–P8):
- (Đỗ & Phan, 2026b) = P8 SIDS; (2026c) = P6 meta; (2026d) = P7 capstone; (2026e) = P3 Vietnam;
  (2026f) = P5 China; Mar et al. (2026) / Mar, K.S. / Mar, T.T. = P4 Singapore.
- All "under review / under revision / under review tại …" + journal names used as the paper's
  target: JABS, APJM, MIR, IJOEM, JIBS, IBR, World Development (only when tagging P3–P8 as the
  candidate's own submission — NOT when citing those journals for OTHER authors' published work).
- All bare "P3 / P4 / P5 / P6 / P7 / P8" prose labels.

## Label → integrated phrase (Vietnamese) — apply consistently
- P3 → "phân tích Việt Nam (của luận án)" / "nghiên cứu Việt Nam" (single-country WBES VN 2009/2015/2023)
- P4 → "phân tích Singapore (của luận án)" / "nghiên cứu Singapore"
- P5 → "phân tích Trung Quốc (của luận án)" / "nghiên cứu Trung Quốc"
- P6 → "phân tích tổng hợp (meta-analysis) của luận án" / "phần tổng hợp định lượng"
- P7 → "phân tích đa quốc gia (45 nền kinh tế) của luận án" / "mẫu gộp châu Á–Thái Bình Dương"
- P8 → "phân tích các quốc đảo nhỏ Thái Bình Dương (SIDS) của luận án"
- "(Đỗ & Phan, 2026d)" etc. as an in-text evidence cite → DELETE the parenthetical; render the
  sentence as the dissertation's own finding ("phân tích … của luận án cho thấy …",
  "kết quả của luận án …"). Do NOT invent a new citation.
- Section headings like "Kết quả P3 (Việt Nam)" → "Kết quả phân tích Việt Nam".

## HARD CONSTRAINTS
- Preserve ALL numbers, statistics, findings, turning points, betas, p-values, tables EXACTLY.
- Preserve the G2/concavity/H4-control framing already in place. Change ONLY label/citation wording.
- Keep citations to OTHER authors' published work untouched (North, Hambrick, Lu & Beamish, Marano
  et al. 2016, Verhoef, World Bank, ADB, IMF, etc.).
- Keep P1 (2026a) and P2 (2026g) self-citations (published).
- Vietnamese PhD academic register; keep sentences fluent after removal (don't leave dangling
  "()" or "," — re-read each edited sentence).
- Do NOT renumber the H1–H6 hypotheses or touch the Upper-Echelons-control / concavity content.

## File groups (parallel agents; no overlap)
- A: thesis/chuong_4_ket_qua_vi.md, thesis/chuong_5_ket_luan_de_xuat_vi.md
- B: thesis/04_05_chapters_results_discussion_vi.md, thesis/11_dissertation_positioning_vi.md,
     thesis/02_theoretical_framework_vi.md
- C: thesis/chuong_1_gioi_thieu_vi.md, thesis/chuong_2_tong_quan_tai_lieu_vi.md,
     thesis/chuong_3_phuong_phap_vi.md, thesis/03_methodology_vi.md, thesis/tom_tat_front_matter_vi.md
- D: thesis/tom_tat_noi_dung_vi.md, thesis/14_cd1_part1_intro_theory_vi.md,
     thesis/15_cd1_part2_findings_vi.md, thesis/16_cd1_part3_cases_conclusion_vi.md
- E: chuyen_de/cd2/00_cd2_ctu_final_vi.md
- (Reference list thesis/04_references_apa7.md + danh mục công trình: handled by orchestrator.)

## Verification (per file, after edit)
grep must return ZERO for: `\bP[3-8]\b`, "Đỗ & Phan, 2026[b-f]", "Mar et al", "under review",
"under revision", and the journal-as-own-target tags. Numbers/findings unchanged (spot-check N's,
TPs). No dangling punctuation.
