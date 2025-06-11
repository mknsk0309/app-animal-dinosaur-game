#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
設定ファイル読み込みモジュール
"""

import os
import json

class ConfigLoader:
    """設定ファイルを読み込むクラス"""
    
    # シングルトンインスタンス
    _instance = None
    
    @classmethod
    def get_instance(cls):
        """
        シングルトンインスタンスを取得する
        
        Returns:
            ConfigLoader: シングルトンインスタンス
        """
        if cls._instance is None:
            cls._instance = ConfigLoader()
        return cls._instance
    
    def __init__(self):
        """設定ローダーを初期化する"""
        # 設定のキャッシュ
        self.configs = {}
        
        # データディレクトリのパス
        self.data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
        
        # データディレクトリが存在するか確認
        if not os.path.exists(self.data_path):
            print(f"警告: データディレクトリが見つかりません: {self.data_path}")
            os.makedirs(self.data_path, exist_ok=True)
    
    def load_config(self, config_name):
        """
        設定ファイルを読み込む
        
        Args:
            config_name (str): 設定ファイル名（拡張子なし）
            
        Returns:
            dict: 設定データ
        """
        # キャッシュにあればそれを返す
        if config_name in self.configs:
            return self.configs[config_name]
        
        # 設定ファイルのパス
        config_path = os.path.join(self.data_path, f"{config_name}.json")
        
        # 設定ファイルを読み込む
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config_data = json.load(f)
            
            # キャッシュに保存
            self.configs[config_name] = config_data
            
            return config_data
        except FileNotFoundError:
            print(f"設定ファイルが見つかりません: {config_path}")
            return {}
        except json.JSONDecodeError:
            print(f"設定ファイルの形式が不正です: {config_path}")
            return {}
    
    def get_environments(self):
        """
        環境設定を取得する
        
        Returns:
            dict: 環境設定
        """
        config = self.load_config("environments")
        return config.get("environments", {})
    
    def get_characters(self):
        """
        キャラクター設定を取得する
        
        Returns:
            dict: キャラクター設定
        """
        return self.load_config("characters")
    
    def get_game_config(self):
        """
        ゲーム設定を取得する
        
        Returns:
            dict: ゲーム設定
        """
        return self.load_config("game_config")
    
    def get_difficulty_config(self, difficulty):
        """
        難易度設定を取得する
        
        Args:
            difficulty (str): 難易度（"easy", "normal", "hard"）
            
        Returns:
            dict: 難易度設定
        """
        game_config = self.get_game_config()
        difficulty_levels = game_config.get("difficulty_levels", {})
        return difficulty_levels.get(difficulty, {})