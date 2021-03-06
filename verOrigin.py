"""
Dino Runner Clone
"""
from os import SEEK_SET
import sys
import time
from pygame.display import get_window_size
import settings
from settings import *
from display import *
import gameover

# 변수 설정
class element:
    scores = 0
    gravity = 5
    time1 = time.time()
    velocidade = 100
    game_speed = 1.2
    game_over = False
    isRetry = False
    isJump = False
    isSlide = False
    pause = False
    temp_velocity = 0
    temp_gravity = 0

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
                        if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and element.pause is False:
                            if dinosour.character.player.y >= dinosour.character.player.early_Y:
                                sound_jump.play()
                                element.time1 = time.time()
                                element.velocidade = -45  # 점프 높이 설정
                                dinosour.character.player.y = dinosour.character.player.early_Y
                                element.gravity = 10
                                element.isJump = True
                        if event.key == pygame.K_DOWN or event.key == pygame.K_d:
                            dinosour.setSlide()
                            element.isSlide = True
                        # pause
                        if event.key == pygame.K_p and element.pause is False and element.isJump is False:
                            print("state : paused")
                            element.game_speed = 0
                            element.pause = True
                        if event.key == pygame.K_ESCAPE and element.pause is True:
                            element.game_speed = 1.2
                            for i in range(200):
                                clock.tick(60)
                                if (i < 150):
                                    gui.display_count(3 - (int)(i / 50))
                                elif (i >= 150):
                                    gui.display_count("GO")
                                pygame.display.update()
                            element.pause = False
                            print("state : resume")

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
                element.isJump = False

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
            # 4-4. 그리기
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
            bird_obj.move(screen, element.game_speed, bird_game_speed_multi+0.8, bird_x_limit, bird_x_start, bird_y_start)
            screen.blit(dinosour.character.player.update_surface(), (dinosour.character.player.x, dinosour.character.player.y))
            
            #캐릭터와 장애물간 충돌 
            if dinosour.character.check_collision(player_rect, cactus_obj) or dinosour.character.check_collision_bird(player_rect, bird_obj):
                sound_hit.play()
                element.game_over = True
                element.isRetry = True

            if not element.game_over and element.pause is False:
                element.scores += 0.5  # 스코어

            if element.pause is True:
                gui.display_pause()


            if element.game_over:
                gameover.GameOver.saveScore(element.scores)
                settings.state = "gameover"
                return

            #400점 기준 속력 상승
            if (element.scores % 400 == 1):
                element.game_speed+=0.1
                
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
        element.isJump = False
        element.isSlide = False
        element.pause = False
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
        dinosour.setRun()