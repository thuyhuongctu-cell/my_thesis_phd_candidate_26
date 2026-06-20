# CANONICAL_NUMBERS — Nguồn sự thật duy nhất (single source of truth)

> **Khóa ngày 2026-06-13; cập nhật 2026-06-19 (loại Timor-Leste).** Mọi con số mẫu/điểm
> uốn/hệ số trong luận án, chuyên đề và papers PHẢI khớp bảng này. Khi một con số thay đổi,
> sửa Ở ĐÂY trước rồi propagate. Mọi giá trị đã tái lập qua `scripts/p7_run_50econ.py`,
> `p10_japan/replication/p10_japan_models.py` (xem `REESTIMATION_LOG_2026-06-13.md`).
> Lưu ý liêm chính: số chỉ đổi sau khi chạy estimation thật, không bịa.
>
> **CẬP NHẬT 2026-06-19 — Timor-Leste bị loại khỏi khung.** Timor-Leste không phải Pacific
> Island Country (Ngân hàng Thế giới: 11 nước) và không thuộc danh sách Pacific SIDS của Liên
> Hợp Quốc (14 PSIDS); `icrv_map()` đã sửa. Khung giảm **50 → 49 nền**, Nhóm VI còn **7 nền**.
> Các con số dưới đây là **giá trị TÁI LẬP từ kho .dta đã commit** (chạy lại P7 không Timor,
> 2026-06-19); chênh lệch nhỏ với bộ locked cũ một phần do kho raw là tập con của master đầy đủ.

## 1. Các khung dữ liệu (định nghĩa chính xác)

| Khung | N firms | Số nền | Ghi chú |
|---|--:|--:|---|
| **Pool phân loại ICRV** | 96.415 | 52 nhãn nền | Trước lọc; gán nhóm ICRV (locked; re-lock loại Timor đang chờ master đầy đủ) |
| **Khung phân tích (tái lập từ raw, loại Timor, GỒM Nhật)** | **87.987** | **49** | 99 cặp nền-năm; dùng cho cả mô tả VÀ ước lượng P7 |
| — trong đó Nhật Bản (P10) | 2.168 | 1 | Sóng WBES đầu tiên 2025 |
| **Tham chiếu locked cũ (GỒM Timor)** | 88.869 | 50 | Bộ locked 2026-06-13 trước khi loại Timor; cần re-lock |
| **⚠️ LEGACY — KHÔNG DÙNG** | 91.982 | 49 | Build P7 cũ tiền-Nhật (pipeline trước); đã bị thay thế |

**Quy tắc phát ngôn chuẩn (lặp ở mọi abstract/chương):**
> "Khung phân tích đa quốc gia gồm **87.987 doanh nghiệp trên 49 nền kinh tế** châu Á
> và Thái Bình Dương (99 cặp nền-năm, **bao gồm Nhật Bản 2025**, loại Timor-Leste theo phân
> loại WB/UN); pool phân loại ICRV trước lọc 96.415 doanh nghiệp/52 nhãn nền."

## 2. P7 — Hồi quy toàn mẫu (49 nền, GỒM Nhật, loại Timor, two-way FE economy+year, CRV1)

| Mô hình | N | β₁ (FSTS) | β₂ (FSTS²) | Điểm uốn | p (Lind–Mehlum) |
|---|--:|--:|--:|--:|--:|
| **M2** (FSTS + FSTS², FE) | **80.373** | +1,194*** | −1,404*** | **51,5%** | < 0,001 |
| **M5** (+ kiểm soát, FE) | **78.445** | +0,503*** | −0,727*** | **43,5%** | < 0,001 |

## 3. Điểm uốn theo nhóm ICRV (khung 50 nền) — "BA VÙNG"

> ⚠️ **Cập nhật 2026-06-19 — loại Timor-Leste khỏi SIDS_small.** Timor-Leste không phải Pacific
> Island Country (Ngân hàng Thế giới: 11 nước, không có Timor) và không thuộc danh sách Pacific
> SIDS của Liên Hợp Quốc (14 PSIDS, không có Timor). `icrv_map()` đã được sửa để loại Timor khỏi
> Nhóm VI; SIDS_small còn **7 nền** (Fiji, Kiribati, PNG, Samoa, Solomon, Tonga, Vanuatu) và khung
> giảm từ 50 → **49 nền**. Tác động lên headline P7 không đáng kể (Timor ≈ 0,55% mẫu; TP/β giữ
> nguyên). **Các tổng locked dưới đây (88.869 / 81.022 / nhóm) vẫn gồm Timor và cần RE-LOCK lại
> trên master đầy đủ** — dòng SIDS_small đã được cập nhật theo build raw 7 nền đã verify.
>
> **Bảng mô tả (single source of truth):** `scripts/relock_descriptives_canonical.py` →
> `data_wbes/analysis/descriptives_canonical_49econ.csv` tái lập mọi ô của Bảng 4.1/4.2 (luận án)
> và 2.3.3.1–2.3.6 (CĐ1) từ raw, cùng harmonization P7 (loại Timor). SIDS 7 nền: n(LP)=1.471,
> sd ln(LP)=1,30, FSTS TB 6,2, xuất khẩu 15,5%, FDI 22,9%, đổi mới SP 39,6%, quy trình 27,9%,
> R&D 11,5%, ISO 15,2%, website 47,1%. Các nhóm khác canonical **trùng** Bảng 4.2 vintage.

| Nhóm ICRV | N | Điểm uốn | p (LM) | Diễn giải ba vùng |
|---|--:|--:|--:|---|
| I. Advanced_innovation (gồm Nhật) | 5.581 | 79,1% | 0,304 | **Trên**: gần tuyến tính, TP ngoài miền |
| II. Advanced_resource (GCC) | 2.075 | 62,0% | 0,081 | Trên–giữa |
| III. Upper_mid | 12.055 | 55,0% | 0,263 | Giữa, không định vị tin cậy |
| IV. Lower_mid_transition | 42.094 | **43,0%** | < 0,001 | **Giữa**: chữ U ngược SẮC NÉT |
| V. Emerging | 15.251 | 34,6% | 0,191 | **Dưới**: cấu trúc tan rã |
| VI. SIDS_small (7 nền, loại Timor) | 1.450 | — (n.s.) | — | **Dưới**: chữ U ngược tan rã (độ dốc −0,085 p_wild=,66; độ cong +0,696 p_wild=,082); FIP là trường hợp giới hạn |

## 4. Các construct/nghiên cứu thành phần

| Đại lượng | Giá trị canonical | Nguồn / lưu ý |
|---|---|---|
| **FIP β (P8)** | **−1,339** (SE 0,386; p < 0,001) | Đặc tả MỨC theo PPP, KHÁC z-spec (z-spec cho −0,098). Exporters N=26. Dẫn bằng 9 nền N=1.469 (β=−0,510) |
| **Meta-analysis k (P6)** | **k = 238** | ⚠️ CẦN hoàn tất search/extraction thật; đóng băng 1 giá trị/thống kê |
| **P10 Nhật Bản** | FSTS tuyến tính +0,671***; bậc hai n.s.; phần bù xuất khẩu +0,258*** | N=2.168; xuất khẩu 16,8%; website 83,8%; tuổi 50,4; nữ QL 7,3% |
| **P9 Ấn Độ** | N gộp = 28.717 (3 sóng) | 2014/2022/2025 |
| **P5 Trung Quốc** | N gộp = 4.544 (2012: 2.610; 2024: 1.934) | 2012/2024 |

## 5. Tình trạng Nhật Bản trong ước lượng (SỬA quan niệm cũ)

**Nhật Bản ĐÃ nằm trong ước lượng P7 canonical** (2.168 dòng trong khung 88.869/50 nền).
Câu cũ trong Mục 4.1.5 luận án ("Nhật chưa vào ước lượng P7, là vòng tái ước lượng tiếp theo")
**ĐÃ LỖI THỜI** — vòng tái ước lượng 50 nền đã chạy (xem REESTIMATION_LOG). Cập nhật:
P7 = 50 nền gồm Nhật; P8 (SIDS) và P9 (Ấn Độ) là pool con riêng không liên quan Nhật.

## 6. Bản đồ "số nào nằm ở file nào" (audit chéo)

| Con số ĐÚNG | KHÔNG được xuất hiện (legacy) |
|---|---|
| 88.869 / 50 nền | 91.982 / 49 nền (trừ khi gắn nhãn "build cũ") |
| 81.022 (M2) / 79.080 (M5) | 84.910 (M2 cũ) / 38.342 (M5 cũ) |
| TP M5 = 43,6%; M2 = 51,5% | TP 40,0% / 36% / 34,6% (cũ) |
| Ba vùng (Nhóm IV 43,0%) | gradient đơn điệu 28% đến 55% |

## Gói kiểm định độ vững bổ sung (2026-06, P7 50 nền)
> Chi tiết: `data_wbes/analysis/p7_robustness_suite_2026-06.md`; thuật toán: `dist/osf/P7_capstone/code/p7_run_50econ.py` + bootstrap WCR thủ công (FWL).
- **Cụm nhỏ (wild-cluster CGM, B=9.999):** độ cong Nhóm IV p: 0,001 (CRV1) → ≈0,10 (wild); Đang nổi ≈0,33; SIDS-linear ≈0,30 → suy luận phi tuyến neo ở cấp gộp (M2, 49 cụm, β₂=−1,399, p<,001).
- **Đa kiểm định (Holm/Bonferroni):** cả 4 tương tác TCI/DAI không có ý nghĩa thô lẫn sau hiệu chỉnh → kết luận level-shifter vững.
- **Bất biến đo lường:** mục web/TCI hiện diện ~99% ở cả 3 lược đồ; DAI mean 0,30→0,46→0,53 (khuếch tán thực).
- **Chọn lọc (IMR):** M5 TP 43,6%→43,5%; β₂=−0,732 (p<,001); IMR=−0,414 (p=,317, n.s.) → không có thiên lệch chọn lọc trong độ cong.
