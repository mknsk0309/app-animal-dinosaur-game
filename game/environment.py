#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
環境（ステージ）クラス
"""

class Environment:
    """環境（ステージ）を表すクラス"""
    
    # 環境の種類
    TYPE_JUNGLE = "jungle"
    TYPE_OCEAN = "ocean"
    TYPE_DESERT = "desert"
    TYPE_FOREST = "forest"
    
    # キャラクター情報はCharacterクラスに移動しました
    
    # 環境ごとのカード裏面
    CARD_BACKS = {
        TYPE_JUNGLE: ["tree1", "tree2", "flower"],
        TYPE_OCEAN: ["bubble", "coral", "seaweed"],
        TYPE_DESERT: ["cactus", "rock", "sand"],
        TYPE_FOREST: ["mushroom", "grass", "flower"]
    }
    
    # 環境の日本語名
    NAMES = {
        TYPE_JUNGLE: "ジャングル",
        TYPE_OCEAN: "うみ",
        TYPE_DESERT: "さばく",
        TYPE_FOREST: "もり"
    }
    
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
        return cls.CARD_BACKS.get(environment_type, ["flower"])
    
    @classmethod
    def get_name(cls, environment_type):
        """
        環境の日本語名を取得する
        
        Args:
            environment_type (str): 環境の種類
            
        Returns:
            str: 環境の日本語名
        """
        return cls.NAMES.get(environment_type, "不明")