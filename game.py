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
                        return "input"
                    if location[0] >= btn_x and location[0] <= btn_x + btn_wid and location[1] >= btn_y + 60 and location[1]<= btn_y + btn_hei + 60:
                        return "ranking"
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
                        return "gamerun"
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
                            return "main"
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            clock.tick(60)  # 60프레임
            pygame.display.update()    

# 변수 설정
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

class GameRun:
    def gameRun():
        print(name)

        skyR = 255
        skyG = 255
        skyB = 255
        skycolor = RGB(skyR, skyG, skyB, 255)
        
        GameRun.Restart()
        motion_state = "run"
        # 4. 메인 이벤트
        while True:
            if motion_state == "run":
                player_rect = pygame.Rect(rex.player.x+8, rex.player.y, 26, 60)
            elif motion_state == "slide":
                player_rect = pygame.Rect(rex.player.x + 8, 100, 26, 60)

            # 4-1. FPS 설정
            clock.tick(60)  # 60프레임
            # 4-2. 각종 입력 감지
            for event in pygame.event.get():
                # 게임 종료
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if not element.game_over:
                    rex.player.run("run")
                    if event.type == pygame.KEYDOWN:
                        # 윗 방향키도 점프 추가
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                            if rex.player.y >= 250:
                                sound_jump.play()
                                element.time1 = time.time()
                                element.velocidade = -45  # 점프 높이 설정
                                rex.player.y = 250
                                element.gravity = 10
                            if element.JumpTwice == True :
                                sound_jump.play()
                                element.time1 = time.time()
                                element.velocidade = -45  # 점프 높이 설정
                                rex.player.y = rex.player.y
                                element.gravity = 10       
                        # 슬라이딩 구현
                        if rex.player.y >= 200 and event.key == pygame.K_DOWN:
                            rex.player.run("slide")
                            motion_state = "slide"
                        else:
                            rex.player.run("run")
                            motion_state = "run"


            t = time.time() - element.time1
            if element.velocidade < 100 and rex.player.y <= 250:
                if element.velocidade > 0:
                    element.gravity = 5
                rex.player.y += (int(element.velocidade * t))
                element.velocidade += element.gravity * t
            if rex.player.y > 250:
                rex.player.y = 250

            # 4-4. 그리기
            surface.fill(skycolor.getColor())
            screen.blit(surface, (0, 0))
            gui.display_score(element.scores)
            screen.blit(rex.player.update_surface(), (rex.player.x, rex.player.y))

            cactus_x_start = random.randint(800, 1100)
            cloud_x_start = random.randint(800, 1200)
            cloud_y_start = random.randint(20, 200)
            bird_x_start = random.randint(1300,1500)
            # 장애물, 배경, 구름을 움직이게 설정
            terrain_obj.move(screen, element.game_speed, terrain_game_speed_multi, terrain_x_limit, terrain_x_start, terrain_y_start)
            cloud_obj.move(screen, element.game_speed, cloud_game_speed_multi, cloud_x_limit, cloud_x_start , cloud_y_start)
            cactus_obj.move(screen, element.game_speed, cactus_game_speed_multi, cactus_x_limit , cactus_x_start, cactus_y_start)
            bird_obj.move(screen, element.game_speed, bird_game_speed_multi, bird_x_limit , bird_x_start, bird_y_start)
            
            # 아이템을 움직이게 설정
            Shield_obj.move(screen, element.game_speed, Shield_game_speed_multi, Shield_x_limit , Shield_x_start, Shield_y_start)
            Dash_obj.move(screen, element.game_speed, Dash_game_speed_multi, Dash_x_limit , Dash_x_start, Dash_y_start)
            Mini_obj.move(screen, element.game_speed, Mini_game_speed_multi, Mini_x_limit , Mini_x_start, Mini_y_start)
            Middle_obj.move(screen, element.game_speed, Middle_game_speed_multi, Middle_x_limit , Middle_x_start, Middle_y_start)
            Big_obj.move(screen, element.game_speed, Big_game_speed_multi, Big_x_limit , Big_x_start, Big_y_start)
            Jump_obj.move(screen, element.game_speed, Jump_game_speed_multi, Jump_x_limit , Jump_x_start, Jump_y_start)
            # 게임 설정

            #캐릭터와 장애물간 충돌 
            if rex.check_collision(player_rect, cactus_obj, obs_dx=10, obs_dy=15) or rex.check_collision(player_rect, bird_obj, obs_dx=10, obs_dy=15):
                sound_hit.play()
                if element.Shield == False and element.Dash == False:
                    element.game_over = True
                    element.isRetry = True
                elif element.Shield == True:
                    element.Shield = False
                if not element.game_over:
                    cactus_obj.Crash(cactus_x_start,cactus_y_start)



            if element.game_over:
                #gui.display_game_over()
                #game_speed = 0
                rex.player.create_animation(64, 34, 50, 57, False, duration=120, rows=1, cols=1)
                gameover.GameOver.over(gui)

            if not element.game_over:
                element.scores += 0.5  # 스코어
            
            # 아이템 획득 부분 및 해당 아이템 구동 부분
            #실드 아이템
            if rex.check_collision(player_rect, Shield_obj, obs_dx=5, obs_dy=10) :
                element.Shield = True
                Shield_obj.Crash(Shield_x_start,Shield_y_start)
            #대쉬 아이템
            if rex.check_collision(player_rect, Dash_obj, obs_dx=5, obs_dy=10):
                element.Dash = True
                element.Dash_Target_Score = element.scores+100
                element.game_speed += element.game_speed/20
            if element.Dash == True and element.Dash_Target_Score <= element.scores:
                element.game_speed -= element.game_speed/20
                element.Dash = False
            # 추가 포인트 아이템
            if rex.check_collision(player_rect, Mini_obj, obs_dx=5, obs_dy=10) :
                element.scores += 10
                Mini_obj.Crash(Mini_x_start,Mini_y_start)
            if rex.check_collision(player_rect, Middle_obj, obs_dx=5, obs_dy=10) :
                element.scores += 50
                Middle_obj.Crash(Middle_x_start,Middle_y_start)
            if rex.check_collision(player_rect, Big_obj, obs_dx=5, obs_dy=10) :
                element.scores += 100
                Big_obj.Crash(Big_x_start,Big_y_start)
            
            #2회 점프 아이템
            if rex.check_collision(player_rect, Jump_obj, obs_dx=5, obs_dy=10):
                element.JumpTwice = True
                element.Jump_Target_Score = element.scores + 100
            if element.Dash == True and element.Jump_Target_Score <= element.scores:
                element.JumpTwice = False
                
            #100점 기준 배경 변경
            if (element.scores % 400 == 0):
               skycolor.setColor(255, 255, 255, 255)
            elif (element.scores % 400 == 100):
               skycolor.setColor(241, 95, 95, 255)
            elif (element.scores % 400 == 200):
               skycolor.setColor(53, 53, 53, 255)
            elif (element.scores % 400 == 300):
               skycolor.setColor(165, 102, 255, 255)

            #400점 기준 속력 상승
            if (element.scores % 400 == 1):
                element.game_speed+=0.1
                #print(game_speed)
                
            # 4-5. 업데이트
            pygame.display.update()

            while element.isRetry:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            cactus_obj.Crash(cactus_x_start,cactus_y_start)
                            GameRun.Restart()
                            break
                        if event.key == pygame.K_n:
                            gameover.GameOver.saveScore(element.scores)
                            return "gameover"
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                    if event.type == pygame.QUIT :
                        pygame.quit()
                        sys.exit()

    def Restart():
        element.scores = 0
        element.gravity = 5
        element.time1 = time.time()
        element.velocidade = 100
        element.game_speed = 1.2
        element.game_over = False
        element.isRetry = False
        element.Shield = False
        element.Dash   = False
        element.Dash_Target_Score = 0
        element.JumpTwice = False
        element.Jump_Target_Score = 0
        element.isJump = 0
        rex.player.y = 250
        terrain_obj.Yinit()
        cactus_obj.coord_list[0][0] = 600
        cactus_obj.coord_list[1][0] = 900
        cactus_obj.coord_list[2][0] = 1100
        cactus_obj.coord_list[3][0] = 1500
        bird_obj.coord_list[0][0] = 50