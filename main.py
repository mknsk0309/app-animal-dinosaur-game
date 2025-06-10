#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
どうぶつ・きょうりゅうかくれんぼ
メインゲームファイル
"""

import sys
import pygame
import asyncio
import platform
from ui.menu import MainMenu
from game.game_manager import GameManager
from utils.config import Config

class Game:
    """メインゲームクラス"""
    
    def __init__(self):
        """ゲームの初期化"""
        pygame.init()
        pygame.mixer.init()
        
        # タッチイベントをマウスイベントに変換する設定
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION, pygame.FINGERDOWN, pygame.FINGERUP, pygame.FINGERMOTION])
        
        # 設定の読み込み
        self.config = Config()
        
        # 画面の設定
        self.screen_width = self.config.get("screen_width", 800)
        self.screen_height = self.config.get("screen_height", 600)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("どうぶつ・きょうりゅうかくれんぼ")
        
        # ゲームの状態管理
        self.game_manager = GameManager()
        
        # メインメニューの初期化
        self.current_screen = MainMenu(self.screen, self.game_manager)
        
        # クロックの初期化
        self.clock = pygame.time.Clock()
        self.fps = self.config.get("fps", 30)
        
        # ゲームの実行状態
        self.running = True
        
        # Emscripten環境かどうかを判定
        self.is_web = platform.system() == "Emscripten"
        self.web_started = not self.is_web  # デスクトップ環境では最初から開始
    
    async def run(self):
        """メインゲームループ（非同期版）"""
        while self.running:
            # イベント処理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                # Web環境でのスタート処理
                if self.is_web and not self.web_started:
                    if event.type in (pygame.MOUSEBUTTONDOWN, pygame.FINGERDOWN, pygame.KEYDOWN):
                        self.web_started = True
                
                # ゲームが開始されている場合のみイベント処理
                if self.web_started:
                    # 現在の画面にイベントを渡す
                    self.current_screen.handle_event(event)
            
            # Web環境で開始前の場合はスタート画面を表示
            if self.is_web and not self.web_started:
                self.screen.fill((240, 248, 255))  # 背景色
                font = pygame.font.SysFont(None, 48)
                text = font.render("タップしてスタート", True, (0, 0, 0))
                text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
                self.screen.blit(text, text_rect)
            else:
                # 通常のゲーム処理
                # 画面の更新
                self.current_screen.update()
                
                # 画面の描画
                self.screen.fill((240, 248, 255))  # 背景色（薄い水色）
                self.current_screen.draw()
            
            pygame.display.flip()
            
            # 次の画面に切り替える必要があるか確認
            if self.web_started:
                next_screen = self.current_screen.get_next_screen()
                if next_screen:
                    self.current_screen = next_screen
            
            # フレームレートの制御
            self.clock.tick(self.fps)
            
            # WebAssembly環境では制御を戻す必要がある
            if self.is_web:
                await asyncio.sleep(0)
        
        # ゲーム終了時の処理
        pygame.quit()
        sys.exit()

# Pygbagのために非同期メイン関数を追加
async def main():
    game = Game()
    await game.run()

if __name__ == "__main__":
    if platform.system() == "Emscripten":
        # ブラウザ環境では非同期実行
        asyncio.run(main())
    else:
        # デスクトップ環境では通常実行
        game = Game()
        asyncio.run(game.run())
