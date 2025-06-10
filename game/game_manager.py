#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ゲーム状態管理モジュール
"""

class GameManager:
    """ゲーム全体の状態を管理するクラス"""
    
    # ゲームの状態を表す定数
    STATE_MENU = "menu"
    STATE_GAME = "game"
    STATE_ENCYCLOPEDIA = "encyclopedia"
    STATE_STICKER_BOOK = "sticker_book"
    STATE_ENVIRONMENT_SELECT = "environment_select"
    
    def __init__(self):
        """ゲームマネージャーの初期化"""
        # 現在の状態
        self.current_state = self.STATE_MENU
        
        # 選択された環境
        self.current_environment = None
        
        # 発見されたキャラクター
        self.discovered_characters = []
        
        # 難易度
        self.difficulty = "easy"
    
    def change_state(self, new_state):
        """
        ゲームの状態を変更する
        
        Args:
            new_state (str): 新しい状態
        """
        self.current_state = new_state
    
    def select_environment(self, environment):
        """
        環境を選択する
        
        Args:
            environment (str): 選択された環境
        """
        self.current_environment = environment
    
    def discover_character(self, character):
        """
        キャラクターを発見したとマークする
        
        Args:
            character (str): 発見されたキャラクターのID
        """
        if character not in self.discovered_characters:
            self.discovered_characters.append(character)
    
    def reset_game(self):
        """ゲームをリセットする"""
        self.current_environment = None
    
    def set_difficulty(self, difficulty):
        """
        難易度を設定する
        
        Args:
            difficulty (str): 難易度 ("easy" または "normal")
        """
        self.difficulty = difficulty
