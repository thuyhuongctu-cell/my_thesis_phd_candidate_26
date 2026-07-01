# SKILLS TRANSFER GUIDE — Chuyển Skills sang Tài khoản Khác

**Ngày tạo:** 20/05/2026  
**Tổng skills hiện có:** 379 skills (56MB)  
**Đường dẫn gốc:** `/root/.claude/skills/`

---

## CÁCH 1 — TAR/ZIP và COPY (Nhanh nhất)

### Trên máy hiện tại (tạo archive):
```bash
cd /root/.claude

# Tạo archive CHỈ skills (không bao gồm credentials/data nhạy cảm)
tar -czf ~/skills_transfer_20260520.tar.gz \
  skills/ \
  INDEX.json

# Kích thước sau nén: ~15–20MB
ls -lh ~/skills_transfer_20260520.tar.gz
```

### Trên máy/tài khoản mới (giải nén):
```bash
# Tạo thư mục .claude nếu chưa có
mkdir -p ~/.claude

# Giải nén vào ~/.claude/
tar -xzf skills_transfer_20260520.tar.gz -C ~/.claude/

# Xác nhận
ls ~/.claude/skills/ | wc -l
# Expected output: 379
```

---

## CÁCH 2 — GitHub Repository Riêng (Khuyến nghị cho dùng lâu dài)

Tạo một **private GitHub repo** chứa toàn bộ skills folder:

```bash
# Trên máy gốc
mkdir /tmp/claude-skills-repo
cp -r /root/.claude/skills/ /tmp/claude-skills-repo/
cp /root/.claude/INDEX.json /tmp/claude-skills-repo/
cd /tmp/claude-skills-repo
git init
git add -A
git commit -m "Skills snapshot 20260520 — 379 skills for PhD dissertation"
git remote add origin https://github.com/thuyhuongctu-cell/claude-skills-private.git
git push -u origin main
```

```bash
# Trên tài khoản/máy mới
mkdir -p ~/.claude
cd ~/.claude
git clone https://github.com/thuyhuongctu-cell/claude-skills-private.git skills-repo
cp -r skills-repo/skills ./skills
cp skills-repo/INDEX.json ./INDEX.json
```

---

## DANH SÁCH SKILLS THEO NHÓM (379 skills)

### NHÓM A — Meta-Analysis & Research Synthesis ⭐ (Quan trọng nhất cho P6)
| Skill | Dùng cho |
|-------|---------|
| `meta-analysis-extraction-workflow` | L2 extraction protocol, escalc() formulas |
| `meta-analysis-internationalization-performance` | I–P specific patterns & benchmarks |
| `meta-analysis-statistical-extraction` | Convert t/F/β đến Pearson r |
| `three-level-meta-analysis` | rma.mv() R execution, moderator tests |
| `systematic-review-meta-analysis-mcp` | PRISMA workflow automation |
| `prisma-meta-analysis` | PRISMA 2020 compliance checklist |
| `prisma-meta-analysis-internationalization` | I–P PRISMA search strings |
| `prisma-systematic-review-workflow` | Step-by-step screening workflow |
| `wos-api-restricted-server` | WoS API queries |
| `wos-meta-analysis-extraction` | WoS-specific extraction |
| `truy-cap-nghien-cuu-mang-han-che` | Truy cập nghiên cứu qua mạng hạn chế |
| `reference-enrichment` | DOI/CrossRef enrichment |
| `research-screening-assistant` | AI-assisted screening |

### NHÓM B — Academic Writing & International Business ⭐
| Skill | Dùng cho |
|-------|---------|
| `international-business-phd-research` | IB PhD context, hypothesis building |
| `international-business-dissertation-assistant` | Dissertation workflow |
| `conceptual-model-international-business` | Mô hình khái niệm, diagram |
| `khung-nghien-cuu-ly-thuyet` | Khung lý thuyết tiếng Việt |
| `viet-nghien-cuu-kinh-doanh-quoc-te` | Viết IB bằng tiếng Việt |
| `vietnamese-academic-glossary-editor` | Thuật ngữ song ngữ |
| `academic-writer` | Academic writing patterns |
| `academic-pipeline` | 10-stage manuscript pipeline |
| `academic-manuscript-quality-toolkit` | Pre-submission quality check |
| `academic-manuscript-submission-checker` | Submission readiness |
| `academic-theory-hypotheses-development` | Xây dựng giả thuyết |
| `authorial-rewrite` | Voice-consistent rewriting |
| `paper-writing` | Section-level writing |
| `paper-revision` | Revision management |
| `rebuttal-writing` | Trả lời reviewer |
| `world-bank-country-classification-research` | ICRV coding, WB classification |
| `international-business-research-naming` | DAI/TCI/FSTS naming consistency |

### NHÓM C — Data Analysis & Statistics ⭐
| Skill | Dùng cho |
|-------|---------|
| `stata-phan-tich-du-lieu` | Stata analysis (tiếng Việt) |
| `stata-thuc-thi-batch` | Batch Stata execution |
| `stata-output-formatting` | Format Stata output |
| `rp-analysis-econometrics` | Econometrics R/Stata |
| `rp-analysis-statistics` | Statistical analysis |
| `rp-analysis-wrangling` | Data wrangling Python/R |
| `rp-analysis-dataviz` | Visualization |
| `data-analysis-research` | Research data analysis |

### NHÓM D — Literature Search & Management
| Skill | Dùng cho |
|-------|---------|
| `literature-researcher` | Systematic literature research |
| `literature-search` | Search strategy design |
| `literature-review` | Writing literature review |
| `rp-literature-search` | RP-specific search |
| `rp-literature-fulltext` | Full-text retrieval |
| `rp-literature-discovery` | Discovery pipeline |
| `semanticscholar-skill` | Semantic Scholar API |
| `paper-zotero` | Zotero MCP integration |
| `cli-anything-zotero` | Zotero CLI harness |
| `citation-management` | Citation workflow |
| `bibcheck` | BibTeX checking |
| `deep-research` | Multi-source deep research |

### NHÓM E — Document Generation & Formatting
| Skill | Dùng cho |
|-------|---------|
| `markdown-to-word` | Convert .md đến .docx |
| `docx-thesis-format` | CTU thesis formatting |
| `chinh-sua-tai-lieu-latex-khoa-hoc` | LaTeX editing cho bài báo |
| `latex-formatting` | LaTeX tools |
| `rp-writing-latex` | LaTeX academic writing |
| `academic-pptx` | PowerPoint generation |
| `academic-slides` | Slide design |
| `posterskill` | Poster creation |
| `cli-anything-libreoffice` | LibreOffice CLI |
| `cli-anything-mermaid` | Mermaid diagrams |
| `figure-generation` | Figure automation |
| `table-generation` | Table generation |
| `tikz-iterate` | TikZ figure iteration |
| `scientific-visualization` | Scientific figures |

### NHÓM F — ABS Journal Standards
| Skill | Dùng cho |
|-------|---------|
| `aws-international-business` | IB journal (JIBS, JWB, IBR, MIR) standards |
| `aws-strategy` | Strategy journals |
| `aws-economics` | Economics journals |
| `aws-finance` | Finance journals |
| `aws-non-abs` | Non-ABS venue |
| `aws-mgmt` + 8 more `aws-*` | Field-specific guidelines |

### NHÓM G — Workflow & Productivity
| Skill | Dùng cho |
|-------|---------|
| `ctu-thesis-dossier-build` | CTU hồ sơ luận án |
| `karpathy-guidelines` | Coding discipline |
| `replication-package` | Replication workflow |
| `academic-deep-research-clawhub` | Deep research orchestration |
| `lfe-boot`, `lfe-builder`, `lfe-inspector` | LFE framework |
| `paper-assembly`, `paper-compilation` | Paper assembly pipeline |
| `audit-reproducibility` | Reproducibility audit |
| `planning`, `executing-plans` | Planning execution |

---

## SKILLS ĐƯỢC ĐỀ XUẤT CÀI THÊM

### Cho P6 L2 Extraction (việc còn lại quan trọng nhất):

**1. `full-text-pdf-extractor`** — Tự động extract text từ PDF và pre-fill extraction fields
- Dùng AI vision để đọc regression tables trong PDF
- Output: JSON với r, n, t-stat, F-stat pre-filled

**2. `zotero-group-library-sync`** — Sync papers từ Zotero group library sang tracker CSV
- Giúp kết nối Zotero reference manager với extraction workflow

**3. `elicit-ai-integration`** — Kết nối Elicit.org API để hỗ trợ screening
- Elicit có built-in meta-analysis extraction tools (2026 version)

**4. `openai-batch-api-screener`** — Batch screening với GPT-4o Vision
- Upload 50 PDF abstracts cùng lúc, nhận Y/N/UNSURE trong 1 request
- Chi phí thấp (~$0.001/abstract)

### Cho Luận án Integration:

**5. `thesis-cross-reference-checker`** — Kiểm tra nhất quán số liệu xuyên chương
- Tìm k=238 có xuất hiện đúng ở tất cả chương không
- Kiểm tra turning points có khớp giữa Ch.3 và Ch.4 không

**6. `ctu-thesis-format-enforcer`** — Enforce CTU formatting rules tự động
- Font Times New Roman 13pt, spacing 1.5, margins 3cm/2.5cm/2.5cm/2cm
- Heading hierarchy theo quy định CTU

**7. `journal-response-template-ib`** — Template trả lời reviewer cho IB journals
- Khi P3-P8 nhận được Major/Minor Revision
- Đã có `rebuttal-writing` skill nhưng IB-specific hơn

### Cho Submission Process:

**8. `scholarone-submission-guide`** — Hướng dẫn từng bước ScholarOne
- Mapping fields từ manuscript sang ScholarOne metadata forms
- Common errors và cách tránh

---

## KIỂM TRA SKILLS ĐÃ CÀI ĐÚNG

```bash
# Kiểm tra tổng số
ls ~/.claude/skills/ | wc -l

# Kiểm tra skills quan trọng nhất có đủ không
for skill in \
  meta-analysis-extraction-workflow \
  three-level-meta-analysis \
  international-business-phd-research \
  viet-nghien-cuu-kinh-doanh-quoc-te \
  stata-phan-tich-du-lieu \
  markdown-to-word \
  ctu-thesis-dossier-build \
  aws-international-business; do
  if [ -d ~/.claude/skills/$skill ]; then
    echo "✅ $skill"
  else
    echo "❌ MISSING: $skill"
  fi
done
```

---

*Lưu tại: `writing_guides/SKILLS_TRANSFER_GUIDE.md`*  
*Cập nhật: 20/05/2026 | 379 skills, 56MB*
