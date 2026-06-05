# SHTT Dossier Audit Report — M-AIDA v7.0

**Ngày kiểm tra:** 2026-06-05
**Phạm vi:** Toàn bộ 7 file gốc + 4 file evidence_ctu/ + 4 file system/ trong `SUBMISSION_PACKAGE/10_MAIDA_SHTT/`
**Mục đích:** Rà soát tính hoàn chỉnh + nhất quán + sẵn sàng nộp Cục Bản quyền Tác giả Việt Nam (COV).

---

## ✅ Đã pass

| Kiểm tra | Kết quả |
|---|:-:|
| **Khung pháp lý** Điều 27.1 vs 27.2 Luật SHTT 2005 (sđ 2009, 2019, 2022) | ✅ Chính xác, có evidence (3 QĐ CTU + cam đoan NCS) |
| **3 ownership models** A/B/C với risk-benefit analysis | ✅ Đầy đủ, có template thư xin ý kiến CTU |
| **Phạm vi bảo hộ** (§6.1 phần tác giả tự viết) vs **third-party** (§6.2 PDF.js/Claude/Google Fonts) | ✅ Phân định rõ ràng |
| **Originality claims** (5 đóng góp cụ thể: regex extraction, t/β/F→r conversion, HITL UI, audit trail, ontology) | ✅ Cụ thể, không overclaim |
| **Scope statement** "extraction tool, NOT meta-analysis computation" | ✅ Đã làm rõ ở 3 README (commit `b1da0c6`) |
| **SHA-256 hash** của `MAIDA_intake.html` | ✅ Hash documented (`bd74600c...`) khớp với file thực tế |
| **File size + line count** | ✅ 23.285 bytes + 260 lines khớp với §App của 00_mo_ta |
| **CITATION.cff** format chuẩn CFF 1.2.0, ORCID hợp lệ | ✅ Đầy đủ |
| **Citation format** "Đỗ, T. H., & Phan, A. T. (2026)" | ✅ Nhất quán across 4 files |
| **3 QĐ CTU** (3010, 4768, 4769) có evidence_ctu/ summaries | ✅ Đầy đủ |
| **Bản cam đoan nguồn lực cá nhân** (file 06) | ✅ Đầy đủ 7 điểm cam kết theo Điều 27.1 |
| **NCS personal info** (Đỗ Thùy Hương · P1323001 · DOB · Cần Thơ) | ✅ Khớp với hồ sơ CTU |

---

## ⚠️ Cần xử lý trước khi nộp

### Issue 1 — Địa chỉ COV không nhất quán (MEDIUM, action required)

**Phát hiện:**
- Dossier (4 files, 6 occurrences) đồng nhất ghi: **51–53 Ngô Quyền, Hoàn Kiếm, Hà Nội**
- Tuy nhiên, **Cục Bản quyền tác giả Việt Nam (COV) hiện tại có trụ sở mới**: **Số 33 Ngọc Hà, Ba Đình, Hà Nội** (theo website chính thức cov.gov.vn, từ 2023 trở đi)
- Địa chỉ 51–53 Ngô Quyền là trụ sở của **Bộ VHTT&DL** (Bộ chủ quản của COV), không phải COV trực tiếp

**Khuyến nghị:**
- ⚠️ **TRƯỚC KHI ĐI NỘP**, NCS gọi điện thoại xác nhận với COV qua:
  - Tổng đài COV: **024.3823.6663** (giờ hành chính)
  - Website: **https://cov.gov.vn** → Liên hệ
  - Hoặc kiểm tra qua trang dịch vụ công: https://dichvucong.gov.vn (tra cứu "Cục Bản quyền tác giả")
- Tùy địa chỉ thực tế tại thời điểm nộp, cập nhật trong:
  - `02_checklist_nop_ho_so.md` (3 chỗ)
  - `03_huong_dan_toi_uu.md` (3 chỗ)
  - `00_mo_ta_tac_pham_vi.md` (footer cuối file)
- **VPĐD phía Nam (nếu NCS nộp ở TP.HCM)**: 170 Nguyễn Đình Chiểu, P.6, Q.3 — đã ghi đúng trong `03_huong_dan_toi_uu.md` L115

### Issue 2 — Online submission URL cần xác minh (LOW)

**Phát hiện:**
- `03_huong_dan_toi_uu.md` L107 ghi: `https://dichvucong.banquyentacgia.gov.vn`
- Cổng dịch vụ công quốc gia: `https://dichvucong.gov.vn` (chính thức)
- COV có thể có sub-portal riêng tại `cov.gov.vn` hoặc tích hợp vào DVC quốc gia

**Khuyến nghị:** NCS xác minh URL nộp online tại thời điểm chuẩn bị (có thể đường dẫn đã thay đổi).

### Issue 3 — Thông tin cá nhân (PII) trong source-controlled files (LOW, informational)

**Phát hiện:**
- `05_evidence_quyet_dinh_CTU.md` L15: "Ngày sinh: 04/6/1994 · Nơi sinh: Cần Thơ"
- `06_cam_doan_nguon_luc_ca_nhan.md` L16-17: "Ngày sinh: 04/06/1994 · Nơi sinh: Cần Thơ"

**Đánh giá:**
- Repo hiện đang ở chế độ **private** theo `.claude/CLAUDE.md` ("repo private until defense complete") → PII đang được bảo vệ
- DOB cần cho form COV → bắt buộc phải có trong các file này
- Số CCCD vẫn để trống `_____________________` → ✅ đúng practice (NCS điền local khi in)

**Khuyến nghị:**
- Trước khi repo chuyển sang public (sau bảo vệ), cân nhắc:
  - (a) Giữ nguyên (DOB không phải dữ liệu nhạy cảm cao — đã công khai trên các profile học thuật)
  - (b) Hoặc redact DOB từ 2 file này (chỉ giữ trong bản in nộp COV)

### Issue 4 — Tiêu đề file 01 ("MẪU MÃ NGUỒN") vs nội dung (TOÀN BỘ mã nguồn) (TRIVIAL)

**Phát hiện:** File 01 tên là "Source Code **Samples**" nhưng nội dung L7-9 nói rõ "Tài liệu này cung cấp **toàn bộ** mã nguồn".

**Khuyến nghị:** Rename internal title từ "MẪU MÃ NGUỒN" → "TOÀN BỘ MÃ NGUỒN" cho khớp nội dung. Không ảnh hưởng giá trị pháp lý.

---

## 📋 Checklist nộp hồ sơ (tóm tắt)

Trước khi đi nộp Cục BQTG, hoàn tất:

### A. Thông tin cá nhân (NCS điền local)
- [ ] CCCD số + ngày cấp + nơi cấp (cả 2 tác giả)
- [ ] Địa chỉ thường trú (cả 2 tác giả)
- [ ] Điện thoại (cả 2 tác giả)
- [ ] Tick Model A / B / C trong §3.2 file 00 (sau khi consult CTU)
- [ ] Tick public/private GitHub trong §12 file 00
- [ ] Tick một option trong mục 6 của file 06 (sau khi có phản hồi CTU)

### B. Tài liệu in (2 bản gốc + photo)
- [ ] Tờ khai chính thức Cục BQTG (lấy tại trụ sở hoặc download)
- [ ] `00_mo_ta_tac_pham_vi.docx`
- [ ] `01_source_code_samples.docx` (toàn bộ 260 dòng, có copyright header)
- [ ] CCCD công chứng (cả 2 tác giả, < 6 tháng)
- [ ] `06_cam_doan_nguon_luc_ca_nhan.docx` đã ký
- [ ] Bản photo 3 QĐ CTU (3010 + 4768 + 4769) làm evidence
- [ ] Email gửi/nhận với Phòng KHCN CTU (in từ Gmail)

### C. Trước khi đi (Pre-flight)
- [ ] **GỌI COV xác nhận địa chỉ + giờ tiếp nhận** (Issue 1)
- [ ] Tiền mặt 180.000 VND (hoặc thẻ ATM)
- [ ] Photo backup tất cả tài liệu lên Google Drive cá nhân
- [ ] Confirm với PGS.TS. Phan Anh Tú về authorship (Model A/B/C)

### D. Tại COV
- [ ] Nhận biên lai có mã số đơn
- [ ] Ghi rõ ngày hẹn nhận kết quả
- [ ] Hỏi rõ kênh thông báo (email/SMS/portal)

---

## 🎯 Kết luận

**Hồ sơ SHTT đã sẵn sàng về mặt nội dung pháp lý + kỹ thuật.** Cần xử lý 1 vấn đề trung bình (Issue 1 — địa chỉ COV) trước khi đi nộp; 3 vấn đề còn lại là LOW/TRIVIAL không cản trở nộp.

**Khuyến nghị thứ tự hành động:**
1. **TUẦN 1**: Gọi điện COV xác nhận địa chỉ (024.3823.6663) → cập nhật 4 files
2. **TUẦN 1**: Email Phòng KHCN CTU (Bước 1-2 trong file 03 + Section 9 trong file 04)
3. **TUẦN 2**: Confirm authorship với PGS.TS. Phan Anh Tú (Bước 2 trong file 05)
4. **TUẦN 2-3**: Đợi CTU phản hồi → tick Model A/B/C trong file 00
5. **TUẦN 3**: In hồ sơ + công chứng CCCD + chuẩn bị tiền mặt
6. **TUẦN 4**: Đi nộp tại COV (Hà Nội hoặc TP.HCM)
7. **TUẦN 5-7**: Đợi thẩm định (15-25 ngày làm việc) → nhận cert
8. **TUẦN 8**: Cập nhật repo (CITATION.cff + footnote luận án/P6 với số cert)

**Tổng thời gian dự kiến:** 6-8 tuần từ ngày gọi COV xác nhận.

---

*Audit by claude-opus-4-7 trên branch `claude/vietnamese-academic-standards-QuiLM` ngày 2026-06-05.*
