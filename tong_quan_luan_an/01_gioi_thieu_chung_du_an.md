# 1. Giới thiệu chung về dự án luận án

> Tài liệu tổng quan — NCS Đỗ Thùy Hương · GVHD: PGS.TS. Phan Anh Tú · VLUTE / Trường Đại học Cần Thơ.
> Cập nhật 2026-06-23. Mọi số liệu khớp `data_wbes/analysis/CANONICAL_NUMBERS.md`.

## 1.1 Tên đề tài và phạm vi

**Quốc tế hóa và hiệu quả hoạt động kinh doanh của các doanh nghiệp ở châu Á.**

Luận án nghiên cứu mối quan hệ giữa **mức độ quốc tế hóa** (internationalization, đo bằng cường độ xuất khẩu trên doanh thu — FSTS) và **hiệu quả hoạt động kinh doanh của doanh nghiệp** (firm performance, đo bằng năng suất lao động chuẩn hóa trong nội bộ nền–năm) trên một phạm vi rộng các nền kinh tế châu Á và Thái Bình Dương, với trọng tâm là **vai trò điều tiết của bối cảnh thể chế quốc gia**.

## 1.2 Hình thức luận án: luận án dạng tổng hợp (compilation/kappa)

Luận án được tổ chức theo dạng **tổng hợp** (compilation thesis): một bài luận tổng hợp xuyên suốt (kappa) tích hợp một chùm nghiên cứu thành phần độc lập nhưng cùng trả lời một bộ câu hỏi nghiên cứu chung. Cấu phần gồm:

| Cấu phần | Vai trò | Bối cảnh / ICRV |
|---|---|---|
| **P1** | Nghiên cứu nền tảng đa quốc gia (17 nền, N=40.633) | Cơ sở khung CDCM; "lá chắn số" |
| **P2** | DNVVN Trung Quốc | Bổ trợ tính bền thời gian (III) |
| **P3** | Việt Nam (3 đợt 2009/2015/2023) | Chế độ chuyển đổi (IV) |
| **P4** | Singapore | Biên trên thể chế mạnh (I) |
| **P5** | Trung Quốc 2012–2024 | Trung bình cao (III) |
| **P6** | **Phân tích tổng hợp ba tầng** (k=238, K=288) | Toàn cầu — xác lập trục thể chế |
| **P7** | **Nghiên cứu tổng hợp toàn mẫu 50 nền** | Toàn phổ ICRV (I–VI) |
| **P8** | Đảo nhỏ Thái Bình Dương (SIDS) | Biên dưới — FIP (VI) |
| **P9** | Ấn Độ (3 sóng 2014/2022/2025) | Điều kiện biên thời gian (IV) |
| **P10** | Nhật Bản 2025 (sóng WBES đầu tiên) | Biên trên (I) |
| **Chương sách** | Ấn Độ — tầng quản trị | Bằng chứng H4 (IV) |
| **Chuyên đề 1 (CĐ1)** | Tổng quan mô tả + phân tầng ICRV | Khung mô tả toàn dự án |
| **Chuyên đề 2 (CĐ2)** | Khung lý thuyết CDCM + thiết kế thực nghiệm | Khung phân tích |

P6 và P7 là **hai trụ cột tích hợp**: P6 xác lập (bằng phân tích tổng hợp các cỡ ảnh hưởng đã công bố) rằng quan hệ I–P là dương–nhỏ nhưng **dị biệt do thể chế**; P7 (bằng dữ liệu doanh nghiệp gốc) cho thấy **cấu trúc** của dị biệt đó.

## 1.3 Dữ liệu và khung phân tích (canonical)

- **Nguồn:** World Bank Enterprise Surveys (WBES) — vi dữ liệu doanh nghiệp; ba thế hệ bảng hỏi (PICS3 / Standardized / BREADY-BEE) được hài hòa hóa (xem Phụ lục A).
- **Khung phân tích canonical:** **88.869 doanh nghiệp trên 50 nền kinh tế** châu Á và Thái Bình Dương, **103 cặp nền–năm** (2003–2025, **bao gồm Nhật Bản 2025**).
- **Pool phân loại ICRV:** 96.415 doanh nghiệp / 52 nhãn nền (trước lọc, để gán nhóm thể chế).
- **Khung mô tả LP hợp lệ:** 84.998 DN / 50 nền / 107 cặp nền–năm (cơ sở Bảng 4.1/4.2).
- **Tái lập:** mọi headline đã được chạy lại từ vi dữ liệu thô `data_wbes/raw_dta/` bằng Python tương đương Stata (xem `reviews/REPLICATION_CROSSCHECK_2026-06-23.md` và `*/replication/REPRO_2026-06-23/estimates.csv`).

## 1.4 Khung lý thuyết: CDCM – ICRV – FIP

- **CDCM** (Country–Digital–Capability Moderation): khung điều tiết ba tầng — **bối cảnh quốc gia** (thể chế), **năng lực số/công nghệ** (DAI, TCI), và **đặc điểm nhà quản trị** — điều hòa quan hệ quốc tế hóa–hiệu quả. Bốn lý thuyết nền: Uppsala, RBV (quan điểm dựa trên nguồn lực), Institutional Theory, Upper Echelons Theory.
- **ICRV** (Institutional Context Regime Variation): phổ **sáu chế độ thể chế** đặc thù châu Á–Thái Bình Dương (I tiên tiến đổi mới → VI đảo nhỏ SIDS), thay cho phân loại nhị phân "phát triển/mới nổi".
- **FIP** (Forced Internationalization Penalty): khái niệm mới — **gánh nặng quốc tế hóa cưỡng bức** ở các nền đảo nhỏ, như **điều kiện biên cực trị** của họ đường cong chữ U ngược.
- **Hình thái ba vùng** (three-zone morphology): chữ U ngược **sắc nét** ở vùng giữa (chế độ chuyển đổi), **duỗi thẳng gần tuyến tính** ở biên trên (thể chế mạnh), **mất cấu trúc / đảo dấu** ở biên dưới (thể chế yếu, SIDS). Điểm uốn ước lượng theo Lind–Mehlum.

## 1.5 Câu hỏi nghiên cứu

- **RQ1 —** Quan hệ quốc tế hóa–hiệu quả có tồn tại một cách hệ thống không, và **bối cảnh thể chế** có điều tiết nó không? *(P6)*
- **RQ2 —** Dạng hàm của quan hệ này biểu hiện thế nào ở **từng chế độ thể chế đơn quốc gia** trải khắp phổ? *(P3, P4, P5, P2)*
- **RQ3 —** Khung CDCM có **khái quát hóa** trên toàn mẫu 50 nền không, và **năng lực số/công nghệ** (DAI/TCI) tác động qua cơ chế nào? *(P7, P8)*
- **RQ4 —** Phổ thể chế điều tiết **dạng hàm** (không chỉ độ lớn) ra sao, và đâu là các **điều kiện biên** (không gian SIDS, thời gian chuyển đổi, biên trên)? *(P7, P9, P10, chương sách)*

## 1.6 Tuyên bố lý thuyết trung tâm (thesis statement)

> **Mức độ quốc tế hóa cải thiện hiệu quả doanh nghiệp theo một dạng hàm, mà bản thân dạng hàm đó lại là một hàm của vị trí thể chế.** Độ dày "đệm thể chế" quyết định liệu quan hệ I–P là gần tuyến tính dương (biên trên), chữ U ngược sắc nét (chế độ chuyển đổi), hay mất cấu trúc và đảo dấu (biên dưới).

Tuyên bố này nâng luận điểm kinh điển "bối cảnh quan trọng" từ một nhận định định tính (thể chế điều tiết *độ lớn* hiệu ứng) lên một **mệnh đề định lượng kiểm định được** (thể chế điều tiết *dấu và dạng* hiệu ứng), và xác định tường minh điểm — chế độ SIDS — nơi cả họ lý thuyết chữ U ngược không còn ứng dụng.

## 1.7 Cấu trúc luận án (5 chương)

1. **Chương 1 — Giới thiệu:** bối cảnh, khoảng trống, câu hỏi, đóng góp dự kiến.
2. **Chương 2 — Tổng quan tài liệu:** quan hệ I–P, năm dạng hàm (tuyến tính, chữ U ngược, chữ S, chữ M, gánh nặng bắt buộc), các lý thuyết nền, khung CDCM.
3. **Chương 3 — Phương pháp:** đo lường DOI/hiệu quả, dữ liệu WBES, hài hòa hóa, mô hình bậc hai + FE hai chiều + sai số chuẩn theo cụm, kiểm định Lind–Mehlum.
4. **Chương 4 — Kết quả:** mô tả, tương quan, hồi quy toàn mẫu, phổ điểm uốn ICRV, các trường hợp biên (P8, P9, P10).
5. **Chương 5 — Kết luận và đề xuất:** bàn luận theo CDCM, so sánh với tài liệu, đóng góp lý thuyết, hàm ý chính sách/quản trị, hạn chế và hướng tương lai.

→ Quan hệ chi tiết giữa các nghiên cứu thành phần, chương và chuyên đề: xem **`02_truc_quan_hoa_quan_he.md`**.
