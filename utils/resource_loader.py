#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
リソース読み込みモジュール
"""

import os
import pygame

class ResourceLoader:
    """リソースを読み込むクラス"""
    
    # シングルトンインスタンス
    _instance = None
    
    @classmethod
    def get_instance(cls):
        """
        シングルトンインスタンスを取得する
        
        Returns:
            ResourceLoader: シングルトンインスタンス
        """
        if cls._instance is None:
            cls._instance = ResourceLoader()
        return cls._instance
    
    def __init__(self):
        """リソースローダーを初期化する"""
        # 画像のキャッシュ
        self.images = {}
        
        # 画像のパス
        self.image_path = os.path.join("assets", "images")
        
        # 画像ディレクトリが存在するか確認
        if not os.path.exists(self.image_path):
            print(f"警告: 画像ディレクトリが見つかりません: {self.image_path}")
            os.makedirs(self.image_path, exist_ok=True)
    
    def load_image(self, path, scale=None, keep_aspect_ratio=True):
        """
        画像を読み込む
        
        Args:
            path (str): 画像ファイルのパス（assets/images/からの相対パス）
            scale (tuple, optional): 画像のスケール (width, height)
            keep_aspect_ratio (bool): アスペクト比を維持するかどうか
            
        Returns:
            pygame.Surface: 読み込んだ画像
        """
        # キャッシュキー
        cache_key = f"{path}_{scale}_{keep_aspect_ratio}"
        
        # キャッシュにあればそれを返す
        if cache_key in self.images:
            return self.images[cache_key]
        
        # 画像の完全パス
        full_path = os.path.join(self.image_path, path)
        
        # 画像を読み込む
        try:
            image = pygame.image.load(full_path).convert_alpha()
            
            # スケールが指定されていれば変更
            if scale:
                if keep_aspect_ratio:
                    # アスペクト比を維持してリサイズ
                    original_width, original_height = image.get_size()
                    target_width, target_height = scale
                    
                    # 縦横比を計算
                    width_ratio = target_width / original_width
                    height_ratio = target_height / original_height
                    
                    # 小さい方の比率を使用してアスペクト比を維持
                    ratio = min(width_ratio, height_ratio)
                    
                    new_width = int(original_width * ratio)
                    new_height = int(original_height * ratio)
                    
                    # リサイズした画像を作成
                    resized_image = pygame.transform.scale(image, (new_width, new_height))
                    
                    # 指定サイズの透明な画像を作成
                    final_image = pygame.Surface(scale, pygame.SRCALPHA)
                    
                    # 中央に配置
                    x_offset = (target_width - new_width) // 2
                    y_offset = (target_height - new_height) // 2
                    
                    final_image.blit(resized_image, (x_offset, y_offset))
                    image = final_image
                else:
                    # アスペクト比を無視してリサイズ
                    image = pygame.transform.scale(image, scale)
            
            # キャッシュに保存
            self.images[cache_key] = image
            
            return image
        except pygame.error as e:
            print(f"画像の読み込みに失敗しました: {full_path}")
            print(f"エラー: {e}")
            
            # 代わりにプレースホルダー画像を返す
            placeholder = self._create_placeholder_image(scale)
            return placeholder
    
    def _create_placeholder_image(self, scale=(100, 100)):
        """
        プレースホルダー画像を作成する
        
        Args:
            scale (tuple): 画像のサイズ (width, height)
            
        Returns:
            pygame.Surface: プレースホルダー画像
        """
        # デフォルトサイズ
        width, height = scale if scale else (100, 100)
        
        # 透明な画像を作成
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        
        # 背景色（半透明グレー）
        image.fill((200, 200, 200, 128))
        
        # 枠線
        pygame.draw.rect(image, (100, 100, 100), (0, 0, width, height), 2)
        
        # 斜線
        pygame.draw.line(image, (100, 100, 100), (0, 0), (width, height), 2)
        pygame.draw.line(image, (100, 100, 100), (0, height), (width, 0), 2)
        
        return image
    
    def load_character_image(self, character_type, environment, scale=None):
        """
        キャラクター画像を読み込む
        
        Args:
            character_type (str): キャラクターの種類（"lion", "monkey"など）
            environment (str): 環境（"jungle", "ocean"など）
            scale (tuple, optional): 画像のスケール (width, height)
            
        Returns:
            pygame.Surface: キャラクター画像
        """
        # Characterクラスを使用して動物か恐竜かを判定
        from game.character import Character
        character_info = Character.get_character_info(character_type)
        
        if character_info and character_info.get("type") == Character.TYPE_ANIMAL:
            path = os.path.join("characters", "animals", f"{character_type}.png")
        else:
            path = os.path.join("characters", "dinosaurs", f"{character_type}.png")
        
        # キャラクター画像はアスペクト比を維持して読み込む
        return self.load_image(path, scale, keep_aspect_ratio=True)
    
    def load_card_image(self, card_type, flipped=False, scale=None, environment=None):
        """
        カード画像を読み込む
        
        Args:
            card_type (str): カードの種類（"lion", "monkey"など）
            flipped (bool): 裏返しかどうか
            scale (tuple, optional): 画像のスケール (width, height)
            environment (str, optional): 環境（"jungle", "ocean"など）
            
        Returns:
            pygame.Surface: カード画像
        """
        if flipped:
            # 裏面の画像（環境に応じてランダムに選択）
            import random
            from game.environment import Environment
            
            if environment:
                # 環境に応じたカード裏面を選択
                card_backs = Environment.get_card_backs(environment)
            else:
                # 環境が指定されていない場合はすべてのカード裏面から選択
                card_backs = ["bubble", "cactus", "coral", "flower", "grass", 
                             "mushroom", "rock", "sand", "seaweed", "tree1", "tree2"]
            
            back_type = random.choice(card_backs)
            path = os.path.join("card_backs", f"{back_type}.png")
        else:
            # 表面の画像 - Characterクラスを使用して動物か恐竜かを判定
            from game.character import Character
            character_info = Character.get_character_info(card_type)
            
            if character_info and character_info.get("type") == Character.TYPE_ANIMAL:
                path = os.path.join("characters", "animals", f"{card_type}.png")
            else:
                path = os.path.join("characters", "dinosaurs", f"{card_type}.png")
        
        # カード画像はアスペクト比を維持して読み込む
        return self.load_image(path, scale, keep_aspect_ratio=True)
    
    def load_background_image(self, environment, scale=None):
        """
        背景画像を読み込む
        
        Args:
            environment (str): 環境（"jungle", "ocean"など）
            scale (tuple, optional): 画像のスケール (width, height)
            
        Returns:
            pygame.Surface: 背景画像
        """
        path = os.path.join("backgrounds", f"{environment}.png")
        # 背景画像はアスペクト比を維持せずに画面サイズに合わせる
        return self.load_image(path, scale, keep_aspect_ratio=False)