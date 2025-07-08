import os
from datetime import datetime

LAST_IP_PATH = "storage/last_ip.txt"
LOG_DIR = "logs"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_last_ip(ip: str, path: str = LAST_IP_PATH):
    """現在のIPをファイルに保存する"""
    ensure_dir(os.path.dirname(path))
    with open(path, 'w', encoding='utf-8') as f:
        f.write(ip.strip())

def load_last_ip(path: str = LAST_IP_PATH) -> str | None:
    """前回保存されたIPを読み込む"""
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip() or None

def append_ip_log(old_ip: str, new_ip: str):
    """IP変更履歴をログファイルに追記"""
    ensure_dir(LOG_DIR)
    now = datetime.now()
    filename = f"{LOG_DIR}/ip_log_{now.strftime('%Y-%m-%d')}.txt"
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    message = f"[{timestamp}] IP変更: {old_ip} → {new_ip}\n"

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(message)
