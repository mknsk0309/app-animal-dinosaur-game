#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
図鑑画面
"""

import pygame
from ui.button import Button
from utils.font_manager import FontManager

class EncyclopediaScreen:
    """図鑑画面クラス"""
    
    def __init__(self, screen, game_manager):
        """
        図鑑画面を初期化する
        
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
        self.title_font = FontManager.get_instance().get_font(48)
        self.info_font = FontManager.get_instance().get_font(24)
        
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
        
        # TODO: 図鑑機能の実装
        self.under_development = True
    
    def handle_event(self, event):
        """
        イベントを処理する
        
        Args:
            event: pygameのイベント
        """
        # 戻るボタンのイベント処理
        if self.back_button.handle_event(event):
            from ui.menu import MainMenu
            self.next_screen = MainMenu(self.screen, self.game_manager)
    
    def update(self):
        """画面の状態を更新する"""
        # ボタンの更新
        self.back_button.update()
    
    def draw(self):
        """画面を描画する"""
        # 背景を描画（薄い水色）
        self.screen.fill((240, 248, 255))
        
        # タイトルを描画
        title_text = "ずかん"
        title_surface = self.title_font.render(title_text, True, (0, 0, 0))
        title_rect = title_surface.get_rect(center=(self.width // 2, 50))
        self.screen.blit(title_surface, title_rect)
        
        # 開発中メッセージ
        if self.under_development:
            dev_text = "この機能は現在開発中です"
            dev_surface = self.title_font.render(dev_text, True, (200, 0, 0))
            dev_rect = dev_surface.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(dev_surface, dev_rect)
            
            coming_text = "Coming Soon!"
            coming_surface = self.title_font.render(coming_text, True, (0, 0, 200))
            coming_rect = coming_surface.get_rect(center=(self.width // 2, self.height // 2 + 60))
            self.screen.blit(coming_surface, coming_rect)
        
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
