# CANONICAL_NUMBERS — Nguồn sự thật duy nhất (single source of truth)

> **Khóa ngày 2026-06-13.** Mọi con số mẫu/điểm uốn/hệ số trong luận án, chuyên đề
> và papers PHẢI khớp bảng này. Khi một con số thay đổi, sửa Ở ĐÂY trước rồi
> propagate. Mọi giá trị đã tái lập qua `scripts/p7_run_50econ.py`,
> `p10_japan/replication/p10_japan_models.py` (xem `REESTIMATION_LOG_2026-06-13.md`).
> Lưu ý liêm chính: số chỉ đổi sau khi chạy estimation thật, không bịa.

## 1. Các khung dữ liệu (định nghĩa chính xác)

| Khung | N firms | Số nền | Ghi chú |
|---|--:|--:|---|
| **Pool phân loại ICRV** | 96.415 | 52 nhãn nền | Trước lọc; gán nhóm ICRV |
| **Khung phân tích (canonical, GỒM Nhật Bản)** | **88.869** | **50** | 103 cặp nền-năm; dùng cho cả mô tả VÀ ước lượng P7 |
| — trong đó Nhật Bản (P10) | 2.168 | 1 | Sóng WBES đầu tiên 2025 |
| — nếu loại Nhật Bản | 86.701 | 49 | Chỉ để tham chiếu |
| **⚠️ LEGACY — KHÔNG DÙNG** | 91.982 | 49 | Build P7 cũ tiền-Nhật (pipeline trước); đã bị thay thế |

**Quy tắc phát ngôn chuẩn (lặp ở mọi abstract/chương):**
> "Khung phân tích đa quốc gia gồm **88.869 doanh nghiệp trên 50 nền kinh tế** châu Á
> và Thái Bình Dương (103 cặp nền-năm, **bao gồm Nhật Bản 2025**); pool phân loại
> ICRV 96.415 doanh nghiệp/52 nhãn nền."

## 2. P7 — Hồi quy toàn mẫu (50 nền, GỒM Nhật, two-way FE economy+year, CRV1)

| Mô hình | N | β₁ (FSTS) | β₂ (FSTS²) | Điểm uốn | p (Lind–Mehlum) |
|---|--:|--:|--:|--:|--:|
| **M2** (FSTS + FSTS², FE) | **81.022** | +1,189*** | −1,398*** | **51,5%** | < 0,001 |
| **M5** (+ kiểm soát, FE) | **79.080** | +0,500*** | −0,721*** | **43,6%** | < 0,001 |

## 3. Điểm uốn theo nhóm ICRV (khung 50 nền) — "BA VÙNG"

| Nhóm ICRV | N | Điểm uốn | p (LM) | Diễn giải ba vùng |
|---|--:|--:|--:|---|
| I. Advanced_innovation (gồm Nhật) | 5.581 | 79,1% | 0,304 | **Trên**: gần tuyến tính, TP ngoài miền |
| II. Advanced_resource (GCC) | 2.075 | 62,0% | 0,081 | Trên–giữa |
| III. Upper_mid | 12.055 | 55,0% | 0,263 | Giữa, không định vị tin cậy |
| IV. Lower_mid_transition | 42.094 | **43,0%** | < 0,001 | **Giữa**: chữ U ngược SẮC NÉT |
| V. Emerging | 15.457 | 34,8% | 0,184 | **Dưới**: cấu trúc tan rã |
| VI. SIDS_small (z-spec) | 1.818 | — (âm) | — | **Dưới**: đảo chiều → FIP |

## 4. Các construct/nghiên cứu thành phần

| Đại lượng | Giá trị canonical | Nguồn / lưu ý |
|---|---|---|
| **FIP β (P8)** | **−1,339** (SE 0,386; p < 0,001) | Đặc tả MỨC theo PPP, KHÁC z-spec (z-spec cho −0,098). Exporters N=26. Dẫn bằng 9 nền N=1.469 (β=−0,510) |
| **Meta-analysis k (P6)** | **k = 238** | ⚠️ CẦN hoàn tất search/extraction thật; đóng băng 1 giá trị/thống kê |
| **P10 Nhật Bản** | FSTS tuyến tính +0,671***; bậc hai n.s.; phần bù xuất khẩu +0,258*** | N=2.168; xuất khẩu 16,8%; website 83,8%; tuổi 50,4; nữ QL 7,3% |
| **P9 Ấn Độ** | N gộp = 28.717 (3 sóng) | 2014/2022/2025 |
| **P5 Trung Quốc** | N gộp ≈ 4.559 | 2012/2024 |

## 5. Tình trạng Nhật Bản trong ước lượng (SỬA quan niệm cũ)

**Nhật Bản ĐÃ nằm trong ước lượng P7 canonical** (2.168 dòng trong khung 88.869/50 nền).
Câu cũ trong §4.1.5 luận án ("Nhật chưa vào ước lượng P7, là vòng tái ước lượng tiếp theo")
**ĐÃ LỖI THỜI** — vòng tái ước lượng 50 nền đã chạy (xem REESTIMATION_LOG). Cập nhật:
P7 = 50 nền gồm Nhật; P8 (SIDS) và P9 (Ấn Độ) là pool con riêng không liên quan Nhật.

## 6. Bản đồ "số nào nằm ở file nào" (audit chéo)

| Con số ĐÚNG | KHÔNG được xuất hiện (legacy) |
|---|---|
| 88.869 / 50 nền | 91.982 / 49 nền (trừ khi gắn nhãn "build cũ") |
| 81.022 (M2) / 79.080 (M5) | 84.910 (M2 cũ) / 38.342 (M5 cũ) |
| TP M5 = 43,6%; M2 = 51,5% | TP 40,0% / 36% / 34,6% (cũ) |
| Ba vùng (Nhóm IV 43,0%) | gradient đơn điệu 28% → 55% |
