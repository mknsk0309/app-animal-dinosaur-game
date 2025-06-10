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
    
    # 環境ごとの動物
    ANIMALS = {
        TYPE_JUNGLE: ["lion", "monkey", "elephant", "tiger"],
        TYPE_OCEAN: ["dolphin", "whale", "turtle"],
        TYPE_DESERT: ["camel", "scorpion", "lizard"],
        TYPE_FOREST: ["fox", "rabbit", "squirrel", "panda"]
    }
    
    # 全ての動物（環境に関係なく使用可能）
    ALL_ANIMALS = ["lion", "monkey", "elephant", "giraffe", "tiger", "panda", 
                  "dolphin", "whale", "turtle", "camel", "scorpion", "lizard", 
                  "fox", "rabbit", "squirrel"]
    
    # 環境ごとの恐竜
    DINOSAURS = {
        TYPE_JUNGLE: ["tyrannosaurus", "velociraptor"],
        TYPE_OCEAN: ["plesiosaurus", "mosasaurus"],
        TYPE_DESERT: ["pteranodon", "spinosaurus"],
        TYPE_FOREST: ["triceratops", "stegosaurus"]
    }
    
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
    def get_animals(cls, environment_type):
        """
        環境に対応する動物のリストを取得する
        
        Args:
            environment_type (str): 環境の種類
            
        Returns:
            list: 動物のリスト
        """
        return cls.ANIMALS.get(environment_type, [])
    
    @classmethod
    def get_dinosaurs(cls, environment_type):
        """
        環境に対応する恐竜のリストを取得する
        
        Args:
            environment_type (str): 環境の種類
            
        Returns:
            list: 恐竜のリスト
        """
        return cls.DINOSAURS.get(environment_type, [])
    
    @classmethod
    def get_characters(cls, environment_type):
        """
        環境に対応するキャラクター（動物+恐竜）のリストを取得する
        
        Args:
            environment_type (str): 環境の種類
            
        Returns:
            list: キャラクターのリスト
        """
        animals = cls.get_animals(environment_type)
        dinosaurs = cls.get_dinosaurs(environment_type)
        
        # 環境に対応するキャラクターを返す
        # 注意: 各環境には最低6種類のキャラクターが必要
        characters = animals + dinosaurs
        
        # キャラクターが足りない場合は、同じ環境のキャラクターを複製
        if len(characters) < 6:
            # 既存のキャラクターを複製して6種類になるまで追加
            while len(characters) < 6:
                if len(characters) > 0:
                    characters.append(characters[0])  # 最初のキャラクターを再利用
        
        return characters
    
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