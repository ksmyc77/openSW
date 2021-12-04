"""
Dino Runner Clone
"""
from os import SEEK_SET
from random import randint
import sys
import time
from typing import Tuple

from pygame import mouse
from pygame import mixer
from pygame.display import get_window_size

import settings
from settings import *
from display import *
import button
from button import BtnClass


import gameover
import main

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
    Plus = "false"
    isJump = 0
    isSlide = False
    now_speed = game_speed

class GameRun:
    def gameRun():
        GameRun.init()
        # 4. 메인 이벤트
        while True:
            # 4-1. FPS 설정
            clock.tick(60)  # 60프레임

            # 4-2. 각종 입력 감지
            for event in pygame.event.get():
                # 게임 종료
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if not element.game_over:
                    if event.type == pygame.KEYDOWN:
                        # 윗 방향키도 점프 추가
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                            if dinosour.character.player.y >= dinosour.character.player.early_Y:
                                sound_jump.play()
                                element.time1 = time.time()
                                element.velocidade = -45  # 점프 높이 설정
                                dinosour.character.player.y = dinosour.character.player.early_Y
                                element.gravity = 10
                            if element.JumpTwice == True :
                                sound_jump.play()
                                element.time1 = time.time()
                                element.velocidade = -45  # 점프 높이 설정
                                dinosour.character.player.y = dinosour.character.player.y
                                element.gravity = 10
                            element.isJump = True
                        if event.key == pygame.K_DOWN or event.key == pygame.K_d:
                            dinosour.setSlide()
                            element.isSlide = True
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN or event.key == pygame.K_d:
                            dinosour.setRun()
                            if dinosour.character.player.y == dinosour.slide.player.early_Y:
                                dinosour.character.player.y = dinosour.character.player.early_Y
                            element.isSlide = False
            t = time.time() - element.time1
            if element.velocidade < 100 and dinosour.character.player.y <= dinosour.character.player.early_Y:
                if element.velocidade > 0:
                    element.gravity = 5
                dinosour.character.player.y += (int(element.velocidade * t))
                element.velocidade += element.gravity * t
            if dinosour.character.player.y > dinosour.character.player.early_Y:
                dinosour.character.player.y = dinosour.character.player.early_Y

            # 4-4. 그리기
            if(element.isSlide == False):
                if dinosour.dino == "rex":
                    player_rect = pygame.Rect(dinosour.character.player.x + 8, dinosour.character.player.y + 10, 26, 50)
                else:
                    player_rect = pygame.Rect(dinosour.character.player.x +2, dinosour.character.player.y, 38, 43)
            else:
                if dinosour.dino == "rex":
                    player_rect = pygame.Rect(dinosour.character.player.x + 10, dinosour.character.player.y + 28, 26, 26)
                else:
                    player_rect = pygame.Rect(dinosour.character.player.x + 5, dinosour.character.player.y + 28, 50, 22)
            surface.fill(WHITE)
            screen.blit(surface, (0, 0))
            gui.display_score(element.scores)

            cactus_x_start = random.randint(800, 1100)
            cloud_x_start = random.randint(800, 1200)
            cloud_y_start = random.randint(20, 200)
            bird_x_start = random.randint(800, 2000)
            # 장애물, 배경, 구름을 움직이게 설정
            terrain_obj.move(screen, element.game_speed, terrain_game_speed_multi, terrain_x_limit, terrain_x_start, terrain_y_start)
            cloud_obj.move(screen, element.game_speed, cloud_game_speed_multi, cloud_x_limit, cloud_x_start , cloud_y_start)
            cactus_obj.move(screen, element.game_speed, cactus_game_speed_multi, cactus_x_limit , cactus_x_start, cactus_y_start)
            bird_obj.move(screen, element.game_speed, bird_game_speed_multi + 0.8, bird_x_limit, bird_x_start, bird_y_start)
            screen.blit(dinosour.character.player.update_surface(), (dinosour.character.player.x, dinosour.character.player.y))
            # 아이템을 움직이게 설정
            items.move(screen, element.game_speed + 0.4, 6)
            
            #캐릭터와 장애물간 충돌 
            if dinosour.character.check_collision(player_rect, cactus_obj):
                sound_hit.play()
                if element.Shield == False and element.Dash == False:
                    element.game_over = True
                    element.isRetry = True
                elif element.Shield == True:
                    element.Shield = False
                    items.useItem()
                if not element.game_over:
                    cactus_obj.Crash(cactus_x_start, dinosour)

            if dinosour.character.check_collision_bird(player_rect, bird_obj):
                sound_hit.play()
                if element.Shield == False and element.Dash == False:
                    element.game_over = True
                    element.isRetry = True
                elif element.Shield == True:
                    element.Shield = False
                    items.useItem()
                if not element.game_over:
                    bird_obj.Crash(cactus_x_start, dinosour)

            if element.game_over:
                #gui.display_game_over()
                #game_speed = 0
                gameover.GameOver.saveScore(element.scores)
                settings.state = "gameover"
                return

            if not element.game_over:
                element.scores += 0.5  # 스코어
            
            # 아이템 획득 부분 및 해당 아이템 구동 부분
            #실드 아이템
            if dinosour.character.check_collision_item(player_rect, items, obs_dx=5, obs_dy=10) :
                items.getItem()
                if(items.item_list[items.getIndex()] == shield):
                    element.Shield = True
                if(items.item_list[items.getIndex()] == dash and element.Dash == False):
                    element.Dash = True
                    element.Dash_Target_Score = element.scores+50
                    element.game_speed += element.game_speed/20
                    element.now_speed = element.game_speed
                if(items.item_list[items.getIndex()] == jump):
                    element.JumpTwice = True
                    element.Jump_Target_Score = element.scores + 100
                if(items.item_list[items.getIndex()] == mini):
                    element.scores += 10
                    items.useItem()
                if(items.item_list[items.getIndex()] == middle):
                    element.scores += 50
                    items.useItem()
                if(items.item_list[items.getIndex()] == big):
                    element.scores += 100
                    items.useItem()

            if element.JumpTwice == True and element.Jump_Target_Score <= element.scores:
                element.JumpTwice = False 

            if element.Dash == True:
                element.game_speed += element.game_speed/50

            if element.Dash == True and element.Dash_Target_Score <= element.scores:
                element.game_speed -= element.game_speed/20
                if(element.game_speed <= element.now_speed):
                    cactus_obj.Crash_dash(cactus_x_start, dinosour)
                    bird_obj.Crash_dash(bird_x_start, dinosour)
                    items.useItem()
                    element.Dash = False       

            #400점 기준 속력 상승
            if (element.scores % 400 == 1):
                element.game_speed+=0.1
                #print(game_speed)
                
            # 4-5. 업데이트
            pygame.display.update()

    def init():
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
        element.isSlide = False
        dinosour.run.player.y = dinosour.character.player.early_Y
        dinosour.slide.player.y = dinosour.character.player.early_Y
        dinosour.death.player.y = dinosour.character.player.early_Y
        terrain_obj.Yinit()
        cactus_obj.coord_list[0][0] = 600
        cactus_obj.coord_list[1][0] = 900
        cactus_obj.coord_list[2][0] = 1100
        cactus_obj.coord_list[3][0] = 1500
        bird_obj.coord_list[0][0] = 1000
        dinosour.character.player.run("run")
        items.init()
        dinosour.setRun()