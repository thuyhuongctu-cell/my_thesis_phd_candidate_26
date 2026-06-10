# Phản biện KHOA HỌC (Devil's Advocate) + Chuẩn bị bảo vệ — câu hỏi khó & phản hồi

**Ngày:** 2026-06-10 · **Phạm vi:** tấn công vào *luận điểm khoa học* (không phải hình thức), kiểu reviewer Q1 / phản biện hội đồng. Mọi nghi vấn được **kiểm chứng bằng dữ liệu gốc** (`data_wbes/`, replication CSV) — pipeline Python đã tái tạo chính xác kết quả gốc của paper trước khi kết luận.

> Tài liệu này phục vụ **2 mục đích**: (1) bằng chứng tự-phản-biện khoa học; (2) bộ Q&A để NCS chuẩn bị bảo vệ hội đồng.

---

## I. CÁC TẤN CÔNG SUBSTANTIVE ĐÃ KIỂM CHỨNG

### SCI-2 (P8) — "Kết quả chủ đạo chỉ dựa trên 209/959 quan sát" → ✅ ĐÃ GIẢI QUYẾT (thêm robustness vào bài)
**Tấn công:** β = −1.339 (FE đầy đủ) chạy trên N=209 = 22% mẫu sau listwise deletion. Có thể là artifact của selection.
**Kiểm chứng dữ liệu:** 959→209 **gần như hoàn toàn** do biến `foreign_own_pct` (chỉ 22% non-missing); `ln_size`/`firm_age` ~100%. Mean FSTS của nhóm GIỮ vs BỎ = 0.046 vs 0.049 (không lệch theo biến trọng tâm).
**Robustness đã chạy & THÊM VÀO BÀI (§4.4):** bỏ biến foreign-ownership → **β=−0.835, p=.010, N=950**; không control → **β=−0.769, p=.015, N=959**.
**→ Phản hồi hội đồng:** *"FIP không phải artifact của mẫu 209. Trên toàn bộ 950–959 quan sát, hệ số vẫn âm và có ý nghĩa (p<.05). N=209 chỉ do thiếu dữ liệu sở hữu nước ngoài, một biến không liên quan đến FSTS."*

### SCI-3 (P8) — "Bỏ Comoros + Timor để đạt ý nghĩa (p-hacking)?" → ✅ ĐÃ GIẢI QUYẾT
**Tấn công:** 9 nước cho p=.068 (yếu); 7 nước cho p<.001. Việc loại 2 nước = chọn mẫu để có significance.
**Kiểm chứng dữ liệu (FE, control size, full N):** 9 nước (gồm Comoros+Timor): **β=−0.510, p=.008, N=1469**; 7 nước: **β=−0.834, p=.010**.
**→ Phản hồi:** *"FIP có ý nghĩa ở CẢ 9 nước (p=.008) lẫn 7 nước. Việc giới hạn về 7 đảo Thái Bình Dương dựa trên định nghĩa địa lý (loại Comoros-Ấn Độ Dương, Timor-ĐNÁ), làm MẠNH thêm chứ KHÔNG TẠO RA kết quả."* Đã thêm robustness 9-nước vào bài.

### SCI-1 (P9) — "'Tan rã ngưỡng' 2025 chỉ là do xuất khẩu sụp đổ (mất phương sai đuôi)?" → ⚠️ ĐÃ THÊM CAVEAT (phần còn lại là author judgment)
**Tấn công:** 2025 FSTS mean = 2.7% (từ 7.2%), exporter 7% (từ 15.6%), DN có FSTS>50% chỉ còn **141** (từ 536). Độ cong bậc hai 2025 mất ý nghĩa có thể vì **thiếu biến thiên ở đuôi xuất khẩu cao**, không phải vì quan hệ thay đổi cấu trúc.
**Kiểm chứng:** xác nhận đúng — biến thiên đuôi 2025 co lại mạnh.
**Đã thêm caveat vào §6 (4 file):** thừa nhận phát hiện "conditional on the post-Atmanirbhar export contraction".
**→ Phản hồi (có cơ sở bác một phần):** *"Tuy đuôi mỏng đi, DẤU của độ dốc FSTS thấp đảo chiều — dương (sườn lên) năm 2014 → âm đơn điệu 2025. Mất phương sai đuôi chỉ làm độ cong khó ước lượng, KHÔNG tạo ra đảo dấu ở vùng FSTS thấp (nơi có nhiều quan sát)."* Linear 2025 = −0.359, p=.019 (có ý nghĩa). **Khuyến nghị NCS:** nhấn mạnh sign-reversal này khi bảo vệ.

### SCI-4 (P6) — "Ý nghĩa ICRV chỉ do ô Frontier k=3 (1 nghiên cứu outlier)" → ⚠️ HẠN CHẾ ĐÃ KHAI BÁO (cần coder thứ 2 để củng cố)
**Tấn công:** ICRV Q_M=17.35, p=.002 nhưng Frontier r̄=0.349 (k=3, do Pouresmaeili et al. 2018 chi phối). Bỏ ô này có thể làm mất ý nghĩa.
**Trạng thái:** bài ĐÃ tự khai báo (audit B2: "ICRV result driven by k=3 Frontier cell"). Không thể chạy lại rma.mv (metafor không có trong môi trường).
**→ Phản hồi:** *"Chúng tôi trình bày kết quả ICRV như 'informative bounds', không phải bằng chứng xác nhận; phát hiện chính của P6 là PUBLICATION BIAS (r 0.074→0.035), không phải ICRV. Frontier là exploratory với k nhỏ đã nêu rõ."* **Việc NCS nên làm:** chạy leave-one-out bỏ Pouresmaeili + báo cáo Q_M có/không Frontier.

---

## II. CÂU HỎI HỘI ĐỒNG KINH ĐIỂN (luận án kết hợp công trình)

| # | Câu hỏi khó | Phản hồi đề xuất |
|---|---|---|
| Q1 | *"9 bài là 9 mảnh rời rạc hay 1 luận án thống nhất?"* | Khung xuyên suốt: **CDCM** (điều tiết năng lực số theo ngữ cảnh) + **ICRV** (5 chế độ thể chế) + **FIP** (biên SIDS). P3–P5 là 3 điểm trên phổ thể chế (chuyển đổi/upper-middle/tiên tiến); P6 tổng hợp; P7 capstone 49 nền KT; P8 biên dưới (SIDS); P9 biên động (Ấn Độ chuyển đổi). |
| Q2 | *"Trùng lặp với 2 chuyên đề có phải tự đạo văn?"* | Không — Lời cam đoan + Quyết định giao chuyên đề ĐHCT xác lập luận án **phát triển từ chính 2 chuyên đề của NCS**; trùng là hợp lệ, đã khai báo (Đ.2.3). |
| Q3 | *"Đóng góp MỚI thực sự là gì?"* | (i) **FIP** — khái niệm mới: I–P đơn điệu âm khi 3 tiền đề cấu trúc đồng thời vắng; (ii) **threshold dissolution** (P9) — bằng chứng longitudinal đầu tiên ngưỡng *tan rã* chứ không chỉ dịch chuyển; (iii) **public/private digital complement** (UPI Tier-2 âm); (iv) **publication bias** làm đôi hiệu ứng I–P (P6). |
| Q4 | *"Dùng AI thì sao?"* | Khai báo M-AIDA (hỗ trợ trích xuất, PI kiểm chứng 100%) trong P6; luận án có Lời cam đoan theo chuẩn ĐHCT; chuyên đề không khai báo AI (đúng quy định). Mã M-AIDA công khai trên GitHub (chứng minh năng lực lập trình). |
| Q5 | *"Tại sao OLS không phải panel/IV (nhân quả)?"* | Đã khai báo: WBES ẩn danh → cross-section lặp, không match panel được. Kết quả diễn giải **associational**, không nhân quả; đã đề xuất IV (PMJDY cho UPI) cho nghiên cứu sau. |
| Q6 | *"P1/P2 đã đăng ở tạp chí Việt Nam — chất lượng?"* | P1/P2 là công bố nền (VEFR, JFAR); 7 bài thành phần P3–P9 nhắm Q1–Q2 quốc tế (MIR, JWB, IBR, World Development…). |

---

## III. TÓM TẮT HÀNH ĐỘNG

**Đã làm trong vòng này (data-verified, thêm vào bài):**
- P8: 2 robustness mới (full-sample N=950; 9-nước) → giải quyết 2 lỗ hổng nghiêm trọng nhất.
- P9: caveat về co rút biến thiên xuất khẩu 2025.

**NCS nên làm thêm (củng cố, không bắt buộc trước nộp):**
1. P6: leave-one-out bỏ Pouresmaeili → kiểm ICRV Q_M.
2. P9: (tùy chọn) trim-tail robustness 2025 hoặc nhấn sign-reversal khi bảo vệ.
3. Toàn bộ: chuẩn bị trả lời Q1–Q6 ở §II.

**Đánh giá khoa học tổng thể:** sau vòng này, 2/4 tấn công nặng nhất (P8) đã được **bác bằng robustness từ chính dữ liệu**; 2 còn lại (P9 đuôi xuất khẩu, P6 Frontier) đã có caveat trung thực + đường phản hồi. Các paper **vững hơn đáng kể về mặt phòng thủ khoa học**, không chỉ sạch về hình thức.
