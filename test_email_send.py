from notifier.email_notifier import EmailNotifier

# テスト用に送信設定を直接記述
smtp_server = "impcode.sakura.ne.jp"
smtp_port = 465
smtp_user = "ryosuke_takiguchi@impcode.net"
smtp_password = "impcodeadmin1"
mail_to = "ryosuke_takiguchi@impcode.net"
ehlo_name = "impcode.net"

# Notifierのインスタンス生成
notifier = EmailNotifier(
    smtp_server=smtp_server,
    smtp_port=smtp_port,
    smtp_user=smtp_user,
    smtp_password=smtp_password,
    mail_to=mail_to,
    ehlo_name=ehlo_name
)

# 仮の旧IPと新IPを指定してテスト送信
notifier.send_ip_change(old_ip="203.0.113.1", new_ip="203.0.113.42")
