#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
キャラクター（動物・恐竜）クラス
"""

from utils.config_loader import ConfigLoader

class Character:
    """キャラクター（動物・恐竜）を表すクラス"""
    
    # キャラクターの種類
    TYPE_ANIMAL = "animal"
    TYPE_DINOSAUR = "dinosaur"
    
    # 環境の種類（Environmentクラスと同期）
    ENV_JUNGLE = "jungle"
    ENV_OCEAN = "ocean"
    ENV_DESERT = "desert"
    ENV_FOREST = "forest"
    
    @classmethod
    def get_character_info(cls, character_id):
        """
        キャラクター情報を取得する
        
        Args:
            character_id (str): キャラクターID
            
        Returns:
            dict: キャラクター情報
        """
        config_loader = ConfigLoader.get_instance()
        characters = config_loader.get_characters()
        
        # 動物から検索
        for animal in characters.get("animals", []):
            if animal["id"] == character_id:
                animal_info = animal.copy()
                animal_info["type"] = cls.TYPE_ANIMAL
                return animal_info
        
        # 恐竜から検索
        for dinosaur in characters.get("dinosaurs", []):
            if dinosaur["id"] == character_id:
                dino_info = dinosaur.copy()
                dino_info["type"] = cls.TYPE_DINOSAUR
                return dino_info
        
        return {}
    
    @classmethod
    def get_name(cls, character_id):
        """
        キャラクターの日本語名を取得する
        
        Args:
            character_id (str): キャラクターID
            
        Returns:
            str: キャラクターの日本語名
        """
        character = cls.get_character_info(character_id)
        return character.get("name", character_id)
    
    @classmethod
    def get_characters_by_environment(cls, environment_type, difficulty="easy"):
        """
        環境と難易度に対応するキャラクターのリストを取得する
        
        Args:
            environment_type (str): 環境の種類
            difficulty (str): 難易度 ("easy", "normal", "hard")
            
        Returns:
            list: キャラクターIDのリスト
        """
        animals = cls.get_animals_by_environment(environment_type, difficulty)
        dinosaurs = cls.get_dinosaurs_by_environment(environment_type, difficulty)
        
        characters = animals + dinosaurs
        
        # キャラクターが足りない場合は、他の環境から追加
        if len(characters) < 3:  # 最低3種類は必要
            # 他の環境から動物を追加
            for env_type in [cls.ENV_JUNGLE, cls.ENV_OCEAN, cls.ENV_DESERT, cls.ENV_FOREST]:
                if env_type != environment_type:
                    extra_animals = cls.get_animals_by_environment(env_type, "easy")
                    if extra_animals:
                        characters.extend(extra_animals[:2])  # 最大2種類追加
                    if len(characters) >= 3:
                        break
        
        # それでも足りない場合は、既存のキャラクターを複製
        while len(characters) < 3:
            if len(characters) > 0:
                characters.append(characters[0])  # 最初のキャラクターを再利用
        
        return characters
    
    @classmethod
    def get_animals_by_environment(cls, environment_type, difficulty="easy"):
        """
        環境と難易度に対応する動物のリストを取得する
        
        Args:
            environment_type (str): 環境の種類
            difficulty (str): 難易度 ("easy", "normal", "hard")
            
        Returns:
            list: 動物IDのリスト
        """
        config_loader = ConfigLoader.get_instance()
        characters = config_loader.get_characters()
        
        # 難易度に応じた数値に変換
        difficulty_level = 1  # デフォルトは「やさしい」
        if difficulty == "normal":
            difficulty_level = 2
        elif difficulty == "hard":
            difficulty_level = 3
        
        animals = []
        
        # 動物を環境と難易度でフィルタリング
        for animal in characters.get("animals", []):
            # 環境が一致するか確認
            if environment_type in animal.get("environments", []):
                # 難易度チェック
                animal_difficulty = animal.get("difficulty", 1)
                
                # 難易度条件に合致するか確認
                if (difficulty_level == 1 and animal_difficulty == 1) or \
                   (difficulty_level == 2 and animal_difficulty <= 2) or \
                   (difficulty_level == 3):
                    animals.append(animal["id"])
        
        return animals
    
    @classmethod
    def get_dinosaurs_by_environment(cls, environment_type, difficulty="easy"):
        """
        環境と難易度に対応する恐竜のリストを取得する
        
        Args:
            environment_type (str): 環境の種類
            difficulty (str): 難易度 ("easy", "normal", "hard")
            
        Returns:
            list: 恐竜IDのリスト
        """
        config_loader = ConfigLoader.get_instance()
        characters = config_loader.get_characters()
        
        # 難易度に応じた数値に変換
        difficulty_level = 1  # デフォルトは「やさしい」
        if difficulty == "normal":
            difficulty_level = 2
        elif difficulty == "hard":
            difficulty_level = 3
        
        dinosaurs = []
        
        # 恐竜を環境と難易度でフィルタリング
        for dinosaur in characters.get("dinosaurs", []):
            # 環境が一致するか確認
            if environment_type in dinosaur.get("environments", []):
                # 難易度チェック
                dino_difficulty = dinosaur.get("difficulty", 2)  # 恐竜はデフォルトで難易度2
                
                # 難易度条件に合致するか確認
                if (difficulty_level >= 2 and dino_difficulty == 2) or \
                   (difficulty_level == 3 and dino_difficulty == 3):
                    dinosaurs.append(dinosaur["id"])
        
        return dinosaurs