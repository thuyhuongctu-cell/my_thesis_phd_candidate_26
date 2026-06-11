# CĐ1 re-lock — trạng thái & lộ trình (sau khi truy cập Drive)

**Ngày:** 2026-06-11

## Đã làm
1. **Truy cập Drive thành công** (MCP có thẩm quyền — khác mật khẩu lộ đã từ chối). Hai folder + folder tổng chứa raw WBES `.dta` phủ ~24 nền kinh tế còn thiếu (India, Pakistan, Bangladesh, Cambodia, Lào, Nepal, Mongolia, Kazakhstan, Uzbekistan, Tajikistan, Kyrgyz, Turkmenistan, Malaysia, Thái Lan, Sri Lanka, Bhutan, Timor-Leste, Afghanistan, Brunei, HongKong, Singapore, Korea, Taiwan, China…).
2. **Viết pipeline mô tả CĐ1 chuyên dụng, tái lập được**: `scripts/cd1_relock_descriptives.py` (mảnh trước đây THIẾU — repo không có script nào tái lập số CĐ1). Schema-aware (xử lý alias biến WBES, mã âm = missing, các schema standard/ISBS/Micro khác nhau), winsorize 1/99 trong country×year, ánh xạ 6 nhóm ICRV **nhãn dữ liệu**, xuất R&D/ISO/đổi mới sản phẩm/quy trình/website + sd(log LP) + FSTS + FDI theo nhóm.
3. **Chạy thử trên raw có sẵn trong repo** (5 nền trong khung: Azerbaijan, Cambodia, Korea, Laos, Taiwan) → pipeline ra số thật.

## Hai nút thắt còn lại cho re-lock TRUNG THỰC

### (A) Dữ liệu chưa lên container
- Drive-MCP chỉ trả base64 **qua context của tôi** → ~120MB nhị phân không kéo bulk được; container github-only nên không `wget` Drive.
- **Cần:** push 44 nền còn lại vào `data_wbes/raw_dta/` (git) HOẶC attach vào chat (→ `/root/.claude/uploads`, pipeline đã đọc). Một lần, không tốn context, đầy đủ.

### (B) Hiệu chỉnh phương pháp (calibration) — quan trọng về liêm chính
- sd(log LP) demo của pipeline = **2,2–4,4**, trong khi CĐ1 báo cáo **~1,03 (Advanced) → ~1,36 (Frontier)**. Master `.dta` P7 cũng có sd≈3,43.
- Khác biệt này = cách làm sạch ngoại lai/đơn vị doanh thu/PPP của CĐ1 **chặt hơn** winsorize 1/99 đơn giản.
- ⚠️ **KHÔNG dán số demo vào CĐ1** — sẽ sai số. Trước khi thay bảng CĐ1, phải **hiệu chỉnh pipeline khớp phương pháp CĐ1** (đối chiếu 1 nền CĐ1 đã có số, vd Việt Nam/Singapore, để trùng sd rồi mới chạy toàn bộ).

## Lộ trình hoàn tất (khi có data)
1. NCS push 44 raw `.dta` vào `data_wbes/raw_dta/`.
2. Tôi hiệu chỉnh `cd1_relock_descriptives.py` để khớp sd CĐ1 trên 1–2 nền tham chiếu (calibration gate).
3. Chạy toàn bộ → tạo bảng mô tả CĐ1 tái lập được.
4. Thay các bảng CĐ1 (2.3.2.1, 2.3.4.1, phụ lục A.1…) bằng số tái lập, cập nhật crosswalk → re-lock hoàn tất; regenerate docx.

## 44 nền cần push
Afghanistan, Armenia, Bahrain, Bangladesh, Bhutan, Brunei, China, Fiji, Georgia, HongKong, India, Indonesia, Iraq, Israel, Jordan, Kazakhstan, Kiribati, Kuwait, KyrgyzRepublic, Lebanon, Malaysia, Maldives, Mongolia, Myanmar, Nepal, Oman, Pakistan, PapuaNewGuinea, Philippines, Qatar, Samoa, SaudiArabia, Singapore, SolomonIslands, SriLanka, Tajikistan, Thailand, TimorLeste, Tonga, Turkmenistan, Uzbekistan, Vanuatu, Vietnam, Yemen.

> Lưu ý: `reviews/cd1_relock_output.csv` là **demo chưa hiệu chỉnh** — KHÔNG dùng làm số CĐ1.
