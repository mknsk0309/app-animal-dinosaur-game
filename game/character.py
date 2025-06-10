#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
キャラクター（動物・恐竜）クラス
"""

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
    
    # キャラクター情報の定義
    # id: キャラクターの識別子
    # name: 日本語名
    # type: 種類（動物/恐竜）
    # difficulty: 難易度（1: やさしい、2: ふつう、3: むずかしい）
    # environments: 生息環境のリスト
    CHARACTERS = {
        # 動物（難易度1: やさしい）
        "lion": {"name": "ライオン", "type": TYPE_ANIMAL, "difficulty": 1, "environments": [ENV_JUNGLE]},
        "monkey": {"name": "サル", "type": TYPE_ANIMAL, "difficulty": 1, "environments": [ENV_JUNGLE]},
        "zebra": {"name": "シマウマ", "type": TYPE_ANIMAL, "difficulty": 1, "environments": [ENV_JUNGLE]},
        "dolphin": {"name": "イルカ", "type": TYPE_ANIMAL, "difficulty": 1, "environments": [ENV_OCEAN]},
        "whale": {"name": "クジラ", "type": TYPE_ANIMAL, "difficulty": 1, "environments": [ENV_OCEAN]},
        "seal": {"name": "アザラシ", "type": TYPE_ANIMAL, "difficulty": 1, "environments": [ENV_OCEAN]},
        "camel": {"name": "ラクダ", "type": TYPE_ANIMAL, "difficulty": 1, "environments": [ENV_DESERT]},
        "lizard": {"name": "トカゲ", "type": TYPE_ANIMAL, "difficulty": 1, "environments": [ENV_DESERT]},
        "scorpion": {"name": "サソリ", "type": TYPE_ANIMAL, "difficulty": 1, "environments": [ENV_DESERT]},
        "rabbit": {"name": "ウサギ", "type": TYPE_ANIMAL, "difficulty": 1, "environments": [ENV_FOREST]},
        "squirrel": {"name": "リス", "type": TYPE_ANIMAL, "difficulty": 1, "environments": [ENV_FOREST]},
        "dear": {"name": "シカ", "type": TYPE_ANIMAL, "difficulty": 1, "environments": [ENV_FOREST]},
        # 動物（難易度2: ふつう）
        "tiger": {"name": "トラ", "type": TYPE_ANIMAL, "difficulty": 2, "environments": [ENV_JUNGLE]},
        "gorilla": {"name": "ゴリラ", "type": TYPE_ANIMAL, "difficulty": 2, "environments": [ENV_JUNGLE]},
        "owl": {"name": "フクロウ", "type": TYPE_ANIMAL, "difficulty": 2, "environments": [ENV_JUNGLE]},
        "turtle": {"name": "カメ", "type": TYPE_ANIMAL, "difficulty": 2, "environments": [ENV_OCEAN]},
        "octopus": {"name": "タコ", "type": TYPE_ANIMAL, "difficulty": 2, "environments": [ENV_OCEAN]},
        "shark": {"name": "サメ", "type": TYPE_ANIMAL, "difficulty": 2, "environments": [ENV_OCEAN]},
        "elephant": {"name": "ゾウ", "type": TYPE_ANIMAL, "difficulty": 2, "environments": [ENV_DESERT]},
        "rhinoceros": {"name": "サイ", "type": TYPE_ANIMAL, "difficulty": 2, "environments": [ENV_DESERT]},
        "kangaroo": {"name": "カンガルー", "type": TYPE_ANIMAL, "difficulty": 2, "environments": [ENV_DESERT]},
        "fox": {"name": "キツネ", "type": TYPE_ANIMAL, "difficulty": 2, "environments": [ENV_FOREST]},
        "panda": {"name": "パンダ", "type": TYPE_ANIMAL, "difficulty": 2, "environments": [ENV_FOREST]},
        "giraffe": {"name": "キリン", "type": TYPE_ANIMAL, "difficulty": 2, "environments": [ENV_FOREST]},
        
        # 恐竜（難易度2: ふつう）
        "velociraptor": {"name": "ヴェロキラプトル", "type": TYPE_DINOSAUR, "difficulty": 2, "environments": [ENV_JUNGLE]},
        "pachycephalosaurus": {"name": "パキケファロサウルス", "type": TYPE_DINOSAUR, "difficulty": 2, "environments": [ENV_JUNGLE]},
        "plesiosaurus": {"name": "プレシオサウルス", "type": TYPE_DINOSAUR, "difficulty": 2, "environments": [ENV_OCEAN]},
        "mammoth": {"name": "マンモス", "type": TYPE_DINOSAUR, "difficulty": 2, "environments": [ENV_DESERT]},
        "parasaurolophus": {"name": "パラサウロロフス", "type": TYPE_DINOSAUR, "difficulty": 2, "environments": [ENV_DESERT]},
        "deinonychus": {"name": "デイノニクス", "type": TYPE_DINOSAUR, "difficulty": 2, "environments": [ENV_FOREST]},
        "ankylosaurus": {"name": "アンキロサウルス", "type": TYPE_DINOSAUR, "difficulty": 2, "environments": [ENV_FOREST]},
        
        # 恐竜（難易度3: むずかしい）
        "tyrannosaurus": {"name": "ティラノサウルス", "type": TYPE_DINOSAUR, "difficulty": 3, "environments": [ENV_JUNGLE]},
        "brachiosaurus": {"name": "ブラキオサウルス", "type": TYPE_DINOSAUR, "difficulty": 3, "environments": [ENV_JUNGLE]},
        "mosasaurus": {"name": "モササウルス", "type": TYPE_DINOSAUR, "difficulty": 3, "environments": [ENV_OCEAN]},
        "spinosaurus": {"name": "スピノサウルス", "type": TYPE_DINOSAUR, "difficulty": 3, "environments": [ENV_OCEAN]},
        "quetzalcoatlus": {"name": "ケツァツコアトルス", "type": TYPE_DINOSAUR, "difficulty": 3, "environments": [ENV_DESERT]},
        "pteranodon": {"name": "プテラノドン", "type": TYPE_DINOSAUR, "difficulty": 3, "environments": [ENV_DESERT]},
        "stegosaurus": {"name": "ステゴサウルス", "type": TYPE_DINOSAUR, "difficulty": 3, "environments": [ENV_FOREST]},
        "triceratops": {"name": "トリケラトプス", "type": TYPE_DINOSAUR, "difficulty": 3, "environments": [ENV_FOREST]},
    }
    
    @classmethod
    def get_character_info(cls, character_id):
        """
        キャラクター情報を取得する
        
        Args:
            character_id (str): キャラクターID
            
        Returns:
            dict: キャラクター情報
        """
        return cls.CHARACTERS.get(character_id, {})
    
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
        characters = []
        
        # 難易度に応じた数値に変換
        difficulty_level = 1  # デフォルトは「やさしい」
        if difficulty == "normal":
            difficulty_level = 2
        elif difficulty == "hard":
            difficulty_level = 3
        
        # 全キャラクターから条件に合うものを抽出
        for character_id, info in cls.CHARACTERS.items():
            # 環境が一致するか確認
            if environment_type in info.get("environments", []):
                # 難易度チェック
                char_difficulty = info.get("difficulty", 1)
                
                # 難易度条件に合致するか確認
                if (difficulty_level == 1 and char_difficulty == 1) or \
                   (difficulty_level == 2 and char_difficulty <= 2) or \
                   (difficulty_level == 3):
                    characters.append(character_id)
        
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
        characters = cls.get_characters_by_environment(environment_type, difficulty)
        return [c for c in characters if cls.get_character_info(c).get("type") == cls.TYPE_ANIMAL]
    
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
        characters = cls.get_characters_by_environment(environment_type, difficulty)
        return [c for c in characters if cls.get_character_info(c).get("type") == cls.TYPE_DINOSAUR]