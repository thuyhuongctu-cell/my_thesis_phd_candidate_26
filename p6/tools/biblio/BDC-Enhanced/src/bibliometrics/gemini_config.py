import os
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

class GeminiConfig:
    """Gemini API配置管理 - Whisky 最终完美补丁版"""

    def __init__(self, api_key=None, api_url=None, model=None):
        # 🔒 这里的配置依然“焊死”，确保连接到 MKEAI
        self.api_key = os.getenv('GEMINI_API_KEY', 'YOUR_API_KEY')
        self.api_url = "https://generativelanguage.googleapis.com/v1beta"
        
        # 💡 如果之前 gemini-1.5-flash 报 503，可以尝试改成 gemini-2.0-flash
        self.model = "gemini-2.5-flash"
        
        # 基础运行参数
        self.max_tokens = 5000
        self.temperature = 0.1
        self.timeout = 60
        self.max_retries = 3
        self.retry_delay = 5
        self.enabled = True
        self.enable_caching = True
        self.fallback_to_rules = True

    @classmethod
    def from_file(cls, config_file: str = 'config/gemini_config.json') -> 'GeminiConfig':
        """
        从配置文件加载

        Args:
            config_file: 配置文件路径

        Returns:
            GeminiConfig实例
        """
        config_path = Path(config_file)

        if not config_path.exists():
            logger.warning(f"配置文件不存在: {config_file}，使用默认配置")
            return cls()

        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)

            return cls(
                api_key=config_data.get('api_key'),
                api_url=config_data.get('api_url'),
                model=config_data.get('model')
            )
        except Exception as e:
            logger.error(f"加载配置文件失败: {e}")
            return cls()

    @classmethod
    def from_params(cls, api_key: str, api_url: str, model: str) -> 'GeminiConfig':
        """
        从参数创建配置

        Args:
            api_key: API密钥
            api_url: API地址
            model: 模型名称

        Returns:
            GeminiConfig实例
        """
        return cls(api_key=api_key, api_url=api_url, model=model)
    def save_to_file(self, config_file: str = 'config/gemini_config.json'):
        """
        保存配置到文件

        Args:
            config_file: 配置文件路径
        """
        config_path = Path(config_file)
        config_path.parent.mkdir(parents=True, exist_ok=True)

        config_data = {
            'api_key': self.api_key,
            'api_url': self.api_url,
            'model': self.model,
            'max_tokens': self.max_tokens,
            'temperature': self.temperature,
            'timeout': self.timeout,
            'enable_caching': self.enable_caching,
            'fallback_to_rules': self.fallback_to_rules
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, ensure_ascii=False, indent=2)

        logger.info(f"配置已保存到: {config_file}")

    def is_enabled(self) -> bool:
        """✅ 补上缺失的 is_enabled 函数，告诉程序：AI 已准备就绪！"""
        return self.enabled and self.validate()

    def validate(self) -> bool:
        """验证配置是否有效"""
        if not self.api_key:
            logger.error("API密钥未配置")
            return False

        if not self.api_url:
            logger.error("API地址未配置")
            return False

        if not self.model:
            logger.error("模型名称未配置")
            return False

        return True

    def __repr__(self) -> str:
        """字符串表示（隐藏API密钥）"""
        masked_key = f"{self.api_key[:8]}...{self.api_key[-4:]}" if self.api_key else "未配置"
        return (
            f"GeminiConfig(\n"
            f"  api_key={masked_key},\n"
            f"  api_url={self.api_url},\n"
            f"  model={self.model},\n"
            f"  enabled={self.enabled}\n"
            f")"
        )


def create_default_config_file():
    """创建默认配置文件模板"""
    config_path = Path('config/gemini_config.json')
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
