import yaml
import os

DEFAULT_CONFIG_PATH = "config/default.yaml"

class Config:
    def __init__(self, path: str = DEFAULT_CONFIG_PATH):
        self.path = path
        self._config = self._load()

    def _load(self) -> dict:
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"設定ファイルが見つかりません: {self.path}")
        with open(self.path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def get_ip_check_url(self) -> str:
        return self._config.get("ip_check", {}).get("url", "https://api.ipify.org")

    def get_interval(self) -> int:
        return self._config.get("ip_check", {}).get("interval", 300)

    def get_smtp_settings(self) -> dict:
        return self._config.get("smtp", {})
