"""
Dino Runner Clone
"""
from os import SEEK_SET, name, rename
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
    name = ""

class MainMenu:
    def mainMenu():
        while True:
            clock.tick(60)  # 60프레임
            surface.fill((255, 255, 255))
            screen.blit(surface, (0, 0))

            btn_x = 400-68
            btn_y = 210
            btn_wid = 136
            btn_hei = 50

            terrain_obj.move(screen, 0.6, terrain_game_speed_multi, terrain_x_limit, terrain_x_start, terrain_y_start)

            screen.blit(pygame.image.load(os.path.join(BASEDIR, "images/isolated_frames", "title.png")).convert(),(400-185,30))

            BtnRun = BtnClass(screen, btn_setting, btn_x, btn_y, btn_wid, btn_hei, act_setting)
            BtnRanking = BtnClass(screen, btn_rank, btn_x, btn_y + 60, btn_wid, btn_hei, act_rank)
            BtnEXIT = BtnClass(screen, btn_exit, btn_x, btn_y + 120, btn_wid, btn_hei, act_exit)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    location = pygame.mouse.get_pos()
                    if location[0] >= btn_x and location[0] <= btn_x + btn_wid and location[1] >= btn_y and location[1]<= btn_y + btn_hei:
                        settings.state = "input"
                        return
                    if location[0] >= btn_x and location[0] <= btn_x + btn_wid and location[1] >= btn_y + 60 and location[1]<= btn_y + btn_hei + 60:
                        settings.state = "ranking"
                        return
                    if location[0] >= btn_x and location[0] <= btn_x + btn_wid and location[1] >= btn_y + 120 and location[1]<= btn_y + btn_hei + 120:
                        pygame.quit()
                    if element.name != "" and location[0] >= 104 and location[0] <= 146 and location[1] >= 260 and location[1]<= 310:
                        settings.state = "input"
                        element.name = ""
                        return
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit()
            #player_rect = pygame.Rect(dinosour.character.player.x + 4, dinosour.character.player.y + 10, 42, 50)
            #pygame.draw.rect(screen, LTGRAY, player_rect)
            screen.blit(dinosour.character.player.update_surface(), (dinosour.character.player.x, dinosour.character.player.early_Y))
            name = gui.font.render(f'name : {element.name}', False, BLACK)
            gui.screen.blit(name, (dinosour.character.player.x - 60, dinosour.character.player.early_Y - 40))
            rename = gui.font.render(f'Rename?', False, BLACK)
            if(element.name != ""):
                gui.screen.blit(rename, (dinosour.character.player.x - 25, dinosour.character.player.early_Y +50))
            pygame.display.update()

class inputName():
    def inputing():
        if(element.name != ""):
            settings.state = "gameSetting"
            return
        max = 5
        while True:
            surface.fill((255, 255, 255))
            screen.blit(surface, (0, 0))
            terrain_obj.move(screen, 0.6, terrain_game_speed_multi, terrain_x_limit, terrain_x_start, terrain_y_start)
            screen.blit(dinosour.character.player.update_surface(), (380, dinosour.character.player.early_Y))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        element.name = element.name[0:len(element.name)-1]
                        max += 1
                    if event.key == pygame.K_RETURN:
                        settings.state = "gameSetting"
                        return
                    else:
                        if not event.key == pygame.K_SPACE and not event.key == pygame.K_BACKSPACE:
                            if(len(element.name) >= 5):
                                break
                            element.name += event.unicode
                            max -= 1
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            gui.display_text("Write your name and press Enter", 190, 20)      
            gui.display_text(f'(max : {max})', 350, 70)   
            gui.display_text(":" + element.name, 364, 190)
            clock.tick(60)  # 60프레임
            pygame.display.update()

class Ranking:
    def ranking():
        while True:
            clock.tick(60)
            surface.fill((255, 255, 255))
            screen.blit(surface, (0, 0))

            btn_x = 50
            btn_y = 310
            btn_wid = 70
            btn_hei = 40
            terrain_obj.move(screen, 0.4, terrain_game_speed_multi, terrain_x_limit, terrain_x_start, terrain_y_start)

            BtnHome = BtnClass(screen, btn_home, btn_x, btn_y, btn_wid, btn_hei, act_home)

            screen.blit(pygame.image.load(os.path.join(BASEDIR, "images/isolated_frames", "leaderboard.png")).convert(),(400-230,0))
            screen.blit(pygame.image.load(os.path.join(BASEDIR, "images/isolated_frames", "ranking_draw.png")).convert(),(400-222,240))

            if(settings.game_mode == "origin"):
                x = 660
            else:
                x = 670

            rect_m = pygame.Rect(640, 316, 140, 80)
            pygame.draw.rect(screen, DDKGRAY, rect_m)
            rect_m2 = pygame.Rect(650, 326, 120, 60)
            pygame.draw.rect(screen, DKGRAY, rect_m2)
            goMode_button = gui.font.render(f'[{settings.game_mode}]', False, BLACK)
            gui.screen.blit(goMode_button, (x, 330))

            
            temp = []
            names = []
            scores = []
            chars = []
            dinos = []
            with open(settings.game_mode + "Scores.txt", "r") as f:
                text = f.read()
                temp = text.split("\n")
                del temp[len(temp) - 1]

                for i in range(len(temp)):
                    temp2 = temp[i].split(" ")
                    names.append(temp2[0])
                    scores.append(float(temp2[1]))
                    chars.append(int(temp2[2]))
                    dinos.append(str(temp2[3]))
                f.close()

            for i in range(len(scores)):
                scores[i] = float(scores[i])

            for i in range(len(scores) - 1):
                for j in range(len(scores) - 1 - i):
                    if scores[j] < scores[j+1]:
                        names[j], names[j+1] = names[j+1], names[j]
                        scores[j], scores[j+1] = scores[j+1], scores[j]
                        chars[j], chars[j+1] = chars[j+1], chars[j]
                        dinos[j], dinos[j+1] = dinos[j+1], dinos[j]

            if len(scores) >= 3:
                gui.display_rank(names[2], scores[2], 523, 166)
            if len(scores) >= 2:
                gui.display_rank(names[1], scores[1], 227, 166)
            if len(scores) >= 1:
                gui.display_rank(names[0], scores[0], 375, 110)

            user_dino = []
            for i in range (3):
                if(len(dinos) <= i):                   
                    user_dino.append(rex)
                else:
                    if(dinos[i] == "rex"):
                        user_dino.append(rexs[i])
                    if(dinos[i] == "paki"):
                        user_dino.append(pakis[i])
                    if(dinos[i] == "terzi"):
                        user_dino.append(terzis[i])  

            if(user_dino[0].type == "rex"):
                y = 185
            else:
                y = dinosour.character.player.early_Y - 77
            screen.blit(user_dino[0].player.update_surface(), (375, y))

            if(user_dino[1].type == "rex"):
                y = 231
            else:
                y = dinosour.character.player.early_Y-18
            screen.blit(user_dino[1].player.update_surface(), (227, y))

            if(user_dino[2].type == "rex"):
                y = 231
            else:
                y = dinosour.character.player.early_Y-18
            screen.blit(user_dino[2].player.update_surface(), (523, y))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    location = pygame.mouse.get_pos()
                    if location[0] >= btn_x and location[0] <= btn_x + btn_wid and location[1] >= btn_y and location[1]<= btn_y + btn_hei:
                        settings.state = "main"
                        return
                    if location[0] >= 640 and location[0] <= 780 and location[1] >= 316 and location[1]<= 396:
                        if(settings.game_mode == "origin"):
                            settings.game_mode = "item"
                        else:
                            settings.game_mode = "origin"
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()