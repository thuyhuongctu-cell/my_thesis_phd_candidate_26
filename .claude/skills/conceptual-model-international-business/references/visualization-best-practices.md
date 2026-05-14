# Best Practices cho Vẽ và Trình bày Conceptual Models

## Nguyên tắc thiết kế đồ họa

### 1. Clarity over Aesthetics

Mục tiêu: Người đọc hiểu mô hình trong 30 giây.

**Làm:**
- Font size ≥10pt, rõ ràng (Arial, Helvetica, Times New Roman)
- Spacing đủ rộng giữa các elements
- Contrast cao (text đen trên nền trắng)
- Consistent alignment (boxes align neatly)

**Không làm:**
- Fancy fonts khó đọc
- Quá nhiều màu sắc
- Overlapping elements
- Text quá nhỏ hoặc quá dài

### 2. Visual Hierarchy

**Thứ tự quan trọng (từ trái sang phải):**
```
Independent Variables → Mediators → Dependent Variable
                            ↑
                      Moderators
                            
Control Variables (ở dưới hoặc dotted lines)
```

**Size và emphasis:**
- Main constructs: Larger boxes, bold text
- Mediators/Moderators: Medium size
- Controls: Smaller, lighter color hoặc dotted

### 3. Arrow Conventions

**Standard trong academic publishing:**

- **Solid arrow (→):** Direct effect, main hypotheses
- **Dashed arrow (--→):** Moderating effect hoặc control variables
- **Curved arrow:** Feedback loops (ít dùng trong cross-sectional studies)
- **Double-headed arrow (↔):** Correlation, không phải causation

**Direction:**
- Cause → Effect (independent → dependent)
- Left to right, top to bottom

**Labels trên arrows:**
- Hypothesis number: H1, H2, H3...
- Expected sign: (+), (−), (+/−) nếu unclear
- Avoid cluttering: Không ghi quá nhiều text trên arrow

### 4. Color Usage

**Recommended approach:**
- **Grayscale-first:** Nhiều journals in black & white
- Dùng shades of gray để differentiate
- Nếu dùng màu: Ensure colorblind-friendly palette

**Color palette suggestions:**
- Blue: Independent variables
- Green: Mediators
- Orange: Dependent variable
- Gray: Controls
- Red arrows: Negative relationships (optional)

**Tools to check:** Use ColorBrewer or Adobe Color for accessible palettes.

### 5. Box Design

**Cấu trúc box chuẩn:**
```
┌─────────────────────┐
│   Variable Name     │
│  (measurement info) │ ← Optional
└─────────────────────┘
```

**Best practices:**
- Rounded corners: Friendlier, modern
- Consistent size cho cùng type (all IVs same size)
- White or light fill, dark border
- Padding inside boxes cho text

---

## Công cụ và Kỹ thuật

### Microsoft PowerPoint

**Ưu điểm:** Dễ dùng, widely available, đủ cho most models

**Tips:**
1. Dùng **SmartArt** cho quick templates
2. **Insert → Shapes** cho custom design
3. **Align tools** (Arrange → Align) để neat alignment
4. **Group objects** (Ctrl+G) để di chuyển together
5. **Save as PDF** hoặc high-res PNG (File → Export)

**Export settings:**
- File → Export → Change File Type → PNG
- Options → Resolution: 300 DPI minimum

### Draw.io (diagrams.net)

**Ưu điểm:** Free, powerful, web-based, export quality cao

**Workflow:**
1. Vào diagrams.net
2. Choose "Blank Diagram"
3. Drag shapes từ left panel
4. Connect với arrows
5. Export: File → Export as → PNG/PDF/SVG

**Pro tips:**
- Use "Flowchart" shapes cho boxes
- Enable "Grid" và "Snap to Grid" cho alignment
- Duplicate (Ctrl+D) để consistent sizing
- Export as SVG cho vector graphics (scalable)

### Lucidchart

**Ưu điểm:** Professional, collaboration features, templates

**Best for:** Team projects, complex models, cloud collaboration

**Features:**
- Real-time collaboration
- Version history
- Integration với Google Drive, MS Office
- Export to multiple formats

### Adobe Illustrator

**Ưu điểm:** Publication-quality, complete control, vector-based

**Best for:** Final publication figures, complex layouts

**Learning curve:** Steeper, nhưng output quality cao nhất

### R (DiagrammeR) / Python (matplotlib)

**Ưu điểm:** Reproducible, code-based, version control

**Best for:** Researchers comfortable với coding, reproducible research

**Example R code:**
```r
library(DiagrammeR)

grViz("
  digraph conceptual_model {
    graph [rankdir = LR]
    
    node [shape = box]
    IV [label = 'Independent\nVariable']
    DV [label = 'Dependent\nVariable']
    
    IV -> DV [label = 'H1 (+)']
  }
")
```

---

## Technical Requirements cho Submission

### Resolution và Format

**Minimum standards:**
- **Resolution:** 300 DPI (dots per inch) minimum
- **Format:** 
  - Preferred: EPS, PDF (vector)
  - Acceptable: TIFF, PNG (high-res raster)
  - Avoid: JPEG (lossy compression)

**File size:**
- Aim for < 5MB per figure
- Compress nếu cần, nhưng maintain quality

### Dimensions

**Standard journal widths:**
- Single column: ~3.5 inches (9 cm)
- Double column: ~7 inches (18 cm)

**Design at final size:** Tránh scale down quá nhiều (text becomes unreadable)

### Font Requirements

**Safe choices:**
- Arial, Helvetica: Sans-serif, clean
- Times New Roman: Serif, traditional
- Calibri: Modern, readable

**Size:**
- Minimum: 8pt (after scaling to final size)
- Recommended: 10-12pt
- Titles: 12-14pt

**Embed fonts:** Khi export PDF, ensure fonts embedded

---

## Figure Caption Writing

### Structure chuẩn

```
Figure [number]. [Title]

Note: [Explanation of symbols, abbreviations, and any details not obvious from the figure itself]
```

### Ví dụ tốt

**Example 1:**
```
Figure 1. Conceptual Framework for Entry Mode Choice

Note: Solid arrows represent hypothesized direct relationships. 
The dashed arrow indicates a moderating effect. H1-H4 refer to 
hypotheses developed in Section 3. (+) indicates a positive 
relationship; (−) indicates a negative relationship. Control 
variables (firm size, industry, host country GDP) are included 
in the empirical analysis but omitted from the figure for clarity.
```

**Example 2:**
```
Figure 2. Theoretical Model of Digital Transformation and 
International Performance

Note: Gray boxes represent independent variables; white boxes 
represent the dependent variable. Arrows indicate hypothesized 
causal relationships. Numbers on arrows correspond to hypothesis 
numbers (H1-H5). DT = Digital Transformation; AC = Absorptive 
Capacity; IP = International Performance.
```

### Checklist cho captions

✓ Explains all symbols và abbreviations
✓ Clarifies arrow meanings
✓ Notes any omissions (e.g., controls not shown)
✓ Defines any non-obvious terms
✓ References hypothesis numbers nếu có
✓ Concise nhưng complete

---

## Common Mistakes và Fixes

### Mistake 1: Quá phức tạp

**Problem:** 15 boxes, 25 arrows, impossible to read

**Fix:**
- Focus on core relationships (3-6 main paths)
- Move controls ra khỏi main figure (note in caption)
- Consider sub-models nếu truly complex

### Mistake 2: Unclear directionality

**Problem:** Arrows không rõ cause vs. effect

**Fix:**
- Consistent left-to-right flow
- Clear arrow heads
- Label với hypothesis numbers

### Mistake 3: Low resolution

**Problem:** Blurry khi print, text unreadable

**Fix:**
- Always export at ≥300 DPI
- Use vector formats (PDF, EPS) khi possible
- Test print before submission

### Mistake 4: Inconsistent với text

**Problem:** Mô hình shows H1-H5, text discusses H1-H6

**Fix:**
- Cross-check figure với hypotheses section
- Update figure khi revise hypotheses
- Ensure variable names match exactly

### Mistake 5: Missing information

**Problem:** Abbreviations không defined, symbols unclear

**Fix:**
- Comprehensive figure caption
- Define all abbreviations
- Explain all symbols

---

## Checklist trước khi Submit

### Technical Quality

✓ Resolution ≥300 DPI
✓ Correct file format (vector preferred)
✓ Fonts embedded và readable
✓ File size reasonable (<5MB)
✓ Grayscale-compatible (test in B&W)

### Content Quality

✓ All variables from hypotheses included
✓ All hypotheses represented
✓ Direction of arrows correct
✓ Signs (+/−) match hypotheses
✓ Hypothesis numbers match text

### Presentation Quality

✓ Clean, professional appearance
✓ Consistent spacing và alignment
✓ Readable font sizes
✓ Clear visual hierarchy
✓ No overlapping elements

### Documentation

✓ Complete figure caption
✓ All abbreviations defined
✓ All symbols explained
✓ Controls noted (if omitted from figure)
✓ References to hypotheses clear

---

## Pro Tips

**Tip 1: Design for your audience**
- Academic readers: Prioritize clarity và theoretical precision
- Practitioner audiences: Simplify, emphasize practical implications

**Tip 2: Iterate**
- Draft multiple versions
- Get feedback từ colleagues
- Refine based on comments

**Tip 3: Consistency across paper**
- Use same terminology in figure, hypotheses, tables, text
- Maintain consistent variable order
- Match statistical models exactly

**Tip 4: Learn from top journals**
- Study figures trong leading papers
- Note conventions in your field
- Adapt best practices

**Tip 5: Version control**
- Save multiple versions (v1, v2, v3...)
- Keep editable source files
- Document changes

Remember: A great conceptual model figure enhances your paper's clarity, strengthens theoretical contribution, và improves acceptance chances. Đầu tư thời gian để làm đúng!
