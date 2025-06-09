# プロジェクト構成

## ディレクトリ構造

```
app-animal-dinosaur-game/
├── main.py                  # メインゲームエントリーポイント
├── game/                    # ゲームのコアロジック
│   ├── __init__.py
│   ├── game_manager.py      # ゲーム全体の管理
│   ├── card.py              # カードクラス
│   ├── character.py         # キャラクタークラス
│   ├── environment.py       # 環境（ステージ）クラス
│   ├── encyclopedia.py      # 図鑑機能
│   ├── sticker_book.py      # シールブック機能
│   └── hide_and_seek.py     # かくれんぼ機能
├── ui/                      # ユーザーインターフェース
│   ├── __init__.py
│   ├── menu.py              # メインメニュー
│   ├── game_screen.py       # ゲーム画面
│   ├── encyclopedia_ui.py   # 図鑑UI
│   ├── sticker_book_ui.py   # シールブックUI
│   ├── button.py            # ボタンクラス
│   └── animation.py         # アニメーション
├── assets/                  # ゲームアセット
│   ├── images/              # 画像ファイル
│   │   ├── characters/      # キャラクター画像
│   │   │   ├── animals/     # 動物画像
│   │   │   └── dinosaurs/   # 恐竜画像
│   │   ├── backgrounds/     # 背景画像
│   │   ├── cards/           # カード画像
│   │   ├── ui/              # UI要素画像
│   │   └── effects/         # エフェクト画像
│   ├── sounds/              # 音声ファイル
│   │   ├── bgm/             # 背景音楽
│   │   ├── sfx/             # 効果音
│   │   └── voices/          # 音声ガイド
│   └── fonts/               # フォントファイル
├── data/                    # データファイル
│   ├── characters.json      # キャラクター情報
│   ├── environments.json    # 環境情報
│   └── stickers.json        # シール情報
├── utils/                   # ユーティリティ
│   ├── __init__.py
│   ├── config.py            # 設定管理
│   ├── resource_loader.py   # リソース読み込み
│   ├── save_manager.py      # セーブデータ管理
│   └── sound_manager.py     # 音声管理
└── docs/                    # ドキュメント
    ├── README.md            # プロジェクト概要
    ├── game_design.md       # ゲーム設計書
    └── api_docs.md          # API仕様書
```

## 主要クラス設計

### GameManager
ゲーム全体の状態管理を行うクラス
```python
class GameManager:
    def __init__(self):
        self.current_state = "MENU"  # MENU, GAME, ENCYCLOPEDIA, STICKER_BOOK
        self.current_environment = None
        self.discovered_characters = []
        self.score = 0
        
    def change_state(self, new_state):
        # 状態遷移処理
        
    def start_game(self, environment):
        # ゲーム開始処理
        
    def discover_character(self, character):
        # キャラクター発見処理
```

### Card
神経衰弱のカードを表すクラス
```python
class Card:
    def __init__(self, character, position):
        self.character = character
        self.position = position
        self.is_flipped = False
        self.is_matched = False
        
    def flip(self):
        # カードをめくる処理
        
    def update(self):
        # 状態更新処理
        
    def draw(self, surface):
        # 描画処理
```

### Character
動物や恐竜のキャラクターを表すクラス
```python
class Character:
    def __init__(self, id, name, type, environment, image_path, sound_path):
        self.id = id
        self.name = name
        self.type = type  # "animal" or "dinosaur"
        self.environment = environment
        self.image = None  # 画像読み込み
        self.sound = None  # 音声読み込み
        self.is_discovered = False
        
    def play_sound(self):
        # 鳴き声を再生
        
    def animate(self):
        # アニメーション処理
```

### Environment
ゲームの環境（ステージ）を表すクラス
```python
class Environment:
    def __init__(self, id, name, background_path, bgm_path):
        self.id = id
        self.name = name
        self.background = None  # 背景画像読み込み
        self.bgm = None  # BGM読み込み
        self.characters = []  # この環境に登場するキャラクター
        self.is_unlocked = False
        
    def add_character(self, character):
        # キャラクター追加
        
    def play_bgm(self):
        # BGM再生
```

### Encyclopedia
図鑑機能を管理するクラス
```python
class Encyclopedia:
    def __init__(self):
        self.discovered_characters = {}  # 環境ごとに発見したキャラクター
        
    def register_character(self, character):
        # キャラクターを図鑑に登録
        
    def get_completion_rate(self, environment=None):
        # 発見率を計算
        
    def get_character_info(self, character_id):
        # キャラクター情報を取得
```

### StickerBook
シールブック機能を管理するクラス
```python
class StickerBook:
    def __init__(self):
        self.stickers = []  # 獲得したシール
        self.pages = []  # 作成したページ
        
    def add_sticker(self, character):
        # シールを追加
        
    def create_page(self, background):
        # 新しいページを作成
        
    def save_page(self, page):
        # ページを保存
        
    def place_sticker(self, sticker, position, size, rotation):
        # シールを配置
```

## データ構造

### characters.json
```json
{
  "animals": [
    {
      "id": "lion",
      "name": "ライオン",
      "type": "animal",
      "environment": "jungle",
      "image": "lion.png",
      "sound": "lion.wav",
      "description": "ライオンはどうぶつの王さまだよ。大きなたてがみが特徴だね。",
      "facts": ["オスのライオンには、たてがみがあるよ", "家族で生活するよ", "ガオーと鳴くよ"]
    },
    // 他の動物...
  ],
  "dinosaurs": [
    {
      "id": "trex",
      "name": "ティラノサウルス",
      "type": "dinosaur",
      "environment": "jungle",
      "image": "trex.png",
      "sound": "trex.wav",
      "description": "ティラノサウルスは大きな頭と小さな腕を持つ恐竜だよ。",
      "facts": ["とても大きな頭を持っているよ", "小さな腕を持っているよ", "鋭い歯を持っているよ"]
    },
    // 他の恐竜...
  ]
}
```

### environments.json
```json
[
  {
    "id": "jungle",
    "name": "ジャングル",
    "background": "jungle_bg.png",
    "bgm": "jungle_bgm.mp3",
    "characters": ["lion", "monkey", "leopard", "trex", "velociraptor"],
    "unlock_condition": "none"
  },
  {
    "id": "ocean",
    "name": "うみ",
    "background": "ocean_bg.png",
    "bgm": "ocean_bgm.mp3",
    "characters": ["dolphin", "whale", "turtle", "plesiosaurus", "mosasaurus"],
    "unlock_condition": "jungle_complete"
  },
  // 他の環境...
]
```

## 実装フェーズ

### フェーズ1: 基本システム
- Pygameの初期化と基本構造
- カードめくりシステム
- キャラクター表示

### フェーズ2: ゲームメカニクス
- 神経衰弱のマッチングロジック
- かくれんぼ要素
- 環境選択システム

### フェーズ3: 図鑑機能
- 図鑑UI
- キャラクター情報表示
- 発見率計算

### フェーズ4: シールブック機能
- シールブックUI
- シール配置システム
- ページ保存/読み込み

### フェーズ5: 仕上げ
- サウンド実装
- アニメーション追加
- バグ修正とパフォーマンス最適化
