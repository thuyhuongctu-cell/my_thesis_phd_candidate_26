#!/usr/bin/env python3
# run_gui_safely.py
import sys
import os
import traceback

def setup_mac_fixes():
    """设置macOS修复"""
    if sys.platform != 'darwin':
        return
    
    print("应用macOS GUI修复...")
    
    # 1. 设置所有相关环境变量
    os.environ.update({
        'TK_SILENCE_DEPRECATION': '1',
        'MATPLOTLIBRC': '/dev/null',
        'XDG_SESSION_TYPE': 'x11',
    })
    
    # 2. 配置警告过滤
    import warnings
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    warnings.filterwarnings('ignore', message='.*IMKCF.*')
    
    # 3. 预加载框架
    try:
        import ctypes.util
        frameworks = [
            '/System/Library/Frameworks/Tk.framework/Tk',
            '/System/Library/Frameworks/Tcl.framework/Tcl',
            '/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation',
        ]
        for fw in frameworks:
            if os.path.exists(fw):
                ctypes.CDLL(fw)
    except:
        pass

def run_gui_app():
    """安全运行GUI应用"""
    setup_mac_fixes()
    
    try:
        # 动态导入你的应用
        import importlib.util
        
        spec = importlib.util.spec_from_file_location(
            "gui_app", "GUI_app.py"
        )
        module = importlib.util.module_from_spec(spec)
        
        # 在保护的环境中执行
        sys.modules["gui_app"] = module
        spec.loader.exec_module(module)
        
        print("GUI应用启动成功!")
        
    except Exception as e:
        print(f"启动失败: {e}")
        traceback.print_exc()
        
        # 尝试直接执行文件
        print("\n尝试直接执行...")
        os.system(f"python3 GUI_app.py")

if __name__ == "__main__":
    run_gui_app()