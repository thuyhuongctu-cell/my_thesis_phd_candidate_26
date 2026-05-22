#!/usr/bin/env python3
"""
终极修复 - 删除所有 contextlib.redirect_stdout 相关代码
"""

with open('gui_app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip_mode = False

for line in lines:
    # 如果遇到 with contextlib.redirect_stdout，开始跳过
    if 'with contextlib.redirect_stdout' in line:
        skip_mode = True
        # 插入简化版本的代码
        new_lines.append('                                if hasattr(enricher, \'print_statistics\'):\n')
        new_lines.append('                                    self.log("📊 AI补全统计:")\n')
        new_lines.append('                                    self.log("   (详细统计信息请在终端查看)")\n')
        new_lines.append('                                    enricher.print_statistics()\n')
        continue
    
    # 如果正在跳过模式，检查是否结束
    if skip_mode:
        if 'enricher.print_statistics()' in line:
            # 这行是我们要保留的，但我们已经在上面的新行中添加了
            continue
        if 'for line in f_out.getvalue().split' in line:
            continue
        if 'if line.strip():' in line:
            continue
        if 'self.log(f"   {line}")' in line:
            continue
        if 'else:' in line and 'self.log' in line:
            # 遇到 else，结束跳过模式
            skip_mode = False
            new_lines.append(line)
            continue
        # 其他在跳过模式中的行都忽略
        continue
    
    # 正常模式，添加所有行
    new_lines.append(line)

with open('gui_app.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("✅ 已删除所有 contextlib.redirect_stdout 相关代码")
print("   共处理 {} 行代码".format(len(lines)))
