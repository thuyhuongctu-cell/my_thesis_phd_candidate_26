# Báo cáo Peer Review — Chuyên đề Tiến sĩ Số 2 (CĐ2)

**Bản thảo:** "Xây dựng mô hình nghiên cứu về ảnh hưởng của quốc tế hóa đến hiệu quả hoạt động kinh doanh của các doanh nghiệp ở Châu Á" · Đỗ Thùy Hương · HD: PGS.TS. Phan Anh Tú
**Ngày:** 2026-06-10 · **Chế độ:** full (5 reviewers + Editorial Decision) · **Read-only**
**File:** `chuyen_de/cd2/00_cd2_ctu_final_vi.md` (1.148 dòng)

> Loại: chuyên đề **xây dựng mô hình** (conceptual + đặc tả thực nghiệm M0–M7 + hệ giả thuyết H1–H6). Không trình bày kết quả pool (đúng phạm vi đã tuyên bố). Đánh giá: cấu trúc, logic giả thuyết, nhất quán nội bộ & với CĐ1/P7/P8.

---

## Phase 0 — Cấu hình
- **Lĩnh vực:** IB — mô hình hóa quan hệ I–P + điều tiết đa tầng (TCI/DAI/quản trị/thể chế/thời gian). Conceptual + econometric specification.
- **Độ chín:** bản thảo nâng cao, gần hoàn chỉnh.
- **Hội đồng (5):** EIC (IB theory-building) · R1 Phương pháp (econometric spec/identification) · R2 Lĩnh vực (I-P, CDCM, institutional) · R3 Liên ngành · Devil's Advocate.

**Điểm mạnh nổi bật (đồng thuận):** khung tích hợp 5 tầng mạch lạc, ánh xạ tầng đến giả thuyết đến biến đến bằng chứng neo đậu (Bảng 2.1, 2.5) rất tốt; 2 hình khái niệm; chuỗi M0–M7 đặc tả công thức đầy đủ (LaTeX); chiến lược nhận dạng 4 tầng (OLS/FE đến IV đến phi tuyến LM/Paternoster đến mẫu con); kế hoạch robustness 6 nhóm R1–R6 với ngưỡng chấp nhận rõ. Đủ tầm chuyên đề tiến sĩ về **thiết kế**.

---

## 🟥 CRITICAL (Devil's Advocate + R2 + EIC hội tụ)

### D1. Gradient điểm uốn H5 **không đơn điệu** — mâu thuẫn với chính bằng chứng neo đậu
H5 (dòng 542) tuyên bố TP "**giảm đơn điệu** theo thể chế mạnh hơn: V(~50–55%) đến … đến I(~28%)". Cơ chế phát biểu: *"thể chế càng mạnh đến đạt đỉnh ở FSTS thấp hơn"*. **Nhưng** bằng chứng neo đậu P3/P5 chính trong bài cho:
- Nhóm **III** (Trung Quốc, thể chế **mạnh hơn**) TP = **47–49%**
- Nhóm **IV** (Việt Nam, thể chế **yếu hơn**) TP = **39–46%**
 đến Thể chế mạnh hơn (III) lại có TP **cao hơn** IV — **ngược** với cơ chế "đơn điệu giảm". Thứ tự thực tế I(28) < IV(39–46) < III(47–49) < V(50–55) đến III và IV **đảo vị** so với gradient thể chế. Dòng 473 (H1) cũng tự mâu thuẫn: liệt kê "III(47–49) đến IV(39–46)" rồi gọi là "**tăng dần**" (thực ra giảm). đến **Phải sửa phát biểu gradient**: hoặc bỏ "đơn điệu", thừa nhận TP không đơn điệu theo ICRV (III>IV là ngoại lệ cần giải thích bằng cơ chế khác — vd cấu trúc xuất khẩu/GVC), hoặc tái định nghĩa thứ tự gradient.

### D2. P7 turning point: "~28% toàn mẫu" (Mục 2.3.4/H1/H5) ✗ vs "36% pooled, 28% Advanced" (Mục 2.4.3)
- Mục 2.3.4 dòng 469, 535: *"Nhóm I ~28% (**P7 toàn mẫu**); P7 pooled (N=84,910): TP ~28%"*.
- Mục 2.4.3 Hướng 2 dòng 922: *"P7 … H1 (phi tuyến) **TP≈36%**; H5 … TP giảm từ ~55% xuống Advanced ~28%"*.
 đến Mâu thuẫn nội bộ: 28% là TP **regime Advanced-Innovation**, còn **pooled = 36%**. Mục 2.3.4 dán nhãn 28% là "toàn mẫu/pooled" là **SAI**. (Khớp dữ liệu: P7 pooled M2 = 36,4%.) Sửa Mục 2.3.4: "P7 pooled 36%; regime Advanced-Innovation ~28%".

### D3. n_firms theo nhóm ICRV (Bảng 2.8) mâu thuẫn CĐ1 + SIDS sai nặng
Bảng 2.8 (dòng 720-728): I~6.500 · II~8.500 · III~18.000 · IV~28.000 · V~35.000 · **VI~5.185**.
- **VI SIDS ~5.185** >< CĐ1 nói SIDS = **1.371** (và dữ liệu thật 7 Pacific = 1.371). 5.185 trông như **số dư back-calc** (101.185 − 96.000) — sai.
- Toàn bộ phá nhóm khác hẳn CĐ1 Bảng 2.3.2.1 (I 4.220/II 1.932/IV 47.803/V 28.678) đến đây là **bộ thứ ba** mâu thuẫn (xem CĐ1 review C1). Cần đồng bộ một bộ chuẩn xuyên CĐ1+CĐ2.

---

## 🟧 R1 — Phương pháp (MAJOR)

1. **(MAJOR) "Chuỗi lồng nhau" (nested) sai:** Mục 2.3.5 + Đóng góp 5 nói M0–M7 "lồng nhau, so sánh AIC/BIC". Nhưng **M3=M1+TCI, M4=M1+DAI, M5=M1+Manager, M6=M1+ICRV** — tất cả **phân nhánh từ M1**, KHÔNG lồng vào nhau (M4 không chứa M3). đến AIC/BIC chỉ so sánh được trong nhánh (M0⊂M1⊂M2; M1⊂M3; M1⊂M4…), không phải một thang lồng liên tục. Sửa: gọi là "họ mô hình gốc M1" và nêu rõ cặp so sánh hợp lệ.
2. **(MINOR)** M6 bỏ country FE (vì ICRV bất biến theo quốc gia) đến thay Region FE (6 vùng). Hợp lý, nhưng nên cảnh báo: ICRV gần trùng Region đến đa cộng; nêu cách xử lý.
3. **(MINOR)** Cronbach α TCI 0,55–0,65 được biện minh là "formative" (Coltman 2008) — đúng, nhưng α thấp với thang formative thì **không phải tiêu chí phù hợp**; nên bỏ α, dùng tiêu chí formative (VIF/weight) cho nhất quán.
4. **(MINOR)** Ngưỡng F bậc một: Mục 2.3.6 ghi "≥16 (Stock&Yogo)" và "Staiger–Stock" (dòng 904) — thống nhất 1 ngưỡng/nguồn.

## 🟧 R2 — Lĩnh vực (MAJOR)

1. **(MAJOR) Đếm giả thuyết không nhất quán:** tiêu đề/Mục 2.1.2/abstract nói "**H1–H6**" (6); thân bài có H1a,H1b,H2,H3a,H3b,H3c,H4a,H4b,H4c,H5,H6 = **11 sub-hypotheses**; dòng 568 nói "**Chín** giả thuyết" rồi liệt kê 11. đến Chuẩn hóa: "6 giả thuyết chính (H1–H6), 11 mệnh đề con".
2. **(MAJOR) P8 mô tả lệch kết quả gốc:** Mục 2.4.3 Hướng 3 ghi P8 = "**N=1.469, 9 nước**, β(FSTS_c)=**−0,404***". Nhưng **kết quả CHÍNH của P8 = 7 Pacific, N=209, β=−1,339**; 9-nước/N≈1.469 chỉ là **robustness**. CĐ2 đang trình bày robustness như kết quả chính đến thống nhất với bài P8 (nêu cả hai: chính 7-nước/−1,339; robustness 9-nước). Cũng kiểm β: −0,404 (CĐ2) vs −0,510 (robustness P8) — đối chiếu.
3. **(MINOR)** Bảng 2.1 (dòng 397) **đảo thứ tự tầng**: liệt kê Tầng 1 đến 2 đến "Digital Lens" đến **4 (Upper Echelons)** đến **3 (Institutional)** đến Time. Tầng 3 và 4 bị xáo. Sắp lại 1 đến 2 đến 3 đến 4 + Digital Lens cho khớp Mục 2.3.2.
4. **(STRENGTH)** Bảng 2.13 (so sánh CĐ2 vs 5 khung tham chiếu) định vị đóng góp rất rõ; CDCM là đóng góp lý thuyết thực chất.

## 🟨 R3 — Liên ngành (MINOR)

1. **(MINOR) Naming ICRV drift CĐ ↔ dữ liệu:** CĐ2 "Nhóm IV = Emerging (7 nước: VN…Mongolia)" và "Nhóm V = Frontier (17 nước)". Nhưng nhãn dữ liệu phân tích (P7) là `Emerging`=**17 nước** và `Lower_mid_transition`=**7 nước** đến tên "Emerging/Frontier" trong CĐ **hoán đổi** so với label dữ liệu. Hình 2.2 (dòng 429) có cố gắng giải thích ("Việt Nam — Lower_mid_transition … Nhóm IV") nhưng rối. Cần 1 bảng crosswalk "tên CĐ ↔ icrv_label dữ liệu" để hội đồng/độc giả không nhầm.
2. **(STRENGTH)** Phạm vi/hạn chế (Mục 2.4.2) trình bày 3 phần (không-thể-kết-luận / khắc phục / nguồn tham chiếu) rất chuyên nghiệp, trung thực về cross-sectional ≠ nhân quả.

## 🟪 Devil's Advocate (ngoài D1–D3)

1. **(MINOR)** P4 Singapore (Nhóm I) TP=88,6% vs P7-regime-Nhóm-I 28% — chênh **60 đpt** trong cùng Nhóm I. CĐ2 xử lý bằng cách gọi P4 là "ngoại lệ đơn quốc gia (LM p=0,303 n.s.)" — **trung thực và hợp lý**, nhưng nên nói rõ hệ quả: dùng P4 làm "bằng chứng neo đậu H3b" (DAI×FSTS²=+3,119) trong khi chính P4 không có U ngược có ý nghĩa đến neo đậu H3b dựa trên 1 quốc gia, mẫu thưa vùng FSTS cao. Hạ mức "xác nhận" của H3b xuống "gợi ý".
2. **(MINOR typo)** Bảng 2.4 dòng 444: "null (Nhóm **IV, IV**)" — lặp; chắc là "Nhóm III, IV".
3. **Quan sát (không lỗi):** Mục 2.4.3 cập nhật P6/P7/P8 đã hoàn thành là điểm cộng cho tính mạch lạc chuỗi luận án.

---

## 📋 EDITORIAL DECISION

**Quyết định: MAJOR REVISION** (logic gradient + nhất quán nội bộ; KHÔNG phải nội dung lý thuyết).

**Lý do:** Thiết kế mô hình, khung lý thuyết, đặc tả M0–M7 và chiến lược nhận dạng **vững, đủ tầm** (EIC/R1/R2/R3 đồng thuận điểm mạnh). Devil's Advocate nêu **1 CRITICAL về lập luận lõi (D1 — gradient không đơn điệu, mâu thuẫn bằng chứng)** đến theo quy tắc, **không thể Accept** cho tới khi sửa. Cộng D2 (28% vs 36%), D3 (n_firms/SIDS) là lỗi nhất quán nội bộ hội đồng dễ bắt.

### Revision Roadmap
| # | Mức | Việc | Vị trí |
|---|---|---|---|
| 1 | 🟥 | **Sửa phát biểu gradient H5/H1**: bỏ "đơn điệu" hoặc giải thích III>IV (TP 47–49 > 39–46 dù III mạnh hơn) bằng cơ chế phụ (GVC/cấu trúc xuất khẩu), không phải chỉ "gradient thể chế" | Mục 2.3.4 H1 (dòng 473), H5 (dòng 542) |
| 2 | 🟥 | ~~Sửa "P7 toàn mẫu TP ~28%" đến **pooled 36% / Advanced ~28%**~~ Có ĐÃ SỬA 2026-06-10 | Mục 2.3.4 dòng 469, 535 |
| 3 | 🟥 | ~~Đồng bộ n_firms Bảng 2.8; SIDS 5.185 đến 1.371~~ Có ĐÃ RE-LOCK 2026-06-10 (canonical 49-frame từ master .dta) | Bảng 2.8 |
| 4 | 🟧 | ~~Sửa P8 mô tả~~ Có ĐÃ SỬA 2026-06-10 (chính 7-Pacific/N=209/β=−1,339; robustness 9-nước) | Mục 2.4.3 |
| 5 | 🟧 | ~~Chuẩn hóa đếm giả thuyết; sửa "Chín"~~ Có ĐÃ SỬA 2026-06-10 ( đến 11 mệnh đề con dưới 6 giả thuyết chính) | dòng 568 |
| 6 | 🟧 | Bỏ tuyên bố "nested ladder"; nêu cặp so sánh AIC/BIC hợp lệ (nhánh từ M1) | Mục 2.3.5, Đóng góp 5 |
| 7 | 🟧 | Sắp lại thứ tự tầng Bảng 2.1 (1 đến 2 đến 3 đến 4); thêm crosswalk "tên ICRV CĐ ↔ icrv_label dữ liệu" | Bảng 2.1, Mục 2.3.6 |
| 8 | 🟨 | Bỏ Cronbach α cho TCI formative; thống nhất ngưỡng F (16/Staiger-Stock); ~~sửa typo "IV, IV" đến "III, IV"~~ Có ĐÃ SỬA; hạ H3b "xác nhận" đến "gợi ý" | Mục 2.3.6, Bảng 2.4 |

> **Đã sửa cơ học 2026-06-10 (không mơ hồ):** D2 (28% đến pooled 36%/Advanced 28%, 3 chỗ) · đếm giả thuyết (Chín đến 11 con/6 chính) · typo Bảng 2.4 (IV,IV–III,IV). Đồng bộ `chuyen_de/` + `dist/source_md/` + docx. **Còn chờ NCS:** D1 (gradient đơn điệu — tái khung khoa học), D3/Bảng 2.8 (n_firms ICRV chuẩn), nested-ladder, P8 mô tả, crosswalk ICRV.

**Ước lượng:** 1 vòng revision (logic gradient + nhất quán số/giả thuyết) đến sẵn sàng nộp/bảo vệ. **Lưu ý chung CĐ1+CĐ2:** vấn đề **n_firms theo ICRV không khớp giữa các bảng** xuất hiện ở cả hai chuyên đề + có bộ thứ ba — NCS cần **một bảng phân bổ ICRV chuẩn duy nhất** dùng nhất quán xuyên CĐ1, CĐ2, luận án.
