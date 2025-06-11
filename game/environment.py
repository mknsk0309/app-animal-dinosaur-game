#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
環境（ステージ）クラス
"""

from utils.config_loader import ConfigLoader

class Environment:
    """環境（ステージ）を表すクラス"""
    
    # 環境の種類
    TYPE_JUNGLE = "jungle"
    TYPE_OCEAN = "ocean"
    TYPE_DESERT = "desert"
    TYPE_FOREST = "forest"
    
    @classmethod
    def get_animals(cls, environment_type, difficulty="easy"):
        """
        環境と難易度に対応する動物のリストを取得する
        
        Args:
            environment_type (str): 環境の種類
            difficulty (str): 難易度 ("easy", "normal", "hard")
            
        Returns:
            list: 動物のリスト
        """
        from game.character import Character
        return Character.get_animals_by_environment(environment_type, difficulty)
    
    @classmethod
    def get_dinosaurs(cls, environment_type, difficulty="easy"):
        """
        環境と難易度に対応する恐竜のリストを取得する
        
        Args:
            environment_type (str): 環境の種類
            difficulty (str): 難易度 ("easy", "normal", "hard")
            
        Returns:
            list: 恐竜のリスト
        """
        from game.character import Character
        return Character.get_dinosaurs_by_environment(environment_type, difficulty)
    
    @classmethod
    def get_characters(cls, environment_type, difficulty="easy"):
        """
        環境と難易度に対応するキャラクター（動物+恐竜）のリストを取得する
        
        Args:
            environment_type (str): 環境の種類
            difficulty (str): 難易度 ("easy", "normal", "hard")
            
        Returns:
            list: キャラクターのリスト
        """
        from game.character import Character
        return Character.get_characters_by_environment(environment_type, difficulty)
    
    @classmethod
    def get_card_backs(cls, environment_type):
        """
        環境に対応するカード裏面のリストを取得する
        
        Args:
            environment_type (str): 環境の種類
            
        Returns:
            list: カード裏面のリスト
        """
        config_loader = ConfigLoader.get_instance()
        environments = config_loader.get_environments()
        
        if environment_type in environments:
            return environments[environment_type].get("card_backs", ["flower"])
        return ["flower"]
    
    @classmethod
    def get_name(cls, environment_type):
        """
        環境の日本語名を取得する
        
        Args:
            environment_type (str): 環境の種類
            
        Returns:
            str: 環境の日本語名
        """
        config_loader = ConfigLoader.get_instance()
        environments = config_loader.get_environments()
        
        if environment_type in environments:
            return environments[environment_type].get("name", "不明")
        return "不明"
    
    @classmethod
    def get_background_color(cls, environment_type):
        """
        環境の背景色を取得する
        
        Args:
            environment_type (str): 環境の種類
            
        Returns:
            tuple: 背景色 (R, G, B)
        """
        config_loader = ConfigLoader.get_instance()
        environments = config_loader.get_environments()
        
        if environment_type in environments:
            return tuple(environments[environment_type].get("background_color", (240, 248, 255)))
        return (240, 248, 255)  # デフォルトは薄い水色