# 開発者のためのWebリソース集

## 概要
このプロジェクトは、開発者向けの便利なWebサイトを紹介するStreamlitアプリケーションです。
主要な開発リソースやツールを見やすくまとめ、簡単にアクセスできるようにしています。

## デモ
![アプリケーションのスクリーンショット](./screenshot.png)

## 機能
- 主要な開発者向けWebサイトの紹介
- サイトの概要説明と直接リンク
- プレビュー機能によるサイト詳細の確認
- レスポンシブなデザイン

## 技術スタック
- Python 3.8+
- Streamlit
- HTML/CSS

## インストール方法

1. リポジトリのクローン
```bash
git clone https://github.com/yourusername/dev-resources-collection.git
cd dev-resources-collection
```

2. 仮想環境の作成と有効化
```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

3. 必要なパッケージのインストール
```bash
pip install -r requirements.txt
```

## 使用方法

1. アプリケーションの起動
```bash
streamlit run app.py
```

2. ブラウザで以下のURLにアクセス
```
http://localhost:8501
```

## カスタマイズ方法
`app.py`の`WORKS`リストを編集することで、表示するサイトを追加・変更できます：

```python
WORKS = [
    {
        "title": "サイト名",
        "description": "サイトの説明",
        "image_url": "画像のURL",
        "link_url": "サイトのURL"
    },
    # 追加のサイト情報...
]
```

## requirements.txt
```
streamlit>=1.24.0
```

## ライセンス
MIT License

## 作者
[あなたの名前]

## 貢献方法
1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/improvement`)
3. 変更を加えてコミット (`git commit -am 'Add new feature'`)
4. ブランチにプッシュ (`git push origin feature/improvement`)
5. Pull Requestを作成

## 今後の予定
- [ ] サイトのカテゴリ分け機能の追加
- [ ] ユーザーによる評価システムの実装
- [ ] 検索機能の追加
- [ ] ダークモードの実装

## 謝辞
このプロジェクトで紹介している各Webサイトの運営者様に感謝いたします。

---
※ このプロジェクトは教育目的で作成されており、紹介しているWebサイトとは直接の関係はありません。
```



