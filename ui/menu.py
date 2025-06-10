#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
メインメニュー画面
"""

import pygame
from ui.button import Button
from ui.environment_select import EnvironmentSelectScreen
from ui.encyclopedia_ui import EncyclopediaScreen
from ui.sticker_book_ui import StickerBookScreen
from utils.font_manager import FontManager
from utils.resource_loader import ResourceLoader

class MainMenu:
    """メインメニュー画面クラス"""
    
    def __init__(self, screen, game_manager):
        """
        メインメニューを初期化する
        
        Args:
            screen: 描画対象の画面
            game_manager: ゲームマネージャー
        """
        self.screen = screen
        self.game_manager = game_manager
        self.next_screen = None
        
        # 画面サイズを取得
        self.width, self.height = self.screen.get_size()
        
        # タイトルフォント
        self.title_font = FontManager.get_instance().get_font(64)
        
        # リソースローダー
        self.resource_loader = ResourceLoader.get_instance()
        
        # ボタンの作成
        button_width = 350
        button_height = 60
        button_margin = 20
        start_y = self.height // 2 - 50
        
        # スタートボタン
        self.start_button = Button(
            self.width // 2 - button_width // 2,
            start_y,
            button_width,
            button_height,
            "あそぶ",
            font_size=48,
            color=(46, 139, 87),  # 緑色
            hover_color=(60, 179, 113)
        )
        
        # 図鑑ボタン（非活性）
        self.encyclopedia_button = Button(
            self.width // 2 - button_width // 2,
            start_y + button_height + button_margin,
            button_width,
            button_height,
            "ずかん（開発中）",
            font_size=36,
            color=(150, 150, 150),  # グレー色（非活性）
            hover_color=(150, 150, 150)
        )
        
        # シールブックボタン（非活性）
        self.sticker_book_button = Button(
            self.width // 2 - button_width // 2,
            start_y + (button_height + button_margin) * 2,
            button_width,
            button_height,
            "シールブック（開発中）",
            font_size=32,
            color=(150, 150, 150),  # グレー色（非活性）
            hover_color=(150, 150, 150)
        )
        
        # 背景画像の読み込み - 背景色で代用
        self.background = pygame.Surface((self.width, self.height))
        self.background.fill((240, 248, 255))  # 薄い水色
        
        # タイトルロゴはテキストで代用するためNoneに設定
        self.title_logo = None
        
        # キャラクター画像の読み込み
        self.character_image = self.resource_loader.load_character_image(
            "lion", 
            "jungle", 
            (80, 80)
        )
        
        # 動物のキャラクターアニメーション
        self.animal_pos = [100, self.height - 150]
        self.animal_direction = [1, 0]
        self.animal_speed = 2
    
    def handle_event(self, event):
        """
        イベントを処理する
        
        Args:
            event: pygameのイベント
        """
        # スタートボタンのイベント処理
        if self.start_button.handle_event(event):
            self.next_screen = EnvironmentSelectScreen(self.screen, self.game_manager)
        
        # TODO: 図鑑機能とシールブック機能の実装
        # 図鑑ボタンのイベント処理
        # elif self.encyclopedia_button.handle_event(event):
        #     self.next_screen = EncyclopediaScreen(self.screen, self.game_manager)
        # 
        # シールブックボタンのイベント処理
        # elif self.sticker_book_button.handle_event(event):
        #     self.next_screen = StickerBookScreen(self.screen, self.game_manager)
    
    def update(self):
        """画面の状態を更新する"""
        # ボタンの更新
        self.start_button.update()
        self.encyclopedia_button.update()
        self.sticker_book_button.update()
        
        # 動物のアニメーション
        self.animal_pos[0] += self.animal_direction[0] * self.animal_speed
        if self.animal_pos[0] < 50 or self.animal_pos[0] > self.width - 50:
            self.animal_direction[0] *= -1
    
    def draw(self):
        """画面を描画する"""
        # 背景を描画
        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            # 背景画像がない場合は色で塗りつぶす
            self.screen.fill((240, 248, 255))
        
        # タイトルロゴを描画
        if self.title_logo:
            logo_rect = self.title_logo.get_rect(center=(self.width // 2, 130))
            self.screen.blit(self.title_logo, logo_rect)
        else:
            # タイトルロゴがない場合はテキストで描画
            title_text = "どうぶつと恐竜の"
            title_surface = self.title_font.render(title_text, True, (0, 0, 0))
            title_rect = title_surface.get_rect(center=(self.width // 2, 100))
            self.screen.blit(title_surface, title_rect)
            
            # サブタイトルを描画
            subtitle_text = "かくれんぼ神経衰弱"
            subtitle_surface = self.title_font.render(subtitle_text, True, (0, 0, 0))
            subtitle_rect = subtitle_surface.get_rect(center=(self.width // 2, 160))
            self.screen.blit(subtitle_surface, subtitle_rect)
        
        # キャラクターを描画
        if self.character_image:
            self.screen.blit(self.character_image, self.animal_pos)
        else:
            # キャラクター画像がない場合は円で代用
            pygame.draw.circle(self.screen, (255, 165, 0), self.animal_pos, 30)
        
        # ボタンを描画
        self.start_button.draw(self.screen)
        self.encyclopedia_button.draw(self.screen)
        self.sticker_book_button.draw(self.screen)
    
    def get_next_screen(self):
        """
        次の画面を取得する
        
        Returns:
            次の画面、または None
        """
        next_screen = self.next_screen
        self.next_screen = None
        return next_screen
