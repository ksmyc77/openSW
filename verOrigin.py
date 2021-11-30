"""
Dino Runner Clone
"""
from os import SEEK_SET
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
    isJump = 0

class GameRun:
    def gameRun():
        skyR = 255
        skyG = 255
        skyB = 255
        skycolor = RGB(skyR, skyG, skyB, 255)
        GameRun.init()
        # 4. 메인 이벤트
        while True:
            # 4-1. FPS 설정
            clock.tick(60)  # 60프레임
            dinosour.character.player.run("run")

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
                            if dinosour.character.player.y >= 250:
                                sound_jump.play()
                                element.time1 = time.time()
                                element.velocidade = -45  # 점프 높이 설정
                                dinosour.character.player.y = 250
                                element.gravity = 10
                        if event.key == pygame.K_DOWN or event.key == pygame.K_d:
                            dinosour.setSlide()
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN or event.key == pygame.K_d:
                            dinosour.setRun()
            t = time.time() - element.time1
            if element.velocidade < 100 and dinosour.character.player.y <= 250:
                if element.velocidade > 0:
                    element.gravity = 5
                dinosour.character.player.y += (int(element.velocidade * t))
                element.velocidade += element.gravity * t
            if dinosour.character.player.y > 250:
                dinosour.character.player.y = 250

            # 4-4. 그리기
            player_rect = pygame.Rect(dinosour.character.player.x + 8, dinosour.character.player.y, 26, 60) # 이게 메인루프 안에 있어야지만 충돌을 감지함..
            surface.fill(skycolor.getColor())
            screen.blit(surface, (0, 0))
            gui.display_score(element.scores)

            cactus_x_start = random.randint(800, 1100)
            cloud_x_start = random.randint(800, 1200)
            cloud_y_start = random.randint(20, 200)
            # 장애물, 배경, 구름을 움직이게 설정
            terrain_obj.move(screen, element.game_speed, terrain_game_speed_multi, terrain_x_limit, terrain_x_start, terrain_y_start)
            cloud_obj.move(screen, element.game_speed, cloud_game_speed_multi, cloud_x_limit, cloud_x_start , cloud_y_start)
            cactus_obj.move(screen, element.game_speed, cactus_game_speed_multi, cactus_x_limit , cactus_x_start, cactus_y_start)
            screen.blit(dinosour.character.player.update_surface(), (dinosour.character.player.x, dinosour.character.player.y))
            
            #캐릭터와 장애물간 충돌 
            if dinosour.character.check_collision(player_rect, cactus_obj, obs_dx=10, obs_dy=15):
                sound_hit.play()
                element.game_over = True
                element.isRetry = True

            if element.game_over:
                #gui.display_game_over()
                #game_speed = 0
                gameover.GameOver.over()

            if not element.game_over:
                element.scores += 0.5  # 스코어
                
            #100점 기준 배경 변경
            #if (scores % 400 == 0):
            #    skycolor.setColor(255, 255, 255, 255)
            #elif (scores % 400 == 100):
            #    skycolor.setColor(241, 95, 95, 255)
            #elif (scores % 400 == 200):
            #    skycolor.setColor(53, 53, 53, 255)
            #elif (scores % 400 == 300):
            #    skycolor.setColor(165, 102, 255, 255)

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
                            GameRun.init()
                            break
                        if event.key == pygame.K_n:
                            gameover.GameOver.saveScore(element.scores)
                            settings.state = "gameover"
                            return
                        if event.key == pygame.K_ESCAPE:
                            settings.state = "quit"
                            return
                    if event.type == pygame.QUIT :
                        settings.state = "quit"
                        return

    def init():
        element.scores = 0
        element.gravity = 5
        element.time1 = time.time()
        element.velocidade = 100
        element.game_speed = 1.2
        element.game_over = False
        element.isRetry = False
        element.isJump = 0
        dinosour.run.player.y = 250
        dinosour.slide.player.y = 250
        terrain_obj.Yinit()
        cactus_obj.coord_list[0][0] = 600
        cactus_obj.coord_list[1][0] = 900
        cactus_obj.coord_list[2][0] = 1100
        cactus_obj.coord_list[3][0] = 1500
        dinosour.character.player.run("run")
        dinosour.setRun()