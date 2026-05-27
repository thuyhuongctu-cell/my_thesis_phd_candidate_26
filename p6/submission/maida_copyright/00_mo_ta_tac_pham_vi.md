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

### 6.1. Backend — FastAPI (Python 3.11+)
- Framework: FastAPI 0.115, Uvicorn 0.30, Pydantic 2.7 (kiểm định dữ liệu).
- Xử lý: PyMuPDF 1.24 (trích văn bản PDF); Anthropic Claude SDK 0.31 (pipeline LLM); pandas 2.2,
  numpy 2.0, scipy 1.13 (xử lý thống kê); notion-client 2.2 (đồng bộ Notion).
- Module: `main.py` (8 REST endpoint), `extractor.py` (lớp `StatisticalExtractor`), `models.py`
  (mô hình Pydantic: `ExtractedEffect`, `StudyDatabaseEntry`, `VerificationDecision`),
  `settings.py` (cấu hình runtime), `notion_sync.py` (đồng bộ hai chiều).

### 6.2. Frontend — React 18 + TypeScript
- `App.tsx` (bố cục hai tab Extract / Verify & Lock), `ExtractionPanel.tsx`,
  `VerificationDashboard.tsx`, `VerificationPanel.tsx`, `ExportPanel.tsx`.

---

## 7. CHỨC NĂNG CHI TIẾT (ánh xạ theo quy trình phân tích tổng hợp)

| Bước phân tích tổng hợp | Module M-AIDA | Endpoint |
|---|---|---|
| Trích cỡ ảnh hưởng từ toàn văn | LLM extraction + quy đổi về *r* + chấm tin cậy | `POST /api/extract` |
| Quản lý & lọc nghiên cứu | Study store (lọc theo ICRV/DPL/verified/locked) | `GET /api/studies` |
| **Xác nhận của con người (PI)** | Override trường + phê duyệt + ghi chú | `PATCH /api/studies/{id}/verify` |
| **Khóa toàn vẹn (không đảo ngược)** | Lock + dấu thời gian (audit trail) | `POST /api/studies/{id}/lock` |
| Xuất dữ liệu chuẩn ma trận | CSV streaming (chỉ bản ghi đã khóa) | `GET /api/studies/export/csv` |
| Đồng bộ cộng tác | Push lên Notion (upsert) | `POST /api/notion/sync` |

Trường xuất chuẩn: `study_id, paper_title, authors, year, country, sample_n, effect_r, effect_t,
effect_beta, effect_df, p_value, ci_lower, ci_upper, doi_measure, performance_measure, icrv_regime,
dpl_phase, cdai_score, extraction_confidence, pi_notes, locked_at`.

---

## 8. TÍNH NGUYÊN GỐC VÀ SÁNG TẠO

1. **Phần mềm trích xuất chuyên ngành đầu tiên cho phân tích tổng hợp I–P tại Việt Nam**, mã hóa
   tri thức phương pháp meta-analysis vào pipeline tự động (không có trên thị trường).
2. **Thang tin cậy trích xuất 3 mức** gắn trực tiếp với chuẩn quy đổi Peterson & Brown (2005).
3. **Quy trình PI verify → irreversible lock** với audit trail — phân biệt rõ "bản nháp của máy" và
   "quyết định của nhà nghiên cứu", phù hợp luận án và nghiên cứu bình duyệt.
4. **Lược đồ biến điều tiết độc quyền của luận án** (ICRV / cDAI / DPL) tích hợp sẵn.
5. **Kiến trúc FastAPI + React 18/TypeScript** type-safe, container hóa bằng Docker.

## 9. CÔNG NGHỆ SỬ DỤNG
Backend: Python 3.11+, FastAPI 0.115, Uvicorn 0.30, Anthropic Claude SDK 0.31 (model
`claude-sonnet-4-6`), PyMuPDF 1.24, notion-client 2.2, pandas 2.2 / numpy 2.0 / scipy 1.13,
pydantic 2.7. Frontend: TypeScript 5.x, React 18, build Vite. Triển khai: Docker (Dockerfile +
docker-compose), CORS cấu hình cho phát triển.

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

*Tài liệu phục vụ đăng ký quyền tác giả tại Cục Bản quyền Tác giả Việt Nam (COV), 51–53 Ngô Quyền,
Hoàn Kiếm, Hà Nội. Quy trình & lệ phí: xem `02_checklist_nop_ho_so.md`.*
