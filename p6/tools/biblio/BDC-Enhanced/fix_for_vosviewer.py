#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_for_vosviewer.py
====================
将合并清洗后的 WoS 文件优化为 VOSviewer 可正确解析的格式。

核心修复：
  1. AU/AF    每个作者独立一行（首行含标签，续行3空格缩进）
  2. CR       每条引用独立一行（从单行压缩格式拆分还原）
  3. 含逗号的行加双引号包裹
  4. 长文本（AB/TI/FX等）按70字符折行
  5. 输出 CRLF 换行，UTF-8 无 BOM

用法:
  python3 fix_for_vosviewer.py  <输入文件>  <输出文件>
"""

import re
import sys
from pathlib import Path

# ── 常量 ────────────────────────────────────────────────────────────
WRAP_WIDTH   = 70
CONT_INDENT  = "   "   # 3个空格

# 需要按词折行的长文本字段
WRAP_FIELDS = {
    'AB', 'TI', 'DE', 'ID', 'FX', 'FU', 'C3', 'WC', 'SC',
    'NF', 'CT', 'CY', 'CL', 'SP', 'HO', 'GP',
}

# CR引用分隔：识别新引用起始的小写前缀词（多词姓）
_LOW_PREFIXES = (
    'van', 'de', 'del', 'den', 'der', 'von', 'el', 'al',
    'le', 'la', 'di', 'da', 'dos', 'du', 'bin', 'Abu', 'Al', 'El',
)
_LOW_PREFIX_RE = '|'.join(_LOW_PREFIXES)

# 新引用起始的正则（lookahead）
_CR_SEP = re.compile(
    r'\s+'
    r'(?='
    r'(?:(?:' + _LOW_PREFIX_RE + r')\s+)*'     # 可选小写前缀
    r'[A-Z][A-Za-z\-\.\']+\s+[A-Z]{1,5},'      # 姓氏 + 缩写,
    r'\s+\d{4}'                                   # 年份
    r')'
)


# ── 工具函数 ─────────────────────────────────────────────────────────

def clean_value(val: str) -> str:
    """去除数据中残留的孤立双引号"""
    val = val.rstrip('"').lstrip('"')
    val = val.replace('""', '\x00DQ\x00')
    val = val.replace('"', '')
    val = val.replace('\x00DQ\x00', '""')
    return val.strip()


def needs_quotes(line: str) -> bool:
    return ',' in line


def wrap_field(tag: str, value: str) -> list:
    """长文本按词折行，含逗号则每行加引号"""
    value = clean_value(value)
    if not value:
        return []
    has_comma = ',' in value
    pfx1, pfxc = f"{tag} ", CONT_INDENT
    words = value.split()
    lines, cur, first = [], "", True
    for w in words:
        cand = (cur + " " + w).strip() if cur else w
        lim = WRAP_WIDTH - len(pfx1 if first else pfxc)
        if len(cand) <= lim:
            cur = cand
        else:
            if cur:
                lines.append((pfx1 if first else pfxc) + cur)
                first = False
            cur = w
    if cur:
        lines.append((pfx1 if first else pfxc) + cur)
    if has_comma:
        lines = [f'"{ln}"' for ln in lines]
    return lines


def split_authors(tag: str, value: str) -> list:
    """AU/AF：每个作者独立一行"""
    value = clean_value(value)
    if not value:
        return []
    tokens = value.split()
    authors = []
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.endswith(','):
            last = t.rstrip(',')
            fp, j = [], i + 1
            while j < len(tokens) and not tokens[j].endswith(','):
                fp.append(tokens[j]); j += 1
            fn = ' '.join(fp)
            authors.append(f'{last}, {fn}' if fn else last)
            i = j
        elif i + 1 < len(tokens) and tokens[i + 1].endswith(','):
            combined = t + ' ' + tokens[i + 1].rstrip(',')
            fp, j = [], i + 2
            while j < len(tokens) and not tokens[j].endswith(','):
                fp.append(tokens[j]); j += 1
            fn = ' '.join(fp)
            authors.append(f'{combined}, {fn}' if fn else combined)
            i = j
        else:
            authors.append(t); i += 1

    result = []
    for idx, a in enumerate(authors):
        a = a.strip()
        if not a:
            continue
        prefix = f"{tag} " if idx == 0 else CONT_INDENT
        ln = prefix + a
        if needs_quotes(ln):
            ln = f'"{ln}"'
        result.append(ln)
    return result


def split_institutions(tag: str, value: str) -> list:
    """C1：每个机构条目独立一行（不折行，与 WoS 原始格式一致）"""
    value = clean_value(value)
    if not value:
        return []
    parts = re.split(r'\.\s+(?=\[)', value)
    if len(parts) == 1:
        raw = re.split(r'\.\s+', value)
        parts = [p + '.' if not p.endswith('.') and idx < len(raw) - 1 else p
                 for idx, p in enumerate(raw)]
    result = []
    for entry_idx, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue
        prefix = f"{tag} " if entry_idx == 0 else CONT_INDENT
        ln = prefix + part
        if needs_quotes(ln):
            ln = f'"{ln}"'
        result.append(ln)
    return result


def split_semicolon(tag: str, value: str) -> list:
    """OI/RI：每条目独立一行"""
    value = clean_value(value)
    if not value:
        return []
    parts = [p.strip() for p in value.split(';') if p.strip()]
    result = []
    for i, part in enumerate(parts):
        prefix = f"{tag} " if i == 0 else CONT_INDENT
        ln = prefix + part
        if needs_quotes(ln):
            ln = f'"{ln}"'
        result.append(ln)
    return result


def split_cr_citations(tag: str, value: str) -> list:
    """
    CR：将单行压缩的引用列表拆分为每条引用独立一行。

    WoS 合并后的 CR 字段把所有引用拼成一行，如：
      CR Smith A, 2020, NATURE, V1 Jones B, 2019, CELL, V2 ...

    拆分后输出：
      CR Smith A, 2020, NATURE, V1
         Jones B, 2019, CELL, V2
         ...

    含逗号的行整行加引号（引用几乎都含逗号）。
    """
    value = clean_value(value)
    if not value:
        return []

    # 按新引用起始位置分割
    raw_parts = _CR_SEP.split(value.strip())

    # 后处理：合并被错误切断的多词姓（不含年份的碎片合并入下一条）
    merged = []
    i = 0
    while i < len(raw_parts):
        p = raw_parts[i].strip()
        if re.search(r',\s+\d{4}', p):
            merged.append(p)
            i += 1
        else:
            # 碎片：合并到下一条的开头
            if i + 1 < len(raw_parts):
                raw_parts[i + 1] = p + ' ' + raw_parts[i + 1]
            i += 1

    citations = merged if merged else [value.strip()]

    result = []
    for idx, cite in enumerate(citations):
        cite = cite.strip()
        if not cite:
            continue
        prefix = f"{tag} " if idx == 0 else CONT_INDENT
        ln = prefix + cite
        if needs_quotes(ln):
            ln = f'"{ln}"'
        result.append(ln)
    return result


def simple_field(tag: str, value: str) -> list:
    """普通单值字段：含逗号加引号"""
    value = clean_value(value)
    if not value:
        return []
    ln = f"{tag} {value}"
    if needs_quotes(ln):
        ln = f'"{ln}"'
    return [ln]


# ── 解析 ─────────────────────────────────────────────────────────────

def parse_records(text: str) -> list:
    """解析 merged 格式文件为记录列表 [(tag, value), ...]"""
    records = []
    current_record = []
    current_tag = None
    current_val = []
    tag_re = re.compile(r'^([A-Z][A-Z0-9])\s+(.*)')
    header_re = re.compile(r'^(FN|VR)\s+')

    def flush():
        if current_tag and current_val:
            current_record.append((current_tag, ' '.join(current_val).strip()))

    for line in text.splitlines():
        line = line.lstrip('\ufeff').rstrip()
        if line == 'ER':
            flush()
            current_tag, current_val = None, []
            if current_record:
                records.append(current_record)
                current_record = []
            continue
        if header_re.match(line) or not line:
            continue
        m = tag_re.match(line)
        if m:
            flush()
            current_tag = m.group(1)
            current_val = [m.group(2).strip('"').strip()]
        elif line.startswith(CONT_INDENT) or line.startswith(' '):
            if current_tag:
                current_val.append(line.strip().strip('"'))

    flush()
    if current_record:
        records.append(current_record)
    return records


# ── 格式化 ────────────────────────────────────────────────────────────

def format_record(record: list) -> list:
    out = []
    for tag, value in record:
        value = value.strip()
        if tag in ('AU', 'AF'):
            out.extend(split_authors(tag, value))
        elif tag == 'C1':
            out.extend(split_institutions(tag, value))
        elif tag in ('OI', 'RI'):
            out.extend(split_semicolon(tag, value))
        elif tag == 'CR':
            out.extend(split_cr_citations(tag, value))
        elif tag in WRAP_FIELDS:
            out.extend(wrap_field(tag, value))
        else:
            out.extend(simple_field(tag, value))
    return out


# ── 统计 ─────────────────────────────────────────────────────────────

def print_stats(records: list):
    total = len(records)
    with_cr = sum(1 for r in records if any(t == 'CR' for t, _ in r))
    total_cites = 0
    for r in records:
        for t, v in r:
            if t == 'CR':
                parts = _CR_SEP.split(v.strip())
                merged = []
                i = 0
                while i < len(parts):
                    p = parts[i].strip()
                    if re.search(r',\s+\d{4}', p):
                        merged.append(p)
                        i += 1
                    else:
                        if i + 1 < len(parts):
                            parts[i + 1] = p + ' ' + parts[i + 1]
                        i += 1
                total_cites += len(merged) if merged else 1

    print(f"   📄 总记录数:        {total:,}")
    print(f"   🔗 含引用记录:      {with_cr:,}")
    print(f"   📚 总引用条目数:    {total_cites:,}")
    print(f"   ⬜ 无引用记录:      {total - with_cr:,}")


# ── 主流程 ────────────────────────────────────────────────────────────

def convert(input_path: str, output_path: str):
    print(f"\n{'='*60}")
    print(f"🔧 WoS VOSviewer 格式修复工具")
    print(f"{'='*60}")
    print(f"📖 读取: {input_path}")

    with open(input_path, 'r', encoding='utf-8-sig') as f:
        text = f.read()

    print("🔍 解析记录...")
    records = parse_records(text)
    print(f"   找到 {len(records):,} 条记录")

    print("\n📊 输入文件统计:")
    print_stats(records)

    print("\n🔧 转换格式（修复CR字段 + WoS标准格式）...")
    out_lines = [
        "FN Clarivate Analytics Web of Science",
        "VR 1.0",
    ]
    for record in records:
        out_lines.append("")
        out_lines.extend(format_record(record))
        out_lines.append("ER")
    out_lines.append("")

    print(f"💾 写出: {output_path}")
    with open(output_path, 'w', encoding='utf-8', newline='\r\n') as f:
        f.write('\n'.join(out_lines))

    # 验证输出
    with open(output_path, 'r', encoding='utf-8') as f:
        out_records = parse_records(f.read())

    print(f"\n✅ 转换完成！")
    print(f"\n📊 输出文件统计:")
    print_stats(out_records)

    print(f"\n📋 格式说明:")
    print(f"   • AU/AF: 每位作者独立一行")
    print(f"   • CR:    每条引用独立一行（VOSviewer引用网络可正常构建）")
    print(f"   • C1:    每个机构独立一行")
    print(f"   • 含逗号字段: 加双引号包裹")
    print(f"   • 换行符: CRLF，编码: UTF-8 无 BOM")
    print(f"\n💡 导入VOSviewer时选择 'Web of Science' 格式即可")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("用法: python3 fix_for_vosviewer.py <输入文件> <输出文件>")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
