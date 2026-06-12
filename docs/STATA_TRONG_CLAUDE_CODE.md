# Kế hoạch: Chạy Stata trong Claude Code để gỡ các nút thắt định lượng

> Ngày 2026-06-11. Trả lời câu hỏi của NCS: *"Có skill Stata rồi sao không dùng?"*
> — Vì **container Claude Code trên web KHÔNG có binary Stata** (phần mềm thương mại,
> không thể cài trong môi trường này; đã kiểm chứng `which stata stata-mp xstata` → trống).
> Skill là *bộ hướng dẫn điều khiển* Stata; muốn chạy thật cần **máy có Stata 17+ license**
> (máy cá nhân/máy trường của NCS). Tài liệu này là kế hoạch cụ thể để làm điều đó.

## 1. Các nút thắt cần Stata thật

| # | Nút thắt | File liên quan |
|---|---|---|
| N1 | Tái lập P7 không khớp bản công bố (thiếu spec gốc: PPP/weights/trimming) | `data_wbes/analysis/P7_REESTIMATION_NOTE.md` |
| N2 | Xác thực bảng hệ số trong bản thảo P7/P8/P9 bằng chạy lại do-file trước khi nộp (bản thảo đầy đủ tại `p7|p8|p9_india/submission/*_package/`) | `scripts/stata/*.do` |
| N3 | Re-estimate P7 + Japan-2025 + 31 sóng mới ≥2024 | `data_wbes/analysis/DATA_UPDATE_MANIFEST.md` |
| N4 | Đồng bộ định lượng các bảng CĐ1 còn ở bản khóa (2.3.6.x, 2.3.8.x) | `CD1_PIPELINE_RESULTS.md` §D |

## 2. Ba route đã nghiên cứu (chọn theo hoàn cảnh)

### Route A — Stata-MCP (khuyến nghị; tích hợp sâu nhất)
Extension **Stata-MCP** (github.com/hanlulong/stata-mcp — chính tác giả danh mục
awesome-ai-for-economists) chạy Stata từ VS Code/Cursor và **expose tools cho Claude Code**
(`stata_run_file`, `stata_run_selection`, data viewer, hiển thị graph).

**Yêu cầu**: Stata **17+** (Windows/macOS/Linux), VS Code, UV (tự cài).
**Cài đặt (~2 phút)**:
1. VS Code → Extensions → tìm **"Stata MCP"** → Install (extension tự khởi động server cổng 4000).
2. Đăng ký với Claude Code (1 lệnh):
   ```bash
   claude mcp add --transport http stata-mcp http://localhost:4000/mcp-streamable --scope user
   ```
3. Mở Claude Code tại repo này → Claude gọi được `stata_run_file` trực tiếp.

### Route B — pystata (chính thức của StataCorp; không cần VS Code)
Stata 17+ kèm tích hợp Python chính thức. Trong Claude Code cục bộ, Claude chạy Python
điều khiển Stata:
```python
import stata_setup
stata_setup.config('C:/Program Files/Stata18/', 'mp')   # đường dẫn + edition (mp/se/be)
from pystata import stata
stata.run('do scripts/stata/p7_reestimate.do')
```
Cài bridge: `pip install stata-setup`. Tài liệu: stata.com/python.

### Route C — Batch mode thuần (đơn giản nhất; skill `stata-wbes-runner` đã hỗ trợ)
Claude Code cục bộ gọi thẳng:
```bash
stata-mp -b do scripts/stata/p7_reestimate.do   # log: p7_reestimate.log
```
Helper kiểm lỗi đã có sẵn: `.claude/skills/stata-wbes-runner/run_stata.sh`
(tự phát hiện binary, parse mã lỗi `r(NNN);` trong log).

> **Web container (môi trường này)**: không route nào chạy được vì không có Stata.
> Mọi thứ đã chuẩn bị sẵn để chạy **trên máy NCS** — xem §4.

## 3. Do-file ĐÃ VIẾT SẴN (sẵn sàng chạy ngay khi có Stata)

| File | Làm gì | Benchmark phải đối chiếu |
|---|---|---|
| `scripts/stata/00_prep_data.do` | CSV master → `p7_analytic.dta` (khung 49 nền, **lp_z within country-year** — sửa artifact tiền tệ, fsts/fsts2, encode FE) | N ≈ 75.607 |
| `scripts/stata/p7_reestimate.do` | M2/M5 (`reghdfe` + country/year FE, cluster country) + `utest` Lind–Mehlum + TP từng nhóm ICRV + M11 moderation | **TP M5 = 40,0%**; gradient I≈28%→V/VI≈55% |
| `scripts/stata/p8_sids_fip.do` | FIP M1 tuyến tính (Pacific 7) + robustness VI-8 + exporters-only | **β = −1,339, p<,001**; exporters N=26 |

Một lần duy nhất trước khi chạy: `ssc install reghdfe ftools utest estout`.

**Quy tắc liêm chính (đã ghi trong header mỗi do-file)**: kết quả do-file này chỉ
*thay thế* số đã khóa trong luận án **sau khi** NCS xác nhận spec khớp pipeline gốc
(PPP, trọng số, trimming) — nếu lệch, đối chiếu với do-file gốc của nhóm tác giả trước.

## 4. Lộ trình thực thi trên máy NCS (checklist)

- [ ] 1. Cài Claude Code cục bộ (desktop/CLI) + clone repo, checkout nhánh `claude/phd-thesis-review-L9Gml`.
- [ ] 2. Chọn Route A (Stata-MCP) hoặc C (batch). Route A nếu dùng VS Code hằng ngày.
- [ ] 3. `ssc install reghdfe ftools utest estout`.
- [ ] 4. Chạy `00_prep_data.do` → kiểm tra N.
- [ ] 5. Chạy `p7_reestimate.do` → so TP_M5 với 40,0%:
      - **Khớp (±1 điểm %)** → spec đúng → được phép chạy thêm Japan/sóng mới (N3) và điền bảng hệ số (N2).
      - **Lệch** → tìm do-file gốc P7, đối chiếu PPP/weights — KHÔNG thay số khóa.
- [ ] 6. Chạy `p8_sids_fip.do` → so β với −1,339.
- [ ] 7. Khi khớp: đối chiếu hệ số từ `dist/stata_out/*.csv` với các bảng trong bản thảo
      P7/P8/P9 (`p7|p8|p9_india/submission/*_package/01_manuscript_blinded.md`) — sửa nếu lệch —
      và cập nhật footnote Japan ở Ch4 §4.6.1 thành kết quả định lượng.

## 5. Nguồn tham khảo
- Stata-MCP: https://github.com/hanlulong/stata-mcp (Stata 17+; `claude mcp add --transport http stata-mcp http://localhost:4000/mcp-streamable`)
- pystata: https://www.stata.com/python/ · cấu hình: https://www.stata.com/python/pystata18/config.html · PyPI `stata-setup`
- Hướng dẫn "How to Create a Stata Skill in Claude Code" — The AI Economist (PDF đã lưu trong uploads; cơ sở cho skill `stata-wbes-runner`)
- Skill nội bộ: `.claude/skills/stata-wbes-runner/`, `stata-thuc-thi-batch`, `stata-khong-license-giai-phap`
