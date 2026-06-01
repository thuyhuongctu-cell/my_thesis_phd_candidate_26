# M-AIDA — Hướng tối ưu để đăng ký SHTT (Path of Minimum Friction)

**⚠️ CẬP NHẬT 31/05/2026:** Vì **CTU là cơ sở cấp bằng PhD của NCS**, hồ sơ chủ sở hữu CẦN consult với Phòng KHCN CTU trước khi nộp. Xem chi tiết tại `04_phan_tich_chu_so_huu_va_ctu.md` để chọn 1 trong 3 ownership models + template thư xin ý kiến CTU.

**Mục tiêu:** Lấy Giấy chứng nhận đăng ký quyền tác giả đối với chương trình máy tính (Điều 14.1.m + Điều 22 Luật SHTT 2005, sđ 2022) cho M-AIDA v7.0 trong **8-10 tuần** (bao gồm 2-4 tuần consult CTU) với rủi ro tối thiểu.

**Quyết định kiến trúc đã chọn (TENTATIVE — confirm sau khi consult CTU):**
- ✅ Đồng tác giả: Đỗ Thùy Hương + Phan Anh Tú (giữ status quo trong CITATION.cff)
- ⏳ **Chủ sở hữu**: CHỜ phản hồi CTU — có thể là Model A (2 tác giả cá nhân), Model B (2 tác giả + CTU), hoặc Model C (CTU sole). Mặc định khuyến nghị **Model B** vì NCS đang trong giai đoạn PhD.
- ✅ Loại tác phẩm: Chương trình máy tính
- ✅ Hình thức công bố: NCS quyết định public/private GitHub tại thời điểm nộp (xem §12 của `00_mo_ta_tac_pham_vi.md`)
- ✅ Phạm vi bảo hộ: Chỉ phần mã do tác giả viết (xem §6.1 mô tả tác phẩm); third-party (PDF.js, Claude API, Google Fonts) đã loại trừ ở §6.2

---

## NHỮNG GÌ CLAUDE ĐÃ LÀM XONG (sẵn sàng nộp)

| File | Nội dung | Trạng thái |
|---|---|---|
| `p6/tools/maida/MAIDA_intake.html` | 260 dòng mã nguồn chính, v7.0.0 | ✅ Code stable, last commit 29/05/2026 |
| `p6/tools/maida/README.md` | Tóm tắt kiến trúc + cách dùng | ✅ Đầy đủ |
| `p6/tools/maida/CITATION.cff` | Citation file đồng tác giả + ORCID | ✅ Đầy đủ |
| `p6/submission/maida_copyright/00_mo_ta_tac_pham_vi.md` | Mô tả tác phẩm 14 mục — đã điền §6.1 phần tự xây dựng, §6.2 third-party disclosure, §12 publication status, §13 copyright notice, §14 citation | ✅ Sẵn sàng |
| `p6/submission/maida_copyright/01_source_code_samples.md` | Mẫu mã nguồn — copyright header đã điền © 2026, Created 29/05/2026 | ✅ Sẵn sàng |
| `p6/submission/maida_copyright/02_checklist_nop_ho_so.md` | Checklist Cục BQTG | ✅ Đã có |

---

## NHỮNG GÌ NCS CẦN ĐIỀN THỦ CÔNG (~30 phút)

Thông tin cá nhân pháp lý — không nên đặt trong repo public; điền vào bản in trước khi mang đến Cục:

### Trong tờ khai chính thức (mẫu của Cục BQTG, lấy tại 51-53 Ngô Quyền hoặc trực tuyến):

| Trường | Đỗ Thùy Hương | Phan Anh Tú |
|---|---|---|
| Họ tên đầy đủ | (đã có) | (đã có) |
| Ngày sinh (DD/MM/YYYY) | ⬜ | ⬜ |
| Quốc tịch | Việt Nam | Việt Nam |
| Số CCCD | ⬜ | ⬜ |
| Ngày cấp CCCD | ⬜ | ⬜ |
| Nơi cấp CCCD | ⬜ | ⬜ |
| Địa chỉ thường trú | ⬜ | ⬜ |
| Điện thoại | ⬜ | ⬜ |
| Email | huongp1323001@gstudent.ctu.edu.vn | patu@ctu.edu.vn |
| ORCID | 0000-0002-7711-2487 | 0000-0003-0667-3137 |

### Quyết định cuối trước khi nộp:

1. **Quyết định public/private GitHub repo?**
   - Nếu repo đang public (default sau khi push lên `thuyhuongctu-cell/MY_THESIS_PHD_CANDIDATE_26`): tích ô "Đã công bố" trong §12 của mô tả tác phẩm + ghi link
   - Nếu muốn giữ private chờ cert: tích ô "Chưa công bố"; nhớ set private trên GitHub trước khi nộp
   - **Khuyến nghị:** giữ public (đã public) — pháp luật Việt Nam không phân biệt; public tăng evidence of authorship

2. **Quyết định liên hệ supervisor?**
   - Phan Anh Tú đã đứng tên trong CITATION.cff → coi như đã đồng ý
   - Trước khi đi công chứng, gửi anh xem `00_mo_ta_tac_pham_vi.md` để confirm

---

## QUY TRÌNH 8-10 TUẦN (sau khi bổ sung CTU consultation)

### Tuần 1-2: Consult CTU (BƯỚC MỚI — BẮT BUỘC)

**Trước khi làm gì:**
- [ ] Đọc `04_phan_tich_chu_so_huu_va_ctu.md` để hiểu 3 ownership models
- [ ] In template thư xin ý kiến CTU (Section 9 trong file 04)
- [ ] Điền thông tin NCS vào thư

**Tuần 1 (Mon-Wed):**
- [ ] Gửi thư xin ý kiến đến **Phòng Khoa học Công nghệ CTU** (đồng kính gửi supervisor)
- [ ] Đồng thời send email tóm tắt + attach `00_mo_ta_tac_pham_vi.docx` để Phòng KHCN có context
- [ ] Liên hệ supervisor Phan Anh Tú để consult ý kiến cá nhân về CTU practice

**Tuần 1-2 (Thu-Fri):**
- [ ] Đợi phản hồi từ CTU (thường 5-10 ngày làm việc)
- [ ] Nếu CTU không phản hồi sau 7 ngày: follow up qua email + điện thoại
- [ ] Ghi nhận phản hồi của CTU bằng văn bản (giấy hoặc email)

**Quyết định cuối Tuần 2:**
- 🅰️ Nếu CTU không claim → tiếp Model A (2 tác giả cá nhân đồng chủ sở hữu)
- 🅱️ Nếu CTU yêu cầu co-ownership → Model B (3 chủ sở hữu, có CTU); cần chữ ký đại diện CTU
- 🅲️ Nếu CTU yêu cầu sole owner → Model C; CTU đứng tên nộp, NCS chỉ là tác giả

→ Tùy theo Model, sửa `00_mo_ta_tac_pham_vi.md` mục Chủ sở hữu trước khi in nộp.

### Tuần 3: Chuẩn bị hồ sơ in ấn

**Ngày 1-2 (NCS):**
- [ ] Confirm với supervisor Phan Anh Tú: gửi `00_mo_ta_tac_pham_vi.md` + `01_source_code_samples.md` + CITATION.cff để anh xem; xin chữ ký đồng ý
- [ ] Điền 11 trường cá nhân vào tờ khai chính thức (xem bảng trên)

**Ngày 3:**
- [ ] In **2 bản** mỗi tài liệu (gốc + photo):
  - Tờ khai chính thức (mẫu Cục BQTG)
  - `00_mo_ta_tac_pham_vi.docx` (rendered PDF/in từ md)
  - `01_source_code_samples.docx`
- [ ] Ký tên + đóng dấu giáp lai mỗi trang (cả 2 tác giả)

**Ngày 4:**
- [ ] Công chứng CCCD của cả 2 tác giả (Phòng công chứng nhà nước, ~50k VND/người)
- [ ] In thêm CITATION.cff + README.md làm tài liệu bổ sung (khuyến nghị, không bắt buộc)

### Tuần 2: Nộp hồ sơ

**Lựa chọn 1 — Online (khuyến nghị):**
- Truy cập: https://dichvucong.banquyentacgia.gov.vn
- Đăng ký tài khoản tác giả + xác minh CCCD điện tử
- Upload PDF của các tài liệu đã in
- Thanh toán phí 180,000 VND qua VNPay / chuyển khoản
- Theo dõi trạng thái qua portal

**Lựa chọn 2 — Trực tiếp:**
- Địa chỉ: **51-53 Ngô Quyền, Hoàn Kiếm, Hà Nội** (Trụ sở chính)
- Hoặc VPĐD phía Nam: **170 Nguyễn Đình Chiểu, P.6, Q.3, TP.HCM**
- Thời gian tiếp nhận: 8h-11h30, 13h30-16h30, T2-T6
- Mang theo:
  - Bộ hồ sơ 2 bản (đã ký + đóng dấu giáp lai)
  - CCCD công chứng 2 tác giả
  - Tiền mặt 180,000 VND (nhận biên lai thu)

### Tuần 3-5: Cục thẩm định (15-25 ngày làm việc)

- Cục kiểm tra hình thức hồ sơ + tính sáng tạo
- Nếu có yêu cầu bổ sung: phản hồi qua email/portal trong 7 ngày
- Khả năng yêu cầu bổ sung: ~15% các hồ sơ; thường là yêu cầu mô tả rõ hơn về phần thuộc tác giả

### Tuần 6: Nhận Giấy chứng nhận

- Trực tiếp: đến lấy tại Cục với CCCD gốc + biên lai
- Online: PDF cert gửi qua email; bản giấy gửi bưu điện
- Lưu cert trong: `p6/submission/maida_copyright/certificate.pdf`

---

## SAU KHI NHẬN GIẤY CHỨNG NHẬN

### Cập nhật repo (5 phút)

1. **`p6/tools/maida/CITATION.cff`** — uncomment + điền:
   ```yaml
   date-released: "YYYY-MM-DD"  # Ngày cấp cert
   identifiers:
     - type: other
       value: "COV Số đăng ký: ###/QTG-COV"  # Số cert thực tế
       description: "Cục Bản quyền Tác giả Việt Nam"
   ```

2. **`p6/p6_meta_manuscript_en.md` §3.2.4** — thêm footnote:
   > *Footnote: The M-AIDA software is registered as a computer program with the Vietnam Copyright Office, Registration No. [###/QTG-COV], dated [DD/MM/YYYY].*

3. **`thesis/chuong_3_phuong_phap_vi.md` §3.2.4** — thêm footnote tương đương VI:
   > *Phần mềm M-AIDA đã được đăng ký quyền tác giả đối với chương trình máy tính tại Cục Bản quyền Tác giả Việt Nam, Số đăng ký [###/QTG-COV], cấp ngày [DD/MM/YYYY].*

### Sử dụng cert làm bằng chứng (chiến lược)

- **CV academic**: thêm vào section "Software / Methodological Contributions"
- **Cover letter P6 → MIR**: đề cập trong §"Methodological Contributions" như defensive evidence
- **Bài báo methodology tương lai** (Research Synthesis Methods / Organizational Research Methods): cert là prior-art evidence cho originality claim
- **Bảo vệ luận án**: trả lời phản biện về originality methodology với cert + GitHub commit log

---

## CHI PHÍ TỔNG CỘNG (ước lượng)

| Khoản mục | Chi phí |
|---|---|
| Phí nhà nước Cục BQTG | 180,000 VND |
| Công chứng CCCD (2 người) | 100,000 VND |
| In ấn + photocopy (~50 trang × 2 bản) | 50,000 VND |
| Phí gửi bưu điện (nếu nộp Hà Nội từ Cần Thơ) | 40,000 VND |
| **Tổng** | **~370,000 VND** |

**Thời gian NCS dành:** ~6-8 giờ (chia làm 3-4 buổi)

---

## TÌNH HUỐNG VƯỚNG MẮC + GIẢI PHÁP

### Q1: Supervisor không đồng ý đứng tên tác giả software?
→ Sửa CITATION.cff + mô tả tác phẩm thành solo (Đỗ Thùy Hương). Phan Anh Tú có thể được ghi nhận trong §"Acknowledgements" của mô tả tác phẩm thay vì authors. Mất thêm 1 tuần.

### Q2: CTU đòi đứng tên chủ sở hữu?
→ Tham vấn Phòng KHCN của CTU. Hai phương án:
   (a) NCS giữ ownership cá nhân với điều khoản license back cho CTU (academic use free)
   (b) CTU đứng tên owner; NCS giữ "author rights" (quyền tinh thần — moral rights — không chuyển nhượng được theo Điều 19)
→ Khuyến nghị (a) nếu CTU chưa có IP policy bắt buộc.

### Q3: Cục yêu cầu nộp bản in toàn bộ 260 dòng code?
→ `01_source_code_samples.md` hiện đã chứa các đoạn đại diện. Nếu Cục muốn full code, in toàn bộ `MAIDA_intake.html` (~12 trang A4 font 10pt) + đóng giáp lai. Không phải vấn đề lớn.

### Q4: Repository GitHub đã public từ trước khi nộp — có ảnh hưởng?
→ KHÔNG. Luật Việt Nam (Điều 6.1) công nhận quyền tác giả phát sinh tự động kể từ khi tác phẩm được sáng tạo và thể hiện dưới hình thức vật chất. Đăng ký SHTT là *xác nhận quyền có sẵn*, không phải *cấp quyền mới*. Ngày commit GitHub là evidence of creation date.

### Q5: NCS muốn open source M-AIDA sau khi nhận cert?
→ Hoàn toàn được. Sau khi có cert (xác nhận tính nguyên gốc), NCS có thể release MIT/Apache 2.0 nếu muốn. Cert + license không xung đột.

---

## CHECKLIST CUỐI

Trước khi đi nộp, kiểm tra:

- [ ] CITATION.cff đã chính xác authorship + ORCID
- [ ] `00_mo_ta_tac_pham_vi.docx` đã chọn ô public/private trong §12
- [ ] `01_source_code_samples.docx` copyright header © 2026 đã điền
- [ ] 11 trường cá nhân trong tờ khai đã điền (cả 2 tác giả)
- [ ] Supervisor đã ký xác nhận đồng ý đứng tên tác giả
- [ ] CCCD 2 tác giả đã công chứng (bản còn hạn ≤ 6 tháng)
- [ ] 180,000 VND tiền mặt hoặc tài khoản chuyển khoản sẵn sàng
- [ ] 2 bản hồ sơ in (gốc + photo)
- [ ] Photo backup các tài liệu trên điện thoại

**Khi cả 9 ô đã tick → có thể nộp ngay.**

---

*Tài liệu này tạo 2026-05-31 sau khi đã rà soát thực tế code M-AIDA + hồ sơ đăng ký hiện có. Không dùng nguồn từ tài liệu Qwen.*
