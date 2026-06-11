# Trạng thái dự án & sẵn sàng bảo vệ — tổng hợp phiên 2026-06-11

> Tài liệu consolidate cho NCS Đỗ Thùy Hương. Nhánh `claude/phd-thesis-review-L9Gml` (PR #17).
> Tất cả đã commit + push. Mọi số liệu nêu dưới đã qua linter (`scripts/check-consistency.py`: 0 vấn đề).

## 1. Kết luận tổng thể
**Luận án ĐẠT chuẩn bảo vệ** (review độc lập 9,5/10 nền tảng). Toàn bộ mâu thuẫn số nội bộ
đã được sửa; khung số liệu đã khóa và nhất quán xuyên 5 chương + 2 chuyên đề; bổ sung phụ lục
phương pháp luận hợp nhất dữ liệu (song ngữ). Các việc còn lại là **mở rộng tùy chọn**, không
chặn bảo vệ.

## 2. Khung số liệu CANONICAL (đã khóa)
| Đại lượng | Giá trị | Hiện diện |
|---|---|---|
| Pool phân loại ICRV | **96.415 DN / 52 nền** | 3× trong thesis |
| Mẫu phân tích chính | **91.982 DN / 49 nền** | 9× |
| N hồi quy P7 (M2) | **84.910** | 9× |
| Nhóm ICRV | I=4.222 · II=2.269 · III=13.993 · IV=50.926 · V=18.569 · VI=1.885 | Bảng 4.1 |
- Linter sạch; **0 số cũ rò rỉ** (101.185/47 nền/4.544/108 cặp đã xóa khỏi 5 chương).

## 3. Sửa review (10/10 issue) — đã hoàn tất
I-01 FIP β −0,404→**−1,339, p<,001** · I-02 SIDS N=26 · I-03/04 SIDS 7/9 nền + 7 nước ·
I-05 P5 China N=4.559 · I-06 "gần đơn điệu" · I-07 khai báo H1c · I-08 re-lock CĐ1 →
canonical · I-10 "47"→"49" · I-16 M4 H4→H3 · MINOR (Hình 4.1, K=288, Paternoster FSTS², §5.1.6).
Báo cáo: `reviews/independent_review_2026-06-11.md`.

## 4. Dữ liệu WBES (kho `data_wbes/raw_dta/`)
- **Coverage đủ 49/49 nền** (I 5/5 · II 6/6 GCC · III 6/6 · IV 7/7 · V 17/17 · VI 8/8 Pacific).
- Đã lọc **non-Asia** (Kenya/Kosovo/Cyprus/Turkey/West Bank) + đợt **trước 2006**; dedupe nước-năm.
- **Japan-2025** (khảo sát lần đầu) đã lưu kho — ghi nhận ở Ch4 §4.6.1 + CĐ1 là nền thứ 50 phân
  loại (94.032 DN), **chưa nhập mô hình** (chờ re-estimate). Manifest: `DATA_UPDATE_MANIFEST.md`.
- ROS + LP-z theo nhóm ICRV (sửa artifact tiền tệ): `FP_DESCRIPTIVES_RESULTS.md`.
- Bảng mô tả CĐ1 §2.3.3.2/2.3.4.1/2.3.5.1 đồng bộ raw 49 nền: `CD1_PIPELINE_RESULTS.md`.

## 5. Phụ lục phương pháp luận (MỚI — trả lời câu hỏi hội đồng về gộp dữ liệu)
- `thesis/phu_luc_A_hop_nhat_du_lieu_vi.md` (VI) + `thesis/appendix_A_data_harmonisation_en.md` (EN).
- 6 bước S1–S6 + **Hình A.1 Mermaid** (dòng dữ liệu PRISMA) + xử lý artifact tiền tệ (z within
  country-year + two-way FE) + pooled cross-section + trọng số + dữ liệu thiếu. APA7: Deaton 1985,
  Wooldridge 2010, Cameron & Trivedi 2005, Solon et al. 2015, Little & Rubin 2019, Feenstra et al.
  2015, Verbeek 2008, Kaufmann et al. 2011. Tái lập: `scripts/build_pooled_dataset.py`.

## 6. Ranh giới liêm chính (đã ghi rõ)
Thử ước lượng lại P7 với Japan (`scripts/p7_reestimate_check.py`): **không tái lập được gradient
đã công bố** → KHÔNG bịa hệ số. Số P7 trong luận án giữ trên mẫu 49 nền đã khóa; cập nhật định
lượng cần nhóm tác giả chạy lại do-file gốc. Chi tiết: `P7_REESTIMATION_NOTE.md`.

## 7. Hạ tầng AI (đã cài)
- **18 skill kinh tế** trong `.claude/skills/` (stata-regression, python-panel-data, latex-tables,
  econ-visualization, academic-paper-writer, overleaf-sync-now…) + skill riêng `stata-wbes-runner`,
  `read-dta`.
- **3 MCP server** trong `.mcp.json`: world-bank, data360, oecd (đã build). TAM (8 nguồn) vendored,
  chờ API keys.
- ⚠️ **Mạng web container chặn mọi host dữ liệu** (`api.worldbank.org`, `sdmx.oecd.org`,
  `data360api` → 403 host_not_allowed). MCP **load được** nhưng kéo live data cần: allowlist 3 host
  đó trong *Environment → Network policy*, hoặc chạy Claude Desktop/Code cục bộ.

## 8. Việc mở rộng TÙY CHỌN (không chặn bảo vệ)
1. **Re-estimate P7+Japan**: nhóm tác giả chạy do-file gốc trên `data_wbes/raw_dta/` (49 nền +
   Japan + sóng ≥2024 — danh sách trong manifest), thay turning point/hệ số mới vào §4.6.
2. **Front matter bản 5 chương**: đã hoàn thiện danh mục bảng/hình; còn tóm tắt/mục lục tự sinh khi
   xuất bản cuối.
3. **Kéo WGI live** kiểm chứng độc lập phân tầng ICRV (khi mở network policy).
4. **Bản LaTeX nộp tạp chí** P3–P9 dùng skill `latex-tables` + `overleaf-sync-now`.

## 9. Cách dùng Fable 5
Phiên này chạy Opus 4.8. Để dùng **Fable 5** (`claude-fable-5`): mở **phiên mới** và chọn ở model
picker (web) / `/model` (CLI). Mọi việc đã push nên chuyển phiên không mất tiến độ.
