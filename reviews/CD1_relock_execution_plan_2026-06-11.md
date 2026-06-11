# KẾ HOẠCH THỰC HIỆN — Re-lock mô tả CĐ1 bằng pipeline tái lập

**Ngày:** 2026-06-11 · **Mục tiêu:** thay toàn bộ số liệu mô tả CĐ1 (bản khóa cũ 47 nền/101.185 DN, membership cũ) bằng số **tái lập được** từ `scripts/cd1_relock_descriptives.py` theo nhãn dữ liệu (49 nền/96.415 phân loại), đã validated phương pháp.

**Nguyên tắc xuyên suốt:** mỗi số thay vào CĐ1 PHẢI đến từ output pipeline (cùng một pipeline cho mọi bảng) — không trộn nguồn, không bịa. Chỉ thay **số mô tả định lượng**; phần lý luận/khung/case-study định tính giữ nguyên.

---

## PHASE 0 — Quyết định & chuẩn bị (cần NCS)

| # | Quyết định | Khuyến nghị |
|---|---|---|
| **D1** | Re-lock TOÀN BỘ CĐ1 về 49/96.415 (thay mọi bảng) **hay** giữ bản khóa CĐ1 + ghi chú dual-lock (đã có dòng 41, 228)? | NCS trước đã chọn **re-lock toàn bộ** → kế hoạch này theo đó. CĐ1 là chuyên đề độc lập; re-lock là thay đổi lớn — xác nhận trước khi chạy. |
| **D2** | Cách nạp 44 raw `.dta` | Push vào `data_wbes/raw_dta/` (git) — vĩnh viễn, full compute, tái lập. |
| **D3** | Nền tham chiếu để validate per-economy | Việt Nam (CĐ1 có n, sd, FSTS), Singapore, Trung Quốc. |

---

## PHASE 1 — Nạp dữ liệu (prerequisite cứng)
1. NCS push 44 raw `.dta` → `data_wbes/raw_dta/` (danh sách trong `CD1_relock_status_2026-06-11.md`).
2. Tôi verify: đọc được, đếm nền/sóng, phát hiện schema lạ (ISBS/Micro/panel-zip cần giải nén).
3. Mở rộng pipeline nếu có schema chưa phủ (panel `.zip` → giải nén; ISBS/Micro → map biến riêng hoặc loại có ghi chú).

## PHASE 2 — Cổng hiệu chỉnh (CALIBRATION GATE)
1. Chạy pipeline trên nền tham chiếu (D3) → đối chiếu sd/FSTS/% với số CĐ1 đã công bố.
2. **Gate:** sd + tỷ lệ chính khớp CĐ1 trong dung sai (±0,05 sd; ±2đpt tỷ lệ) → PASS, đi tiếp. Nếu lệch → soát lại trích biến/winsorize/yes-rate, KHÔNG chạy tiếp tới khi khớp.
   *(Đã validated sơ bộ: Advanced sd 1,123 vs ~1,03; Emerging 1,387 vs ~1,36.)*

## PHASE 3 — Chạy toàn bộ → bảng tái lập
1. `python3 scripts/cd1_relock_descriptives.py` → output per-group + bổ sung per-economy.
2. Sinh đúng cấu trúc các bảng CĐ1 (script tạo CSV; tôi format sang Markdown).

## PHASE 4 — Re-lock manuscript CĐ1 (ánh xạ bảng → output)

| Phần CĐ1 | Hiện (bản khóa cũ) | Thay bằng (nhãn dữ liệu) |
|---|---|---|
| Abstract (d39,54), §2.1 (d199,205,274), §2.3.3 (d453) | 47 nền · 101.185 · 108 cặp | **49 nền · 96.415 phân loại** (mô tả) · 102 cặp |
| **Bảng 2.3.2.1** (d418) danh sách 6 nhóm + n | IV Emerging 47.803 / V Frontier 28.678 / III 16.693 / Adv 6.640 / SIDS 1.371 | **IV Lower_mid 50.926 / V Emerging 18.569 / III 17.905 / I 4.708 / II 2.269 / VI 2.038**; membership: BGD/PAK→IV, LKA/JOR→V |
| **Bảng 2.3.3.1** sd LP (d463) | n=108 cặp; sd theo nhóm cũ | sd_log_lp (within-cluster) từ pipeline theo 6 nhóm |
| **Bảng 2.3.3.2** FSTS/xuất khẩu/CAGR (d483) | số cũ | FSTS%, exporter% từ pipeline |
| **Bảng 2.3.4.1** đổi mới & số (d515) | R&D/ISO/đổi mới/website cũ | rd/iso/prod/proc/website % từ pipeline |
| **Bảng 2.3.5.1** cấu trúc DN (d539) | số cũ | size/FDI từ pipeline |
| **Bảng 2.3.6.4** sub-nhóm Emerging (d621) n=47.803 | nhóm 7 nước cũ | tái cấu trúc theo Nhóm IV mới (Lower_mid) hoặc giữ + đổi nhãn |
| **Bảng 2.3.7.1** 7 tiểu cảnh (d716,720) | VN 3.077 / CN 4.889 / India 42.278 | **VN 2.958 / CN 4.559** (số bài gốc) / India (số P9) |
| §2.3.7.3/4/5 tiêu đề | n=3.077 / 4.889 / 42.278 | số đã sửa |
| **Bảng 2.3.8.1** Pearson (d735) | n=101.185 | n mới + hệ số tái tính (nếu chạy được) |
| **Phụ lục A.1** (d1035) | bảng phạm vi cũ | bảng phạm vi 49 nền |
| Ghi chú dual-lock (d41,228) | "giữ bản khóa cũ… chờ re-lock 43 .dta" | cập nhật: **đã re-lock**; crosswalk membership giữ để minh bạch lịch sử |
| Hình 2.3.3.1/2/3, 2.3.5.1 caption (d122-126,455,457) | 101.185 | 96.415 (hoặc số phân loại mới) |

## PHASE 5 — Coupling & nhất quán
1. Thesis **Ch4 Bảng 4.2**: gỡ caveat "bản khóa CĐ1" → dùng số tái lập (giờ cùng nguồn).
2. CĐ2: đã ở 49-frame — verify khớp.
3. Chạy `scripts/check-consistency.py` → 0 issue.
4. Cập nhật `MASTER_CONSISTENCY_RECONCILIATION` + `RELOCK_EXECUTION_PLAN` (đánh dấu CĐ1 done).

## PHASE 6 — Đầu ra
1. Regenerate CĐ1 docx (pandoc `-f markdown-yaml_metadata_block`) + sync dist.
2. Commit theo từng phase; push.

---

## Rủi ro & giảm thiểu
- **Schema lạ (ISBS/Micro/panel-zip)** → một số nền có thể thiếu biến đổi mới → ghi chú "n/a", không bịa; nêu rõ độ phủ.
- **Hệ số Pearson (Bảng 2.3.8.1)** cần ma trận tương quan đầy đủ — nếu pipeline chưa xuất, để PENDING, không thay số cũ bằng số sai.
- **India 16MB** và nền lớn: nếu chỉ push được 1 phần → re-lock PARTIAL, ghi rõ nền nào đã/chưa, KHÔNG suy số.
- **Thay đổi lớn ở chuyên đề đã nộp** → mỗi bảng thay đều ghi nguồn pipeline + giữ crosswalk minh bạch.

## Ước lượng
- Phase 1–2: ~1 phiên sau khi có data (verify + calibration gate).
- Phase 3–4: ~1–2 phiên (chạy + thay ~12 bảng + reconcile prose).
- Phase 5–6: ~0,5 phiên.

## Trạng thái sẵn sàng
✅ Pipeline xây xong + validated phương pháp. ✅ Inventory bảng/số xong. ⏳ Chờ **D1 (xác nhận scope)** + **data (Phase 1)**.
