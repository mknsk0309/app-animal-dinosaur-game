#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ボタンコンポーネント
"""

import pygame
from utils.font_manager import FontManager

class Button:
    """ボタンクラス"""
    
    def __init__(self, x, y, width, height, text, font_size=32, 
                 color=(70, 130, 180), hover_color=(30, 144, 255), 
                 text_color=(255, 255, 255), border_radius=10):
        """
        ボタンを初期化する
        
        Args:
            x (int): X座標
            y (int): Y座標
            width (int): 幅
            height (int): 高さ
            text (str): ボタンのテキスト
            font_size (int): フォントサイズ
            color (tuple): ボタンの色 (R, G, B)
            hover_color (tuple): ホバー時の色 (R, G, B)
            text_color (tuple): テキストの色 (R, G, B)
            border_radius (int): 角の丸みの半径
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font_size = font_size
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.border_radius = border_radius
        self.is_hovered = False
        self.is_clicked = False
        
        # フォントの初期化
        self.font = FontManager.get_instance().get_font(font_size)
        
        # クリック効果音
        self.click_sound = None
        
        # アニメーション用の変数
        self.scale = 1.0
        self.target_scale = 1.0
        self.animation_speed = 0.2
    
    def set_click_sound(self, sound_file):
        """
        クリック効果音を設定する
        
        Args:
            sound_file (str): 効果音ファイルのパス
        """
        self.click_sound = pygame.mixer.Sound(sound_file)
    
    def update(self):
        """ボタンの状態を更新する"""
        # マウスの位置を取得
        mouse_pos = pygame.mouse.get_pos()
        
        # ホバー状態を更新
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        
        # タッチイベントの処理（ホバー状態の更新）
        for event in pygame.event.get([pygame.FINGERMOTION, pygame.FINGERDOWN]):
            if event.type in (pygame.FINGERMOTION, pygame.FINGERDOWN):
                # タッチ位置をスクリーン座標に変換
                display_size = pygame.display.get_surface().get_size()
                touch_x = event.x * display_size[0]
                touch_y = event.y * display_size[1]
                
                # ボタンの領域内かチェック
                if self.rect.collidepoint(touch_x, touch_y):
                    self.is_hovered = True
        
        # アニメーション更新
        if self.is_hovered:
            self.target_scale = 1.03  # 1.05から1.03に縮小
        else:
            self.target_scale = 1.0
        
        # スケールを目標値に近づける
        self.scale += (self.target_scale - self.scale) * self.animation_speed
    
    def handle_event(self, event):
        """
        イベントを処理する
        
        Args:
            event: pygameのイベント
            
        Returns:
            bool: クリックされたかどうか
        """
        # タッチイベントの処理を追加
        if event.type == pygame.FINGERDOWN:
            # タッチ位置をスクリーン座標に変換
            display_size = pygame.display.get_surface().get_size()
            touch_x = event.x * display_size[0]
            touch_y = event.y * display_size[1]
            
            # ボタンの領域内かチェック
            if self.rect.collidepoint(touch_x, touch_y):
                self.is_clicked = True
                if self.click_sound:
                    self.click_sound.play()
                return True
        
        # 通常のマウスクリック処理
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.is_hovered:  # 左クリック
                self.is_clicked = True
                if self.click_sound:
                    self.click_sound.play()
                return True
        
        return False
    
    def draw(self, screen):
        """
        ボタンを描画する
        
        Args:
            screen: 描画対象の画面
        """
        # ボタンの拡大縮小を適用
        scaled_rect = pygame.Rect(
            self.rect.x - (self.rect.width * (self.scale - 1)) / 2,
            self.rect.y - (self.rect.height * (self.scale - 1)) / 2,
            self.rect.width * self.scale,
            self.rect.height * self.scale
        )
        
        # ボタンの背景を描画
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, scaled_rect, border_radius=self.border_radius)
        
        # テキストを描画
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=scaled_rect.center)
        screen.blit(text_surface, text_rect)
