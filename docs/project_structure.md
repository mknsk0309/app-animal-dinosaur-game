# プロジェクト構成

## 現在のディレクトリ構造

```
app-animal-dinosaur-game/
├── main.py                  # メインゲームエントリーポイント
├── game/                    # ゲームのコアロジック
│   ├── __init__.py
│   ├── game_manager.py      # ゲーム全体の管理
│   ├── environment.py       # 環境（ステージ）クラス
│   └── character.py         # キャラクター管理クラス
├── ui/                      # ユーザーインターフェース
│   ├── __init__.py
│   ├── button.py            # ボタンクラス
│   ├── menu.py              # メインメニュー
│   ├── environment_select.py # 環境選択画面
│   ├── difficulty_select.py # 難易度選択画面
│   ├── game_screen.py       # ゲーム画面
│   ├── encyclopedia_ui.py   # 図鑑UI（開発中）
│   └── sticker_book_ui.py   # シールブックUI（開発中）
├── assets/                  # ゲームアセット
│   ├── images/              # 画像ファイル
│   │   ├── backgrounds/     # 背景画像
│   │   ├── card_backs/      # カード裏面画像
│   │   ├── characters/      # キャラクター画像
│   │   │   ├── animals/     # 動物画像
│   │   │   └── dinosaurs/   # 恐竜画像
│   │   └── ui/              # UI要素画像
│   ├── sounds/              # 音声ファイル（未実装）
│   └── fonts/               # フォントファイル
│       └── MPLUSRounded1c-Medium.ttf # 日本語フォント
├── utils/                   # ユーティリティ
│   ├── __init__.py
│   ├── config.py            # 設定管理
│   ├── config_loader.py     # 設定ファイル読み込み
│   ├── font_manager.py      # フォント管理
│   └── resource_loader.py   # リソース読み込み
├── data/                    # データファイル
│   ├── characters.json      # キャラクター情報
│   ├── environments.json    # 環境情報
│   └── game_config.json     # ゲーム設定
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
│   ├── encyclopedia.py      # 図鑑機能
│   ├── sticker_book.py      # シールブック機能
│   └── hide_and_seek.py     # かくれんぼ機能
├── assets/
│   └── sounds/              # 音声ファイル
│       ├── bgm/             # 背景音楽
│       ├── sfx/             # 効果音
│       └── voices/          # 音声ガイド
└── utils/
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
        
        # 難易度
        self.difficulty = "easy"
    
    def change_state(self, new_state):
        # 状態遷移処理
        
    def select_environment(self, environment):
        # 環境選択処理
        
    def discover_character(self, character):
        # キャラクター発見処理
        
    def reset_game(self):
        # ゲームリセット処理
        
    def set_difficulty(self, difficulty):
        # 難易度設定処理
```

### Environment
環境（ステージ）を表すクラス
```python
class Environment:
    # 環境の種類
    TYPE_JUNGLE = "jungle"
    TYPE_OCEAN = "ocean"
    TYPE_DESERT = "desert"
    TYPE_FOREST = "forest"
    
    @classmethod
    def get_card_backs(cls, environment_type):
        # 環境に対応するカード裏面のリストを取得
        
    @classmethod
    def get_name(cls, environment_type):
        # 環境の日本語名を取得
        
    @classmethod
    def get_background_color(cls, environment_type):
        # 環境の背景色を取得
```

### Character
キャラクター（動物・恐竜）を表すクラス
```python
class Character:
    # キャラクターの種類
    TYPE_ANIMAL = "animal"
    TYPE_DINOSAUR = "dinosaur"
    
    @classmethod
    def get_character_info(cls, character_id):
        # キャラクター情報を取得
        
    @classmethod
    def get_name(cls, character_id):
        # キャラクターの日本語名を取得
        
    @classmethod
    def get_characters_by_environment(cls, environment_type, difficulty):
        # 環境と難易度に対応するキャラクターのリストを取得
```

### ConfigLoader
設定ファイルを読み込むクラス
```python
class ConfigLoader:
    @classmethod
    def get_instance(cls):
        # シングルトンインスタンスを取得
        
    def load_config(self, config_name):
        # 設定ファイルを読み込む
        
    def get_environments(self):
        # 環境設定を取得
        
    def get_characters(self):
        # キャラクター設定を取得
        
    def get_game_config(self):
        # ゲーム設定を取得
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
- キャラクター表示

### フェーズ2: ゲームメカニクス ✅
- カードめくりのマッチングロジック
- 環境選択システム
- 環境ごとの動物・恐竜の表示
- 画像表示機能の実装
- 難易度設定機能（かんたん・ふつう・むずかしい）
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

## データ構造

### JSONファイル
- **environments.json**: 環境の設定（名前、背景色、カード裏面）
- **characters.json**: キャラクター情報（動物と恐竜）
- **game_config.json**: ゲーム設定（難易度など）