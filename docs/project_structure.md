# プロジェクト構成

## 現在のディレクトリ構造

```
app-animal-dinosaur-game/
├── main.py                  # メインゲームエントリーポイント
├── game/                    # ゲームのコアロジック
│   ├── __init__.py
│   └── game_manager.py      # ゲーム全体の管理
├── ui/                      # ユーザーインターフェース
│   ├── __init__.py
│   ├── button.py            # ボタンクラス
│   ├── menu.py              # メインメニュー
│   ├── environment_select.py # 環境選択画面
│   ├── game_screen.py       # ゲーム画面
│   ├── encyclopedia_ui.py   # 図鑑UI（開発中）
│   └── sticker_book_ui.py   # シールブックUI（開発中）
├── assets/                  # ゲームアセット
│   ├── images/              # 画像ファイル（未実装）
│   ├── sounds/              # 音声ファイル（未実装）
│   └── fonts/               # フォントファイル
│       └── MPLUSRounded1c-Medium.ttf # 日本語フォント
├── utils/                   # ユーティリティ
│   ├── __init__.py
│   ├── config.py            # 設定管理
│   └── font_manager.py      # フォント管理
└── docs/                    # ドキュメント
    ├── game_design.md       # ゲーム設計書
    ├── project_structure.md # プロジェクト構造
    ├── commit_rules.md      # コミットメッセージのルール
    └── devcontainer_usage.md # VSCode DevContainerの使い方
```

## 今後の実装予定

### 追加予定のファイル
```
app-animal-dinosaur-game/
├── game/
│   ├── card.py              # カードクラス
│   ├── character.py         # キャラクタークラス
│   ├── environment.py       # 環境（ステージ）クラス
│   ├── encyclopedia.py      # 図鑑機能
│   ├── sticker_book.py      # シールブック機能
│   └── hide_and_seek.py     # かくれんぼ機能
├── assets/
│   ├── images/              # 画像ファイル
│   │   ├── characters/      # キャラクター画像
│   │   │   ├── animals/     # 動物画像
│   │   │   └── dinosaurs/   # 恐竜画像
│   │   ├── backgrounds/     # 背景画像
│   │   ├── cards/           # カード画像
│   │   ├── ui/              # UI要素画像
│   │   └── effects/         # エフェクト画像
│   └── sounds/              # 音声ファイル
│       ├── bgm/             # 背景音楽
│       ├── sfx/             # 効果音
│       └── voices/          # 音声ガイド
├── data/                    # データファイル
│   ├── characters.json      # キャラクター情報
│   ├── environments.json    # 環境情報
│   └── stickers.json        # シール情報
└── utils/
    ├── resource_loader.py   # リソース読み込み
    ├── save_manager.py      # セーブデータ管理
    └── sound_manager.py     # 音声管理
```

## 実装済みクラス設計

### GameManager
ゲーム全体の状態管理を行うクラス
```python
class GameManager:
    def __init__(self):
        # 現在の状態
        self.current_state = self.STATE_MENU
        
        # 選択された環境
        self.current_environment = None
        
        # 発見されたキャラクター
        self.discovered_characters = []
        
        # スコア
        self.score = 0
        
        # 難易度
        self.difficulty = "easy"
    
    def change_state(self, new_state):
        # 状態遷移処理
        
    def select_environment(self, environment):
        # 環境選択処理
        
    def discover_character(self, character):
        # キャラクター発見処理
        
    def add_score(self, points):
        # スコア追加処理
        
    def reset_game(self):
        # ゲームリセット処理
        
    def set_difficulty(self, difficulty):
        # 難易度設定処理
```

### Button
UIボタンを表すクラス
```python
class Button:
    def __init__(self, x, y, width, height, text, font_size=32, 
                 color=(70, 130, 180), hover_color=(30, 144, 255), 
                 text_color=(255, 255, 255), border_radius=10):
        # ボタンの初期化
        
    def set_click_sound(self, sound_file):
        # クリック効果音設定
        
    def update(self):
        # 状態更新処理
        
    def handle_event(self, event):
        # イベント処理
        
    def draw(self, screen):
        # 描画処理
```

## 実装フェーズの進捗状況

### フェーズ1: 基本システム ✅
- Pygameの初期化と基本構造
- カードめくりシステム
- キャラクター表示（プレースホルダー）

### フェーズ2: ゲームメカニクス ✅
- 神経衰弱のマッチングロジック
- 環境選択システム
- かくれんぼ要素（未実装）

### フェーズ3: 図鑑機能 🔄
- 図鑑UI（基本構造のみ）
- キャラクター情報表示（未実装）
- 発見率計算（未実装）

### フェーズ4: シールブック機能 🔄
- シールブックUI（基本構造のみ）
- シール配置システム（未実装）
- ページ保存/読み込み（未実装）

### フェーズ5: 仕上げ ⬜
- サウンド実装
- アニメーション追加
- バグ修正とパフォーマンス最適化
