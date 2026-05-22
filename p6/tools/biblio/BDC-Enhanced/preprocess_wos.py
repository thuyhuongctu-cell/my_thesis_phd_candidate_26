#!/usr/bin/env python3
"""
预处理WOS文件：移除所有行首和行尾的引号
"""

import sys
import os

input_file = "data/wos.txt"
output_file = "data/wos_clean.txt"

print(f"📖 读取: {input_file}")
with open(input_file, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

print(f"🔧 移除引号...")
clean_lines = []
for line in lines:
    # 移除行首引号
    if line.startswith('"'):
        line = line[1:]
    # 移除行尾引号（保留换行符）
    if line.rstrip('\n\r').endswith('"'):
        line = line.rstrip('\n\r')[:-1] + '\n'
    clean_lines.append(line)

with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(clean_lines)

print(f"✅ 已保存: {output_file}")

# 测试解析
sys.path.append('.')
from merge_with_repair import WoSParser

parser = WoSParser()
records = parser.parse_file(output_file)
print(f"\n✅ 解析预处理文件: {len(records)} 条记录")

if records and 'AU' in records[0]:
    print(f"\n🎉 成功！AU字段已恢复")
    print(f"   第一条记录作者数: {len(records[0]['AU'])}")
else:
    print(f"\n❌ 仍然失败")

print(f"\n💡 现在可以用 wos_clean.txt 替换原文件")
