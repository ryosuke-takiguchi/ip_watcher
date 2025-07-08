from config.config import Config
from core.checker import IPChecker
from core.watcher import IPWatcher
from notifier.email_notifier import EmailNotifier
from utils.logger import log

def main():
    log("=== IP監視プログラム 起動 ===")

    # 設定ファイルの読み込み
    config = Config()

    # IP取得クラスの初期化
    checker = IPChecker(url=config.get_ip_check_url())

    # 通知（メール）クラスの初期化
    smtp_conf = config.get_smtp_settings()
    notifier = EmailNotifier(
        smtp_server=smtp_conf["server"],
        smtp_port=smtp_conf["port"],
        smtp_user=smtp_conf["user"],
        smtp_password=smtp_conf["password"],
        mail_to=smtp_conf["to"],
        ehlo_name=smtp_conf.get("ehlo_name", "") 
    )

    # IP監視クラスの初期化と開始
    interval = config.get_interval()
    watcher = IPWatcher(checker=checker, notifier=notifier, interval=interval)
    watcher.start()

if __name__ == "__main__":
    main()
