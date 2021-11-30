"""
Dino Runner Clone
"""
from os import SEEK_SET
import sys
import time
from typing import Tuple

from pygame import mouse
from pygame import mixer
from pygame.constants import K_SPACE
from pygame.display import get_window_size

import settings
from settings import *
from display import *
import button
from button import BtnClass


import gameover
import main

class element:
    scores = 0
    gravity = 5
    time1 = time.time()
    velocidade = 100
    game_speed = 1.2
    game_over = False
    isRetry = False
    Shield = False
    Dash   = False
    Dash_Target_Score = 0
    JumpTwice = False
    Jump_Target_Score = 0
    isJump = 0
    now_speed = game_speed

class MainMenu:
    def mainMenu():
        while True:
            surface.fill((255, 255, 255))
            screen.blit(surface, (0, 0))

            btn_x = 400-68
            btn_y = 210
            btn_wid = 136
            btn_hei = 50

            terrain_obj.move(screen, element.game_speed, terrain_game_speed_multi, terrain_x_limit, terrain_x_start, terrain_y_start)

            screen.blit(pygame.image.load(os.path.join(BASEDIR, "images/isolated_frames", "title.png")).convert(),(400-185,30))

            BtnRun = BtnClass(screen, btn_setting, btn_x, btn_y, btn_wid, btn_hei, act_setting)
            BtnRanking = BtnClass(screen, btn_rank, btn_x, btn_y + 60, btn_wid, btn_hei, act_rank)
            BtnEXIT = BtnClass(screen, btn_exit, btn_x, btn_y + 120, btn_wid, btn_hei, act_exit)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    location = pygame.mouse.get_pos()
                    if location[0] >= btn_x and location[0] <= btn_x + btn_wid and location[1] >= btn_y and location[1]<= btn_y + btn_hei:
                        settings.state = "input"
                    if location[0] >= btn_x and location[0] <= btn_x + btn_wid and location[1] >= btn_y + 60 and location[1]<= btn_y + btn_hei + 60:
                        settings.state = "ranking"
                    if location[0] >= btn_x and location[0] <= btn_x + btn_wid and location[1] >= btn_y + 120 and location[1]<= btn_y + btn_hei + 120:
                        pygame.quit()
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit()

            clock.tick(60)  # 60프레임
            pygame.display.update()

class inputName():
    def inputing():
        global name
        name = ''

        while True:
            surface.fill((255, 255, 255))
            screen.blit(surface, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif event.key == pygame.K_RETURN:
                        settings.state = "gamerun"
                    else:
                        if not event.key == pygame.K_SPACE:
                            name += event.unicode
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            gui.display_text("Write your name and press Enter to start", 50, 100)       
            gui.display_text(":" + name, 100, 140)

            clock.tick(60)  # 60프레임
            pygame.display.update()

class Ranking:
    def ranking():
        while True:
            surface.fill((255, 255, 255))
            screen.blit(surface, (0, 0))

            btn_x = 50
            btn_y = 310
            btn_wid = 70
            btn_hei = 40
            terrain_obj.move(screen, element.game_speed, terrain_game_speed_multi, terrain_x_limit, terrain_x_start, terrain_y_start)

            BtnHome = BtnClass(screen, btn_home, btn_x, btn_y, btn_wid, btn_hei, act_home)

            screen.blit(pygame.image.load(os.path.join(BASEDIR, "images/isolated_frames", "leaderboard.png")).convert(),(400-230,10))
            screen.blit(pygame.image.load(os.path.join(BASEDIR, "images/isolated_frames", "ranking_draw.png")).convert(),(400-222,240))
            
            temp = []
            names = []
            scores = []
            chars = []
            with open("scores.txt", "r") as f:
                text = f.read()
                temp = text.split("\n")
                del temp[len(temp) - 1]

                for i in range(len(temp)):
                    temp2 = temp[i].split(" ")
                    names.append(temp2[0])
                    scores.append(float(temp2[1]))
                    chars.append(int(temp2[2]))
                f.close()

            for i in range(len(scores)):
                scores[i] = float(scores[i])

            for i in range(len(scores) - 1):
                for j in range(len(scores) - 1 - i):
                    if scores[j] < scores[j+1]:
                        names[j], names[j+1] = names[j+1], names[j]
                        scores[j], scores[j+1] = scores[j+1], scores[j]
                        chars[j], chars[j+1] = chars[j+1], chars[j]

            if len(scores) >= 3:
                gui.display_rank(names[2], scores[2], 523, 166)
            if len(scores) >= 2:
                gui.display_rank(names[1], scores[1], 227, 166)
            if len(scores) >= 1:
                gui.display_rank(names[0], scores[0], 375, 110)

            screen.blit(rex.player.update_surface(), (375, 185))
            screen.blit(rex.player.update_surface(), (227, 231))
            screen.blit(rex.player.update_surface(), (523, 231))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        location = pygame.mouse.get_pos()
                        if location[0] >= btn_x and location[0] <= btn_x + btn_wid and location[1] >= btn_y and location[1]<= btn_y + btn_hei:
                            settings.state = "main"
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            clock.tick(60)  # 60프레임
            pygame.display.update()    