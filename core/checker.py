import requests
from utils.logger import log

class IPChecker:
    def __init__(self, url: str = "https://api.ipify.org"):
        self.url = url

    def get_ip(self) -> str | None:
        try:
            response = requests.get(self.url, timeout=5)
            response.raise_for_status()
            ip = response.text.strip()
            log(f"[IPChecker] 現在のIPアドレス: {ip}")
            return ip
        except requests.RequestException as e:
            log(f"[IPChecker] IP取得失敗: {e}")
            return None
