"""
Dino Runner Clone
"""
from os import SEEK_SET
import sys
import time

from pygame.display import get_window_size
from settings import *
from display import *

def main():

    # 변수 설정
    scores = 0
    gravity = 5
    time1 = time.time()
    velocidade = 100
    game_speed = 1.2
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    game_over = False
<<<<<<< Updated upstream
=======
    isRetry = False
    Shield = False
    Dash   = False
    Dash_Target_Score = 0
    JumpTwice = False
    NoMoreJump = False
    Jump_Target_Score = 0
    isJump = 2
>>>>>>> Stashed changes
    skyR = 255
    skyG = 255
    skyB = 255
    skycolor = RGB(skyR, skyG, skyB, 255)

    # 요소
    clock = pygame.time.Clock()  # 시계 객체 생성
    gui = display.Display(screen,myfont)

    # 캐릭터, 장애물, 배경 객체 생성
    rex = character.Player(rex_sprite_path)
    cactus_obj = backgorund.ScenarioElement(sprite, cactus_rect, cactus_list_coord)
    terrain_obj = backgorund.ScenarioElement(sprite, terrain_rect, terrain_list_coord)
    cloud_obj = backgorund.ScenarioElement(sprite, cloud_rect, cloud_list_coord)

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
            if not game_over:
                if event.type == pygame.KEYDOWN:
                    # 윗 방향키도 점프 추가
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        if rex.player.y >= 250:
                            sounda.play()
                            time1 = time.time()
                            velocidade = -45  # 점프 높이 설정
                            rex.player.y = 250
                            gravity = 10
<<<<<<< Updated upstream
=======
                            isJump = 1
                            print(isJump)
                            if JumpTwice == True:
                                sounda.play()
                                time1 = time.time()
                                velocidade = -45  # 점프 높이 설정
                                rex.player.y = rex.player.y
                                gravity = 10
                                isJump = 0
                                print(isJump)
>>>>>>> Stashed changes
        t = time.time() - time1

        if velocidade < 100 and rex.player.y <= 250:
            if velocidade > 0:
                gravity = 5
            rex.player.y += (int(velocidade * t))
            velocidade += gravity * t
        if rex.player.y > 250:
            rex.player.y = 250
            isJump = 2
            print(isJump)

        # 4-4. 그리기
        player_rect = pygame.Rect(rex.player.x + 8, rex.player.y, 26, 60) # 이게 메인루프 안에 있어야지만 충돌을 감지함..
        surface = pygame.Surface(screen.get_size())
        surface = surface.convert()
        surface.fill(skycolor.getColor())
        screen.blit(surface, (0, 0))
        #pygame.draw.rect(screen, WHITE, player_rect)
        gui.display_score(scores)
        screen.blit(rex.player.update_surface(), (rex.player.x, rex.player.y))

        # 장애물, 배경, 구름을 움직이게 설정
        terrain_obj.move(screen, game_speed, terrain_game_speed_multi, terrain_x_limit, terrain_x_start, terrain_y_start)
        cloud_obj.move(screen, game_speed, cloud_game_speed_multi, cloud_x_limit, cloud_x_start , cloud_y_start)
        cactus_obj.move(screen, game_speed, cactus_game_speed_multi, cactus_x_limit , cactus_x_start, cactus_y_start)

        # 게임 설정
        rex.player.run("run")
        if rex.check_collision(player_rect, cactus_obj, obs_dx=10, obs_dy=15):
            game_over = True

        if game_over:
            gui.display_game_over()
            game_speed = 0
        if not game_over:
            scores += 0.5  # 스코어
<<<<<<< Updated upstream
            #100점 기준 배경 변경
            if (scores % 400 == 0):
                skycolor.setColor(255, 255, 255, 255)
            elif (scores % 400 == 100):
                skycolor.setColor(241, 95, 95, 255)
            elif (scores % 400 == 200):
                skycolor.setColor(53, 53, 53, 255)
            elif (scores % 400 == 300):
                skycolor.setColor(165, 102, 255, 255)
=======
        
        # 아이템 획득 부분 및 해당 아이템 구동 부분
        #실드 아이템
        if rex.check_collision(player_rect, Shield_obj, obs_dx=5, obs_dy=10) :
            Shield = True
            Shield_obj.Crash(Shield_x_start,Shield_y_start)
        #대쉬 아이템
        if rex.check_collision(player_rect, Dash_obj, obs_dx=5, obs_dy=10):
            Dash = True
            Dash_Target_Score = scores+50
            game_speed += game_speed/20
        if Dash == True :
            if Dash_Target_Score <= scores:
                game_speed -= game_speed/20
                Dash = False
        # 추가 포인트 아이템
        if rex.check_collision(player_rect, Mini_obj, obs_dx=5, obs_dy=10) :
            scores += 10
            Mini_obj.Crash(Mini_x_start,Mini_y_start)
        if rex.check_collision(player_rect, Middle_obj, obs_dx=5, obs_dy=10) :
            scores += 50
            Middle_obj.Crash(Middle_x_start,Middle_y_start)
        if rex.check_collision(player_rect, Big_obj, obs_dx=5, obs_dy=10) :
            scores += 80
            Big_obj.Crash(Big_x_start,Big_y_start)
        
        #2회 점프 아이템
        if rex.check_collision(player_rect, Jump_obj, obs_dx=5, obs_dy=10):
            JumpTwice = True
            Jump_Target_Score = scores + 100
        if JumpTwice == True :
            if Jump_Target_Score <= scores:
                JumpTwice = False
        #100점 기준 배경 변경
        if (scores % 400 == 0):
            skycolor.setColor(255, 255, 255, 255)
        elif (scores % 400 == 100):
            skycolor.setColor(241, 95, 95, 255)
        elif (scores % 400 == 200):
            skycolor.setColor(53, 53, 53, 255)
        elif (scores % 400 == 300):
            skycolor.setColor(165, 102, 255, 255)
>>>>>>> Stashed changes

            #400점 기준 속력 상승
            if (scores % 400 == 1):
                game_speed+=0.1
                print(game_speed)

        # 4-5. 업데이트
        pygame.display.update()

if __name__ == '__main__':
    main()