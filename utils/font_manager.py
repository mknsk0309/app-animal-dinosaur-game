#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
フォント管理モジュール
"""

import os
import pygame

class FontManager:
    """フォントを管理するクラス"""
    
    # シングルトンインスタンス
    _instance = None
    
    @classmethod
    def get_instance(cls):
        """
        シングルトンインスタンスを取得する
        
        Returns:
            FontManager: シングルトンインスタンス
        """
        if cls._instance is None:
            cls._instance = FontManager()
        return cls._instance
    
    def __init__(self):
        """フォントマネージャーを初期化する"""
        # フォントのキャッシュ
        self.fonts = {}
        
        # フォントファイルのパス
        self.font_path = os.path.join("assets", "fonts", "MPLUSRounded1c-Medium.ttf")
        
        # フォントが存在するか確認
        if not os.path.exists(self.font_path):
            print(f"警告: フォントファイルが見つかりません: {self.font_path}")
            print("システムのデフォルトフォントを使用します。")
    
    def get_font(self, size):
        """
        指定したサイズのフォントを取得する
        
        Args:
            size (int): フォントサイズ
            
        Returns:
            pygame.font.Font: フォントオブジェクト
        """
        # キャッシュにあればそれを返す
        if size in self.fonts:
            return self.fonts[size]
        
        # フォントを作成
        try:
            font = pygame.font.Font(self.font_path, size)
        except:
            # フォントの読み込みに失敗した場合はデフォルトフォントを使用
            print(f"フォントの読み込みに失敗しました: {self.font_path}")
            print(f"システムのデフォルトフォントを使用します。サイズ: {size}")
            font = pygame.font.SysFont(None, size)
        
        # キャッシュに保存
        self.fonts[size] = font
        
        return font
