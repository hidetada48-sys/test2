# X Bookmark → NotebookLM 同期ツール

XのブックマークをテキストファイルとしてGoogle Drive経由でNotebookLMに同期するツール。

## セットアップ

### 1. 必要なものをインストール

```bash
pip install playwright
playwright install chromium
```

### 2. 設定ファイルを作成

`config.example.json` をコピーして `config.json` を作成し、rcloneのリモート名を確認して設定する。

```bash
cp config.example.json config.json
rclone listremotes  # リモート名を確認
```

### 3. 【一回だけ】セッションを保存する

**ブラウザ画面が表示できる環境（Windows等）で実行すること。**

```bash
python scripts/save_session.py
```

ブラウザが開くので、Xに手動でログインして Enter を押す。

### 4. ブックマークを取得・アップロード

```bash
python scripts/fetch_bookmarks.py
```

## ファイル構成

```
~/.x-bookmark-sync/
├── config.json          # 設定ファイル（Gitに入れない）
├── session.json         # セッション情報（Gitに入れない）
├── processed_ids.json   # 処理済みID記録
└── output/              # 生成されたテキストファイル
```

## NotebookLMへの追加方法

1. [NotebookLM](https://notebooklm.google.com) を開く
2. 「ソースを追加」→「Google ドライブ」を選択
3. `X-Bookmarks-NotebookLM` フォルダを選択

## 注意事項

- `config.json` と `session.json` はGitに含まれません（.gitignoreで除外済み）
- セッションの有効期限が切れた場合は `save_session.py` を再実行してください
