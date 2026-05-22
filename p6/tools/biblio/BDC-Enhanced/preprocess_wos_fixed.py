#!/usr/bin/env python3
"""
预处理WOS文件：移除所有行首和行尾的引号
"""
import sys
import os

# 修复路径
input_file = "data/wos.txt"
output_file = "data/wos_clean.txt"

print(f"📖 读取: {input_file}")

# 检查输入文件是否存在
if not os.path.exists(input_file):
    print(f"❌ 文件不存在: {input_file}")
    sys.exit(1)

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

# 确保输出目录存在
os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(clean_lines)

print(f"✅ 已保存: {output_file}")

# 测试解析
sys.path.append('.')
try:
    from merge_with_repair import WoSParser
    parser = WoSParser()
    records = parser.parse_file(output_file)
    print(f"\n✅ 解析预处理文件: {len(records)} 条记录")
    
    if records and 'AU' in records[0]:
        print(f"\n🎉 成功！AU字段已恢复")
        aus = records[0]['AU']
        if isinstance(aus, list):
            print(f"   第一条记录作者数: {len(aus)}")
            print(f"   第一作者: {aus[0]}")
        else:
            print(f"   作者: {aus}")
    else:
        print(f"\n❌ 仍然失败 - AU字段缺失")
        
        # 调试：打印第一条记录的字段
        if records:
            print(f"\n📋 第一条记录的字段: {list(records[0].keys())}")
            if 'TI' in records[0]:
                print(f"   标题: {records[0]['TI'][:100]}")
            if 'SO' in records[0]:
                print(f"   期刊: {records[0]['SO']}")
except Exception as e:
    print(f"❌ 解析失败: {e}")

print(f"\n💡 现在可以用 wos_clean.txt 替换原文件")
print(f"   cp {output_file} {input_file}.backup && cp {output_file} {input_file}")
