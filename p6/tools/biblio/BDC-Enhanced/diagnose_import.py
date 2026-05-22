#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
导入问题诊断工具

这个脚本帮助诊断为什么 'from merge import BibliometricMerger' 会失败
"""

import os
import sys
from pathlib import Path

def diagnose_import_issue():
    """诊断导入问题"""
    
    print("=" * 80)
    print("🔍 导入问题诊断")
    print("=" * 80)
    
    # 1. 检查当前工作目录
    print("\n1️⃣  当前工作目录")
    print("-" * 80)
    cwd = os.getcwd()
    print(f"   {cwd}")
    
    # 2. 检查 merge.py 是否存在于当前目录
    print("\n2️⃣  检查 merge.py 文件")
    print("-" * 80)
    
    merge_locations = [
        Path(cwd) / "merge.py",
        Path(__file__).parent / "merge.py",
        Path(__file__).parent / "merge.py",
    ]
    
    for loc in merge_locations:
        if loc.exists():
            print(f"   ✅ 找到: {loc}")
            print(f"      大小: {loc.stat().st_size} bytes")
            
            # 检查是否包含 BibliometricMerger 类
            with open(loc, 'r') as f:
                content = f.read()
                if 'class BibliometricMerger' in content:
                    print(f"      ✅ 包含 BibliometricMerger 类")
                else:
                    print(f"      ❌ 不包含 BibliometricMerger 类")
        else:
            print(f"   ❌ 未找到: {loc}")
    
    # 3. 检查 sys.path
    print("\n3️⃣  Python 模块搜索路径 (sys.path)")
    print("-" * 80)
    for i, path in enumerate(sys.path[:10], 1):
        print(f"   {i}. {path}")
        if i == 10 and len(sys.path) > 10:
            print(f"   ... 还有 {len(sys.path) - 10} 个路径")
    
    # 4. 尝试添加项目目录到 sys.path
    print("\n4️⃣  添加项目目录到 sys.path")
    print("-" * 80)
    
    project_dir = str(Path(__file__).parent.absolute())
    if os.path.exists(project_dir):
        if project_dir not in sys.path:
            sys.path.insert(0, project_dir)
            print(f"   ✅ 已添加: {project_dir}")
        else:
            print(f"   ℹ️  已存在: {project_dir}")
    else:
        print(f"   ❌ 目录不存在: {project_dir}")
    
    # 5. 尝试导入 merge 模块
    print("\n5️⃣  尝试导入 merge 模块")
    print("-" * 80)
    
    try:
        import merge
        print(f"   ✅ 成功导入 merge 模块")
        print(f"      模块路径: {merge.__file__}")
        
        # 检查是否有 BibliometricMerger 类
        if hasattr(merge, 'BibliometricMerger'):
            print(f"      ✅ 找到 BibliometricMerger 类")
            
            # 尝试实例化
            try:
                merger = merge.BibliometricMerger()
                print(f"      ✅ 成功实例化 BibliometricMerger")
            except Exception as e:
                print(f"      ❌ 实例化失败: {e}")
        else:
            print(f"      ❌ 未找到 BibliometricMerger 类")
            print(f"      可用的类/函数:")
            for name in dir(merge):
                if not name.startswith('_'):
                    print(f"         - {name}")
    
    except ImportError as e:
        print(f"   ❌ 导入失败: {e}")
        
        # 提供详细的失败原因分析
        print("\n   🔍 失败原因分析:")
        print("   " + "-" * 76)
        
        # 检查是否是文件不存在
        if not any(loc.exists() for loc in merge_locations):
            print("   ⚠️  原因1: merge.py 文件不存在于任何预期位置")
            print("   解决方案: 确保 merge.py 与 gui_app.py 在同一目录")
        
        # 检查是否是路径问题
        elif project_dir not in sys.path:
            print("   ⚠️  原因2: 项目目录不在 Python 搜索路径中")
            print("   解决方案: 在导入前添加路径修复代码")
        
        # 可能是语法错误
        else:
            print("   ⚠️  原因3: merge.py 可能存在语法错误")
            print("   解决方案: 检查 merge.py 是否有语法错误")
    
    except Exception as e:
        print(f"   ❌ 意外错误: {e}")
        import traceback
        traceback.print_exc()
    
    # 6. 检查 gui_app.py 的导入方式
    print("\n6️⃣  检查 gui_app.py 的导入代码")
    print("-" * 80)
    
    gui_app_file = Path(project_dir) / "gui_app.py"
    if gui_app_file.exists():
        with open(gui_app_file, 'r') as f:
            lines = f.readlines()
            
        # 查找导入 merge 的行
        for i, line in enumerate(lines, 1):
            if 'from merge import' in line:
                print(f"   第 {i} 行: {line.strip()}")
                
                # 检查前面是否有路径修复代码
                context_start = max(0, i - 10)
                context = lines[context_start:i]
                
                has_path_fix = any('sys.path.insert' in l for l in context)
                if has_path_fix:
                    print(f"      ✅ 有路径修复代码")
                else:
                    print(f"      ❌ 缺少路径修复代码")
    
    # 总结
    print("\n" + "=" * 80)
    print("📋 诊断总结")
    print("=" * 80)
    
    print("\n如果导入失败，最可能的原因是:")
    print("1. merge.py 不在 gui_app.py 的同一目录")
    print("2. Python 运行时的工作目录不对")
    print("3. sys.path 没有包含项目目录")
    
    print("\n推荐解决方案:")
    print("1. 确保 merge.py 和 gui_app.py 在同一目录")
    print("2. 在 gui_app.py 中导入 merge 之前添加:")
    print("""
    from pathlib import Path
    import sys
    current_dir = Path(__file__).parent.absolute()
    if str(current_dir) not in sys.path:
        sys.path.insert(0, str(current_dir))
    """)
    print("3. 或者在命令行运行时:")
    print(f"   cd {project_dir}")    print("   python3 gui_app.py")


if __name__ == '__main__':
    diagnose_import_issue()
