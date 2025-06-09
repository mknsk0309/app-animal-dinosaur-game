#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ゲーム画面
"""

import pygame
from ui.button import Button
from utils.font_manager import FontManager

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
        
        # 選択された環境
        self.environment = self.game_manager.current_environment
        
        # 戻るボタン
        self.back_button = Button(
            50,
            self.height - 80,
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
        self.matched_pairs = 0
        self.total_pairs = len(self.cards) // 2
        self.game_over = False
        
        # 環境に応じた背景色
        self.background_colors = {
            "jungle": (34, 139, 34),  # 森林緑
            "ocean": (0, 105, 148),   # 海色
            "desert": (210, 180, 140), # 砂色
            "forest": (139, 69, 19)   # 茶色
        }
    
    def initialize_cards(self):
        """カードを初期化する"""
        # 難易度に応じたカードの配置
        if self.game_manager.difficulty == "easy":
            rows, cols = 2, 3  # 6枚（3ペア）
        else:
            rows, cols = 3, 4  # 12枚（6ペア）
        
        # カードのサイズと間隔
        card_width = 100
        card_height = 150
        margin = 20
        
        # カードの配置開始位置
        start_x = (self.width - (cols * card_width + (cols - 1) * margin)) // 2
        start_y = (self.height - (rows * card_height + (rows - 1) * margin)) // 2
        
        # カードの作成（仮のプレースホルダー）
        self.cards = []
        card_types = ["lion", "monkey", "elephant", "giraffe", "tiger", "panda"]
        
        # 難易度に応じたペア数
        pairs_count = 3 if self.game_manager.difficulty == "easy" else 6
        
        # カードの作成
        for i in range(rows):
            for j in range(cols):
                index = i * cols + j
                card_type = card_types[index // 2 % pairs_count]
                x = start_x + j * (card_width + margin)
                y = start_y + i * (card_height + margin)
                
                self.cards.append({
                    "rect": pygame.Rect(x, y, card_width, card_height),
                    "type": card_type,
                    "flipped": False,
                    "matched": False
                })
        
        # カードをシャッフル（仮の実装）
        import random
        random.shuffle(self.cards)
    
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
                        # 2枚目を選んだ時点で待機時間を設定
                        self.wait_time = 30  # 約0.5秒（30フレーム）
                    break
    
    def update(self):
        """画面の状態を更新する"""
        # ボタンの更新
        self.back_button.update()
        
        # 待機時間の更新
        if self.wait_time > 0:
            self.wait_time -= 1
            if self.wait_time == 0:
                # 2枚のカードを比較
                if self.first_card is not None and self.second_card is not None:
                    first_card = self.cards[self.first_card]
                    second_card = self.cards[self.second_card]
                    
                    # カードが一致した場合
                    if first_card["type"] == second_card["type"]:
                        first_card["matched"] = True
                        second_card["matched"] = True
                        self.matched_pairs += 1
                        
                        # キャラクターを発見したとマークする
                        self.game_manager.discover_character(first_card["type"])
                        
                        # スコアを追加
                        self.game_manager.add_score(100)
                        
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
    
    def draw(self):
        """画面を描画する"""
        # 環境に応じた背景色
        bg_color = self.background_colors.get(self.environment, (240, 248, 255))
        self.screen.fill(bg_color)
        
        # 環境名を描画
        environment_names = {
            "jungle": "ジャングル",
            "ocean": "うみ",
            "desert": "さばく",
            "forest": "もり"
        }
        title_text = f"{environment_names.get(self.environment, '不明')}で あそぶ"
        title_surface = self.title_font.render(title_text, True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.width // 2, 40))
        self.screen.blit(title_surface, title_rect)
        
        # スコアを描画
        score_text = f"スコア: {self.game_manager.score}"
        score_surface = self.info_font.render(score_text, True, (255, 255, 255))
        self.screen.blit(score_surface, (20, 20))
        
        # 見つけたペアの数を描画
        pairs_text = f"みつけたペア: {self.matched_pairs}/{self.total_pairs}"
        pairs_surface = self.info_font.render(pairs_text, True, (255, 255, 255))
        self.screen.blit(pairs_surface, (self.width - 200, 20))
        
        # カードを描画
        for card in self.cards:
            if card["matched"]:
                # マッチしたカードは透明に
                pygame.draw.rect(self.screen, (200, 200, 200, 128), card["rect"], border_radius=10)
            elif card["flipped"]:
                # めくられたカード
                pygame.draw.rect(self.screen, (255, 255, 255), card["rect"], border_radius=10)
                
                # カードの種類に応じた色（仮）
                card_colors = {
                    "lion": (255, 165, 0),     # オレンジ
                    "monkey": (139, 69, 19),   # 茶色
                    "elephant": (128, 128, 128), # グレー
                    "giraffe": (255, 215, 0),  # 金色
                    "tiger": (255, 140, 0),    # 濃いオレンジ
                    "panda": (0, 0, 0)         # 黒
                }
                color = card_colors.get(card["type"], (0, 0, 0))
                
                # 動物の絵の代わりに円を描画（仮）
                center_x = card["rect"].centerx
                center_y = card["rect"].centery
                pygame.draw.circle(self.screen, color, (center_x, center_y), 30)
                
                # 動物の名前を描画
                card_names = {
                    "lion": "ライオン",
                    "monkey": "サル",
                    "elephant": "ゾウ",
                    "giraffe": "キリン",
                    "tiger": "トラ",
                    "panda": "パンダ"
                }
                name = card_names.get(card["type"], "")
                name_surface = self.info_font.render(name, True, (0, 0, 0))
                name_rect = name_surface.get_rect(center=(center_x, center_y + 50))
                self.screen.blit(name_surface, name_rect)
            else:
                # 裏向きのカード
                pygame.draw.rect(self.screen, (70, 130, 180), card["rect"], border_radius=10)
                
                # カードの模様（仮）
                pygame.draw.rect(
                    self.screen, 
                    (30, 100, 150), 
                    (card["rect"].left + 10, card["rect"].top + 10, 
                     card["rect"].width - 20, card["rect"].height - 20), 
                    border_radius=5
                )
        
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
            
            # スコア表示
            score_text = f"スコア: {self.game_manager.score}"
            score_surface = congrats_font.render(score_text, True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(self.width // 2, self.height // 2 + 50))
            self.screen.blit(score_surface, score_rect)
        
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
