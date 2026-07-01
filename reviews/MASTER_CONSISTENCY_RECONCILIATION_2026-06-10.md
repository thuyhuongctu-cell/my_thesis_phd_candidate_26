# BẢNG ĐỐI CHIẾU CHUẨN TOÀN DỰ ÁN — Luận án ↔ Chuyên đề ↔ Paper

**Ngày:** 2026-06-10 · **Mục đích:** thiết lập **một nguồn số liệu chuẩn DUY NHẤT** (từ dữ liệu thật) để mọi tài liệu (luận án 5 chương, CĐ1, CĐ2, P3–P9) **khớp nhau**. Mọi con số dưới đây tính trực tiếp từ `data_wbes/p7/p7_pooled_clean.csv` — **không bịa**.

> Nguyên tắc: dữ liệu là chuẩn (ground truth); tài liệu phải khớp dữ liệu (hoặc ghi rõ "bản khóa khác" nếu cố ý). Các quyết định **phân loại regime** và **chọn bản khóa dữ liệu** là của NCS — máy chỉ đối chiếu, không tự đổi membership/lock.

---

## A. NGUỒN CHUẨN — phân bổ ICRV từ dữ liệu thật (bản khóa hiện tại)

**52 nền kinh tế có nhãn · 96.415 doanh nghiệp** (đã loại 3 bản trùng `_panel`). Đây là "pool phân loại ICRV ≈ 96.415" mà luận án Ch4 nêu.

| icrv_label (dữ liệu) | # nước | # firms | Các nước |
|---|:--:|:--:|---|
| Advanced_innovation | 6 | 4.708 | Cyprus, HongKong, Israel, Korea, Singapore, Taiwan |
| Advanced_resource | 6 | 2.269 | Bahrain, Brunei, Kuwait, **Oman**, Qatar, SaudiArabia |
| Upper_mid | 7 | 17.905 | Armenia, China, Georgia, Kazakhstan, Malaysia, Thailand, **Turkey** |
| Lower_mid_transition | 7 | 50.926 | Bangladesh, India, Indonesia, Mongolia, Pakistan, Philippines, Vietnam |
| Emerging | 17 | 18.569 | Afghanistan, Azerbaijan, Bhutan, Cambodia, Iraq, Jordan, Kyrgyz, Laos, Lebanon, Maldives, Myanmar, Nepal, SriLanka, Tajikistan, Turkmenistan, Uzbekistan, Yemen |
| SIDS_small | 9 | 2.038 | Comoros, Fiji, Kiribati, PNG, Samoa, Solomon, **TimorLeste**, Tonga, Vanuatu |
| **TỔNG** | **52** | **96.415** | |

### Khung 49 nền kinh tế châu Á–TBD (luận án) = 52 − {Comoros, Turkey, Cyprus}
| icrv_label | # nước | # firms |
|---|:--:|:--:|
| Advanced_innovation | 5 (−Cyprus) | 4.222 |
| Advanced_resource | 6 | 2.269 |
| Upper_mid | 6 (−Turkey) | 13.993 |
| Lower_mid_transition | 7 | 50.926 |
| Emerging | 17 | 18.569 |
| SIDS_small | 8 (−Comoros) | 1.885 |
| **TỔNG** | **49** | **91.864** ≈ luận án "91.982" (lệch 0,1%) |

**7 Pacific SIDS (P8 mẫu chính)** = Fiji, Kiribati, PNG, Samoa, Solomon, Tonga, Vanuatu đến **1.371** firms (pool thô); N=959 (analytic sau lọc missing); N=209 (M1 complete-case).

---

## B. 🔴 LỆCH THÀNH VIÊN REGIME (CĐ phân loại lý thuyết ≠ nhãn dữ liệu) — NCS PHẢI QUYẾT

Đây là vấn đề **nghiêm trọng hơn bảng số**: một số nước được CĐ1/CĐ2 xếp nhóm **khác** với nhãn trong dữ liệu phân tích (P7). Hai bên phải khớp — hoặc sửa CĐ, hoặc sửa nhãn dữ liệu (NCS quyết).

| Nước | CĐ1/CĐ2 xếp | Nhãn dữ liệu | Hệ quả |
|---|---|---|---|
| **Sri Lanka** | Nhóm IV "Emerging" | `Emerging` (=nhóm 17, tương ứng "Frontier" của CĐ) | Lệch nhóm |
| **Jordan** | Nhóm IV "Emerging" | `Emerging` (nhóm 17) | Lệch nhóm |
| **Bangladesh** | Nhóm V "Frontier" | `Lower_mid_transition` (=nhóm 7, "Emerging" CĐ) | Lệch nhóm |
| **Pakistan** | Nhóm V "Frontier" | `Lower_mid_transition` (nhóm 7) | Lệch nhóm |
| **Timor-Leste** | Nhóm V "Frontier" | `SIDS_small` | Lệch nhóm |
| **Oman** | (không liệt kê) | `Advanced_resource` | CĐ thiếu Oman trong Nhóm II |
| **Cyprus** | (không liệt kê — ngoài Á) | `Advanced_innovation` | Ngoài khung 49; OK nếu loại |
| **Turkey** | (không liệt kê — ngoài Á) | `Upper_mid` | Ngoài khung 49; OK nếu loại |
| **Comoros** | (không liệt kê — ngoài Á) | `SIDS_small` | Ngoài khung 49; robustness P8 |

> ⚠️ **Tên hoán đổi:** CĐ gọi nhóm 7-nước-đông-dân là "Emerging (Nhóm IV)" và nhóm 17-nước là "Frontier (Nhóm V)". Dữ liệu gọi NGƯỢC LẠI: `Lower_mid_transition` = 7 nước, `Emerging` = 17 nước. **Cần 1 bảng crosswalk tên-CĐ ↔ icrv_label** dùng nhất quán; và thống nhất membership của Sri Lanka/Jordan/Bangladesh/Pakistan/Timor-Leste.

---

## C. MA TRẬN ĐỐI CHIẾU SỐ LIỆU XUYÊN TÀI LIỆU

| Đại lượng | Chuẩn (dữ liệu/paper) | Luận án 5 chương | CĐ1 | CĐ2 | Trạng thái |
|---|---|---|---|---|---|
| Số nền kinh tế (phân tích chính) | **49** (Á–TBD) | 49 Có | **47** (bản khóa cũ) | **47** (bản khóa cũ) | ⚠️ CĐ dùng lock 47/101.185; có ghi chú đối chiếu — chấp nhận nếu nêu rõ |
| Pool firms (phân loại) | **96.415** | "≈96.415" Có | **101.185** (lock cũ) | **101.185** (lock cũ) | ⚠️ khác lock |
| Mẫu hồi quy chính | **91.864** | "91.982" Có | — | (đặc tả, không chạy) | Có |
| Per-ICRV n_firms | (Bảng A trên) | (Ch4 regime %) | **Bảng 2.3.2.1 ≠ A.1** 🔴 | **Bảng 2.8** 🔴 | 🔴 **3 bảng mâu thuẫn** — đồng bộ về Bảng A |
| SIDS (pool) | **1.371** (7 Pacific) | 1.371 Có | 1.371 / ~~2.385~~ 🔴 | ~~5.185~~ 🔴 | 🔴 sửa A.1 + Bảng 2.8 |
| P3 Việt Nam N | **2.958** (bài P3) | — | **3.077** 🔴 | 2.958 Có | 🔴 CĐ1 lệch |
| P5 Trung Quốc N | **4.559** (bài P5) | — | **4.889** 🔴 | 4.559 Có | 🔴 CĐ1 lệch |
| P7 turning point | **36%** pooled | 36% Có | — | ~~28% toàn mẫu~~ đến đã sửa Có | Có (CĐ2 vừa sửa) |
| P8 kết quả chính | **7 Pacific, N=209, β=−1,339** | (Ch4 Mục 4.7) | 7 nước/1.371 Có | **9 nước/1.469/−0,404** (robustness) 🔴 | 🔴 CĐ2 trình bày robustness như chính |
| P6 | k=238, K=288, r=0,074 | — | — | k=238/K=288 Có | Có |
| P9 Ấn Độ TP | 61,8 đến 40,7 đến tan rã | (Ch4) | — | — | Có |

---

## D. KHUYẾN NGHỊ — chính sách chuẩn để mọi tài liệu khớp

### D1. Bản khóa dữ liệu (data lock) — NCS chọn 1 trong 2:
- **(a) Khuyến nghị:** tuyên bố rõ **2 bản khóa**: CĐ1/CĐ2 dùng lock 2025 (47 nước/101.185); luận án + paper dùng lock cập nhật (49 nước/96.415 phân loại / 91.864 phân tích). Đặt **một ghi chú đối chiếu chuẩn** (như CĐ1 dòng 41 đã có) vào **mọi** tài liệu. đến Ít sửa nhất, trung thực.
- **(b) Tốn công hơn:** re-lock toàn bộ CĐ1/CĐ2 về 49/96.415 để mọi nơi một con số.

### D2. Bảng phân bổ ICRV chuẩn DUY NHẤT
Dùng **Bảng A** ở trên làm chuẩn; thay mọi bảng per-ICRV trong CĐ1 (Bảng 2.3.2.1, Phụ lục A.1) và CĐ2 (Bảng 2.8) bằng cùng số (theo lock đã chọn ở D1). Bỏ các bảng nháp cũ.

### D3. Thống nhất membership regime (Mục B) — NCS quyết:
Sri Lanka, Jordan đến IV hay V? Bangladesh, Pakistan đến IV hay V? Timor-Leste đến V hay VI(SIDS)? Oman có trong II không? Sau khi quyết, **sửa cho khớp cả văn bản CĐ lẫn nhãn dữ liệu**, kèm 1 bảng crosswalk tên-CĐ ↔ icrv_label.

### D4. Sample size paper — sửa CĐ1 cho khớp bài gốc:
- Việt Nam (P3): **2.958** (sửa CĐ1 "3.077").
- Trung Quốc (P5): **4.559** (sửa CĐ1 "4.889").
- *(Lưu ý: CĐ1 có thể dùng số pool thô khác mẫu phân tích bài; nếu cố ý thì ghi rõ "pool mô tả" vs "mẫu hồi quy".)*

### D5. P8 trong CĐ2: nêu **chính = 7 Pacific/N=209/β=−1,339**, 9-nước/N≈1.469 là robustness.

---

## E. Việc máy có thể làm ngay khi NCS quyết
1. NCS chọn lock (D1) + membership (D3) + cung cấp số paper đúng (D4).
2. Máy sẽ: thay bảng per-ICRV chuẩn (D2) xuyên CĐ1/CĐ2/luận án; sửa sample size; sửa P8; thêm crosswalk + ghi chú lock; regenerate docx.
> Máy **không tự** đổi membership/lock vì đó là quyết định khoa học của NCS — sẽ thành "bịa" nếu tự chọn.
