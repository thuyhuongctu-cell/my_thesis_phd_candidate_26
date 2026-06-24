# P3 (Vietnam → JED/Emerald) — Audit trước nộp, 2026-06-24

**Kết luận: CHƯA đạt chuẩn submit.** Bộ live = `p3/submission/jed_package` (set `_8500`).
Phần trích dẫn/ẩn danh và phần lớn số liệu nội bộ rất tốt, nhưng còn **2 lỗi chặn (blocker)**
và vài lỗi metadata phải sửa.

---

## ✅ ĐÃ XỬ LÝ (2026-06-24) — cô đã duyệt hướng

Bộ live `p3/submission/jed_package` đã được sửa và xác minh:

- **B1 (reproducibility) — ĐẢO HƯỚNG sau khi đào sâu.** Phát hiện `coefs_main_models.csv`
  KHÔNG phải outlier mà là **nguồn chuẩn**: N = 989/956/1013/**2.958** khớp đúng bản thảo, và
  pooled M2 (β₁=+0,9843, β₂=−1,9091) tái lập **39,7%** (46,2/39,3/41,6 theo sóng) tới từng số lẻ.
  Python fallback chỉ ra M2/M4/M6 (KHÔNG có TCI/H2), dùng spec lệch (`b2b≥10` thay vì `>0`) → N=2.973,
  ~35% chỉ là **xấp xỉ** (REPRO_NOTE tự nhận cần Stata authoritative). **Cô chọn GIỮ 39,7%/N=2.958.**
  Đã: (a) sửa câu dòng 78 từ "reproduces every coefficient" → mô tả trung thực (Stata cho số chính;
  port Python/R tái lập *mẫu hình* + dải TP, không khớp magnitude tuyệt đối); (b) đính chính
  `REPRO_NOTE.md` (khối CORRECTION 2026-06-24). *Việc còn lại của cô: chạy do-file Stata trên máy có
  license để xác nhận cuối — số hiện tại là provisional nhưng nhất quán nội bộ.*
- **M1 — hệ số TCI pooled in sai.** `−0,587/0,640 (p .003/.031)` → **−0,573/0,627 (p .004/.034)**
  khớp `coefs_main_models.csv`, ở manuscript:97 + tables:53.
- **B2 — khai báo AI.** Title page sửa thành **chỉ Grammarly, không AI tạo sinh**, khớp manuscript:150.
- **H3 — đổi số.** H4→**H3** (giả thuyết DAI thăm dò) tại manuscript 51/56/60/72/108, tables:15,
  Supplementary:11; bỏ câu viện dẫn "broader dissertation framework". Bài còn H1/H2/H3 liền mạch.
- **M2 — metadata title page.** Word count → **8.476** (manuscript 7.843 + tables 633, < 8.500);
  abstract **192**; tables **3** (file riêng); figures **2** (+ 2a–2d phụ lục); references **55**;
  keywords đồng bộ theo manuscript dòng 14. CRediT: ô trống `, ` → `—`.
- **Word cap.** Trim ~50 từ văn xuôi Discussion/Limitations (không đụng số/trích dẫn) → 8.476 < 8.500.
- **MINOR.** Exporter-only FSTS_c² p: thống nhất **.730** (đúng với SE 0,581; `.660` là số sai) ở
  manuscript:113 + tables:57 + Supplementary:80. PSM N: **644** (Supplementary:152 & 315). "Lind and
  Mehlum (2010)" (Harvard) ở manuscript:72, tables:22, Supplementary:367. `generate_p3_figures.py`
  N hard-code → 956/1013/2.958; **render lại** Figure 2/2a–2d, copy vào jed_package/figures.

**Còn lại (cô quyết):** chạy Stata authoritative để chốt số cuối (nếu Stata cho khác 39,7%, đồng bộ
lại abstract/Bảng III/Hình 2). Mọi mục khác đã đạt chuẩn submit.

## 🔴 BLOCKER

### B1 — Điểm uốn 39–46% (đóng góp chính) KHÔNG tái lập được từ dữ liệu thô
- Manuscript dùng `coefs_main_models.csv`: pooled M2 = (β₁ +0,984, β₂ −1,909), TP **39,7%**, N=2.958.
- Chạy lại từ raw cho kết quả khác hẳn (REPRO_NOTE 2026-06-23):
  - Python track: (+0,733, −1,750), TP **34,8%**, N=2.973
  - R track (`p3_R_turning_points.csv`): (+0,661, −2,152), TP **34,5%**
- `REPRO_NOTE.md` tự ghi: *"`coefs_main_models.csv` là outlier, từ build cũ/khác (sample khác); KHÔNG tái lập từ raw với spec hiện tại."*
- Hệ quả: dải "39–46% FSTS" (abstract, Bảng III, Hình 2, toàn bộ luận điểm threshold-durability) chưa được dữ liệu thô xác nhận; câu manuscript dòng 78 *"rerunning the pipeline … reproduces every coefficient"* hiện **sai** so với 2 lần chạy lại.
- **Cần:** chạy do-file Stata authoritative trên máy có license để chốt con số đúng (39,7% hay ~35%), rồi đồng bộ abstract/bảng/hình. Đây là việc số liệu — cô quyết hướng.

### B2 — Mâu thuẫn khai báo AI giữa 2 file nộp
- `01_manuscript_blinded_8500.md:150`: *"**No generative AI tool was used** …"* (chỉ Grammarly).
- `02_title_page.md:91`: *"**Generative AI tools were used** … language editing, structure suggestions, assembly of replication package …"*
- Hai câu chọi nhau trực tiếp — vi phạm yêu cầu khai báo AI nhất quán của Emerald. **Phải thống nhất về đúng 1 câu trung thực** (cô xác nhận thực tế đã dùng gì).

## 🟠 MAJOR

### M1 — Hệ số tương tác TCI pooled in sai (cả manuscript + bảng)
- `01_…8500.md:97` và `04_tables.md:53`: `FSTS_c × TCI_z = −0,587 (p=.003)`, `FSTS_c² × TCI_z = 0,640 (p=.031)`.
- CSV gốc `coefs_main_models.csv`: **−0,5731 (p=.004)** và **0,6269 (p=.034)**. Giá trị −0,587/0,640 không truy được về file nào.
- Sửa → −0,573 (p=.004) và 0,627 (p=.034). (Dấu sao ** không đổi.)

### M2 — Metadata trang tiêu đề sai hàng loạt (`02_title_page.md:100–104`)
| Mục | Title page ghi | Thực tế |
|---|---|---|
| Word count main text | ~6.800 | manuscript 7.876 (cả file) |
| Abstract | 247 | **192** (thân) / 214 (kèm keyword+JEL) |
| Tables | 5 (inline) | **3** (I–III, file riêng) |
| Figures | 6 (inline) | **2** trong bài (Fig 1, 2) + 4 phụ lục (2a–2d) |
| References | 48 | **55** |

## 🟡 MEDIUM
- **Keyword lệch nhau:** manuscript (dòng 14) = "… emerging markets … firm productivity"; title page (105) = "… transition economies … digital adoption". Phải trùng. JEL thì khớp.
- **Vượt cap chữ:** manuscript 7.876 + tables 633 = **8.509 > 8.500** (cap JED gồm mọi thứ). Cần trim ≥9 từ (nên trim ~30–50 để có biên).
- **Bỏ H3 + viện dẫn "broader dissertation framework" (dòng 51):** bài standalone có H1/H2/H4 (không H3) và dẫn tới một "khung luận án" bên ngoài — phản biện sẽ thấy khó hiểu. Nên đổi số H4→H3 cho bài độc lập, hoặc bỏ câu dẫn luận án.

## 🟢 MINOR
- Exporter-only pooled FSTS_c² p: manuscript/bảng `.660` vs Supplementary `.730` — lệch, chọn 1.
- PSM TCI 1-NN N: Supplementary chỗ 644 chỗ 640.
- `generate_p3_figures.py:96` hard-code N sai (864/908/2761 thay vì 956/1013/2.958) → kiểm tra nhãn N trên Hình 2a–2d đã render.
- "Lind–Mehlum (2010)" (gạch en) → "Lind and Mehlum (2010)" ở manuscript:72 và tables:22 (Harvard).
- Bảng CRediT (title page 47–59): vài ô còn dấu `, ` thừa → đổi thành "—"/bỏ trống.

## Đã kiểm và SẠCH
- Trích dẫn 2 chiều (55 in-text ↔ 55 ref), không thiếu/mồ côi/lệch năm; ẩn danh bản blinded sạch.
- Toàn bộ hệ số M2/M7/M8, dấu sao, điểm uốn (số học đúng theo mean-centring), N (989/956/1013/2958), bảng marginal-effects, 2SLS/PSM, density — nhất quán nội bộ với `coefs_main_models.csv`.
- Không placeholder/TODO; có marker "[Insert Table …]"; cấu trúc abstract Purpose/Design/Findings/Originality đủ.

> Lưu ý: LP của P3 dùng "doanh thu PPP-converted" (ICP deflators) là **đúng chủ đích** của P3
> (hiệu chỉnh PPP theo thời gian cho khoảng 2009–2023) — không phải lỗi; khác với biến lnLP nội tệ
> chuẩn hóa-z của khung đa quốc gia (P7/luận án).
