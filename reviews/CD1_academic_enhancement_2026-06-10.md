# CĐ1 — Đánh giá chất lượng học thuật & đề xuất bổ sung nội dung

**Chuyên đề:** "Thực trạng về hiệu quả hoạt động kinh doanh của các doanh nghiệp ở Châu Á" (Firm Performance landscape) · 2026-06-10
**Câu hỏi:** đã hợp lý chưa & cần bổ sung gì để nâng chất lượng học thuật.

---

## A. KẾT LUẬN TỔNG QUAN — ĐÃ HỢP LÝ 

CĐ1 **vững và đủ tầm chuyên đề tiến sĩ** về mặt thiết kế descriptive-diagnostic:
- **Lý luận mạnh:** 5 meta-analysis (Bausch&Krist, Kirca, Marano, Schwens, Wu) + 3 lý thuyết nền (RBV, Institutional, Uppsala) + điều kiện biên U-curve + khung 4-tầng số + CDCM.
- **Đa chiều:** 4 chiều hiệu quả (LP, lợi nhuận, tăng trưởng, đổi mới) × 6 regime ICRV × 7 tiểu cảnh điển hình.
- **Quy mô:** 18 bảng, 14 hình, ~96–101k DN — rộng nhất khu vực.
- **Minh bạch:** 7 giới hạn nêu rõ; ghi chú đo lường (winsorize, FSTS construction); đã bàn weights/missing.
- **Đóng góp định hướng:** phân nhóm con Advanced; FIP ở SIDS — nối chặt sang CĐ2/luận án.

 đến **Không có lỗi cấu trúc/khoa học chặn.** Các điểm dưới là **nâng cấp** (enhancement), không phải sửa lỗi.

---

## B. 🔝 BỔ SUNG ƯU TIÊN CAO — nâng từ "mô tả tốt" lên "publication-grade"

### B1. Thêm **kiểm định suy diễn** cho khác biệt giữa regime (hiện chỉ mô tả mean/sd)
CĐ1 khẳng định "phân tán năng suất tăng đơn điệu theo regime" và nhiều so sánh nhóm, nhưng **chỉ bằng mean/sd**, chưa có test. Bổ sung:
- **Kruskal–Wallis** (hoặc ANOVA + Welch) cho LP/FSTS/website/FDI **xuyên 6 regime** + **post-hoc Dunn/Games-Howell** đến khẳng định khác biệt có ý nghĩa.
- **Khoảng tin cậy 95%** cho mỗi ước lượng nhóm (bootstrap cho nhóm nhỏ SIDS).
> *Hội đồng/reviewer Scopus sẽ hỏi: "khác biệt regime có significant không?" — hiện chưa trả lời được.*

### B2. **Vận hành hóa luận điểm "phân bổ sai nguồn lực"** (Hsieh–Klenow được trích nhưng chưa đo)
CĐ1 dẫn Hsieh & Klenow (2009, 2014) làm khung cho "phân tán năng suất = misallocation", nhưng **chưa phân rã**. Bổ sung:
- **Phân rã phương sai Theil/MLD** năng suất: **within-regime vs between-regime** (và within vs between country) đến định lượng bao nhiêu % dị biệt là do thể chế (between) so với nội bộ (within).
- Có thể thêm **Gini** năng suất theo regime.
> Biến phương sai năng suất từ "mô tả" thành "bằng chứng misallocation có cấu trúc" — đóng góp thực chất.

### B3. Thêm **Bảng 1 thống kê mô tả toàn mẫu** + **ma trận tương quan đầy đủ** (chuẩn empirical paper)
- **Bảng 1 chuẩn:** mean/median/sd/min/max/N cho **tất cả** biến chính (LP, FSTS, exporter, website, FDI, TCI components, firm size, age) — toàn mẫu + có thể theo regime. *(Hiện số liệu rải rác nhiều bảng nhỏ, thiếu 1 bảng tổng.)*
- **Ma trận tương quan** giữa **tất cả** biến (hiện chỉ có Pearson I–P theo regime ở Bảng 2.3.8.1) đến kiểm tra đa cộng + pattern liên biến.

### B4. Đào sâu **khái niệm "firm performance"** (hiện hơi mỏng)
Phần đo lường hiệu quả chỉ dựa Venkatraman & Ramanujam (1986). Bổ sung **tranh luận đo lường đa chiều**:
- **Combs, Crook & Shook (2005)** — thao tác hóa hiệu quả tổ chức; **Richard, Devinney, Yip & Johnson (2009)** — đo lường hiệu quả doanh nghiệp (đa nguồn, subjective vs objective).
- Biện minh vì sao chọn **năng suất lao động** làm thước đo chính giữa các lựa chọn (ROA/ROS/Tobin's Q) — điểm mạnh/yếu.
> *(Đây cũng là 2 reference mà review luận án 06-07 đánh dấu thiếu — bổ sung 1 công đôi việc.)*

---

## C. 🟡 BỔ SUNG NÊN CÓ — tăng độ tin cậy & external validity

### C1. **Kiểm chứng ngoài (benchmarking)** số liệu WBES
So sánh năng suất/FSTS từ WBES với **nguồn vĩ mô độc lập** (national accounts, ADB Productivity, OECD, WB WDI) cho vài nước đến xác nhận bức tranh WBES không lệch hệ thống.

### C2. **So sánh khung ICRV với phân loại sẵn có**
Đối chiếu 6 nhóm ICRV với **WB income groups / WGI clusters / Varieties of Capitalism (Hall & Soskice)** đến chứng minh ICRV **không trùng lặp**, có giá trị phân biệt (đã có nguyên tắc "tính phân biệt" Mục 2.3.2.1 nhưng chưa kiểm định thực nghiệm).

### C3. **Phân rã thành phần ngành (shift-share)**
Khác biệt năng suất giữa regime có phải do **cơ cấu ngành** (sector mix) hay **năng suất trong ngành**? Thêm shift-share / sector-fixed comparison đến loại trừ "regime difference chỉ là sector composition".

### C4. **Tiểu-panel cân bằng cho phân tích thời gian**
Các bảng "Δ 2018-2025 vs 2009-2012" là **so sánh cohort chéo**, không panel. Bổ sung **tập con nước có ≥2 sóng** (FJI/PNG/VUT, VN, China…) + quỹ đạo within-economy đến củng cố claim "nhảy vọt số" (hiện chỉ Mongolia có).

### C5. **Minh họa trực quan mạnh hơn** (giá trị cốt lõi của landscape paper)
- **Bản đồ 49 nước** tô màu theo regime ICRV.
- **Scatter FSTS × ln(LP)** toàn mẫu, tô màu regime + **LOWESS theo regime** đến trực quan hóa I–P phi tuyến (đang mô tả bằng lời).
- **Heatmap 4 chiều hiệu quả × 6 regime** (z-score) đến 1 hình tóm tắt toàn bộ.

---

## D. 🟢 TINH CHỈNH NHỎ
- Schema-break BREADY 2025: hệ thống phòng thủ 3 tầng **đề xuất** nhưng chưa **trình diễn** — thêm 1 bảng before/after cho chỉ số bị ảnh hưởng (Ấn Độ FSTS 7,7 đến 2,7%) để minh chứng.
- Bối cảnh 2026 (xung đột Trung Đông, thuế quan Mỹ) ở Mục 2.1: nêu rõ **chưa nằm trong data 2025** (caveat thời điểm).
- Chuyển Mục 2.3.9.2 (5 khoảng trống) thành **bảng "khoảng trống đến câu hỏi nghiên cứu CĐ2"** chính thức đến nối logic sang CĐ2 mạch lạc hơn.

---

## E. LƯU Ý THỰC THI
Nhiều mục B1–B3, C1–C5 **cần chạy lại trên dữ liệu** (Kruskal/Theil/Table 1/correlation/scatter). Phần lớn biến có trong master `.dta` (LP, FSTS, website, FDI, exporter, TCI) đến **tôi tính được khi re-lock** (cùng lúc có 43 raw `.dta` để khớp pipeline CĐ1). Riêng:
- B4 (Combs/Richard) + C2 (so sánh taxonomy) + D (caveat) = **văn bản thuần, làm được ngay** không cần data.
- B1/B2/B3/C1/C3/C4/C5 = cần data (chờ 43 `.dta` hoặc dùng master `.dta` cho các biến sẵn có, chấp nhận thiếu R&D/đổi mới).

**Khuyến nghị thứ tự:** B4 + D (ngay) đến B1/B2/B3 (khi có data) đến C (publication round).
