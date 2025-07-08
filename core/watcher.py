import time
from utils.logger import log
from storage.file_storage import load_last_ip, save_last_ip

class IPWatcher:
    def __init__(self, checker, notifier, interval: int = 300):
        self.checker = checker          # IPCheckerインスタンス
        self.notifier = notifier        # Notifierインスタンス（メール送信用）
        self.interval = interval
        self.last_ip = load_last_ip()  # 起動時に前回のIPを読み込む

    def start(self):
        log("[Watcher] IP変更監視を開始します。")

        while True:
            current_ip = self.checker.get_ip()
            if current_ip is None:
                time.sleep(self.interval)
                continue

            if self.last_ip != current_ip:
                if self.last_ip:
                    log(f"[Watcher] IP変更検知: {self.last_ip} → {current_ip}")
                    self.notifier.send_ip_change(self.last_ip, current_ip)
                else:
                    log(f"[Watcher] 初回IP記録: {current_ip}")

                self.last_ip = current_ip
                save_last_ip(current_ip)
            else:
                log(f"[Watcher] IP変化なし: {current_ip}")

            time.sleep(self.interval)
