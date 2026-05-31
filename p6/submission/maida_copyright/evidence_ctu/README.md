# Evidence — 3 Quyết định CTU (OCR Markdown)

**Mục đích:** Bản OCR Markdown của 3 quyết định gốc của Trường Đại học Cần Thơ liên quan đến NCS Đỗ Thùy Hương (P1323001), dùng làm **bằng chứng pháp lý** đi kèm hồ sơ đăng ký quyền tác giả M-AIDA tại Cục Bản quyền Tác giả Việt Nam.

**Cơ sở pháp lý:** Điều 27.1 Luật SHTT 2005 (sửa đổi 2022) — "Tác giả là chủ sở hữu quyền tác giả đối với tác phẩm do mình tự sáng tạo bằng thời gian, tài chính và cơ sở vật chất - kỹ thuật của mình".

**Quy trình tạo:**
1. PDF gốc upload bởi NCS (định dạng scan ảnh)
2. OCR bằng `tesseract-ocr` 5.3 với mô hình tiếng Việt (`vie+eng`)
3. Render PDF → ảnh 300 DPI bằng `pdf2image` + `poppler-utils`
4. Output Markdown UTF-8 (1 file/quyết định)

⚠️ **Bản OCR có thể có sai sót ký tự tiếng Việt** (đặc biệt dấu thanh). PDF gốc luôn là *nguồn chính thức* khi nộp Cục BQTG. File `.md` này dùng để:
- Trích dẫn nội dung quyết định trong các tài liệu hồ sơ
- Search nhanh các điều khoản khi cần check
- Lưu trong repository để các tài liệu kế thừa có thể reference

## Danh mục

| # | File | Số | Ngày | Nội dung |
|---|---|---|---|---|
| 1 | `3010_qd_cong_nhan_ncs.md` | **3010/QĐ-ĐHCT** | 23/6/2023 | Công nhận NCS Khóa 2023.1, giao luận án tiến sĩ, phân công người hướng dẫn |
| 2 | `4768_qd_giao_chuyen_de.md` | **4768/QĐ-ĐHCT** | 15/10/2024 | Giao Chuyên đề 1, Chuyên đề 2, và Tiểu luận tổng quan tiến sĩ |
| 3 | `4769_qd_dieu_chinh_ten_lats.md` | **4769/QĐ-ĐHCT** | 15/10/2024 | Điều chỉnh tên luận án tiến sĩ (ASEAN → Châu Á) |

## Các điểm quan trọng đã verify từ OCR

### Từ QĐ 3010 (Công nhận NCS):
- ✅ NCS: **Đỗ Thùy Hương**, Mã NCS **P1323001**, ngành **Quản trị kinh doanh** (mã 9340101)
- ✅ Thời gian đào tạo: **10/2023 → 10/2026** (chính thức), tối đa **10/2029**
- ✅ Người hướng dẫn: **PGS.TS. Phan Anh Tú**, Trường Đại học Cần Thơ
- ✅ Tên luận án ban đầu: *"Quốc tế hóa và hiệu quả hoạt động kinh doanh của các doanh nghiệp tại các nước thuộc khối ASEAN"*
- ⚠️ Điều khoản tài chính: **"NCS đóng học phí chậm tiến độ"** (NCS đóng học phí, KHÔNG nhận học bổng từ CTU) — bằng chứng quan trọng cho Điều 27.1
- ❌ **KHÔNG có** điều khoản về sở hữu trí tuệ (IP)
- ❌ **KHÔNG có** điều khoản giao nhiệm vụ phát triển phần mềm

### Từ QĐ 4768 (Giao chuyên đề):
- ✅ Tên CĐ1: *"Thực trạng về hiệu quả hoạt động kinh doanh của các doanh nghiệp ở Châu Á"* — HD: TS. Nguyễn Minh Cảnh
- ✅ Tên CĐ2: *"Xây dựng mô hình nghiên cứu về ảnh hưởng của quốc tế hóa đến hiệu quả hoạt động kinh doanh của các doanh nghiệp ở Châu Á"* — HD: PGS.TS. Phan Anh Tú
- ✅ Tên TLTQ: *"Tổng quan tài liệu về ảnh hưởng của quốc tế hóa đến hiệu quả hoạt động kinh doanh của các doanh nghiệp"* — HD: PGS.TS. Phan Anh Tú
- ❌ **KHÔNG có** điều khoản giao nhiệm vụ phát triển phần mềm M-AIDA hay bất kỳ phần mềm nào

### Từ QĐ 4769 (Điều chỉnh tên luận án):
- ✅ Tên LATS cũ: *"...các doanh nghiệp tại các nước thuộc khối ASEAN"*
- ✅ Tên LATS mới: *"...các doanh nghiệp ở Châu Á"*
- ✅ Lý do: theo kết luận của hội đồng đánh giá đề cương chi tiết
- ❌ **KHÔNG có** điều khoản về IP

## Kết luận pháp lý

3 quyết định trên xác lập quan hệ **đào tạo NCS** giữa NCS Đỗ Thùy Hương và Trường Đại học Cần Thơ:
- NCS đóng học phí cho CTU
- CTU giao đề tài học thuật (luận án, CĐ, TLTQ) làm sản phẩm đào tạo
- CTU **không** giao nhiệm vụ sáng tạo phần mềm cụ thể
- CTU **không** cấp kinh phí phát triển M-AIDA
- CTU **không** có điều khoản claim ownership trên sản phẩm trí tuệ của NCS

→ **Điều 27.2 Luật SHTT (tổ chức là chủ sở hữu)** KHÔNG áp dụng.
→ Cùng với cam đoan NCS về nguồn lực cá nhân (file `06_cam_doan_nguon_luc_ca_nhan.md`), **Điều 27.1 (tác giả là chủ sở hữu)** áp dụng.
→ NCS (và supervisor nếu có đóng góp code) là chủ sở hữu hợp pháp của M-AIDA.

---

*Tài liệu này tạo 2026-05-31 bằng quy trình OCR (markitdown + tesseract vie+eng) sau khi NCS cung cấp 3 PDF gốc. Bản gốc PDF luôn là nguồn chính thức khi nộp hồ sơ Cục BQTG.*
