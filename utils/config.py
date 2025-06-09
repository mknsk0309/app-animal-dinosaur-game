#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
設定管理モジュール
"""

import json
import os

class Config:
    """設定を管理するクラス"""
    
    def __init__(self, config_file="config.json"):
        """
        設定を初期化する
        
        Args:
            config_file (str): 設定ファイルのパス
        """
        self.config_file = config_file
        self.config = self._load_config()
        
        # デフォルト設定
        self.default_config = {
            "screen_width": 800,
            "screen_height": 600,
            "fps": 30,
            "sound_volume": 0.7,
            "music_volume": 0.5,
            "fullscreen": False,
            "difficulty": "easy"
        }
        
        # 設定がなければデフォルト値を使用
        for key, value in self.default_config.items():
            if key not in self.config:
                self.config[key] = value
    
    def _load_config(self):
        """
        設定ファイルを読み込む
        
        Returns:
            dict: 設定データ
        """
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                print(f"設定ファイルの読み込みに失敗しました: {self.config_file}")
                return {}
        return {}
    
    def save_config(self):
        """設定ファイルを保存する"""
        try:
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)
        except IOError:
            print(f"設定ファイルの保存に失敗しました: {self.config_file}")
    
    def get(self, key, default=None):
        """
        設定値を取得する
        
        Args:
            key (str): 設定キー
            default: デフォルト値
            
        Returns:
            設定値
        """
        return self.config.get(key, default)
    
    def set(self, key, value):
        """
        設定値を設定する
        
        Args:
            key (str): 設定キー
            value: 設定値
        """
        self.config[key] = value
        self.save_config()
