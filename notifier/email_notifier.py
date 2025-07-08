import smtplib
import ssl
from email.mime.text import MIMEText
from utils.logger import log
from notifier.base import Notifier

class EmailNotifier(Notifier):
    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str,
                 smtp_password: str, mail_to: str, ehlo_name: str = ""):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password
        self.mail_to = mail_to
        self.ehlo_name = ehlo_name.strip()

    def send_ip_change(self, old_ip: str, new_ip: str):
        subject = "IPアドレス変更検知"
        body = f"グローバルIPが変更されました。\n\n旧IP: {old_ip}\n新IP: {new_ip}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.smtp_user
        msg['To'] = self.mail_to

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=context) as server:
                if self.ehlo_name:
                    server.ehlo(name=self.ehlo_name)
                else:
                    server.ehlo()

                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)

            log(f"[EmailNotifier] メール送信成功: {new_ip}")

        except Exception as e:
            log(f"[EmailNotifier] メール送信失敗: {e}")