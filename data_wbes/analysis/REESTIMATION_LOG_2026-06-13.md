# Biên bản tái lập ước lượng — P7 (50 nền) và P10 (Nhật Bản 2025)

*Ngày chạy: 2026-06-13. Skill: `stata-wbes-runner`. Branch: `claude/phd-thesis-review-L9Gml`.*

## 1. Môi trường thực thi

| Thành phần | Trạng thái |
|---|---|
| Stata binary (stata / stata-mp / stata-se / xstata) | **Không có** trong container đám mây này |
| Python (pandas, numpy, pyreadstat) | Có |
| pyfixest | 0.60.0 (tương đương `reghdfe`) |
| Do-file Stata đã commit | `scripts/stata/00_prep_data.do`, `p7_reestimate.do`, `p8_sids_fip.do` |

Theo quy trình của skill (Mục 1, Mục 3) và skill `stata-khong-license-giai-phap`: khi
không có Stata license, đường dẫn fallback Python đã được validate là phương án
hợp lệ cho kinh tế lượng pooled cross-section. Các do-file Stata được commit để
NCS chạy đối chứng trên máy có license trước khi gửi tạp chí (yêu cầu của QUY
TẮC LIÊM CHÍNH Mục 0).

**Đường dẫn đã chạy: Fallback Python (pyfixest/numpy).**

## 2. P7 — 50 nền kinh tế (`scripts/p7_run_50econ.py`)

Mẫu phân tích: 88.869 dòng, 50 nền, 103 cặp nước-năm.

| Mô hình | N | β₁ | p₁ | β₂ | p₂ | Điểm uốn | p (Lind–Mehlum) | R²_within |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| M2 (FSTS + FSTS², FE) | 81.022 | +1,189 | 0,000 | −1,398 | 0,000 | **51,5%** | 0,000 | 0,008 |
| M5 (+ kiểm soát, FE) | 79.080 | +0,500 | 0,000 | −0,721 | 0,000 | **43,6%** | 0,000 | 0,047 |

Điểm uốn theo nhóm ICRV:

| Nhóm | N | β₁ | β₂ | Điểm uốn | p (LM) |
|---|--:|--:|--:|--:|--:|
| Advanced_innovation | 5.581 | +0,698 | −0,504 | 79,1% | 0,304 (không định vị) |
| Advanced_resource | 2.075 | +0,854 | −0,730 | 62,0% | 0,081 |
| Upper_mid | 12.055 | +0,168 | −0,189 | 55,0% | 0,263 |
| Lower_mid_transition | 42.094 | +0,709 | −1,012 | **43,0%** | 0,000 |
| Emerging | 15.457 | +0,218 | −0,455 | 34,8% | 0,184 |
| SIDS_small (tuyến tính, z-spec) | 1.818 | −0,098 | — | — | — |

Kết quả khớp chính xác số liệu khóa trong `data_wbes/analysis/p7_50econ_results.md`.
Lưu ý: FIP β = −1,339 của P8 là đặc tả MỨC theo PPP (khác z-spec ở đây cho ra
−0,098); phân biệt này được ghi rõ trong `data_wbes/analysis/P7_REESTIMATION_NOTE.md`.

## 3. P10 — Nhật Bản 2025 (`p10_japan/replication/p10_japan_models.py`)

Nguồn: `data_wbes/raw_dta/Japan-2025-full-data.dta` (N = 2.168 cơ sở).

**Bảng 1 (mô tả):** lnlp TB 16,984 (sd 0,843); FSTS 4,1%; xuất khẩu 16,8%;
TCI 0,273; website 83,8%; sở hữu nước ngoài 1,9%; tuổi 50,4 năm; nữ quản lý 7,3%.
FSTS có điều kiện xuất khẩu = 24,6%; xuất khẩu gián tiếp > 0 = 64,2%.

**Bảng 3 (chuỗi M1–M5):** tuyến tính M1 +0,671 (p < 0,001); số hạng bậc hai
không ý nghĩa ở mọi đặc tả (M2 −0,606, p = 0,323); điểm uốn đại số 90–108% nằm
ngoài miền dữ liệu. TCI +0,100 (p < 0,001), DAI +0,110 (p = 0,028).

**Bảng 4 (biên rộng, LPM):** sở hữu nước ngoài +0,408 (p < 0,001), TCI +0,083
(p < 0,001), DAI +0,046 (p = 0,005), tuổi +0,026 (p = 0,010); R² = 0,228.
Phần bù doanh nghiệp xuất khẩu = +0,258 (p < 0,001).

**Bảng 5 (độ vững):** số hạng bậc hai không ý nghĩa trong cả 6 đặc tả
(R2 p = 0,662; R3 p = 0,448; R5 p = 0,378; R6 p = 0,551).

Mọi con số khớp chính xác bản thảo P10 (`01_manuscript_blinded.md`) và mục
Mục 4.1.5/Mục 4.6 của luận án.

## 4. Kết luận

Toàn bộ số liệu kinh tế lượng được báo cáo trong luận án (P7) và bản thảo P10
đã tái lập thành công qua pipeline Python đã validate. Không có hệ số nào bị bịa
hoặc chỉnh tay. Bước còn lại trước khi gửi tạp chí: chạy đối chứng các do-file
`scripts/stata/*.do` trên máy có Stata license (QUY TẮC LIÊM CHÍNH Mục 0).
