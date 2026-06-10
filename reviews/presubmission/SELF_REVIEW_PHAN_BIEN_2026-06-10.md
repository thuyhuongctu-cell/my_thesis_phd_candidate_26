# PHẢN BIỆN HỌC THUẬT — Rà soát toàn bộ nội dung đã triển khai (Fable 5)

**Ngày:** 2026-06-10 · **Vai trò:** phản biện độc lập, đối tượng = chính các sản phẩm đã triển khai trong chuỗi phiên
**Phương pháp:** mọi nghi vấn đều được **kiểm chứng bằng grep/dữ liệu/code trước khi kết luận** (file:line kèm theo); các nghi vấn không xác nhận được ghi rõ ở mục "Đã bác bỏ" để minh bạch.

---

## A. PHÁT HIỆN NGHIÊM TRỌNG (CRITICAL — chặn nộp cho paper liên quan)

### A1. P9 — Cover letter MIR **mâu thuẫn với phát hiện trung tâm của chính manuscript**
`p9_india/submission/mir_package/03_cover_letter.md:25`:
> *"replicates and extends the **threshold-durability** finding… **If India also exhibits durability** under far more severe institutional change…"*

Manuscript kết luận điều **ngược lại**: ngưỡng **tan rã** (threshold dissolution/collapse) — tựa đề bài là *"When Institutional Transformation **Breaks** the Threshold: The **Disappearance** of the Inverted-U"*. Cover letter được soạn từ giai đoạn giả thuyết (durability) và **chưa bao giờ cập nhật sau khi có kết quả**. Một biên tập viên đọc cover trước manuscript sẽ thấy tác giả không hiểu bài của chính mình. *(ijoem/jabs cover do agent viết sau — đã kiểm tra, không dính lỗi này.)*

Cùng file còn 2 lỗi:
- **Dòng 25:** *"P5, under review at IJOEM"* / *"P3, under review at JED"* — **sai sự thật** cho đến khi các bài đó thực sự được nộp. Nếu P9 nộp trước, đây là tuyên bố trạng thái giả → rủi ro liêm chính với editor. Phải sửa thành "manuscript in preparation/under submission preparation".
- **Dòng 40:** bảng differentiation ghi *"Up to **~22,000 obs**"* trong khi manuscript ghi **N = 28,717**.

### A2. P6 — Mô tả ICR dùng **thì quá khứ cho việc chưa xảy ra**
`p6/submission/jim_package/01_manuscript_blinded.md:919` (cả 4 package):
> *"the two authors independently **coded** a 20% stratified subsample… agreement **was assessed** with Cohen's κ… Disagreements **were resolved** by discussion"*

— trong khi 6 ô giá trị vẫn là `[insert after dual-coding]`. Văn bản **khẳng định một quy trình đã hoàn tất nhưng thực tế chưa làm**. Đây đúng loại lỗi "OSF preceded extraction" đã từng phải sửa. Nếu nộp khi quên điền, đây là tuyên bố sai. **Sửa:** chuyển sang thì mô tả protocol ("are independently coded… agreement is assessed…") hoặc tương lai, và chỉ chuyển sang quá khứ khi κ/ICC đã có thật.

### A3. P6 — Tàn dư **"third reviewer / two screeners" mâu thuẫn nhóm 2 tác giả**
- `jim:604`, `ibr:636`, `jwb:636`: *"Disagreements at both stages were resolved by **a third reviewer**"*
- `apjm:196`: *"**Two screeners** applied criteria… with **a third reviewer** adjudicating"*
- `p6/osf/P6_OSF_Preregistration_Template.md:54`: *"Two independent screeners… a third reviewer adjudicating"*

Bài có **2 tác giả**. Ai là người thứ ba? Mâu thuẫn trực diện với khung ICR mới (tác giả 1 mã toàn bộ; tác giả 2 mã kép 20%). Reviewer sẽ hỏi ngay; nếu không có người thứ ba thật, đây là mô tả quy trình không có thực.

### A4. P6 — **OSF template lệch pha với manuscript đã reframe**
`p6/osf/P6_OSF_Preregistration_Template.md` §5 vẫn mô tả chiến lược **census WoS+Scopus đầy đủ** kèm *"validated against a 30-paper known-item set (recall 29/30 = 97%)"* và §6 "two screeners + third reviewer" — trong khi cả 4 manuscript đã chuyển sang **citation-anchored bounded search**. Checklist đang hướng dẫn NCS đăng ký template này: nếu đăng ký nguyên trạng, **OSF registration và manuscript mâu thuẫn nhau công khai, có timestamp** — tệ hơn không đăng ký. Template **phải được cập nhật trước khi đăng ký OSF**. Tương tự, `thesis/p6_prisma_protocol.md:177` ("2 reviewers độc lập sàng lọc") trong luận án cũng cần đồng bộ.

---

## B. PHÁT HIỆN LỚN (MAJOR)

### B1. Bản dịch VI **lệch pha** với EN sau các vòng sửa (đã kiểm chứng từng file)
| File VI | Bằng chứng lệch |
|---|---|
| `p9_india_vi.md` | chứa **cả** 28.742 (cũ) **và** 28.717 (mới) → tự mâu thuẫn nội bộ; abstract bản dài chưa rút gọn; danh mục TLTK trước khi gỡ 13 orphan |
| `p5_china_vi.md` | còn nguyên đoạn **"217 panel core"** đã bị xóa khỏi EN (và bị chính audit dữ liệu bác bỏ) |
| `p6_meta_vi.md` | còn count cũ **90/78** (×2) và **75** Medium; chưa có 91/79 |

VI là hồ sơ trình hội đồng — nếu hội đồng đối chiếu EN↔VI sẽ thấy số liệu khác nhau. **Sửa:** tái sinh các đoạn lệch (không cần dịch lại toàn bộ).

### B2. P8 — Kết luận vẫn nói *"robust support… from 959 firms"* **không kèm caveat N=209**
`p8/.../01_manuscript_blinded.md:282`. Caveat chỉ mới được thêm ở abstract + lần đầu trong §4. Một reviewer đọc Conclusion độc lập sẽ hiểu sai cơ sở ước lượng. Cần lặp ngắn gọn caveat ở Conclusion (cả 3 package).

### B3. P8 — Bảng 1 ghi **"N (firms)"** nhưng đếm **firm-year observations**
Fiji 165 trải 2 đợt 2009+2025 (không có panel linkage) → 165 là quan sát doanh nghiệp-năm, không chắc là doanh nghiệp duy nhất. Kế thừa từ wording gốc ("959 firms across multiple country-year waves") nhưng nên ghi "Obs." cho chính xác.

### B4. P9 — Package MIR dùng **abstract cấu trúc Emerald + mục "Highlights"** trong khi MIR (Springer) chuẩn là abstract một đoạn, không Highlights
Chính title page tự ghi *"standard MIR if Springer"* nhưng manuscript lại để Purpose/Design/Findings + Highlights (vốn là convention Elsevier). Mâu thuẫn tự khai. Cần bản abstract một-đoạn cho MIR (giữ structured cho IJOEM/JABS).

### B5. P4 — Câu làm rõ N=84 (complete-case của ~18% exporter) chỉ thêm vào **mbr**, chưa rà tương đương ở mir/apbr (phrasing khác nhưng cùng độ mơ hồ).

---

## C. PHÁT HIỆN NHỎ (MINOR)
1. P6 jim dòng 3 ghi tên tạp chí đích ngay trong bản blinded (một số editor không thích; vô hại).
2. P9 có **10 keywords** (nhiều tạp chí giới hạn 6–8).
3. Việc gỡ AI-tone là **thay từ đồng nghĩa** ("exceptional", "no comparable historical precedent" vẫn là siêu so sánh) — chấp nhận được về học thuật, nhưng nên hiểu đây là làm sạch bề mặt, không phải thay đổi bản chất lập luận.
4. P7 jibs còn tên file `02_title_page_source.md` / `03_cover_letter_source.md` (đã ghi chú trong UPLOAD_INDEX, nên đổi tên hẳn).

---

## D. NGHI VẤN ĐÃ KIỂM CHỨNG VÀ **BÁC BỎ** (minh bạch quy trình)
1. ~~P3 lệch số giữa các package (jed sửa TP 41.6, mbr/jabs/thunderbird còn 42.0)~~ — **Bác bỏ**: mbr/jabs/thunderbird không chứa TP wave-specific lẫn ref Wolfolds (nội dung rút gọn khác jed); không có lệch.
2. ~~P5: xóa "217 panel core" có thể sai chiều (nếu 217 là thật và code cluster theo idstd)~~ — **Bác bỏ, fix được xác nhận đúng**: `04_run_models.do` dùng `vce(robust)` (không cluster idstd), và chính `03_build_pooled.do:58` ghi audit *"[WARN] Verified Python found 0 duplicate idstd"* — tức claim 217 panel core là **sai so với dữ liệu**, việc xóa là chính xác.

---

## E. KẾT LUẬN PHẢN BIỆN
Khối lượng triển khai lớn và phần "vệ sinh bản thảo" rất tốt, nhưng vòng phản biện này tìm ra **4 lỗi CRITICAL thật** — đáng chú ý là chúng cùng một bản chất: **văn bản khẳng định điều chưa/không xảy ra** (cover letter kể câu chuyện ngược kết quả; ICR thì quá khứ; "third reviewer" không tồn tại; OSF template kể chiến lược search cũ). Đây là loại lỗi nguy hiểm nhất với editor/hội đồng vì nó chạm vào **độ tin cậy của tác giả**, không phải hình thức.

**Thứ tự sửa đề xuất:** A1 (P9 MIR cover) → A2+A3 (P6 ICR tense + third reviewer, 4 package) → A4 (OSF template + protocol luận án) → B1 (đồng bộ VI) → B2–B5.

*Người phản biện lưu ý: các lỗi A1–A4 đều do chính quá trình tự động hóa trước đó tạo ra hoặc bỏ sót — báo cáo này là một phần của chu trình tự kiểm soát chất lượng, và mọi phát hiện đều kèm bằng chứng tái kiểm chứng được.*
