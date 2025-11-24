# Senior Navi (シニアナビ) - 簡易介護チェックアプリ

高齢者が簡単な質問に答えるだけで、要介護の可能性を簡易判定できるWebアプリケーションです。
見やすく、分かりやすいUIで、誰でも簡単にセルフチェックが可能です。

## 特徴
- **かんたん操作**: 「はい」「いいえ」の2択で答えるだけ。
- **見やすい画面**: 大きな文字とコントラストの効いた配色。
- **即時判定**: 回答後すぐに結果とアドバイスを表示。
- **履歴機能**: 過去のチェック結果を保存・確認可能。

## 技術スタック
- **フロントエンド**: React (Vite)
- **バックエンド**: FastAPI (Python)
- **データベース**: SQLite (ローカル保存)
- **インフラ**: Docker / Docker Compose

## 開発環境のセットアップ

### 必要要件
- Docker Desktop

### 起動方法
1. リポジトリをクローンします。
   ```bash
   git clone <repository-url>
   cd senior-navi
   ```

2. Docker Composeで起動します。
   ```bash
   docker compose up --build
   ```

3. ブラウザでアクセスします。
   - アプリ本体: http://localhost:5173
   - APIドキュメント: http://localhost:8000/docs

## ディレクトリ構成
```
senior-navi/
├── backend/        # FastAPI バックエンド
├── frontend/       # React フロントエンド
├── docker-compose.yml
├── Dockerfile      # 本番用（シングルコンテナ）ビルド定義
└── README.md
```

## ライセンス
MIT License
