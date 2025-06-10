#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
環境選択画面
"""

import pygame
from ui.button import Button
from ui.game_screen import GameScreen
from utils.font_manager import FontManager
from utils.resource_loader import ResourceLoader

class EnvironmentSelectScreen:
    """環境選択画面クラス"""
    
    def __init__(self, screen, game_manager):
        """
        環境選択画面を初期化する
        
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
        self.description_font = FontManager.get_instance().get_font(24)
        
        # リソースローダー
        self.resource_loader = ResourceLoader.get_instance()
        
        # 背景画像はダミーで代用
        self.background_image = None
        
        # 環境ボタンの作成
        button_width = 200
        button_height = 150
        button_margin = 30
        start_x = self.width // 2 - (button_width * 2 + button_margin) // 2
        start_y = self.height // 2 - (button_height * 2 + button_margin) // 2
        
        # 環境のサムネイル画像
        self.environment_thumbnails = {
            "jungle": self.resource_loader.load_background_image("jungle", (button_width, button_height)),
            "ocean": self.resource_loader.load_background_image("ocean", (button_width, button_height)),
            "desert": self.resource_loader.load_background_image("desert", (button_width, button_height)),
            "forest": self.resource_loader.load_background_image("forest", (button_width, button_height))
        }
        
        # ロックアイコンはダミーで代用
        self.lock_icon = None
        
        # ジャングルボタン
        self.jungle_button = Button(
            start_x,
            start_y,
            button_width,
            button_height,
            "ジャングル",
            font_size=36,
            color=(34, 139, 34),  # 森林緑
            hover_color=(50, 205, 50)
        )
        
        # 海ボタン
        self.ocean_button = Button(
            start_x + button_width + button_margin,
            start_y,
            button_width,
            button_height,
            "うみ",
            font_size=36,
            color=(0, 105, 148),  # 海色
            hover_color=(0, 154, 205)
        )
        
        # 砂漠ボタン（最初はロック）
        self.desert_button = Button(
            start_x,
            start_y + button_height + button_margin,
            button_width,
            button_height,
            "さばく",
            font_size=36,
            color=(210, 180, 140),  # 砂色
            hover_color=(244, 164, 96)
        )
        
        # 森ボタン（最初はロック）
        self.forest_button = Button(
            start_x + button_width + button_margin,
            start_y + button_height + button_margin,
            button_width,
            button_height,
            "もり",
            font_size=36,
            color=(139, 69, 19),  # 茶色
            hover_color=(160, 82, 45)
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
        
        # 難易度ボタン（難易度に応じた色で表示）
        difficulty_colors = {
            "easy": (46, 139, 87),    # 緑色
            "normal": (70, 130, 180), # 青色
            "hard": (178, 34, 34)     # 赤色
        }
        difficulty_hover_colors = {
            "easy": (60, 179, 113),   # 緑色（ホバー時）
            "normal": (30, 144, 255), # 青色（ホバー時）
            "hard": (220, 20, 60)     # 赤色（ホバー時）
        }
        
        self.difficulty_button = Button(
            self.width - 170,
            self.height - 80,
            150,
            50,
            self._get_difficulty_text(),
            font_size=28,
            color=difficulty_colors.get(self.game_manager.difficulty, (70, 130, 180)),
            hover_color=difficulty_hover_colors.get(self.game_manager.difficulty, (30, 144, 255))
        )
        
        # 環境のロック状態（全て解放）
        self.environment_locked = {
            "jungle": False,
            "ocean": False,
            "desert": False,
            "forest": False
        }
    
    def handle_event(self, event):
        """
        イベントを処理する
        
        Args:
            event: pygameのイベント
        """
        # ジャングルボタンのイベント処理
        if not self.environment_locked["jungle"] and self.jungle_button.handle_event(event):
            self.game_manager.select_environment("jungle")
            self.next_screen = GameScreen(self.screen, self.game_manager)
        
        # 海ボタンのイベント処理
        elif not self.environment_locked["ocean"] and self.ocean_button.handle_event(event):
            self.game_manager.select_environment("ocean")
            self.next_screen = GameScreen(self.screen, self.game_manager)
        
        # 砂漠ボタンのイベント処理
        elif not self.environment_locked["desert"] and self.desert_button.handle_event(event):
            self.game_manager.select_environment("desert")
            self.next_screen = GameScreen(self.screen, self.game_manager)
        
        # 森ボタンのイベント処理
        elif not self.environment_locked["forest"] and self.forest_button.handle_event(event):
            self.game_manager.select_environment("forest")
            self.next_screen = GameScreen(self.screen, self.game_manager)
        
        # 難易度ボタンのイベント処理
        elif self.difficulty_button.handle_event(event):
            from ui.difficulty_select import DifficultySelectScreen
            self.next_screen = DifficultySelectScreen(self.screen, self.game_manager, self)
        
        # 戻るボタンのイベント処理
        elif self.back_button.handle_event(event):
            from ui.menu import MainMenu
            self.next_screen = MainMenu(self.screen, self.game_manager)
    
    def update(self):
        """画面の状態を更新する"""
        # ボタンの更新
        self.jungle_button.update()
        self.ocean_button.update()
        self.desert_button.update()
        self.forest_button.update()
        self.back_button.update()
        self.difficulty_button.update()
        
        # 難易度ボタンのテキストと色を更新
        self.difficulty_button.text = self._get_difficulty_text()
        
        # 難易度に応じた色に更新
        difficulty_colors = {
            "easy": (46, 139, 87),    # 緑色
            "normal": (70, 130, 180), # 青色
            "hard": (178, 34, 34)     # 赤色
        }
        difficulty_hover_colors = {
            "easy": (60, 179, 113),   # 緑色（ホバー時）
            "normal": (30, 144, 255), # 青色（ホバー時）
            "hard": (220, 20, 60)     # 赤色（ホバー時）
        }
        
        self.difficulty_button.color = difficulty_colors.get(self.game_manager.difficulty, (70, 130, 180))
        self.difficulty_button.hover_color = difficulty_hover_colors.get(self.game_manager.difficulty, (30, 144, 255))
    
    def draw(self):
        """画面を描画する"""
        # 背景を描画
        if self.background_image:
            self.screen.blit(self.background_image, (0, 0))
        else:
            # 背景画像がない場合は色で塗りつぶす
            self.screen.fill((240, 248, 255))
        
        # タイトルを描画
        title_text = "どこであそぶ？"
        title_surface = self.title_font.render(title_text, True, (0, 0, 0))
        title_rect = title_surface.get_rect(center=(self.width // 2, 70))
        self.screen.blit(title_surface, title_rect)
        
        # ボタンを描画
        self.jungle_button.draw(self.screen)
        self.ocean_button.draw(self.screen)
        self.desert_button.draw(self.screen)
        self.forest_button.draw(self.screen)
        self.back_button.draw(self.screen)
        
        # 環境のサムネイル画像を描画
        if self.environment_thumbnails["jungle"]:
            self.screen.blit(self.environment_thumbnails["jungle"], self.jungle_button.rect)
        
        if self.environment_thumbnails["ocean"]:
            self.screen.blit(self.environment_thumbnails["ocean"], self.ocean_button.rect)
        
        if self.environment_thumbnails["desert"]:
            self.screen.blit(self.environment_thumbnails["desert"], self.desert_button.rect)
        
        if self.environment_thumbnails["forest"]:
            self.screen.blit(self.environment_thumbnails["forest"], self.forest_button.rect)
        
        # ボタンのテキストを再描画（サムネイルの上に）
        self._draw_button_text(self.jungle_button, "ジャングル")
        self._draw_button_text(self.ocean_button, "うみ")
        self._draw_button_text(self.desert_button, "さばく")
        self._draw_button_text(self.forest_button, "もり")
        
        # ロックされた環境の表示
        if self.environment_locked["desert"]:
            self._draw_lock(self.desert_button.rect)
        
        if self.environment_locked["forest"]:
            self._draw_lock(self.forest_button.rect)
        
        # 戻るボタンを描画
        self.back_button.draw(self.screen)
        
        # 難易度ボタンを描画
        self.difficulty_button.draw(self.screen)
    
    def _draw_button_text(self, button, text):
        """
        ボタンのテキストを描画する
        
        Args:
            button: ボタンオブジェクト
            text: 表示するテキスト
        """
        font = FontManager.get_instance().get_font(36)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=button.rect.center)
        
        # テキストの背景を半透明にして読みやすくする
        bg_rect = text_rect.inflate(20, 10)
        bg_surface = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
        bg_surface.fill((0, 0, 0, 128))
        self.screen.blit(bg_surface, bg_rect)
        
        # テキストを描画
        self.screen.blit(text_surface, text_rect)
    
    def _draw_lock(self, rect):
        """
        ロックアイコンを描画する
        
        Args:
            rect: ボタンの矩形
        """
        # 半透明の黒いオーバーレイ
        overlay = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self.screen.blit(overlay, rect)
        
        # ロックアイコンを描画
        if self.lock_icon:
            lock_x = rect.centerx - self.lock_icon.get_width() // 2
            lock_y = rect.centery - self.lock_icon.get_height() // 2
            self.screen.blit(self.lock_icon, (lock_x, lock_y))
        else:
            # ロックアイコンがない場合は簡易的に描画
            lock_color = (255, 255, 255)
            lock_width = 40
            lock_height = 50
            lock_x = rect.centerx - lock_width // 2
            lock_y = rect.centery - lock_height // 2
            
            # 南京錠の下部（四角形）
            pygame.draw.rect(
                self.screen, 
                lock_color, 
                (lock_x, lock_y + 15, lock_width, lock_height - 15),
                border_radius=5
            )
            
            # 南京錠の上部（弧）
            pygame.draw.arc(
                self.screen,
                lock_color,
                (lock_x + 5, lock_y - 10, lock_width - 10, 30),
                3.14, 0, 3
            )
    
    def get_next_screen(self):
        """
        次の画面を取得する
        
        Returns:
            次の画面、または None
        """
        next_screen = self.next_screen
        self.next_screen = None
        return next_screen
    def _get_difficulty_text(self):
        """
        現在の難易度に応じたテキストを取得する
        
        Returns:
            str: 難易度テキスト
        """
        difficulty_texts = {
            "easy": "かんたん",
            "normal": "ふつう",
            "hard": "むずかしい"
        }
        return difficulty_texts.get(self.game_manager.difficulty, "かんたん")