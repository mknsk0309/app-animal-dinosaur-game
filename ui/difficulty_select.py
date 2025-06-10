#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
難易度選択画面
"""

import pygame
from ui.button import Button
from utils.font_manager import FontManager

class DifficultySelectScreen:
    """難易度選択画面クラス"""
    
    def __init__(self, screen, game_manager, previous_screen):
        """
        難易度選択画面を初期化する
        
        Args:
            screen: 描画対象の画面
            game_manager: ゲームマネージャー
            previous_screen: 前の画面
        """
        self.screen = screen
        self.game_manager = game_manager
        self.previous_screen = previous_screen
        self.next_screen = None
        
        # 画面サイズを取得
        self.width, self.height = self.screen.get_size()
        
        # フォント
        self.title_font = FontManager.get_instance().get_font(48)
        self.description_font = FontManager.get_instance().get_font(24)
        
        # 難易度ボタンの作成
        button_width = 300
        button_height = 80
        button_margin = 30
        start_y = self.height // 2 - (button_height * 3 + button_margin * 2) // 2
        
        # かんたんボタン
        self.easy_button = Button(
            self.width // 2 - button_width // 2,
            start_y,
            button_width,
            button_height,
            "かんたん",
            font_size=36,
            color=(46, 139, 87),  # 緑色
            hover_color=(60, 179, 113)
        )
        
        # ふつうボタン
        self.normal_button = Button(
            self.width // 2 - button_width // 2,
            start_y + button_height + button_margin,
            button_width,
            button_height,
            "ふつう",
            font_size=36,
            color=(70, 130, 180),  # 青色
            hover_color=(30, 144, 255)
        )
        
        # むずかしいボタン
        self.hard_button = Button(
            self.width // 2 - button_width // 2,
            start_y + (button_height + button_margin) * 2,
            button_width,
            button_height,
            "むずかしい",
            font_size=36,
            color=(178, 34, 34),  # 赤色
            hover_color=(220, 20, 60)
        )
        
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
        
        # 現在の難易度を強調表示
        self._highlight_current_difficulty()
    
    def _highlight_current_difficulty(self):
        """現在の難易度ボタンを強調表示する"""
        # すべてのボタンを通常の色に戻す
        self.easy_button.color = (46, 139, 87)
        self.normal_button.color = (70, 130, 180)
        self.hard_button.color = (178, 34, 34)
        
        # 現在の難易度のボタンを強調表示
        if self.game_manager.difficulty == "easy":
            self.easy_button.color = (60, 179, 113)
        elif self.game_manager.difficulty == "normal":
            self.normal_button.color = (30, 144, 255)
        elif self.game_manager.difficulty == "hard":
            self.hard_button.color = (220, 20, 60)
    
    def handle_event(self, event):
        """
        イベントを処理する
        
        Args:
            event: pygameのイベント
        """
        # かんたんボタンのイベント処理
        if self.easy_button.handle_event(event):
            self.game_manager.set_difficulty("easy")
            self._highlight_current_difficulty()
        
        # ふつうボタンのイベント処理
        elif self.normal_button.handle_event(event):
            self.game_manager.set_difficulty("normal")
            self._highlight_current_difficulty()
        
        # むずかしいボタンのイベント処理
        elif self.hard_button.handle_event(event):
            self.game_manager.set_difficulty("hard")
            self._highlight_current_difficulty()
        
        # 戻るボタンのイベント処理
        elif self.back_button.handle_event(event):
            self.next_screen = self.previous_screen
    
    def update(self):
        """画面の状態を更新する"""
        # ボタンの更新
        self.easy_button.update()
        self.normal_button.update()
        self.hard_button.update()
        self.back_button.update()
    
    def draw(self):
        """画面を描画する"""
        # 背景を描画（薄い水色）
        self.screen.fill((240, 248, 255))
        
        # タイトルを描画
        title_text = "むずかしさを えらぶ"
        title_surface = self.title_font.render(title_text, True, (0, 0, 0))
        title_rect = title_surface.get_rect(center=(self.width // 2, 70))
        self.screen.blit(title_surface, title_rect)
        
        # 難易度の説明
        descriptions = {
            "easy": "カードが少なくて かんたん！",
            "normal": "カードが ふえるよ",
            "hard": "カードがたくさん！ むずかしいよ"
        }
        
        # 現在選択されている難易度の説明を表示
        desc_text = descriptions.get(self.game_manager.difficulty, "")
        desc_surface = self.description_font.render(desc_text, True, (0, 0, 0))
        desc_rect = desc_surface.get_rect(center=(self.width // 2, 120))
        self.screen.blit(desc_surface, desc_rect)
        
        # ボタンを描画
        self.easy_button.draw(self.screen)
        self.normal_button.draw(self.screen)
        self.hard_button.draw(self.screen)
        self.back_button.draw(self.screen)
        
        # 選択中の難易度に黄色い枠を描画
        border_width = 5
        padding = 15  # ボタンと枠の間の余白
        if self.game_manager.difficulty == "easy":
            pygame.draw.rect(self.screen, (255, 255, 0), self.easy_button.rect.inflate(padding*2, padding*2), border_width)
        elif self.game_manager.difficulty == "normal":
            pygame.draw.rect(self.screen, (255, 255, 0), self.normal_button.rect.inflate(padding*2, padding*2), border_width)
        elif self.game_manager.difficulty == "hard":
            pygame.draw.rect(self.screen, (255, 255, 0), self.hard_button.rect.inflate(padding*2, padding*2), border_width)
    
    def get_next_screen(self):
        """
        次の画面を取得する
        
        Returns:
            次の画面、または None
        """
        next_screen = self.next_screen
        self.next_screen = None
        return next_screen