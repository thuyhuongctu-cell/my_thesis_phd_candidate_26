# P6 — Báo cáo trạng thái kết quả, kế hoạch nâng cấp & điều chỉnh đăng ký sở hữu trí tuệ (25/05/2026)

> Phạm vi: Paper 6 — "Institutional Context, Digital Adoption, and the Internationalization–Performance
> Relationship: A Three-Level Meta-Analysis" (Đỗ Thùy Hương & Phan Anh Tú, Trường Kinh tế, ĐH Cần Thơ).
> Liên quan **Chương 2** luận án (cơ sở lý thuyết & phương pháp tổng hợp tài liệu).

---

## PHẦN A — TRẠNG THÁI KẾT QUẢ HIỆN TẠI (đã xác minh)

### A1. Phạm vi dữ liệu
- **k = 238 nghiên cứu sơ cấp**, **K = 288 mức ảnh hưởng (effect sizes)**, 49 nền kinh tế, giai đoạn 1977–2026.
- Quy trình PRISMA 2020; tìm kiếm trên Web of Science + Scopus.
- Mô hình: **phân tích tổng hợp hồi quy ba tầng (three-level MARA)** (Cheung, 2014; Van den Noortgate et al., 2013) bằng `metafor` (R).
- Tiền đăng ký **OSF**: https://osf.io/z37kn (DOI 10.17605/OSF.IO/Z37KN) — đăng ký 18/05/2026, đang hoạt động.

### A2. Kết quả nền (baseline)
- Hiệu ứng gộp **r̄ = 0,074** (95% CI [0,060, 0,088], p < ,001).
- Dị biệt **I² = 62,4%** (Tầng 2 trong-nghiên-cứu 54,1% — chủ đạo; Tầng 3 giữa-nghiên-cứu 8,4%).
- Tái lập và mở rộng mốc ICBEF 2025 (r = 0,07, k = 113).

### A3. Kiểm định ba giả thuyết điều tiết
| Yếu tố điều tiết | Thống kê | Kết luận |
|---|---|---|
| **ICRV** (6 nhóm chế độ thể chế) | Q_M = 17,35 (df = 4, p = ,002) | Omnibus **có ý nghĩa**, NHƯNG bị chi phối bởi ô Frontier thưa (k = 3); **gradient định hướng E1a/E1b CHƯA xác nhận** |
| **cDAI** (áp dụng số cấp quốc gia) | Q_M = 1,23 (p = ,541) | Không có ý nghĩa |
| **DPL** (giai đoạn Digital Paradox Lifecycle) | Q_M = 0,56 (p = ,755) | Không có ý nghĩa |

### A4. Sai lệch xuất bản (publication bias)
- Begg τ = −0,134 (p = ,0007); Egger b = 0,475 (p = ,057 — biên).
- Trim-and-fill: chèn k = 58 nghiên cứu thiếu → **r_adj = 0,035** (95% CI [0,023, 0,048]) — dương nhưng suy giảm.

### A5. Thông điệp khoa học & hạn chế hiện tại
- Đóng góp: meta-analysis ba tầng đầu tiên của I→P kiểm định đồng thời ICRV, cDAI, DPL.
- **Hạn chế then chốt**: ba giả thuyết điều tiết có bằng chứng yếu/chưa xác nhận; sai lệch xuất bản đáng kể. Phát hiện tái định khung "câu đố dị biệt": phương sai chưa giải thích của I→P có thể phản ánh **lựa chọn phía xuất bản** nhiều hơn là điều tiết thể chế/số.
- **Trạng thái nộp**: tập hand-coded (k = 238) đã xác minh, tái lập được toàn bộ bảng/hình → sẵn sàng nộp **International Business Review (IBR)**; hồ sơ trong `p6/submission/ibr_package/`.

---

## PHẦN B — KẾ HOẠCH NÂNG CẤP / BỔ SUNG KẾT QUẢ MỚI HƠN + OSF

### B1. Nguồn bổ sung đã chuẩn bị
- **`p6/p6_screening_candidates_20260525.md`**: 24 ứng viên nghiên cứu sơ cấp thực nghiệm 2020–2025 đủ điều kiện sơ bộ (kèm DOI) + 11 ứng viên biên cần đọc toàn văn.
- 7 meta-analysis mới hơn (Aydemir 2024, Schüler 2024, Fan et al. 2024, Tihanyi 2005, Perry 2011, Tashman 2022, Sharma 2023) → dùng cho **benchmarking/tổng quan**, KHÔNG tính vào k.

### B2. Quy trình nâng cấp (6 bước)
1. **Sàng lọc toàn văn** 24 (+11 biên) ứng viên theo tiêu chí PRISMA (DV là hiệu quả; trích xuất được r).
2. **Trích xuất effect size** bằng hệ thống **M-AIDA** (PDF → LLM → confidence scoring → PI verify → lock → CSV).
3. **PI xác minh + khóa** (pi_locked) từng bản ghi để bảo đảm tính toàn vẹn dữ liệu.
4. **Chạy lại three-level MARA** với k mở rộng (238 → dự kiến ~260+); cập nhật r̄, I², phân rã tầng.
5. **Kiểm định lại điều tiết** — ưu tiên **lấp ô chế độ thể chế thưa** (Frontier/SIDS) để kiểm định trực tiếp gradient ICRV E1a/E1b hiện chưa xác nhận.
6. **Cập nhật chẩn đoán sai lệch xuất bản** (Begg/Egger/trim-and-fill) trên tập mở rộng.

### B3. Cập nhật OSF (giữ tính minh bạch tiền đăng ký)
- Nộp **bản hiệu đính (amendment/update)** cho đăng ký z37kn, ghi rõ:
  - Mở rộng **mốc tìm kiếm đến 2026** và danh sách nghiên cứu bổ sung.
  - Phân biệt rõ phần **khẳng định (confirmatory)** theo tiền đăng ký gốc và phần **thăm dò (exploratory)** mới.
- Tải lên OSF các **component**: tập dữ liệu mở rộng (CSV đã khóa), sơ đồ PRISMA cập nhật, log M-AIDA, mã R (`metafor`).
- Giữ nguyên bản preregistration gốc; mọi thay đổi phân tích đều có dấu vết (audit trail).

> Lưu ý liêm chính học thuật: bổ sung studies mới làm thay đổi k/K và có thể đổi kết luận về moderator;
> phải nêu rõ trong manuscript là cập nhật sau tiền đăng ký, không trình bày như phân tích khẳng định gốc.

---

## PHẦN C — ĐIỀU CHỈNH ĐĂNG KÝ SỞ HỮU TRÍ TUỆ (M-AIDA) — gắn Chương 2

### C1. Hiện trạng
- Hệ thống **M-AIDA v7.0.0** (Meta-Analysis Intelligent Data Assistant) — phần mềm trích xuất dữ liệu thống kê từ nghiên cứu sơ cấp (PDF) đưa vào meta-analysis I→P.
- Hồ sơ đăng ký bản quyền tại **Cục Bản quyền Tác giả Việt Nam (COV)** đã soạn: `p6/submission/maida_copyright/` (mô tả tác phẩm, mẫu mã nguồn, checklist).
- Mã nguồn: `p6/tools/maida/` (backend FastAPI/Python + frontend React/TypeScript).
- **Còn để trống (placeholder)**: họ tên tác giả, ngày sinh, địa chỉ, CMND/CCCD, điện thoại/email, năm ©, ngày hoàn thành.

### C2. Điều chỉnh cần thực hiện
1. **Điền thông tin chủ sở hữu**: Đỗ Thùy Hương — đầy đủ nhân thân + ngày hoàn thành = ngày commit cuối của v7 (xem `git log`).
2. **Cập nhật phiên bản theo đợt mở rộng**: khi M-AIDA được dùng để trích xuất bộ studies bổ sung (Phần B), nâng mô tả lên **v7.1** (hoặc ghi nhận amendment), cập nhật số endpoint, thang confidence (Peterson & Brown, 2005), bộ mã moderator (ICRV/DPL/cDAI) cho khớp tính năng cuối.
3. **Đồng bộ mô tả ↔ mã nguồn**: bảo đảm `00_mo_ta_tac_pham_vi.md` và `01_source_code_samples.md` phản ánh đúng `p6/tools/maida/` hiện tại (số module, endpoint).
4. **Gắn vào Chương 2 luận án**: trình bày M-AIDA như **công cụ phương pháp** của quy trình tổng hợp dữ liệu (data extraction protocol) trong Chương 2; trích dẫn số đăng ký bản quyền COV (khi có) làm minh chứng đóng góp phương pháp nguyên gốc.
5. **Nhất quán liêm chính**: nêu rõ trong Chương 2 và manuscript P6 vai trò của LLM trong trích xuất + cơ chế **PI verification/lock** (con người ra quyết định cuối) — phù hợp quy định sử dụng AI trong nghiên cứu.

### C3. Mối liên hệ Chương 2 ↔ P6
- Chương 2 (phương pháp tổng hợp tài liệu) mô tả: chiến lược tìm kiếm PRISMA → sàng lọc → **trích xuất bằng M-AIDA** → mã hóa moderator → three-level MARA.
- M-AIDA là **đóng góp phương pháp** (registered IP) củng cố tính tái lập và minh bạch của P6; OSF (z37kn) + bản quyền COV cùng tạo bộ minh chứng phương pháp.

---

## TÓM TẮT HÀNH ĐỘNG
- **A (kết quả)**: k = 238/K = 288 đã xác minh, sẵn sàng nộp IBR; ba moderator hạn chế, có publication bias.
- **B (nâng cấp)**: sàng lọc + trích xuất 24 (+11) studies mới → chạy lại MARA → lấp ô Frontier → cập nhật OSF dạng amendment.
- **C (IP)**: điền nhân thân + nâng v7.1 cho M-AIDA, đồng bộ mô tả↔mã, gắn vào Chương 2 làm công cụ phương pháp.

> Phụ thuộc môi trường: bước trích xuất (B2) cần toàn văn PDF + R/`metafor`; thực thi khi có công cụ.
