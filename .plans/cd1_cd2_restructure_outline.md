# Outline restructure CĐ1 + CĐ2 sang chuẩn mục CTU

> **Mục tiêu**: Chuyển CĐ1 + CĐ2 từ structure CHƯƠNG (chapter) sang MỤC (section) theo chuẩn CTU per `NCS_Huong_dan_viet_TLTQ.docx` + QĐ 1799/QĐ-ĐHCT.
>
> **Trạng thái**: ⏳ Đang chờ NCS approve outline trước khi implement.

---

## Phần 1: CĐ1 outline mapping (3 files → 3 files với mục headers)

### Nguồn → Đích (mapping chi tiết)

| File hiện tại | Heading hiện tại | → | Heading mới (chuẩn CTU) | Hành động |
|---|---|---|---|---|
| **`14_cd1_part1`** | `# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 1: BÌA, TÓM TẮT, CHƯƠNG 1–3)` | → | `# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — PHẦN 1: THÔNG TIN CHUNG + §2.1 ĐẶT VẤN ĐỀ + §2.2 PHƯƠNG PHÁP NGHIÊN CỨU` | Title rename |
|  | `## TRANG BÌA` | → | (giữ nguyên trong **PHẦN 1: THÔNG TIN CHUNG**) | Add wrapper |
|  | `## LỜI CAM ĐOAN` | → | (giữ trong Phần 1) | Add wrapper |
|  | `## TÓM TẮT` | → | (giữ trong Phần 1) | — |
|  | `## ABSTRACT` | → | (giữ trong Phần 1) | — |
|  | `## MỤC LỤC` | → | (giữ trong Phần 1; regenerate khi rebuild) | Update sau |
|  | `## DANH MỤC BẢNG / HÌNH / TỪ VIẾT TẮT` | → | (giữ trong Phần 1) | — |
|  | `## CHƯƠNG 1 — GIỚI THIỆU` | → | `## PHẦN 2 — NỘI DUNG CHUYÊN ĐỀ` + `### 2.1 Đặt vấn đề` | Wrap + rename |
|  | `### 1.1 Đặt vấn đề` (in Chương 1) | → | `#### 2.1.1 Giới thiệu` | Rename |
|  | `### 1.2 Mục tiêu chuyên đề` | → | `#### 2.1.2 Mục tiêu` | Rename |
|  | `### 1.3 Phạm vi và đối tượng nghiên cứu` | → | `#### 2.1.4 Giới hạn của chuyên đề` | Rename |
|  | `### 1.4 Phương pháp tiếp cận` | → | `#### 2.1.3 Nội dung` | Rename + content reorder |
|  | `### 1.5 Đóng góp dự kiến của chuyên đề` | → | `#### 2.1.5 Ý nghĩa` | Rename |
|  | `### 1.6 Kết cấu chuyên đề` | → | (xóa hoặc gộp vào 2.1.3) | Merge |
|  | `## CHƯƠNG 2 — CƠ SỞ LÝ LUẬN VỀ HIỆU QUẢ HOẠT ĐỘNG KINH DOANH` | → | `### 2.2 Phương pháp nghiên cứu` + `#### 2.2.1 Cơ sở lý luận về hiệu quả hoạt động kinh doanh` | Wrap + rename |
|  | `### §2.6 ĐIỀU KIỆN BIÊN CHO U-CURVE LU & BEAMISH (2004)` | → | `##### 2.2.1.1 Điều kiện biên cho U-curve` | Rename (giữ nội dung) |
|  | `### §2.7 KHUNG 4-TIER CHUYỂN ĐỔI SỐ + CDCM` | → | `##### 2.2.1.2 Khung 4-Tier chuyển đổi số + CDCM` | Rename |
|  | `## CHƯƠNG 3 — KHUNG PHÂN LOẠI 6 PHÂN NHÓM CON ICRV` | → | `#### 2.2.2 Khung phân loại 6 sub-regime ICRV` | Demote chương → tiểu mục |
|  | (cần thêm) | → | `#### 2.2.3 Nguồn dữ liệu WBES và phương pháp mô tả-chẩn đoán` | NEW (viết mới ~150 từ) |
| **`15_cd1_part2`** | `# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 2: CHƯƠNG 4)` | → | `# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — PHẦN 2 (tiếp): §2.3 KẾT QUẢ VÀ THẢO LUẬN (Thực trạng tổng thể)` | Title rename |
|  | `## CHƯƠNG 4 — THỰC TRẠNG HIỆU QUẢ DOANH NGHIỆP CHÂU Á 2009–2025` | → | `### 2.3 Kết quả và thảo luận` + `#### 2.3.1 Thực trạng tổng thể hiệu quả doanh nghiệp châu Á 2009-2025` | Wrap + rename |
|  | (tất cả §4.1 - §4.7 sub-headings) | → | (giữ với numbering 2.3.1.1, 2.3.1.2, ...) | Renumber tiểu mục |
| **`16_cd1_part3`** | `# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 3: CHƯƠNG 5–7 + TLTK + Phụ lục)` | → | `# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — PHẦN 2 (tiếp): §2.3 (tiếp) + §2.4 KẾT LUẬN VÀ ĐỀ XUẤT + TLTK + PHỤ LỤC` | Title rename |
|  | `## CHƯƠNG 5 — BẢY TIỂU CẢNH ĐIỂN HÌNH` | → | `#### 2.3.2 Bảy tiểu cảnh điển hình` | Demote |
|  | `### 5.1 Singapore` ... `### 5.8 So sánh tổng hợp` | → | `##### 2.3.2.1 Singapore` ... `##### 2.3.2.8 So sánh tổng hợp` | Renumber |
|  | `## CHƯƠNG 6 — CÁC YẾU TỐ GIẢI THÍCH SƠ BỘ` | → | `#### 2.3.3 Các yếu tố giải thích sơ bộ` | Demote |
|  | `### 6.1 Pattern giới tính` | → | `##### 2.3.3.1 Pattern giới tính` | Renumber |
|  | `### 6.2 Đường cong U của innovation` | → | `##### 2.3.3.2 Đường cong U của innovation` | Renumber |
|  | `### 6.3 OECD MAGIC` | → | `##### 2.3.3.3 Bối cảnh OECD MAGIC` | Renumber |
|  | `### 6.4 OECD Economic Outlook` | → | `##### 2.3.3.4 Bối cảnh OECD Economic Outlook` | Renumber |
|  | `## CHƯƠNG 7 — KHOẢNG TRỐNG THỰC TIỄN VÀ KẾT LUẬN` | → | `### 2.4 Kết luận và đề xuất` | Wrap (chương → mục lớn) |
|  | `### 7.1 Khoảng trống NC thực tiễn` | → | `#### 2.4.1 Khoảng trống nghiên cứu thực tiễn` | Renumber |
|  | `### 7.2 Kết luận chính (8 kết luận)` | → | `#### 2.4.2 Kết luận chính` | Renumber |
|  | `### 7.3 Hàm ý cho luận án và CĐ2` | → | `#### 2.4.3 Hàm ý cho luận án và Chuyên đề 2` | Renumber |
|  | `### 7.4 Hạn chế của chuyên đề` | → | `#### 2.4.4 Hạn chế của chuyên đề` | Renumber |
|  | `### 7.5 Kế hoạch hoàn thiện` | → | `#### 2.4.5 Kế hoạch hoàn thiện` | Renumber |
|  | `## TÀI LIỆU THAM KHẢO` | → | `## TÀI LIỆU THAM KHẢO` | Giữ nguyên |
|  | `## PHỤ LỤC` | → | `## PHỤ LỤC` | Giữ nguyên |

### Tóm tắt thay đổi CĐ1

- **3 chương** (1+2+3) → **2 mục lớn** (§2.1 + §2.2)
- **1 chương** (4) → **1 tiểu mục cấp 4** (§2.3.1)
- **3 chương** (5+6+7) → **2 tiểu mục cấp 4 + 1 mục lớn** (§2.3.2 + §2.3.3 + §2.4)
- **Total: 7 chương → 4 mục (2.1, 2.2, 2.3, 2.4) + tiểu mục cấp 3-5**
- **Content preserved 100%**, chỉ rename headers + add wrappers
- **Cần viết mới ~150 từ** cho §2.2.3 (Nguồn dữ liệu WBES + phương pháp)
- Effort estimate: **~2 hours** (mechanical heading renames + verify)

---

## Phần 2: CĐ2 outline mapping (1 file → 1 file với mục headers)

### Nguồn → Đích

| Heading hiện tại | → | Heading mới (chuẩn CTU) | Hành động |
|---|---|---|---|
| `# Khung lý thuyết và hệ giả thuyết` | → | `# CHUYÊN ĐỀ TIẾN SĨ SỐ 2 — XÂY DỰNG MÔ HÌNH NGHIÊN CỨU VỀ ẢNH HƯỞNG CỦA QUỐC TẾ HÓA ĐẾN HIỆU QUẢ HOẠT ĐỘNG KINH DOANH CỦA CÁC DOANH NGHIỆP Ở CHÂU Á` | Tên đầy đủ theo QĐ 4768 |
| (chưa có) | → | `## PHẦN 1 — THÔNG TIN CHUNG` | Add Phần 1 wrapper |
| (chưa có) | → | `### TRANG BÌA` (link `templates/cover_pages/09_trang_bia_chuyen_de_2.md`) | NEW (≈ template) |
| (chưa có) | → | `### LỜI CAM ĐOAN` | NEW (~120 từ) |
| (chưa có) | → | `### TÓM TẮT` (300-500 từ) | NEW (~400 từ) |
| (chưa có) | → | `### ABSTRACT` (EN, 300-500 từ) | NEW (~400 từ) |
| (chưa có) | → | `### MỤC LỤC` | NEW (auto-generate) |
| (chưa có) | → | `### DANH MỤC BẢNG / HÌNH / TỪ VIẾT TẮT` | NEW (~50 từ mỗi danh mục) |
| (chưa có) | → | `## PHẦN 2 — NỘI DUNG CHUYÊN ĐỀ 2` | Add Phần 2 wrapper |
| `## 1. Logic xây dựng khung lý thuyết` | → | `### 2.1 Đặt vấn đề` | Wrap + rename |
| (cần phân chia trong §1) | → | `#### 2.1.1 Giới thiệu` (paragraphs 1-2 of §1) | Restructure |
|  | → | `#### 2.1.2 Mục tiêu của chuyên đề 2` | NEW (~80 từ) |
|  | → | `#### 2.1.3 Nội dung chuyên đề` | NEW (~80 từ) |
|  | → | `#### 2.1.4 Giới hạn nghiên cứu` | NEW (~80 từ) |
|  | → | `#### 2.1.5 Ý nghĩa khoa học và thực tiễn` | NEW (~120 từ) |
| `## 2. Bốn lý thuyết nền` | → | `### 2.2 Phương pháp nghiên cứu` + `#### 2.2.1 Bốn lý thuyết nền của khung tích hợp` | Wrap + rename |
| `### 2.1 Mô hình quốc tế hóa Uppsala` | → | `##### 2.2.1.1 Mô hình Uppsala (Uppsala Internationalization Model)` | Renumber |
| `### 2.2 RBV` | → | `##### 2.2.1.2 Quan điểm dựa trên nguồn lực (Resource-Based View)` | Renumber |
| `### 2.3 Institutional Theory` | → | `##### 2.2.1.3 Lý thuyết thể chế (Institutional Theory)` | Renumber |
| `### 2.4 Upper Echelons Theory` | → | `##### 2.2.1.4 Lý thuyết tầng lớp lãnh đạo (Upper Echelons Theory)` | Renumber |
| `## 3. Lớp mở rộng: Lăng kính năng lực số` | → | `#### 2.2.2 Lớp mở rộng: Lăng kính năng lực số (Digital Capability Lens)` | Demote |
| `## 3.5 Vị thế của lớp năng lực số trong khung CIMT-ICRV-CDCM` | → | `#### 2.2.3 Khung phân tầng CIMT–ICRV–CDCM` | Demote + retitle |
| `## 6. Ánh xạ giả thuyết sang phương pháp` | → | `#### 2.2.4 Ánh xạ giả thuyết H1-H6 sang phương pháp kiểm định` | Demote + renumber (move up) |
| `## 4. Mô hình khái niệm tích hợp` | → | `### 2.3 Kết quả và thảo luận` + `#### 2.3.1 Mô hình khái niệm tích hợp` | Wrap + demote |
| `## 5. Hệ giả thuyết H1–H6` | → | `#### 2.3.2 Hệ giả thuyết H1–H6` | Demote |
| `### H1: Phi tuyến chữ U ngược` | → | `##### 2.3.2.1 H1 — Phi tuyến chữ U ngược` | Renumber |
| `### H1b: Điều kiện biên` | → | `##### 2.3.2.2 H1b — Điều kiện biên SIDS/FIP` | Renumber |
| `### H2: TCI moderation` | → | `##### 2.3.2.3 H2 — TCI moderation` | Renumber |
| `### H3: DAI moderation` | → | `##### 2.3.2.4 H3 — DAI moderation` | Renumber |
| `### H4: Upper Echelons control` | → | `##### 2.3.2.5 H4 — Upper Echelons control` | Renumber |
| `### H5: ICRV moderation` | → | `##### 2.3.2.6 H5 — ICRV moderation` | Renumber |
| `### H6: Dị biệt thời gian` | → | `##### 2.3.2.7 H6 — Dị biệt thời gian` | Renumber |
| (cần thêm) | → | `#### 2.3.3 Thảo luận về tính nhất quán của khung phân tầng với văn liệu hiện hành` | NEW (~300 từ) |
| `## 7. Kết nối với tài liệu nghiên cứu quốc tế` | → | `### 2.4 Kết luận và đề xuất` + `#### 2.4.1 Kết nối với tài liệu IB quốc tế` | Wrap + rename |
| (cần thêm) | → | `#### 2.4.2 Đóng góp lý thuyết` | NEW (~200 từ) |
| (cần thêm) | → | `#### 2.4.3 Hàm ý cho luận án và nghiên cứu thực nghiệm` | NEW (~200 từ) |
| (cần thêm) | → | `#### 2.4.4 Hạn chế và hướng nghiên cứu tiếp theo` | NEW (~150 từ) |
| (cần thêm cuối file) | → | `## TÀI LIỆU THAM KHẢO` (link `04_references_apa7.md`) | Add cross-reference |
| (cần thêm) | → | `## PHỤ LỤC` | NEW (optional) |

### Tóm tắt thay đổi CĐ2

- **0 chương** → **4 mục lớn** (§2.1 + §2.2 + §2.3 + §2.4)
- **7 sections** hiện tại → restructured thành các tiểu mục cấp 4-5
- **Cần bổ sung**:
  - PHẦN 1 hoàn toàn mới (~1,200 từ tổng cho front matter)
  - §2.1.2-2.1.5 (~360 từ tổng)
  - §2.2.4 ánh xạ method (chuyển từ §6 hiện tại, không phải mới)
  - §2.3.3 thảo luận (~300 từ)
  - §2.4.2-2.4.4 (~550 từ)
  - **Tổng content mới cần viết: ~2,400 từ**
- **Content cũ preserved**, chỉ rename headers + add wrappers + content mới ở các phần thiếu
- Effort estimate: **~3-4 hours** (heading restructure + viết các phần mới)

---

## Tổng effort estimate

| Task | Effort |
|---|---|
| CĐ1 restructure (3 files, mechanical heading rename + 150 từ mới) | 2 hours |
| CĐ2 restructure (1 file, heading rename + ~2,400 từ mới) | 3-4 hours |
| Verify + humanizer audit + em-dash check | 30 min |
| Build DOCX + sync dist/SUBMISSION_FINAL | 15 min |
| Commit + push | 15 min |
| **TOTAL** | **~6-7 hours** |

---

## Quyết định cần NCS approve

1. **CĐ1**: Đồng ý mapping trên (3 chương → 4 mục)?
2. **CĐ2**: Đồng ý mapping trên (7 sections → 4 mục, + ~2,400 từ mới cho front matter + thảo luận + kết luận)?
3. **File structure**: Giữ 3 files CĐ1 (14/15/16) cho git history, hay merge thành 1 file?
4. **CĐ2 front matter**: Cần TRANG BÌA + LỜI CAM ĐOAN + TÓM TẮT + ABSTRACT + MỤC LỤC + DANH MỤC riêng (theo chuẩn CTU)?
5. **§2.2.3 + §2.2.4 thứ tự**: §2.2.3 Khung CIMT-ICRV-CDCM trước, hay §2.2.3 Ánh xạ phương pháp trước? (Tôi đề xuất Khung trước, ánh xạ sau vì khung là input cho ánh xạ.)

NCS approve outline này thì tôi implement luôn. Hoặc NCS muốn điều chỉnh chỗ nào, ghi cụ thể tôi update outline trước khi implement.
