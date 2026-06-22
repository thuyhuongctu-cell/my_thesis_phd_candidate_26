# Rà soát nội dung luận án — Báo cáo nhất quán nội tại (2026-06-22)

**Phạm vi:** `thesis/chuong_1..5`, phụ lục A/B, `11_dissertation_positioning`, `00_phan_dau`,
đối chiếu chéo với các nghiên cứu thành phần P1–P10 và các tệp khóa số canonical.
**Phương pháp:** ba lượt quét song song — (i) điểm uốn & hệ số, (ii) cỡ mẫu/N & số học cộng dồn,
(iii) hệ giả thuyết & tham chiếu chéo/đánh số bảng-hình.

---

## 0. Tóm tắt điều hành

| # | Hạng mục | Mức độ | Trạng thái |
|---|----------|--------|-----------|
| 1 | **Bảng 4.1 — sáu n nhóm cộng = 98.097 ≠ tổng ghi 96.415** (lệch +1.682), và không khớp CSV canonical | 🔴 Nghiêm trọng | **Cần master file để chốt — KHÔNG tự sửa số** |
| 2 | Nhãn năm hội nghị: "ICBEF 2025" (ch3 ×2) vs "ICBEF 2024" (ch4/ch5/DMTL) | 🟡 Nhẹ | ✅ **Đã sửa → 2024** |
| 3 | TCI Trung Quốc 2012: thân luận án ghi "+0,26" vs bài P5 "+0,28" | 🟡 Nhẹ | ✅ **Đã sửa → +0,28** (ch4:668, ch5:139) |
| 4 | H1c kết luận trong ch4 (có nhãn) nhưng ch5 §5.1.6 bàn không gắn nhãn; H1c vắng trong Bảng 2.2 | 🟠 Trung bình | ⏳ Đề xuất — cần quyết định của NCS |
| 5 | Tiêu đề ch5 "Xác nhận H2 / H5" vs ch4 §4.11 "Xác nhận một phần" | 🟠 Trung bình | ⏳ Đề xuất — chỉnh từ ngữ |
| 6 | H6 chỉ kết luận ở ch4 §4.11, không nhắc lại trong ch5 | 🟡 Nhẹ | ⏳ Đề xuất |
| 7 | Bảng 2.1 / Bảng 2.2 đánh số ngược thứ tự xuất hiện (ch2 §2.5.8) | 🟡 Nhẹ | ⏳ Đề xuất |

**Kết luận chung:** Bộ số kinh tế lượng cốt lõi (điểm uốn P3/P4/P5/P7/P9/P10, hệ số TCI/DAI,
meta P6) **nhất quán** xuyên năm chương và khớp tệp khóa canonical. Phân biệt 43,6% (toàn mẫu M5)
vs 43,0% (Nhóm IV) là **đúng**, không phải lỗi. Mọi tham chiếu chéo `Mục/Bảng/Hình` đều phân giải
được (không có tham chiếu treo). Vấn đề duy nhất ở mức số liệu là **Bảng 4.1** (hạng mục 1).

---

## 1. 🔴 Bảng 4.1 — n các nhóm ICRV không cộng về tổng, và lệch CSV canonical

**Vị trí:** `thesis/chuong_4_ket_qua_vi.md:25–31` (và caption :21, :35).

### 1.1 Lỗi cộng dồn nội tại
```
Nhóm I 6.390 + II 2.269 + III 17.905 + IV 50.926 + V 18.569 + VI 2.038 = 98.097
Tổng ghi trong bảng (:31) ................................................ 96.415
Lệch ..................................................................... +1.682
```
Hàng "Tổng (phân loại ICRV) = 96.415" tự mâu thuẫn với chính cột n của bảng.

### 1.2 So với nguồn canonical `data_wbes/analysis/cd1_relock_descriptives_by_icrv.csv`
| Nhóm | Bảng 4.1 | CSV canonical | Chênh | Ghi chú |
|------|---------:|--------------:|------:|---------|
| I (Adv. đổi mới) | 6.390 | 4.222 | +2.168 | = đúng Nhật Bản 2025 (4.222 + 2.168) → bản **gồm Nhật** |
| II (Adv. tài nguyên) | 2.269 | 2.269 | 0 | khớp |
| III (Trung bình cao) | 17.905 | 13.993 | **+3.912** | **không giải thích được** (nghi vấn vintage cũ/khác) |
| IV (Chuyển đổi TB-thấp) | 50.926 | 50.926 | 0 | khớp |
| V (Đang nổi) | 18.569 | 18.569 | 0 | khớp |
| VI (SIDS) | 2.038 | 1.885 | +153 | lệch |
| **Tổng** | **98.097** | **91.864** | | cả hai ≠ 96.415 |

**Chẩn đoán:** Bảng 4.1 là bản **trộn nhiều vintage** — ba nhóm (II, IV, V) khớp CSV; nhóm I đã
cập nhật gồm Nhật Bản; nhóm III và VI mang số khác (drift). Tổng ghi 96.415 là **pool khóa canonical**
(xuất hiện ở `scripts/build_pooled_dataset.py:118`, `check-consistency.py`, phụ lục, slide) nhưng
**không** bằng tổng cột (98.097) lẫn tổng CSV (91.864).

**Vì sao KHÔNG tự sửa:** Bản phân rã per-nhóm đúng cộng về 96.415 nằm trong **master file** mà NCS
giữ (xem `scripts/build_pooled_dataset.py:26–28`: "official locked pool sizes ... reported from the
master file"; script không tái lập được từ raw subset trong repo). Sửa tay = bịa số. Hơn nữa hạng mục
này **gắn với lần rebuild P7 China-2012 authoritative** mà NCS đã giữ lại cho mình
(`p7/P7_CHINA2012_REBUILD_HANDOFF.md`) — nhóm III (gồm Trung Quốc) chính là nhóm lệch lớn nhất.

**Khuyến nghị:** Trong lần rebuild canonical, xuất lại bảng phân rã ICRV per-nhóm trên **đúng khung
pool 96.415 (gồm Nhật Bản)** rồi thay toàn bộ cột n Bảng 4.1; kiểm tra cộng cột = 96.415 trước khi khóa.

---

## 2–3. ✅ Đã sửa trong lượt này

- **ICBEF 2025 → 2024** (`chuong_3:35`, `chuong_3:37`): danh mục công bố (`00_phan_dau:216`,
  "Sixth ICBEF 2024") và ch4/ch5 đều ghi 2024 cho cùng bản nền k=113/K=200 → ch3 là chỗ sai năm.
- **TCI Trung Quốc 2012 +0,26 → +0,28** (`chuong_4:668`, `chuong_5:139`): bài P5
  (`p5/p5_china_en_clean.md:26,42`) ghi β_z = +0,28 (2012) → +0,43 (2024). Cận trên +0,43 đã đúng;
  chỉ cận dưới lệch. Không ảnh hưởng kết luận.

---

## 4. 🟠 H1c — kết luận không gắn nhãn ở ch5; vắng trong Bảng 2.2

- H1c (tan biến ngưỡng, Ấn Độ) **được phát biểu** `ch2:238` (§2.5.2c) và **kết luận có nhãn** ở
  bảng tổng hợp `ch4:688`.
- Nhưng `ch5 §5.1.6` (dòng 57) bàn đúng hiện tượng P9/Ấn Độ mà **không gắn nhãn "H1c"**, và H1c
  **không có dòng** trong Bảng 2.2 (`ch2:278`, vốn liệt kê H1, H1b, H2–H6).
- **Đề xuất:** thêm "(H1c)" vào §5.1.6 và bổ sung một dòng H1c vào Bảng 2.2 cho cân với H1b. *(Cần
  NCS xác nhận vì đụng khung giả thuyết.)*

## 5. 🟠 Tiêu đề "Xác nhận H2 / H5" (ch5) vs "Xác nhận một phần" (ch4 §4.11)

- `ch5:25` "Xác nhận H2", `ch5:17` "Xác nhận H5" — trong khi `ch4:682/685` ghi "Xác nhận **một phần**"
  (vì tương tác uốn đường cong không có ý nghĩa trên toàn mẫu P7).
- Thân bài ch5 thực ra đã viết "xác nhận một phần" và giải thích (mức nâng sàn xác nhận; uốn đường
  cong tùy bối cảnh). **Đề xuất:** đổi tiêu đề thành "Xác nhận (một phần) H2/H5" để khớp ch4, hoặc
  thêm một mệnh đề làm rõ ngay dưới tiêu đề. *(Đây là tuyên bố lập trường của NCS — cần xác nhận.)*

## 6. 🟡 H6 chỉ kết luận ở ch4

H6 (dị biệt thời gian) có verdict ở `ch4:686` ("không xác nhận tại TQ F=1,83 p=,176; TP dịch chuyển
tại VN") nhưng không được nhắc lại trong phần bàn luận ch5. **Đề xuất:** thêm một câu về H6 vào §5.1
hoặc §5.4 hạn chế.

## 7. 🟡 Bảng 2.1 / Bảng 2.2 đánh số ngược (ch2 §2.5.8)

Bảng 2.2 (tổng hợp giả thuyết) định nghĩa trước ở `ch2:278`, Bảng 2.1 (ánh xạ nghiên cứu thành phần)
sau ở `ch2:298`. Người đọc gặp "Bảng 2.2" trước "Bảng 2.1". **Đề xuất:** hoán đổi số hai bảng (cập
nhật mọi tham chiếu `ch2:296,302–312`). *(Thay đổi lan tỏa — để NCS quyết.)*

---

## 8. ✅ Các hạng mục đã kiểm tra và NHẤT QUÁN

- **Điểm uốn:** P7 M2 51,5% → M5 43,6% (toàn mẫu) vs Nhóm IV 43,0% — đúng và phân biệt rõ.
  VN 39–46% (pooled 39,7%), TQ 47–49% (48,78%), Singapore ~88,6% (kèm cảnh báo CI), Ấn Độ
  61,8%→40,7%→tan biến, Nhật điểm uốn ngoài miền. Khớp `CANONICAL_NUMBERS.md`.
- **Hệ số:** TCI +0,141 / DAI +0,201 (toàn mẫu); Nhật +0,671 (tuyến tính), premium 25,8%;
  FIP −1,339 (chỉ bản 3-cụm N=209, có cảnh báo). Nhất quán.
- **Meta P6:** k=238, K=288, r=0,074, I²=62,4% (54,1%/8,4%), Q_M=17,35 df=4 p=,002; 5-regime
  (P6) vs 6-nhóm (P7) đã được hòa giải tường minh ở `ch4:179`.
- **Cỡ mẫu:** pool 96.415/52; khung 88.869/50; P7 M2 81.022 / M5 79.080; Nhật 2.168; P1 40.633
  (5.251+12.068+23.314 ✅); P8 1.450/7 nền. 91.982/84.910 là **khung pre-Japan** (ghi rõ ở
  `appendix_A:83`) — không phải mâu thuẫn.
- **Tham chiếu chéo:** mọi `Mục X.Y`, `Bảng X.Y`, `Hình X.Y` đều phân giải; không có tham chiếu treo.
  Mọi `Hình 4.x` đều có tệp trong `thesis/figures/`.

---

*Người rà soát: trợ lý AI (3 lượt quét song song có kiểm chứng số học). Hạng mục 1, 4–7 chờ quyết
định/ rebuild của NCS; hạng mục 2–3 đã áp dụng.*
