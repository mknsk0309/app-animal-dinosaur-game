#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ゲーム画面
"""

import pygame
from ui.button import Button
from utils.font_manager import FontManager
from utils.resource_loader import ResourceLoader
from utils.config_loader import ConfigLoader

class GameScreen:
    """ゲーム画面クラス（神経衰弱ゲーム）"""
    
    def __init__(self, screen, game_manager):
        """
        ゲーム画面を初期化する
        
        Args:
            screen: 描画対象の画面
            game_manager: ゲームマネージャー
        """
        self.screen = screen
        self.game_manager = game_manager
        self.next_screen = None
        
        # 画面サイズを取得
        self.width, self.height = self.screen.get_size()
        
        # フォント
        self.title_font = FontManager.get_instance().get_font(36)
        self.info_font = FontManager.get_instance().get_font(24)
        
        # リソースローダー
        self.resource_loader = ResourceLoader.get_instance()
        
        # 設定ローダー
        self.config_loader = ConfigLoader.get_instance()
        
        # 選択された環境
        self.environment = self.game_manager.current_environment
        
        # 背景画像の読み込み
        self.background_image = self.resource_loader.load_background_image(
            self.environment, 
            (self.width, self.height)
        )
        
        # 戻るボタン
        self.back_button = Button(
            50,
            self.height - 100,
            120,
            50,
            "もどる",
            font_size=32,
            color=(100, 100, 100),
            hover_color=(130, 130, 130)
        )
        
        # カードの初期化
        self.initialize_cards()
        
        # ゲーム状態
        self.first_card = None
        self.second_card = None
        self.wait_time = 0
        self.is_match = False  # カードが一致したかどうか
        self.matched_pairs = 0
        self.total_pairs = len(self.cards) // 2
        self.game_over = False
        
        # 環境に応じた背景色（背景画像がない場合のフォールバック）
        from game.environment import Environment
        self.background_color = Environment.get_background_color(self.environment)
    
    def initialize_cards(self):
        """カードを初期化する"""
        # 難易度設定を取得
        difficulty_config = self.config_loader.get_difficulty_config(self.game_manager.difficulty)
        
        # 難易度に応じたカードの配置
        rows = difficulty_config.get("rows", 2)
        cols = difficulty_config.get("cols", 3)
        pairs_count = difficulty_config.get("pairs_count", 3)
        
        # 難易度に応じてカードのサイズと間隔を調整
        card_width = difficulty_config.get("card_width", 140)
        card_height = difficulty_config.get("card_height", 200)
        margin = difficulty_config.get("margin", 30)
        
        # カードの配置開始位置
        start_x = (self.width - (cols * card_width + (cols - 1) * margin)) // 2
        start_y = (self.height - (rows * card_height + (rows - 1) * margin)) // 2
        
        # 環境と難易度に応じたキャラクターを取得
        from game.character import Character
        characters = Character.get_characters_by_environment(self.environment, self.game_manager.difficulty)
        
        # キャラクターが足りない場合は同じキャラクターを複数回使用
        while len(characters) < pairs_count:
            # 既存のキャラクターを複製して追加
            if len(characters) > 0:
                characters.append(characters[0])  # 最初のキャラクターを再利用
            else:
                # 万が一キャラクターがない場合はデフォルトを使用
                characters = ["dolphin", "whale", "turtle"]
        
        # 使用するキャラクターを選択（重複なし）
        import random
        selected_characters = random.sample(characters, pairs_count)
        
        # カードの位置を作成
        positions = []
        if self.game_manager.difficulty == "hard":
            # むずかしいモードでは最後の行の列数が異なる場合がある
            last_row_cols = difficulty_config.get("last_row_cols", cols)
            
            for i in range(rows):
                row_cols = last_row_cols if i == rows - 1 and last_row_cols != cols else cols
                row_start_x = (self.width - (row_cols * card_width + (row_cols - 1) * margin)) // 2
                for j in range(row_cols):
                    x = row_start_x + j * (card_width + margin)
                    y = start_y + i * (card_height + margin)
                    positions.append((x, y))
        else:
            # かんたん・ふつうモードは通常の配置
            for i in range(rows):
                for j in range(cols):
                    x = start_x + j * (card_width + margin)
                    y = start_y + i * (card_height + margin)
                    positions.append((x, y))
        
        # 位置をシャッフル
        random.shuffle(positions)
        
        # カードの作成
        self.cards = []
        
        # 各キャラクターについて2枚ずつカードを作成
        for character in selected_characters:
            for _ in range(2):  # 各キャラクター2枚ずつ
                if positions:
                    x, y = positions.pop(0)
                    
                    # カード画像の読み込み
                    card_back_image = self.resource_loader.load_card_image(
                        character, 
                        flipped=True, 
                        scale=(card_width, card_height),
                        environment=self.environment
                    )
                    
                    card_front_image = self.resource_loader.load_card_image(
                        character, 
                        flipped=False, 
                        scale=(card_width, card_height)
                    )
                    
                    self.cards.append({
                        "rect": pygame.Rect(x, y, card_width, card_height),
                        "type": character,
                        "flipped": False,
                        "matched": False,
                        "back_image": card_back_image,
                        "front_image": card_front_image
                    })
    
    def handle_event(self, event):
        """
        イベントを処理する
        
        Args:
            event: pygameのイベント
        """
        # ゲームオーバー時は戻るボタンのみ有効
        if self.game_over:
            if self.back_button.handle_event(event):
                from ui.environment_select import EnvironmentSelectScreen
                self.next_screen = EnvironmentSelectScreen(self.screen, self.game_manager)
            return
        
        # 待機時間中は入力を無視
        if self.wait_time > 0:
            return
        
        # 戻るボタンのイベント処理
        if self.back_button.handle_event(event):
            from ui.environment_select import EnvironmentSelectScreen
            self.next_screen = EnvironmentSelectScreen(self.screen, self.game_manager)
            return  # 戻るボタンをクリックした場合は、カードの処理をスキップ
        
        # カードクリックの処理
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # すでに2枚めくっている場合は何もしない
            if self.first_card is not None and self.second_card is not None:
                return
            
            # クリックされたカードを探す
            for i, card in enumerate(self.cards):
                if card["rect"].collidepoint(event.pos) and not card["flipped"] and not card["matched"]:
                    # すでに選択されているカードは選択できない
                    if self.first_card == i:
                        return
                    
                    # カードをめくる
                    card["flipped"] = True
                    
                    # 1枚目のカード
                    if self.first_card is None:
                        self.first_card = i
                    # 2枚目のカード
                    elif self.second_card is None:
                        self.second_card = i
                        
                        # 2枚のカードが一致するか確認
                        first_card = self.cards[self.first_card]
                        second_card = self.cards[self.second_card]
                        
                        # カードが一致したかどうかを記録
                        self.is_match = first_card["type"] == second_card["type"]
                        
                        # 待機時間を設定
                        game_config = self.config_loader.get_game_config()
                        difficulty_config = self.config_loader.get_difficulty_config(self.game_manager.difficulty)
                        
                        if self.is_match:
                            # ペア成立時は一定の待機時間
                            self.wait_time = game_config.get("match_wait_time", 30)
                        else:
                            # ペア不成立時は難易度に応じた待機時間
                            self.wait_time = difficulty_config.get("wait_time", 30)
                    break
    
    def update(self):
        """画面の状態を更新する"""
        # ボタンの更新
        self.back_button.update()
        
        # 待機時間の更新
        if self.wait_time > 0:
            self.wait_time -= 1
            if self.wait_time == 0:
                # 待機時間が終了したら、記録した一致状態に基づいて処理
                if self.first_card is not None and self.second_card is not None:
                    first_card = self.cards[self.first_card]
                    second_card = self.cards[self.second_card]
                    
                    # カードが一致した場合
                    if self.is_match:
                        first_card["matched"] = True
                        second_card["matched"] = True
                        self.matched_pairs += 1
                        
                        # キャラクターを発見したとマークする
                        self.game_manager.discover_character(first_card["type"])
                        
                        # すべてのペアが見つかった場合
                        if self.matched_pairs == self.total_pairs:
                            self.game_over = True
                    else:
                        # 一致しなかった場合、カードを裏返す
                        first_card["flipped"] = False
                        second_card["flipped"] = False
                    
                    # カードの選択をリセット
                    self.first_card = None
                    self.second_card = None
                    self.is_match = False
    
    def draw(self):
        """画面を描画する"""
        # 通常の背景を描画
        if self.background_image:
            self.screen.blit(self.background_image, (0, 0))
        else:
            # 背景画像がない場合は色で塗りつぶす
            self.screen.fill(self.background_color)
        
        # 環境名を描画
        from game.environment import Environment
        title_text = f"{Environment.get_name(self.environment)}で あそぶ"
        title_surface = self.title_font.render(title_text, True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.width // 2, 40))
        self.screen.blit(title_surface, title_rect)
        
        # カードを描画
        for card in self.cards:
            if card["matched"]:
                # マッチしたカードは半透明に
                matched_image = card["front_image"].copy()
                matched_image.set_alpha(128)
                self.screen.blit(matched_image, card["rect"])
            elif card["flipped"]:
                # めくられたカード（表面）
                self.screen.blit(card["front_image"], card["rect"])
            else:
                # 裏向きのカード
                self.screen.blit(card["back_image"], card["rect"])
        
        # ゲームオーバー時の表示
        if self.game_over:
            # 半透明のオーバーレイ
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))
            self.screen.blit(overlay, (0, 0))
            
            # おめでとうメッセージ
            congrats_font = FontManager.get_instance().get_font(72)
            congrats_text = "おめでとう！"
            congrats_surface = congrats_font.render(congrats_text, True, (255, 255, 0))
            congrats_rect = congrats_surface.get_rect(center=(self.width // 2, self.height // 2 - 50))
            self.screen.blit(congrats_surface, congrats_rect)
        
        # 戻るボタンを描画
        self.back_button.draw(self.screen)
    
    def get_next_screen(self):
        """
        次の画面を取得する
        
        Returns:
            次の画面、または None
        """
        next_screen = self.next_screen
        self.next_screen = None
        return next_screen