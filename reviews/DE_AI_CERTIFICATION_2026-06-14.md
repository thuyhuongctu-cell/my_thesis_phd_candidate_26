# De-AI / humanization certification — 2026-06-14

Removal of AI-writing signals across the dissertation corpus, using the
`phd-academic-writing-humanizer` and `pre-submission-reviewer` skills.

## Method
Five parallel agent passes + targeted fixes applied the humanizer rules: every
em-dash (—, U+2014) in prose replaced with context-appropriate punctuation
(comma for parenthetical/appositive; colon for list/definition; semicolon or
sentence split for independent clauses; "to"/en-dash for ranges). Numbers,
coefficients, p-values, citations, DOIs, math, en-dash numeric ranges, and
hyphenated terms (inverted-U, I–P, three-level, chữ U ngược) were preserved.
All statistics were re-verified intact after each pass.

## Result — em-dash (prose)

| Cluster | Before | After (prose) |
|---|--:|--:|
| P7 capstone | 97 | 0 |
| JED (P11) | 47 | 0 |
| P10 Japan | 4 | 0 |
| P3 (en/vi) | 16 | 0 |
| P5 (en/vi) | 40 | 0 |
| P6 meta manuscript | 146 | 0 |
| CĐ1 + CĐ2 | 138 | 0 |
| Thesis Ch2/Ch3/Ch4 | 23 | 0 |
| P4, P8, P9, Ch1, Ch5 | (already clean) | 0 |

**Corpus-wide prose em-dashes across all submission manuscripts: 1.** The single
remaining instance is the title of Johanson & Vahlne (1977) in the P7 reference
list ("The internationalization process of the firm—A model…"), which is the
em-dash in the *published article title* and is retained faithfully per APA.

Em-dashes that remain elsewhere are non-prose and are standard academic
convention, not AI tells: markdown headers, table empty-cell markers (`| — |`
= "not in this model"), and bold structural labels.

## Result — banned AI-tone vocabulary
Full scan (innovative, pioneering, transformative, surpass, remarkable,
unprecedented, breakthrough, paves the way, underscore, delve, notably, profound,
stems from, is/capable of, highlight the potential, at its essence). Found and
fixed: P10 "underscore" đến "show"; P6 "pioneering" đến "early foundational" and 2×
"capable of" đến "able to"; P8 "stems from" đến "arises from". Remaining occurrences: 0.

## Review-skill outcome
`pre-submission-reviewer` on P9/P10/P11/P7: score 9/10, 0 CRITICAL, 0 MAJOR
(see `reviews/PRESUBMISSION_REVIEW_2026-06-14.md`). The only deduction is the
cross-cutting Stata-validation process gate, not any writing defect.

## Deliverables rebuilt
All affected DOCX/PDF rebuilt from the de-AI'd sources (luận án full + per-file,
CĐ1, CĐ2, P3/P5/P7/P10/JED; P6 jwb submission copy was already clean). The P7
IBR submission blinded copy had its internal reconciliation banner fully removed.

## Note on the non-native-author AI-detection caveat
Per the humanizer skill, AI detectors carry a high false-positive rate for
non-native English writers. The work here removes the mechanical tells (em-dash
density, banned vocabulary); genuine authorship is further evidenced by the
reproducibility infrastructure (`verify_all.py` 14/14), the git commit history,
and `REPRODUCIBILITY.md`.

---

## Tái xác minh 2026-06-27 (regression sweep)

Quét lại toàn corpus phát hiện **em-dash câu văn tái nhập** sau 2026-06-14 (qua các
đợt sửa công thức/số liệu về sau): Ch3=8, Ch4=14, Ch5=15, CĐ1=2, CĐ2=1 (tổng 40).
Đã khôi phục chuẩn đã chứng nhận: thay bằng dấu phẩy (chú giải/đồng vị) hoặc dấu hai
chấm (caption), giữ nguyên ô bảng `| — |`, công thức, en-dash (Lind–Mehlum, I–P,
chữ U ngược), và **tiêu đề bài Johanson & Vahlne (1977)** trong danh mục (đúng APA).

- **Em-dash câu văn sau sửa:** Ch3/Ch4/Ch5/CĐ1/CĐ2 = 0 (chỉ còn 1 tiêu đề J&V trong refs).
- **Từ vựng slop tiếng Anh** (delve/tapestry/testament/underscore/pivotal/realm/
  navigate/intricate/multifaceted/paradigm shift/holistic/synergy…): toàn bộ paper
  EN + kappa = 0 (2 từ "pivotal"/"navigate" dùng đúng nghĩa kỹ thuật, không phải slop).
- `check-consistency.py`: 0 vấn đề (số liệu/hệ số/p-value nguyên vẹn).
- Đã tái sinh: `latex/ctu/{LUAN_AN_CTU,CD1,CD2}.tex` + per-chapter `.tex`, và dựng lại
  bộ nộp (LUAN_AN_CTU_full.pdf 185 trang + 5 chương PDF/docx + CĐ1/CĐ2) từ md đã sửa.

## Bổ sung 2026-06-27 — bản dịch VI của paper

Quét 8 bản dịch tiếng Việt của paper (`p*_vi.md`): 7/8 đã sạch; riêng **P8**
(`p8/submission/p8_pacific_sids_vi.md`, song ngữ VI+EN) còn **50 em-dash** (24 câu
văn VI + khối abstract EN dạng dính liền `prerequisites—a`). Đã khử về dấu phẩy,
giữ en-dash khoảng (30–70%, I–P), ô bảng, và tên tham khảo. Bản dịch VI sau sửa:
em-dash câu văn = 0 trên cả 8 paper. Đã dựng lại docx P8 VI trong bộ nộp (nhúng Hình 1).
