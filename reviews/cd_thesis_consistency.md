# Đối chiếu Chuyên đề 1/2 với luận án (Task 3)

> Rà soát 16/06/2026. Mục tiêu: nhất quán số liệu và thuật ngữ giữa hai chuyên đề tiến sĩ (CĐ1, CĐ2) và luận án. Nguyên tắc: không bịa; chỉ sửa khi đối chiếu được với nguồn gốc.

## 1. Số liệu trụ cột — NHẤT QUÁN ✅
Cả CĐ1 và CĐ2 dùng đúng bộ số đã khóa của luận án, không có số cũ/sai:
- Khung: 96.415 (phân loại) · 88.869 (phân tích) · 50 nền · 81.022 (P7 M2).
- P6: k = 238 · r̄ = 0,074 · I² = 62,4% · Q_M = 17,35.
- P7: điểm uốn 43,6%. P8/FIP: β = −1,339.
- P5 Trung Quốc: 49,4% (2012), 47,2% (2024) — khớp manuscript P5.
- P3 Việt Nam: 46,2/39,3/41,6/39,7% — khớp luận án.
- Không xuất hiện số cũ (101.185, 36%, ...).

## 2. MỘT MÂU THUẪN THẬT đã phát hiện và SỬA ⚠️→✅
**CĐ2 mô tả sai P2 (Trung Quốc SMEs, JFAR đã công bố):**

| Mục | CĐ2 (trước sửa) | Bài JFAR đã công bố + luận án (đúng) |
|---|---|---|
| Dạng hàm | "Bậc ba / cubic (S-curve ba giai đoạn)" | **Chữ U ngược bậc hai** |
| Điểm uốn | "Hai điểm uốn (cubic)" | **Một điểm uốn 47,8% FSTS** |
| Cỡ mẫu | "2.700 doanh nghiệp" | **4.290 quan sát doanh nghiệp–năm** |

- **Xác minh từ bản gốc** `p2/p2_jfar_china_smes.pdf`: mô hình là `Productivity = β0 + β1·FSTS + β2·FSTS²` (bậc hai); abstract ghi "inverted-U"; β1 = 1.704; điểm uốn = −β1/(2β2) = 47,8%; "sample consists of 4,290 firm-year observations". **Không hề có** "cubic/S-curve/three-stage/two turning points".
- Mô tả cubic trong CĐ2 mâu thuẫn với **chính bài báo đã công bố của NCS** và với luận án (§4.4.8, §2.3.3, Bảng 4.10).
- **Đã sửa CĐ2** (4 chỗ: đoạn văn §2.1, bảng tổng quan, hai dòng bảng so sánh P2–P5) về bậc hai/47,8%/4.290 cho khớp bài gốc + luận án. Đây là **sửa lỗi**, không phải thay đổi nội dung khoa học theo ý chủ quan.

> Lưu ý cho NCS: vì CĐ2 là chuyên đề đã thực hiện trong chương trình, đề nghị chị xác nhận lại bản nộp chính thức của CĐ2 cũng được hiệu chỉnh tương ứng (nếu bản nộp vẫn ghi cubic thì cần đính chính để thống nhất với bài JFAR đã công bố).

## 3. Các điểm KHÔNG phải lỗi (đã kiểm ngữ cảnh)
- CĐ2 còn nhắc "S-curve ba giai đoạn"/"hai điểm uốn" ở phần **tổng quan năm dạng hàm** (Lu & Beamish 2004; Riahi-Belkaoui M-curve) và ở **thủ tục so sánh mô hình** (kiểm định β₃, so AIC/BIC bậc hai vs bậc ba) — đây là thảo luận văn liệu và kiểm định độ vững hợp lệ, **không gán cubic cho P2**.
- CĐ1: so sánh "tuyến tính/bậc hai/bậc ba" bằng AIC/BIC là model-selection hợp lệ; gradient "đơn điệu từ +0,139" là **tương quan** (không phải mức năng suất thô — không dính artifact tiền tệ).

## 4. Khuyến nghị còn lại (tùy chọn, không bắt buộc)
- Nhãn chế độ ICRV tiếng Anh (Advanced innovation/resource, Upper-mid, Lower-mid, Emerging, Frontier) và vài thuật ngữ ("under review", "pattern") còn xuất hiện trong CĐ1/CĐ2 ở các bảng chú giải. Vì hai chuyên đề là tài liệu riêng (có thể đã bảo vệ), tôi **không tự đổi** thuật ngữ ngoài lỗi số liệu; nếu chị muốn đồng bộ hoàn toàn với chuẩn tiếng Việt của luận án, tôi có thể làm trong một lượt riêng.
