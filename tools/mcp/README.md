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

## 3. Awesome AI for Economists (`awesome-ai-for-economists-main/`)
Danh mục công cụ AI cho nhà kinh tế (gồm hướng dẫn tạo **Stata skill** trong Claude
Code — cơ sở cho `.claude/skills/stata-wbes-runner/`). Nguồn:
https://github.com/hanlulong/awesome-ai-for-economists

## Kích hoạt MCP trong phiên Claude Code
Hai server được khai báo trong `.mcp.json` (project-scoped). Khi mở phiên ở repo
này, Claude Code sẽ đề nghị bật chúng. Lưu ý: `uv run` cần mạng ra ngoài (PyPI +
World Bank API) ở lần đầu; nếu môi trường chặn mạng, server sẽ không khởi động —
khi đó dùng pipeline Python cục bộ trong `scripts/`.

## Liên kết phương pháp luận
- `thesis/phu_luc_A_hop_nhat_du_lieu_vi.md` — quy trình hợp nhất dữ liệu (Phụ lục A)
- `.claude/skills/stata-wbes-runner/` — skill chạy Stata/Python tái lập P3–P9
- `scripts/build_pooled_dataset.py`, `scripts/wbes_canon.py` — pipeline tái lập
