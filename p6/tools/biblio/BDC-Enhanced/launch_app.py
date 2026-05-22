#!/usr/bin/env python3
"""
Bibliometric 工具启动脚本 - 修复所有问题
"""

import sys
import os
import warnings
import subprocess

def setup_environment():
    """设置运行环境"""
    # 添加项目目录到Python路径
    project_root = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(project_root, 'src')
    
    sys.path.insert(0, project_root)
    sys.path.insert(0, src_path)
    
    # macOS特定修复
    if sys.platform == 'darwin':
        os.environ.update({
            'TK_SILENCE_DEPRECATION': '1',
            'PYTHONPATH': f'{project_root}:{src_path}',
        })
        
        # 抑制警告
        warnings.filterwarnings('ignore', 
            message='.*TSM AdjustCapsLockLED.*')
        warnings.filterwarnings('ignore',
            message='.*_ISSetPhysicalKeyboardCapsLockLED.*')
        warnings.filterwarnings('ignore',
            message='.*IMKCFRunLoopWakeUpReliable.*')

def check_dependencies():
    """检查依赖"""
    required = ['requests', 'customtkinter', 'pandas']
    
    for package in required:
        try:
            __import__(package)
        except ImportError:
            print(f"错误: 缺少 {package} 模块")
            print(f"请运行: pip3 install {package}")
            return False
    return True

def main():
    """主函数"""
    print("=" * 50)
    print("Bibliometric Data Consolidation Tool")
    print("=" * 50)
    
    # 设置环境
    setup_environment()
    
    # 检查依赖
    if not check_dependencies():
        print("\n正在自动安装缺失的依赖...")
        try:
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', 
                'requests', 'customtkinter', 'pandas', 'openpyxl'
            ])
        except:
            print("请手动安装依赖:")
            print("pip3 install requests customtkinter pandas openpyxl")
            input("按Enter键退出...")
            return
    
    # 导入并运行主应用
    try:
        from gui_app import main as app_main
        app_main()
    except ImportError as e:
        print(f"导入错误: {e}")
        print("\n请确保:")
        print("1. 项目结构完整")
        print("2. 所有依赖已安装")
        print("3. 在项目根目录运行此脚本")
        input("\n按Enter键退出...")
    except Exception as e:
        print(f"运行时错误: {e}")
        import traceback
        traceback.print_exc()
        input("\n按Enter键退出...")

if __name__ == "__main__":
    main()
