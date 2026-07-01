#!/usr/bin/env python3
"""Dựng lại phần 1_papers/ của bộ nộp theo cấu trúc ĐẦY ĐỦ:
mỗi paper = 1 bản dịch tiếng Việt + 3 tạp chí mục tiêu (primary + 2 dự phòng),
và thêm thư mục 4_du_lieu_ket_qua/ (Excel kết quả + Stata .do + file gộp 50 nước P7).

Nguồn lấy từ các gói submission đã có trong repo; chỉ render .docx khi gói
dự phòng mới có .md (chưa render). KHÔNG bịa nội dung — chỉ gom + render.

Chạy:  python3 scripts/build_bo_nop_papers_full.py
"""
import shutil, subprocess, glob
from pathlib import Path

ROOT = Path("/home/user/MY_THESIS_PHD_CANDIDATE_26")
PKG = ROOT / "dist/BO_NOP_HOAN_CHINH_2026-06"
PAPERS = PKG / "1_papers"
DATA = PKG / "4_du_lieu_ket_qua"

# (code, tier, source package dir) — primary đứng đầu. Đã loại gói DEPRECATED/SUPERSEDED.
MAP = {
    "P3":  ("JED",   "p3/submission/p3_vietnam_vi.md", [
        ("JED","primary","p3/submission/jed_package"),
        ("IJOEM","fallback","p3/submission/ijoem_package")]),
    "P4":  ("MIR",   "p4/submission/p4_singapore_vi.md", [
        ("MIR","primary","p4/submission/mir_package"),
        ("MBR","target","p4/submission/mbr_package"),
        ("APBR","safe","p4/submission/apbr_package")]),
    "P5":  ("IJOEM", "p5/submission/p5_china_vi.md", [
        ("IJOEM","primary","p5/submission/ijoem_package"),
        ("APJM","fallback","p5/submission/apjm_package"),
        ("JABS","fallback","p5/submission/jabs_package")]),
    "P6":  ("JWB",   "p6/submission/p6_meta_vi.md", [
        ("JWB","primary","p6/submission/jwb_package"),
        ("JIM","target","p6/submission/jim_package"),
        ("APJM","safe","p6/submission/apjm_package")]),
    "P7":  ("IBR",   "p7/submission/p7_capstone_vi.md", [
        ("IBR","primary","p7/submission/ibr_package"),
        ("GSJ","fallback","p7/submission/gsj_package"),
        ("JIBP","fallback","p7/submission/jibp_package")]),
    "P8":  ("World_Development", "p8/submission/p8_pacific_sids_vi.md", [
        ("World_Development","primary","p8/submission/world_development_redesign"),
        ("JID","target","p8/submission/jid_package"),
        ("EJDR","safe","p8/submission/ejdr_package")]),
    "P9":  ("MIR",   "p9_india/submission/p9_india_vi.md", [
        ("MIR","primary","p9_india/submission/mir_package"),
        ("IJOEM","fallback","p9_india/submission/ijoem_package"),
        ("JABS","fallback","p9_india/submission/jabs_package")]),
    "P10": ("ABM",   "p10_japan/p10_japan_vi.md", [
        ("ABM","primary","p10_japan/submission/abm_package"),
        ("APJM","target","p10_japan/submission/apjm_package"),
        ("IJOEM","fallback","p10_japan/submission/ijoem_package")]),
}

ROLES = [  # (prefix-glob, output filename)
    ("01_manuscript_blinded", "01_manuscript_blinded.docx"),
    ("02_title_page",         "02_title_page.docx"),
    ("03_cover_letter",       "03_cover_letter.docx"),
]

def find(srcdir: Path, prefix: str, ext: str):
    # prefer exact, else 'prefix*'; skip *_source (deprecated jibs convention)
    cands = sorted(srcdir.glob(f"{prefix}*.{ext}"))
    cands = [c for c in cands if "_source" not in c.name]
    # prefer the shortest name (01_manuscript_blinded.docx over _8500/_full)
    return min(cands, key=lambda p: len(p.name)) if cands else None

def render_docx(md: Path, out: Path):
    cmd = ["pandoc", str(md), "-o", str(out),
           "--resource-path", str(md.parent)]
    subprocess.run(cmd, check=True, cwd=ROOT)

def vi_docx(vi_md: Path, out: Path):
    # bản dịch VI: ưu tiên .docx đã có cạnh .md, else render
    cand = vi_md.with_suffix(".docx")
    if cand.exists():
        shutil.copy2(cand, out); return "copied"
    render_docx(vi_md, out); return "rendered"

def build_papers():
    if PAPERS.exists():
        shutil.rmtree(PAPERS)
    PAPERS.mkdir(parents=True)
    log = []
    for pid, (primcode, vi_rel, journals) in MAP.items():
        pdir = PAPERS / f"{pid}_{primcode}"
        pdir.mkdir()
        # bản dịch tiếng Việt ở cấp paper
        vi_md = ROOT / vi_rel
        st = vi_docx(vi_md, pdir / "00_ban_dich_vi.docx")
        log.append(f"{pid}: VI {st}")
        for i, (code, tier, rel) in enumerate(journals, 1):
            src = ROOT / rel
            jdir = pdir / f"{i:02d}_{code}_{tier}"
            jdir.mkdir()
            for prefix, outname in ROLES:
                dx = find(src, prefix, "docx")
                if dx:
                    shutil.copy2(dx, jdir / outname); src_used = dx.name
                else:
                    md = find(src, prefix, "md")
                    if md:
                        render_docx(md, jdir / outname); src_used = md.name + "→docx"
                    else:
                        src_used = "MISSING";
                log.append(f"  {pid}/{code}/{outname}: {src_used}")
            # bản LaTeX PDF (nếu có)
            for pdf in src.glob("04_manuscript_latex.pdf"):
                shutil.copy2(pdf, jdir / "04_manuscript_latex.pdf")
            # figures (nếu có)
            figdir = src / "figures"
            if figdir.is_dir():
                shutil.copytree(figdir, jdir / "figures")
    return log

def build_data():
    if DATA.exists():
        shutil.rmtree(DATA)
    (DATA / "ket_qua_excel").mkdir(parents=True)
    (DATA / "p7_du_lieu_gop_50_nuoc").mkdir(parents=True)
    (DATA / "ma_stata_do").mkdir(parents=True)
    log = []
    # 1) Excel kết quả mỗi paper
    for wb in sorted(glob.glob(str(ROOT / "p*/**/P*_results_workbook.xlsx"), recursive=True)):
        shutil.copy2(wb, DATA / "ket_qua_excel" / Path(wb).name); log.append(f"xlsx {Path(wb).name}")
    # 2) Excel tổng hợp luận án
    for wb in glob.glob(str(ROOT / "dist/figure_data/*.xlsx")):
        shutil.copy2(wb, DATA / "ket_qua_excel" / Path(wb).name); log.append(f"xlsx {Path(wb).name}")
    # 3) File gộp 50 nước cho P7
    for f in ["p7_pooled_clean.csv", "p7_manifest.csv", "p7_variable_log.csv"]:
        s = ROOT / "data_wbes/p7" / f
        if s.exists():
            shutil.copy2(s, DATA / "p7_du_lieu_gop_50_nuoc" / f); log.append(f"p7 {f}")
    # 4) Mã Stata .do
    for do in sorted(glob.glob(str(ROOT / "p*/replication/do/*.do")) +
                     glob.glob(str(ROOT / "scripts/stata/*.do"))):
        rel = Path(do).relative_to(ROOT)
        flat = str(rel).replace("/", "__")
        shutil.copy2(do, DATA / "ma_stata_do" / flat); log.append(f"do {flat}")
    return log

if __name__ == "__main__":
    l1 = build_papers()
    l2 = build_data()
    print("\n".join(l1))
    print("--- data ---")
    print("\n".join(l2))
    print("DONE")
