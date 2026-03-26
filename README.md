## セットアップ手順
### 初期化
```bash
uv init
```

### 静的解析・フォーマッタ
```bash
uv add --dev ruff
```

### テストライブラリー
```bash
uv add --dev pytest
```

### 型チェック
```bash
uv add --dev pyright
```

プロジェクト全体の型チェックを実行
```bash
uv run pyright src
```
