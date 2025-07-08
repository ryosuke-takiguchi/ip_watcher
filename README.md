# IPアドレス変更検知ツール

## 概要
本ツールは、定期的にグローバルIPアドレスを取得・比較し、IPアドレスに変更があった場合に通知するユーティリティです。
自宅サーバーやリモート機器において、動的IPの変更を自動で検出し、メールなどで通知します。

## ディレクトリ構成

```
ip_watcher/
├── config/         # 設定ファイルを管理
├── core/           # IPチェック・監視のロジック
├── notifier/       # 通知処理（メール等）
├── utils/          # ログ出力などのユーティリティ
├── main.py         # エントリーポイント
├── requirements.txt
└── README.md       # このファイル
```

## 使い方

1. `config/config.yaml` を編集して、チェック間隔やSMTP設定を指定します。
2. 仮想環境をアクティブにした状態で `main.py` を実行します。

```bash
python main.py
```

## インストール手順

```bash
# 仮想環境作成
python -m venv venv

# 仮想環境を有効化
venv\Scripts\activate

# 依存ライブラリをインストール
pip install -r requirements.txt
```

※ 将来的には自動セットアップ用のインストールbatファイルを追加予定です

## ライセンス

MIT License

```
Copyright (c) 2025 Ryosuke Takiguchi

本ソフトウェアはMITライセンスのもとで公開されています。
詳細はLICENSEファイルを参照してください。
```

## 作者

- **名前**: Ryosuke Takiguchi  
- **メール**: ryosuke_takiguchi@impcode.net
