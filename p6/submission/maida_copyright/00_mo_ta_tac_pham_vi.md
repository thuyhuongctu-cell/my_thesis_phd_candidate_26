# MÔ TẢ TÁC PHẨM
# (Description of Work — COV Copyright Registration)

---

## 1. TÊN TÁC PHẨM

**M-AIDA** (Meta-Analysis Intelligent Data Assistant — Internationalization & Performance)

Phiên bản: 7.0.0

---

## 2. LOẠI TÁC PHẨM

Phần mềm máy tính (Computer Program)

---

## 3. MỤC ĐÍCH VÀ CHỨC NĂNG TỔNG QUAN

M-AIDA là phần mềm chuyên dụng phục vụ nghiên cứu học thuật trong lĩnh vực Quản trị Kinh doanh Quốc tế (International Business). Phần mềm hỗ trợ các nhà nghiên cứu tự động hóa quy trình trích xuất dữ liệu thống kê từ các bài báo khoa học dạng PDF, kiểm tra và chuẩn hóa kết quả, sau đó xuất tập dữ liệu phục vụ meta-analysis (phân tích tổng hợp định lượng) về mối quan hệ giữa quốc tế hóa doanh nghiệp và hiệu quả hoạt động (Internationalization đến Performance, I–P).

Phần mềm được phát triển để phục vụ trực tiếp Luận án Tiến sĩ "Internationalization and Firm Performance in Asia-Pacific: A Multi-Country Meta-Analysis" (Paper 6 của luận án).

---

## 4. KIẾN TRÚC PHẦN MỀM

M-AIDA gồm hai thành phần chính:

### 4.1. Backend — FastAPI (Python)

**Ngôn ngữ & Framework chính**:
- Python 3.11+
- FastAPI 0.115.0 (REST API framework)
- Pydantic 2.7.0 (data validation & settings)
- Uvicorn 0.30.0 (ASGI server)

**Thư viện xử lý**:
- PyMuPDF 1.24.5 — trích xuất văn bản từ PDF
- Anthropic Claude SDK 0.31.0 — LLM pipeline trích xuất thống kê
- Notion Client 2.2.1 — đồng bộ dữ liệu nghiên cứu lên Notion database
- pandas 2.2.2, numpy 2.0.0, scipy 1.13.1 — xử lý dữ liệu thống kê

**Các module Backend**:
- `main.py` — FastAPI application entry point; định nghĩa 8 REST API endpoints
- `extractor.py` — StatisticalExtractor class: LLM pipeline trích xuất effect sizes từ văn bản PDF
- `models.py` — Pydantic data models: ExtractedEffect, StudyDatabaseEntry, VerificationDecision
- `settings.py` — Cấu hình runtime từ biến môi trường (pydantic-settings)
- `notion_sync.py` — NotionSync class: đồng bộ hai chiều với Notion database

### 4.2. Frontend — React 18 + TypeScript

**Ngôn ngữ & Framework chính**:
- TypeScript 5.x
- React 18 (Hooks: useState, useCallback)

**Các component**:
- `App.tsx` — Root component; two-tab layout (Extract / Verify & Lock)
- `ExtractionPanel.tsx` — Giao diện upload PDF và hiển thị kết quả LLM extraction
- `VerificationDashboard.tsx` — Dashboard cho PI (Principal Investigator) kiểm tra và phê duyệt
- `VerificationPanel.tsx` — Panel thao tác cho từng nghiên cứu (overrides, approval)
- `ExportPanel.tsx` — Xuất CSV từ các nghiên cứu đã khóa (pi_locked=True)

---

## 5. CHỨC NĂNG CHI TIẾT

### 5.1. Module Trích xuất Effect Size (POST /api/extract)

- Nhận file PDF dưới dạng Base64 hoặc multipart upload
- Trích xuất văn bản toàn bộ PDF bằng PyMuPDF
- Gửi văn bản đến Claude API với system prompt chuyên biệt để:
  - Xác định N (sample size), r (Pearson correlation), t-statistic, df, β (standardised regression coefficient), p-value, CI 95%
  - Phân loại 2 chiều xác định được từ văn bản: doi_measure (FSTS/GEO/EXP/FDI/COMP/OTH), performance_measure (ACC/MKT/LAB/MIX); trích cửa sổ dữ liệu (sample_start/sample_end)
  - Các moderator thể chế — icrv_regime (I/II/III/FR/MX, theo WGI Rule of Law), dpl_phase (PRE/SPN/FOL, theo năm dữ liệu trung vị), cdai_score (Digital Adoption Index 0–1) — do PI gán từ bảng tra cứu ngoài ở bước xác minh, KHÔNG do LLM đoán
- Chuyển đổi t đến r theo công thức chuẩn (Cohen, 1988): `r = sqrt(t² / (t² + df))`
- Chuyển đổi β đến r theo Peterson & Brown (2005), dạng rút gọn: `r ≈ β × 0.98` (trùng khít công thức đầy đủ 0.98β + 0.05λ khi β âm; bảo thủ khi β dương)
- Tính extraction_confidence (1.0=direct r; 0.8=from t; 0.6=from β) và tự động đánh dấu requires_verification nếu confidence < 0.7

### 5.2. Module Quản lý Nghiên cứu (GET /api/studies)

- Lưu trữ in-memory study store (dict keyed by UUID study_id)
- Lọc theo: icrv_regime, dpl_phase, verified status, pi_locked status
- Truy vấn từng nghiên cứu theo UUID (GET /api/studies/{id})

### 5.3. Module Xác minh PI (PATCH /api/studies/{id}/verify)

- Cho phép Principal Investigator áp dụng field_overrides lên bất kỳ trường nào của ExtractedEffect
- Cờ pi_approved chuyển requires_verification = False
- Lưu pi_notes (ghi chú tự do của PI)

### 5.4. Module Khóa Dữ liệu (POST /api/studies/{id}/lock)

- Khóa vĩnh viễn bản ghi (pi_locked = True, locked_at = UTC timestamp)
- Thao tác KHÔNG THỂ ĐẢO NGƯỢC — đảm bảo data integrity cho meta-analysis
- Chỉ cho phép khóa các bản ghi đã được PI phê duyệt (requires_verification = False)

### 5.5. Module Xuất Dữ liệu (GET /api/studies/export/csv)

- Xuất CSV streaming chỉ bao gồm các nghiên cứu đã pi_locked
- Field order chuẩn theo quy ước dissertation data matrix
- Headers: study_id, paper_title, authors, year, country, sample_n, effect_r, effect_t, effect_beta, effect_df, p_value, ci_lower, ci_upper, doi_measure, performance_measure, icrv_regime, dpl_phase, cdai_score, extraction_confidence, pi_notes, locked_at

### 5.6. Module Đồng bộ Notion (POST /api/notion/sync)

- Push tất cả nghiên cứu đã pi_locked lên Notion database
- Upsert logic: cập nhật nếu notion_page_id đã có, tạo mới nếu chưa có
- Pagination tự động khi fetch_all_studies()

---

## 6. TÍNH NGUYÊN GỐC VÀ SÁNG TẠO

M-AIDA là phần mềm đầu tiên tại Việt Nam kết hợp:

1. **LLM-powered extraction với confidence scoring**: Sử dụng Claude API với system prompt chuyên biệt cho I–P meta-analysis, với thang đánh giá độ tin cậy 3 mức (direct r / from t / from β) dựa trên Peterson & Brown (2005) — không có trong bất kỳ meta-analysis tool công khai nào.

2. **Workflow PI Verification + Irreversible Lock**: Cơ chế 2 bước (approve đến lock) đảm bảo data integrity và audit trail, phân biệt rõ LLM extraction và quyết định của Principal Investigator — đặc thù cho dissertations và peer-reviewed research.

3. **Domain-specific moderator schema**: Tích hợp sẵn schema moderator của luận án — ICRV regime (5 mức thể chế: I/II/III/FR/MX theo WGI Rule of Law), DPL phase (PRE/SPN/FOL), cDAI score (Digital Adoption Index 0–1) — với nguyên tắc tách bạch: LLM chỉ trích thống kê; moderator thể chế do PI gán từ bảng tra cứu, bảo đảm tính kiểm chứng độc lập.

4. **Notion bidirectional sync**: Cho phép collaborative verification qua Notion workspace mà không cần shared file system.

5. **FastAPI + React 18 stack với TypeScript**: Architecture hiện đại, type-safe, hỗ trợ multipart PDF upload và streaming CSV export.

---

## 7. CÔNG NGHỆ SỬ DỤNG

**Backend**:
- Ngôn ngữ: Python 3.11+
- Framework: FastAPI 0.115.0, Uvicorn 0.30.0
- AI/LLM: Anthropic Claude SDK 0.31.0 (model mặc định: claude-fable-5; cấu hình qua ANTHROPIC_MODEL / ANTHROPIC_DEFAULT_FABLE_MODEL)
- PDF: PyMuPDF 1.24.5
- Database sync: notion-client 2.2.1
- Data processing: pandas 2.2.2, numpy 2.0.0, scipy 1.13.1
- Validation: pydantic 2.7.0, pydantic-settings 2.3.0

**Frontend**:
- Ngôn ngữ: TypeScript 5.x
- Framework: React 18 (functional components, Hooks)
- Build tool: Vite (assumed from project structure)

**Deployment**:
- Docker (Dockerfile có sẵn trong backend/)
- CORS-configured cho localhost:3000 (development)

---

## 8. ĐỐI TƯỢNG NGƯỜI DÙNG

- Nghiên cứu sinh tiến sĩ trong lĩnh vực International Business, Strategy, Management
- Giảng viên và nhà nghiên cứu thực hiện systematic review và meta-analysis
- Nhóm nghiên cứu cần quy trình extraction + verification chuẩn hóa

---

## 9. NGÀY HOÀN THÀNH

[DD/MM/YYYY] — Điền ngày hoàn thành phiên bản 7.0.0 (ngày commit cuối cùng)

---

## 10. TÁC GIẢ / CHỦ SỞ HỮU

Họ và tên đầy đủ: [Điền tên tác giả]
Ngày sinh: [DD/MM/YYYY]
Địa chỉ: [Điền địa chỉ]
Số CMND/CCCD: [Điền số]
Số điện thoại: [Điền số]
Email: [Điền email]
Quốc tịch: Việt Nam

---

## 11. THÔNG BÁO BẢN QUYỀN (COPYRIGHT NOTICE)

```
© [Năm] [Tên tác giả]. All rights reserved.

M-AIDA (Meta-Analysis Intelligent Data Assistant) is protected by
copyright law and international treaties. Unauthorized reproduction
or distribution of this software, or any portion of it, may result
in severe civil and criminal penalties, and will be prosecuted to
the maximum extent possible under the law.

For licensing inquiries, contact: [email]
```

---

## 12. TÌNH TRẠNG CÔNG BỐ

Phần mềm đã được sử dụng nội bộ trong quá trình thực hiện luận án tiến sĩ.
Mã nguồn được lưu trữ trong repository nghiên cứu (không phát hành công khai).

*Ghi chú: Tài liệu này là bản mô tả tác phẩm phục vụ đăng ký bản quyền tại Cục Bản quyền Tác giả Việt Nam (COV), 51–53 Ngô Quyền, Hoàn Kiếm, Hà Nội.*
