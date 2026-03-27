# セットアップ手順

## パッケージ管理ツール
### uvの初期化
```bash
uv init
```

---
## 静的解析・フォーマッタ
```bash
uv add --dev ruff
```

---
## テストライブラリー
```bash
uv add --dev pytest
```

---
## 型チェック
```bash
uv add --dev pyright
```

### 実行
```bash
uv run pyright src
```

---
## Git フック
```bash
uv add --dev pre-commit
```

### 有効化
```bash
uv run pre-commit install
```

### 実行
```bash
uv run pre-commit run --all-files
```
