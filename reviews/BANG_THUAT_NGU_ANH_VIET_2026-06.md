# Bảng thuật ngữ Anh–Việt đề xuất — để cô DUYỆT trước khi áp đồng loạt

*Ngày: 2026-06-24 · Phạm vi áp dụng sau duyệt: 7 file nguồn (Ch1–Ch5 + CĐ1 + CĐ2)*

## ✅ TRẠNG THÁI: ĐÃ DUYỆT & ĐÃ ÁP (2026-06-24)
- **Mục A — Tier/Tầng:** cô chọn **"Bậc 1–4"**. Đã áp cho cả 7 file.
  - Phân biệt theo ngữ cảnh: chỉ "Tầng" nghĩa **bậc đo DAI** → "Bậc". GIỮ nguyên "Tầng"
    cho: bốn tầng lý thuyết (CĐ2:311–341), bốn bước phân tích (CĐ2:771–790), phân rã
    phương sai meta ba tầng (Ch4:172–173), và "nhà cung cấp Tầng 1" (CĐ1:903).
  - Tổng đổi: cd1 32 + cd2 12 (Tier-Anh); Tầng-DAI: ch1 2, ch2 1, ch3 46, ch4 36, ch5 20, cd1/cd2 nhiều.
- **Mục B — thuật ngữ:** ĐÃ áp. Tiếng Anh giữ trong ngoặc 1 lần ở lần đầu mỗi chương; tên
  kiểm định/mô hình/phần mềm/ký hiệu và **tiêu đề trích dẫn** giữ nguyên tiếng Anh.
  - **Điều chỉnh so với bảng gốc:** KHÔNG gộp "yếu tố vệ sinh" (hygiene factor) vào "bộ nâng
    mặt bằng" — đây là hai khái niệm khác nhau (DAI bão hòa vs vai trò TCI). Giữ riêng cả hai.
- **Mục D — sáo rỗng:** ĐÃ áp. "Nhìn chung/Đáng chú ý/Nói cách khác/Tổng hợp lại" về 0 ở cả 7 file;
  giảm "bức tranh"; "chữ ký"→"dấu hiệu đặc trưng".
- **Commit:** `41d465c` (cd1,cd2) · `b72ed8c` (ch3,ch4) · `a995db3` (ch1,ch2,ch5) — PR #17.

---

## Cách dùng bảng này
- Cột **Đề xuất Việt** là phương án em sẽ áp. Cô sửa thẳng vào cột này nếu muốn khác.
- Quy ước: dùng thuật ngữ Việt, **giữ tiếng Anh trong ngoặc đúng 1 lần** ở lần xuất hiện đầu
  mỗi chương, sau đó chỉ dùng Việt.
- Cột **Duyệt**: cô đánh `x` để đồng ý, hoặc ghi chú phương án khác.
- Sau khi cô duyệt, em áp đồng loạt + chuẩn hóa rồi commit theo từng file.

---

## A. ⚠️ Quyết định quan trọng nhất: "Tier" (bậc đo DAI) vs "Tầng" (tầng lý thuyết)

Hiện **"Tầng 1–4"** = bốn tầng lý thuyết (Uppsala, RBV, Thể chế, Thượng tầng quản trị);
**"Tier 1–4"** = các bậc đo lường DAI. Hai khái niệm cùng tồn tại nên **không gộp** được.

| Phương án | Mô tả | Duyệt |
|---|---|---|
| **(khuyến nghị) Bậc 1–4** | DAI dùng "Bậc 1/2/3/4", tách hẳn khỏi "Tầng" lý thuyết. Rõ ràng nhất. | [ ] |
| Giữ "Tier 1–4" | Giữ tiếng Anh cho DAI, chỉ chuẩn hóa cách viết (bỏ lẫn "Tier-1"/"Tier 1"). | [ ] |
| Phương án khác | (cô ghi rõ) | [ ] |

> Dù chọn cách nào, em sẽ chuẩn hóa ~34 chỗ đang viết lẫn gạch nối/cách trống cho nhất quán.

---

## B. Thuật ngữ trộn Anh–Việt trong văn xuôi (đề xuất Việt hóa)

| Tiếng Anh | Đề xuất Việt | Xuất hiện (file) | Duyệt |
|---|---|---|---|
| control variables | biến kiểm soát | Ch3 | [ ] |
| coverage | phạm vi | Ch3 *(đã áp 1 chỗ)* | [ ] |
| panel core | lõi panel | Ch3 | [ ] |
| cluster-robust SE | sai số chuẩn gom cụm | Ch3 | [ ] |
| two-way FE | hiệu ứng cố định hai chiều | Ch3 | [ ] |
| spec / specification | đặc tả | Ch3, Ch4 | [ ] |
| innovation-driven / resource-driven | đổi mới dẫn dắt / tài nguyên dẫn dắt | CĐ1 (~10), CĐ2 | [ ] |
| front-loading | tích trữ trước | CĐ1 | [ ] |
| downstream / mid-stream | hạ nguồn / trung nguồn | CĐ1 | [ ] |
| level-shift / level-shifter / "bộ tăng mức" / "yếu tố vệ sinh" | **bộ nâng mặt bằng** (thống nhất 1 thuật ngữ) | Ch3, Ch4, CĐ1, CĐ2 | [ ] |
| reshaping | định hình lại | Ch5, CĐ1 | [ ] |
| breadth / depth | bề rộng / chiều sâu | Ch5 | [ ] |
| two-sided | hai phía | CĐ2 (~6) | [ ] |
| sub-hypothesis | giả thuyết con | CĐ2 | [ ] |
| exploratory | thăm dò / khám phá | CĐ2 | [ ] |
| magnitude | độ lớn | CĐ1, CĐ2 | [ ] |
| distinctiveness | tính phân biệt | CĐ2 | [ ] |
| website presence | sự hiện diện trang web | CĐ2 | [ ] |
| digital shield | lá chắn số | Ch2, CĐ2 | [ ] |
| null moderation | điều tiết không có ý nghĩa | Ch4 | [ ] |
| dynamism profile | hồ sơ động lực ngành | CĐ1 | [ ] |
| "chữ ký" (signature, ẩn dụ) | dấu hiệu đặc trưng | Ch4 | [ ] |

---

## C. Giữ NGUYÊN tiếng Anh (thuật ngữ/định danh chuẩn — KHÔNG dịch)

ICRV, FSTS, TCI, DAI, FIP, CDCM, WBES, OLS, IV, 2SLS, FE; tên kiểm định (Lind–Mehlum,
Paternoster, Egger); tên mô hình M0–M7; tên phần mềm (reghdfe, pyfixest); ký hiệu thống kê
($r$, $I^2$, $Q_M$, $\beta$, $p$). Các cụm này chỉ chèn tên đầy đủ + viết tắt lần đầu.

---

## D. Khử sáo rỗng / giọng AI (đề xuất, áp cùng đợt nếu cô đồng ý)

| Mẫu | Xử lý | Duyệt |
|---|---|---|
| "Nhìn chung," (mở đoạn) | bỏ, vào thẳng luận điểm | [ ] |
| "Đáng chú ý," / "Đáng chú ý là" | bỏ hoặc thay bằng nội dung cụ thể | [ ] |
| "Nói cách khác," (Ch5 ×4) | thay "Cụ thể hơn," hoặc gộp câu | [ ] |
| "Tổng hợp lại," (Ch2, lặp) | đa dạng hóa từ nối kết đoạn | [ ] |
| "bức tranh …" (danh từ rỗng) | "thực trạng/toàn cảnh/phân bố" — giảm tần suất | [ ] |
| "cốt lõi" (nhấn rỗng, lặp) | diễn đạt cụ thể | [ ] |
| Chuỗi "thứ N" quá dày (Ch1, Ch5) | giữ cấu trúc, đa dạng hóa vài mở đoạn | [ ] |

---

## Sau khi cô duyệt
Em sẽ: (1) áp bảng B+D cho cả 7 file theo quy ước Anh-trong-ngoặc-lần-đầu; (2) chuẩn hóa
Tier/Tầng theo phương án mục A; (3) commit theo từng file; (4) đề xuất chạy
`scripts/build_latex_ctu.sh` để đồng bộ .tex/PDF.
