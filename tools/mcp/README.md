# Công cụ dữ liệu & MCP cho luận án (tools/mcp)

Bộ công cụ hỗ trợ thu thập, phân tích và triển khai dữ liệu cho luận án. Gồm hai
MCP server (cấu hình trong `.mcp.json` ở gốc repo) và một danh mục tham khảo.

## 1. World Bank MCP server (`world_bank_mcp_server-master/`)
Truy cập **World Bank Open Data API**: liệt kê quốc gia, liệt kê chỉ số, và phân
tích chỉ số (dân số, nghèo, quản trị…) cho từng nước. Hữu ích để lấy **WGI** (đầu
vào phân tầng ICRV), GNI, và các chỉ số vĩ mô neo bối cảnh thể chế.

- Chạy (stdio): `uv --directory tools/mcp/world_bank_mcp_server-master run world_bank_mcp_server`
- Phụ thuộc: `fastmcp`, `mcp` (uv tự giải quyết; cần mạng tới PyPI lần đầu).
- Nguồn: github.com/anshumax/world_bank_mcp_server

## 2. Data360 MCP server (`data360-mcp-dev/`)
Truy cập **World Bank Data360** (kho chỉ số phát triển hợp nhất) với bộ công cụ
truy vấn + trực quan hóa; kèm các skill UI (React/Angular) trong `.cursor/skills/`.

- Chạy (stdio): `uv --directory tools/mcp/data360-mcp-dev run fastmcp run src/data360/server.py`
- Chạy (HTTP/SSE): thêm `--transport sse --port 8021`
- Phụ thuộc: xem `pyproject.toml` (uv workspace); cấu hình `.env` theo `.env.example`.

## 3. Awesome AI for Economists (`awesome-ai-for-economists/`)
**Bản clone đầy đủ** của danh mục curated (README ~400 dòng, 22 mục) — nguồn:
https://github.com/hanlulong/awesome-ai-for-economists. Các mục liên quan trực
tiếp dự án của NCS: MCP Servers for Economic Data; Causal Inference & Econometrics;
Forecasting/Nowcasting; Literature Review & Research Discovery; Academic Writing &
LaTeX; Document Processing & OCR; NLP & Sentiment; Survey & Qualitative Research;
Papers & Books; Courses/Conferences 2025–2026. Là cơ sở cho skill
`.claude/skills/stata-wbes-runner/` (theo hướng dẫn "Create a Stata Skill in
Claude Code" của The AI Economist).

## Kích hoạt MCP trong phiên Claude Code
Hai server được khai báo trong `.mcp.json` (project-scoped). Khi mở phiên ở repo
này, Claude Code sẽ đề nghị bật chúng.

**Trạng thái kiểm thử (2026-06-11, Claude Code web container):**
- ✅ Cả hai server **load thành công** (uv giải quyết dependencies qua PyPI).
- ⚠️ Gọi dữ liệu live **bị chặn bởi network policy** của môi trường web:
  `api.worldbank.org` trả 403 `host_not_allowed`. Để dùng live data, chạy trong
  Claude Desktop/Code cục bộ, hoặc thêm `api.worldbank.org` +
  `data360api.worldbank.org` vào allowed hosts của environment
  (Claude Code on the web → Environment → Network policy).
- Khi không có mạng WB: dùng pipeline Python cục bộ trong `scripts/` (đủ cho
  mọi phân tích WBES của luận án vì raw .dta đã nằm trong repo).

## Liên kết phương pháp luận
- `thesis/phu_luc_A_hop_nhat_du_lieu_vi.md` — quy trình hợp nhất dữ liệu (Phụ lục A)
- `.claude/skills/stata-wbes-runner/` — skill chạy Stata/Python tái lập P3–P9
- `scripts/build_pooled_dataset.py`, `scripts/wbes_canon.py` — pipeline tái lập
