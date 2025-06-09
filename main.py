#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
どうぶつと恐竜のかくれんぼ神経衰弱
メインゲームファイル
"""

import sys
import pygame
from ui.menu import MainMenu
from game.game_manager import GameManager
from utils.config import Config

class Game:
    """メインゲームクラス"""
    
    def __init__(self):
        """ゲームの初期化"""
        pygame.init()
        pygame.mixer.init()
        
        # 設定の読み込み
        self.config = Config()
        
        # 画面の設定
        self.screen_width = self.config.get("screen_width", 800)
        self.screen_height = self.config.get("screen_height", 600)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("どうぶつと恐竜のかくれんぼ神経衰弱")
        
        # ゲームの状態管理
        self.game_manager = GameManager()
        
        # メインメニューの初期化
        self.current_screen = MainMenu(self.screen, self.game_manager)
        
        # クロックの初期化
        self.clock = pygame.time.Clock()
        self.fps = self.config.get("fps", 30)
        
        # ゲームの実行状態
        self.running = True
    
    def run(self):
        """メインゲームループ"""
        while self.running:
            # イベント処理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                # 現在の画面にイベントを渡す
                self.current_screen.handle_event(event)
            
            # 画面の更新
            self.current_screen.update()
            
            # 画面の描画
            self.screen.fill((240, 248, 255))  # 背景色（薄い水色）
            self.current_screen.draw()
            pygame.display.flip()
            
            # 次の画面に切り替える必要があるか確認
            next_screen = self.current_screen.get_next_screen()
            if next_screen:
                self.current_screen = next_screen
            
            # フレームレートの制御
            self.clock.tick(self.fps)
        
        # ゲーム終了時の処理
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
