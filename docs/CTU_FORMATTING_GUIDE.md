# CTU PhD Dissertation — Formatting Guide

> Áp dụng cho luận án tiến sĩ tại **Trường Kinh tế, Đại học Cần Thơ (CTU)**.
> Tham chiếu: Quy chế đào tạo TS CTU + chuẩn chung của các trường ĐH VN.
>
> **⚠ NCS lưu ý:** Tài liệu này áp dụng chuẩn chung phổ biến cho luận án TS VN do **không có template chính thức CTU** trong repo. Nếu Phòng Đào tạo Sau đại học CTU có file template hoặc Quy chế cập nhật 2026 với yêu cầu khác (đặc biệt về layout trang bìa, line spacing chính xác, hoặc heading numbering), NCS share để cập nhật.
>
> Cập nhật cuối: 2026-06-03 (post commit `2db8cc5`).

---

## 1. Quy cách trình bày chung

| Mục | Chuẩn CTU | Hiện trạng repo |
|---|---|---|
| Khổ giấy | A4 (21 × 29,7 cm) | ✅ `templates/ctu_thesis_*.docx` |
| Lề trên | 2,0 – 2,5 cm | ✅ 2 cm |
| Lề dưới | 2,0 – 2,5 cm | ✅ 2 cm |
| Lề trái (đóng bìa) | 3,0 – 3,5 cm | ✅ 3 cm |
| Lề phải | 2 cm | ✅ 2 cm |
| Font chữ | Times New Roman | ✅ |
| Cỡ chữ body | 13 pt | ✅ |
| Cỡ chữ heading 1 (CHƯƠNG) | 14–16 pt bold, viết hoa, căn giữa | ⚠ Strict template: 16pt; default: 13pt |
| Cỡ chữ heading 2 (Mục 1.1) | 13–14 pt bold | ⚠ Strict: 14pt; default: 13pt |
| Cỡ chữ heading 3 (Mục 1.1.1) | 13 pt bold italic | ✅ |
| Giãn dòng (line spacing) | **1,5 lines** | ❌ Default template: 1,2; ✅ Strict template: 1,5 |
| Căn lề | Both (justify) | ✅ |
| Lề đầu dòng (first-line indent) | 1 cm (hoặc tab) | ⚠ Strict template: 1cm; default: 0 |
| Đánh số trang | Bottom-center | ✅ pandoc default |
| Đánh số chương | Chương 1, Chương 2... | ✅ |

---

## 2. Cấu trúc bắt buộc

| Phần | Trang | Ghi chú |
|---|---|---|
| 1. **Trang bìa** | i (Roman) | NCS + tên đề tài + tên Trường + năm |
| 2. **Trang bìa phụ** | ii | + tên người hướng dẫn + mã NCS |
| 3. **Lời cam đoan** | iii | NCS ký tên |
| 4. **Lời cảm ơn** | iv-v | Tùy chọn |
| 5. **Tóm tắt tiếng Việt** | vi-vii | 250–500 từ |
| 6. **Abstract** (EN) | viii-ix | 250–500 từ |
| 7. **Mục lục** | x-xii | Auto-generated |
| 8. **Danh mục bảng** | xiii | |
| 9. **Danh mục hình** | xiv | |
| 10. **Danh mục ký hiệu viết tắt** | xv | TCI, DAI, FSTS, ICRV, CIMT, CDCM, etc. |
| 11. **Phần nội dung** (Ch.1–5) | 1+ (Arabic) | Bắt đầu page 1 Arabic |
| 12. **Tài liệu tham khảo** | sau Ch.5 | APA 7 |
| 13. **Phụ lục** | sau References | Bảng dữ liệu, code, etc. |
| 14. **Danh mục công trình** | cuối | Bài báo + chuyên đề đã công bố |

---

## 3. Cấu trúc 5 chương (CTU PhD standard)

| Chương | Tên chuẩn CTU | Files hiện tại |
|---|---|---|
| 1 | Giới thiệu | `chuong_1_gioi_thieu_vi.md` ✅ |
| 2 | Tổng quan tài liệu | `chuong_2_tong_quan_tai_lieu_vi.md` ✅ |
| 3 | Phương pháp nghiên cứu | `chuong_3_phuong_phap_vi.md` ✅ |
| 4 | Kết quả nghiên cứu | `chuong_4_ket_qua_vi.md` ✅ |
| 5 | Kết luận và đề xuất | `chuong_5_ket_luan_de_xuat_vi.md` ✅ |

Mỗi chương cần có:
- Đoạn **giới thiệu chương** (chapter intro paragraph)
- Các **mục đánh số** (1.1, 1.2, 1.1.1, etc.)
- Đoạn **tóm tắt chương** (chapter summary) cuối chương

---

## 4. Quy tắc bảng và hình

| Mục | Chuẩn CTU |
|---|---|
| Đánh số bảng | Bảng X.Y (X = số chương, Y = số thứ tự trong chương) |
| Đánh số hình | Hình X.Y |
| Caption bảng | **Đặt phía trên** bảng |
| Caption hình | **Đặt phía dưới** hình |
| Font caption | Times New Roman 11–12 pt italic |
| Nguồn (Source) | Cuối caption: "Nguồn: ..." |
| Đối với bảng/hình trích | "Nguồn: tác giả tổng hợp từ ..." hoặc cụ thể |

---

## 5. Tài liệu tham khảo

| Mục | Chuẩn CTU |
|---|---|
| Style | **APA 7th** (hoặc Harvard style nếu Phòng đào tạo yêu cầu) |
| Trình bày | Hanging indent 1,27 cm |
| Sắp xếp | Alphabetical theo tên tác giả |
| Phân biệt | Tài liệu tiếng Việt riêng / tiếng Anh riêng (tùy chọn) |

Hiện tại: `thesis/04_references_apa7.md` dùng APA 7 với hanging indent ✓.

---

## 6. Hai template DOCX trong repo

| File | Line spacing | First-line indent | Heading 1 size | Khi nào dùng |
|---|:-:|:-:|:-:|---|
| `templates/ctu_thesis_reference.docx` | 1,2 lines | 0 | 13pt | Default (legacy build) |
| **`templates/ctu_thesis_strict.docx`** | **1,5 lines** ✅ | **1 cm** ✅ | **16pt** ✅ | **CTU PhD strict format** — recommended for final submission |

Để build với template strict:
```bash
pandoc thesis/chuong_2_tong_quan_tai_lieu_vi.md \
  -o thesis/chuong_2_tong_quan_tai_lieu_vi.docx \
  --reference-doc=templates/ctu_thesis_strict.docx
```

Hoặc rebuild toàn bộ:
```bash
bash scripts/build_ctu_thesis_strict.sh
```

---

## 7. Còn cần xác nhận từ Phòng đào tạo SĐH CTU

Vì không có template chính thức trong repo, các điểm sau cần NCS kiểm tra với Phòng đào tạo SĐH CTU:

1. **Layout trang bìa** chính xác (logo CTU, font size cụ thể, cách trình bày)
2. **Lời cam đoan + Lời cảm ơn** có template chuẩn không
3. **Heading numbering** có yêu cầu cụ thể không (1., 1.1., 1.1.1. vs 1.1.1)
4. **Đánh số bảng/hình** theo chương hay sequential toàn luận án
5. **Tóm tắt tiếng Việt** có cấu trúc bắt buộc không (Mục tiêu / Phương pháp / Kết quả / Kết luận)
6. **References style** có chấp nhận APA 7 không, hay yêu cầu Harvard / GB/T 7714

Nếu Phòng đào tạo SĐH CTU có **file template `.docx` chính thức** hoặc **Quy chế trình bày luận án TS 2026**, NCS share lên repo để cập nhật `templates/ctu_thesis_strict.docx` chính xác hơn.

---

## 8. Reference materials nên thêm vào repo

Khi NCS có template + Quy chế chính thức từ Phòng đào tạo SĐH CTU:

```
docs/ctu_template_official/
├── mau_luan_an_TS_CTU.docx       (template chính thức)
├── quy_che_trinh_bay_2026.pdf    (quy chế text)
├── huong_dan_luan_an_TS.pdf      (hướng dẫn chi tiết)
└── README.md                      (NCS cập nhật khi share)
```

Sau khi NCS share, tôi sẽ:
1. Compare current `ctu_thesis_strict.docx` với template chính thức
2. Patch các discrepancies
3. Rebuild toàn bộ DOCX (5 chương + tom_tat + CĐ1 + CĐ2 + 7 papers)
4. Verify visual trong Word
