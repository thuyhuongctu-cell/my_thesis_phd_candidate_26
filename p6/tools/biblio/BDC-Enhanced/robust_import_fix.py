#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
健壮的 merge 模块导入修复

替换 gui_app.py 中的导入代码
"""

def robust_import_merge():
    """
    健壮的 merge 模块导入
    
    在 gui_app.py 的 run_merge_dedup 方法中使用这段代码
    替换原来的导入部分
    """
    
    import sys
    import os
    from pathlib import Path
    
    # 方法1: 使用 __file__ (如果可用)
    try:
        current_dir = Path(__file__).parent.absolute()
        if str(current_dir) not in sys.path:
            sys.path.insert(0, str(current_dir))
    except NameError:
        # __file__ 不可用时的备用方案
        pass
    
    # 方法2: 使用当前工作目录
    cwd = Path(os.getcwd()).absolute()
    if str(cwd) not in sys.path:
        sys.path.insert(0, str(cwd))
    
    # 方法3: 尝试从环境变量或已知位置
    known_locations = [
        str(Path(__file__).parent.absolute()),
        Path.home() / "Desktop" / "Bibliometric-Data-Consolidation-Tool-main_副本2",
    ]
    
    for loc in known_locations:
        loc_path = Path(loc)
        if loc_path.exists() and str(loc_path) not in sys.path:
            sys.path.insert(0, str(loc_path))
    
    # 现在尝试导入
    try:
        from merge import BibliometricMerger
        return BibliometricMerger
    except ImportError as e:
        # 如果还是失败，提供详细的诊断信息
        print("\n" + "=" * 80)
        print("❌ 无法导入 merge 模块")
        print("=" * 80)
        print(f"\n错误: {e}")
        print(f"\nPython 搜索路径 (sys.path):")
        for i, p in enumerate(sys.path[:5], 1):
            print(f"  {i}. {p}")
        
        print(f"\n当前工作目录: {os.getcwd()}")
        
        # 检查 merge.py 是否存在
        print(f"\n检查 merge.py 文件:")
        for loc in [cwd, current_dir if 'current_dir' in locals() else None] + known_locations:
            if loc:
                merge_file = Path(loc) / "merge.py"
                exists = "✅" if merge_file.exists() else "❌"
                print(f"  {exists} {merge_file}")
        
        raise


# ============================================================================
# 在 gui_app.py 中使用的完整代码
# ============================================================================

"""
找到 gui_app.py 的 run_merge_dedup 方法，替换导入部分：

替换这部分:
    # ✅ 修复：添加当前目录到Python路径
    current_dir = Path(__file__).parent.absolute()
    if str(current_dir) not in sys.path:
        sys.path.insert(0, str(current_dir))
    
    # 调用合并去重模块
    from merge import BibliometricMerger

用这个更健壮的版本:
    
    # ✅ 健壮的路径修复
    import sys
    import os
    from pathlib import Path
    
    # 多重路径策略
    paths_to_add = []
    
    # 策略1: gui_app.py 所在目录
    try:
        current_dir = Path(__file__).parent.absolute()
        paths_to_add.append(current_dir)
    except:
        pass
    
    # 策略2: 当前工作目录
    paths_to_add.append(Path(os.getcwd()).absolute())
    
    # 策略3: 已知项目位置
    project_dir = Path(__file__).parent.absolute()
    if project_dir.exists():
        paths_to_add.append(project_dir)
    
    # 添加所有路径
    for path in paths_to_add:
        path_str = str(path)
        if path_str not in sys.path:
            sys.path.insert(0, path_str)
            self.log(f"📁 添加搜索路径: {path_str}")
    
    # 调用合并去重模块
    from merge import BibliometricMerger
"""
