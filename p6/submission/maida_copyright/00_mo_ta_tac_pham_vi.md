# MÔ TẢ TÁC PHẨM — M-AIDA
# (Description of Work — Đăng ký bản quyền phần mềm máy tính, Cục Bản quyền Tác giả Việt Nam)

> Phiên bản tài liệu: 2.0 (chuẩn học thuật, 2026-05-27). Tài liệu mô tả phần mềm **M-AIDA** phục vụ
> đăng ký quyền tác giả đối với chương trình máy tính, đồng thời định vị M-AIDA như một **đóng góp
> phương pháp/hạ tầng nghiên cứu** của luận án tiến sĩ. *Lưu ý phạm vi:* M-AIDA là công cụ hỗ trợ
> quy trình trích xuất; **mọi số liệu đưa vào phân tích tổng hợp đều qua xác nhận của con người
> (Principal Investigator)**. Bài báo phân tích tổng hợp (P6) báo cáo quy trình trích xuất có kiểm
> chứng của con người và không phụ thuộc vào tính tự động của phần mềm.

---

## 1. TÊN TÁC PHẨM

**M-AIDA** — *Meta-Analysis Intelligent Data Assistant* (Trợ lý dữ liệu thông minh cho phân tích
tổng hợp), chuyên biệt cho quan hệ Quốc tế hóa – Hiệu quả doanh nghiệp (Internationalization–
Performance, I–P). Phiên bản: **7.0.0**.

## 2. LOẠI TÁC PHẨM
Chương trình máy tính (Computer Program / Research Software).

## 3. TÁC GIẢ / CHỦ SỞ HỮU
Phần mềm do **Đỗ Thị Thúy Hương** và **Phan Anh Tú** (Trường Kinh tế, Trường Đại học Cần Thơ) tự
nghiên cứu và xây dựng. Tại thời điểm đăng ký, M-AIDA **chưa có sản phẩm tương đương trên thị
trường** trong phạm vi công cụ trích xuất dữ liệu chuyên biệt cho phân tích tổng hợp lĩnh vực kinh
doanh quốc tế.

*(Thông tin cá nhân để hoàn tất đơn COV — tác giả điền: họ tên đầy đủ, ngày sinh, địa chỉ thường
trú, số CCCD, điện thoại, email; quốc tịch Việt Nam.)*

---

## 4. CƠ SỞ HỌC THUẬT VÀ ĐỘNG CƠ XÂY DỰNG (Statement of Need)

### 4.1. Bài toán phương pháp
Phân tích tổng hợp (meta-analysis) trong kinh doanh quốc tế đòi hỏi **trích xuất cỡ ảnh hưởng
(effect size)** từ hàng trăm nghiên cứu sơ cấp dị biệt: hệ số tương quan Pearson *r*, hệ số hồi quy
chuẩn hóa *β*, thống kê *t*, *F*, giá trị *p*, khoảng tin cậy — kèm cỡ mẫu *N* và các biến điều
tiết. Thao tác này khi làm thủ công vừa **chậm và lặp lại**, vừa **dễ sai sót** khi quy đổi giữa các
dạng thống kê và khi mã hóa biến điều tiết theo một khung phân loại nhất quán. Đây là nút thắt năng
suất kinh điển của tổng quan hệ thống: đánh đổi giữa **thông lượng trích xuất** và **độ chính xác**.

### 4.2. Tri thức nền làm cơ sở thiết kế (knowledge-driven design)
M-AIDA **không phải phần mềm trích xuất tổng quát**, mà là kết tinh tri thức phương pháp luận của
tác giả về phân tích tổng hợp trong kinh doanh quốc tế. Cụ thể, các quy tắc nghiệp vụ được **mã hóa
trực tiếp từ chuẩn học thuật**:
- **Thứ tự ưu tiên thống kê** và **công thức quy đổi về *r***: trực tiếp *r* → từ *t* → từ *F* → từ
  *β*, theo Borenstein et al. (2009) và Peterson & Brown (2005) (`r = √(t²/(t²+df))`; `r ≈ β` với
  hiệu chỉnh khi |β| nhỏ). Mỗi đường quy đổi gắn một **mức độ tin cậy** giảm dần.
- **Khung biến điều tiết đặc thù của luận án**: chế độ thể chế ICRV, chỉ số áp dụng số quốc gia
  cDAI, pha Vòng đời Nghịch lý Số DPL (Precede/Span/Follow) — các kiến tạo (construct) do chính tác
  giả phát triển trong khung lý thuyết của luận án.
- **Chuẩn báo cáo**: tuân thủ tinh thần PRISMA 2020 và MARS (Meta-Analysis Reporting Standards), với
  trường dữ liệu xuất ra khớp ma trận dữ liệu của luận án.

Nói cách khác, **giá trị cốt lõi của M-AIDA nằm ở tri thức chuyên ngành được hệ thống hóa**, không
chỉ ở phần lập trình. Chính vì dựa trên hiểu biết sâu về meta-analysis trong international business
mà tác giả mới có thể đặc tả được system prompt, thang tin cậy, và lược đồ biến điều tiết đúng chuẩn.

---

## 5. NGUYÊN LÝ CỐT LÕI — CON NGƯỜI TRONG VÒNG LẶP (Human-in-the-Loop)

M-AIDA được thiết kế trên một nguyên lý phương pháp luận **bất biến**:

> **Tự động hóa để giảm THỜI GIAN; con người để bảo đảm TÍNH HỢP LỆ.**

- Mô hình ngôn ngữ lớn (LLM) chỉ tạo ra **bản nháp trích xuất** kèm điểm tin cậy
  (`extraction_confidence`); bản nháp **không bao giờ** tự động đi vào tập dữ liệu phân tích.
- Bản ghi có `confidence < 0.7` tự động bị gắn cờ `requires_verification`.
- **Principal Investigator (PI)** bắt buộc rà soát, có quyền **ghi đè (override)** bất kỳ trường nào,
  ghi chú lý do, rồi mới **phê duyệt**.
- Chỉ bản ghi đã phê duyệt mới được **khóa vĩnh viễn (irreversible lock)** kèm dấu thời gian UTC,
  tạo **vết kiểm toán (audit trail)** phục vụ minh bạch và tái lập.
- Chỉ các bản ghi đã khóa mới được xuất ra CSV để đưa vào phân tích.

Cơ chế hai bước **phê duyệt → khóa** là **đặc trưng phân biệt M-AIDA với mọi công cụ trích xuất tự
động thuần túy**: nó hiện thực hóa chuẩn mực sử dụng AI có trách nhiệm trong nghiên cứu — AI tăng
tốc, nhưng **con người chịu trách nhiệm cuối cùng** về từng số liệu. Đây cũng là lý do dữ liệu do
quy trình M-AIDA sinh ra đủ tin cậy cho nghiên cứu bình duyệt.

---

## 6. KIẾN TRÚC PHẦN MỀM

M-AIDA v7.0 là **ứng dụng web một tệp (single-file), chạy hoàn toàn phía trình duyệt
(client-side), không yêu cầu máy chủ, cơ sở dữ liệu ngoài hay khóa API**. Toàn bộ giao diện và
logic xử lý nằm trong một tệp `MAIDA_intake.html` (HTML5 + JavaScript ES2017+), kèm thư viện
PDF.js nạp từ CDN để đọc tệp PDF. Lựa chọn kiến trúc này nhằm tối đa hóa tính khả chuyển, khả
năng tái lập và bảo mật dữ liệu (mọi dữ liệu lưu cục bộ trên trình duyệt, không truyền ra ngoài).

Bốn lớp chức năng trong cùng một tệp:
- **Lớp giao diện (Frontend):** bảng điều khiển học thuật ba khối — (01) Nạp tài liệu, (02) Ứng
  viên trích xuất, (03) Dataset đã kiểm chứng — dựng thuần HTML/CSS, không framework.
- **Lớp trích xuất (Extraction Engine):** hai chế độ — (i) `ruleExtract` theo biểu thức chính
  quy (regular expression), chạy ngoại tuyến hoàn toàn; (ii) `aiExtract` dùng mô hình ngôn ngữ
  lớn Claude qua API artifact `window.claude.complete` (trong môi trường claude.ai, không cần
  khóa API); ngoài môi trường đó hệ thống tự chuyển về chế độ quy tắc.
- **Lớp đọc tài liệu (PDF.js):** hàm `readPdf` rút văn bản trực tiếp từ PDF phi cấu trúc, ngay
  trên trình duyệt.
- **Lớp kiểm chứng & lưu trữ:** `renderCands`, `accept`, `renderDS`, `persist`, `loadStore` —
  hiện thực quy trình human-in-the-loop; dữ liệu đã khóa lưu cục bộ (`window.storage` hoặc bộ
  nhớ phiên), kết xuất CSV/JSON bằng `exportCSV` và trình tải JSON.

---

## 7. CHỨC NĂNG CHI TIẾT (ánh xạ theo quy trình phân tích tổng hợp)

| Bước phân tích tổng hợp | Hàm/khối M-AIDA | Khối giao diện |
|---|---|---|
| Nạp PDF/văn bản + siêu dữ liệu | `readPdf` (PDF.js), ô nhập tác giả/năm/quốc gia | 01 · Nạp tài liệu |
| Trích cỡ ảnh hưởng từ toàn văn | `aiExtract` (Claude) / `ruleExtract` (offline) + quy đổi về *r* | 02 · Ứng viên trích xuất |
| **Xác nhận của con người (PI)** | `renderCands` + `accept` (hiệu chỉnh trường, kiểm chứng từng mục) | 02 → 03 |
| **Khóa toàn vẹn** | `accept` ghi bản ghi trạng thái `LOCK` kèm dấu thời gian (audit trail) | 03 · Dataset đã kiểm chứng |
| Xuất dữ liệu chuẩn ma trận | `exportCSV` / trình tải JSON (chỉ bản ghi đã kiểm chứng) | 03 · nút Kết xuất |

Trường xuất chuẩn (CSV): `study_id, effect_id, author, year, country, r, n, fisher_z, measure,
moderator, p, source`. Cấu trúc này tương thích với phần mềm phân tích tổng hợp tiêu chuẩn
(metafor, CMA) và khớp ma trận dữ liệu của luận án.

---

## 8. TÍNH NGUYÊN GỐC VÀ SÁNG TẠO

1. **Phần mềm trích xuất chuyên ngành đầu tiên cho phân tích tổng hợp I–P tại Việt Nam**, mã hóa
   tri thức phương pháp meta-analysis vào pipeline tự động (không có trên thị trường).
2. **Thang tin cậy trích xuất 3 mức** gắn trực tiếp với chuẩn quy đổi Peterson & Brown (2005).
3. **Quy trình PI verify → irreversible lock** với audit trail — phân biệt rõ "bản nháp của máy" và
   "quyết định của nhà nghiên cứu", phù hợp luận án và nghiên cứu bình duyệt.
4. **Lược đồ biến điều tiết độc quyền của luận án** (ICRV / cDAI / DPL) tích hợp sẵn.
5. **Kiến trúc một-tệp client-side** không máy chủ: khả chuyển, tái lập và bảo mật cao (dữ liệu
   không rời trình duyệt), phù hợp nộp kèm hồ sơ bản quyền dưới dạng một bản sao mã nguồn tự chứa.

## 9. CÔNG NGHỆ SỬ DỤNG
Một tệp `MAIDA_intake.html`: HTML5, JavaScript (ES2017+), CSS thuần (không framework); thư viện
**PDF.js 3.11** (đọc PDF) nạp từ CDN; trích xuất AI dùng **Claude** qua API artifact
`window.claude.complete` (model do môi trường claude.ai cung cấp, không nhúng khóa API trong mã
nguồn). Không sử dụng máy chủ, cơ sở dữ liệu ngoài, hay bước biên dịch; chạy trực tiếp trên mọi
trình duyệt hiện đại.

## 10. ĐỐI TƯỢNG NGƯỜI DÙNG
Nghiên cứu sinh, giảng viên, nhóm nghiên cứu thực hiện tổng quan hệ thống và phân tích tổng hợp
trong kinh doanh quốc tế, chiến lược, quản trị — những người cần một quy trình trích xuất **vừa
nhanh vừa có kiểm chứng của con người**.

## 11. QUAN HỆ VỚI LUẬN ÁN (định vị trung thực)
M-AIDA là **đóng góp về phương pháp/hạ tầng nghiên cứu** trong khuôn khổ luận án — một công cụ do
tác giả xây dựng để **tăng tốc bước trích xuất** dữ liệu sơ cấp cho phân tích tổng hợp, với **xác
nhận bắt buộc của con người** ở mọi bản ghi. M-AIDA **không phải là nguồn tạo ra kết quả chưa kiểm
chứng**: nó hỗ trợ quy trình, còn trách nhiệm khoa học thuộc về nhà nghiên cứu. Vì M-AIDA được mô tả
ở chương phương pháp của luận án như một công cụ hỗ trợ (có người trong vòng lặp), bài báo P6 báo
cáo trích xuất theo quy trình có kiểm chứng của con người và **không lệ thuộc** vào tính tự động của
phần mềm.

## 12. NGÀY HOÀN THÀNH / TÌNH TRẠNG CÔNG BỐ
Ngày hoàn thành phiên bản 7.0.0: *[DD/MM/YYYY — ngày commit cuối của v7.0.0; tác giả điền]*. Mã nguồn
lưu trong repository nghiên cứu, **chưa phát hành công khai**; được sử dụng nội bộ phục vụ luận án.

## 13. THÔNG BÁO BẢN QUYỀN
```
© [Năm] Đỗ Thị Thúy Hương & Phan Anh Tú. All rights reserved.
M-AIDA (Meta-Analysis Intelligent Data Assistant) — Proprietary, Research Use Only.
Liên hệ cấp phép: [email tác giả]
```

## 14. CÁCH TRÍCH DẪN (academic citation)
> Đỗ, T. T. H., & Phan, A. T. ([Năm]). *M-AIDA: Meta-Analysis Intelligent Data Assistant* (Phiên bản
> 7.0.0) [Phần mềm máy tính]. Trường Đại học Cần Thơ. Số đăng ký bản quyền: [điền sau khi cấp].

Siêu dữ liệu trích dẫn máy-đọc: xem `p6/tools/maida/CITATION.cff` (Citation File Format 1.2.0).

---

## PHỤ LỤC — DANH MỤC TỆP MÃ NGUỒN NỘP KÈM

Chương trình được phân phối dưới dạng **một tệp mã nguồn độc lập, tự chứa** toàn bộ giao diện và
logic xử lý, chạy trực tiếp trên trình duyệt. Bản sao điện tử của tệp này được nộp kèm hồ sơ.

| Thuộc tính | Giá trị |
|---|---|
| Tên tệp | `MAIDA_intake.html` (`p6/tools/maida/`) |
| Dung lượng | 23.285 byte (≈ 22,7 KB) |
| Số dòng mã | 260 dòng |
| Số hàm chính | 18 hàm |
| Mã băm SHA-256 | `bd74600cc909e396daf0b33549debd081b6c990904f96a5976e9186c2e18d696` |
| Ngôn ngữ | HTML5 + JavaScript (ES2017+); thư viện PDF.js 3.11 |

Các nhóm hàm chính: **quy đổi đại lượng** (`t2r`, `beta2r`, `f2r`, `clampR`, `z`); **trích xuất**
(`ruleExtract` ngoại tuyến, `aiExtract` qua Claude artifact); **đọc tài liệu** (`readPdf`);
**kiểm chứng & quản lý dữ liệu** (`renderCands`, `accept`, `renderDS`, `persist`, `loadStore`);
**kết xuất** (`exportCSV`, trình tải JSON). Mã băm SHA-256 cho phép đối chiếu tính toàn vẹn của
bản sao điện tử nộp kèm với phiên bản gốc.

---

*Tài liệu phục vụ đăng ký quyền tác giả tại Cục Bản quyền Tác giả Việt Nam (COV), 51–53 Ngô Quyền,
Hoàn Kiếm, Hà Nội. Quy trình & lệ phí: xem `02_checklist_nop_ho_so.md`.*
