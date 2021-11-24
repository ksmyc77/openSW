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

def main():
    # 변수 설정

    #로컬 변수
    scores = 0
    gravity = 5
    time1 = time.time()
    velocidade = 100
    game_speed = 1.2
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    game_over = False
    isRetry = False
    Shield = False
    Dash   = False
    Dash_Target_Score = 0
    JumpTwice = False
    Jump_Target_Score = 0
    isJump = 0
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
    Shield_obj = item.ItemElement(sprite,Shield_rect,Shield_list_coord)
    Dash_obj = item.ItemElement(sprite, Dash_rect, Dash_list_coord)
    Middle_obj = item.ItemElement(sprite, Middle_rect, Middle_list_coord)
    Big_obj = item.ItemElement(sprite, Big_rect, Big_list_coord)
    Jump_obj = item.ItemElement(sprite, Jump_rect, Jump_list_coord)
    
    # 현재 페이지 상태를 나타내는 변수
    while settings.state == 'in_main':        
        screen.fill(WHITE)
        for event in pygame.event.get():
            # 게임 종료
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(rex.player.update_surface(), (75, 250))
        terrain_obj.move(screen, game_speed, terrain_game_speed_multi, terrain_x_limit, terrain_x_start, terrain_y_start)  
        screen.blit(pygame.image.load(os.path.join(BASEDIR, "images/isolated_frames", "title.png")).convert(),(400-185,30))
        BtnRun = BtnClass(screen, btn_setting, 400-68, 210, 136, 50, act_setting, To_Setting)
        BtnRanking = BtnClass(screen, btn_rank, 400-68, 270, 136, 50, act_rank, To_Ranking)
        BtnEXIT = BtnClass(screen, btn_exit, 400-68, 330, 136, 50, act_exit, To_EXIT)

        pygame.display.update()
        clock.tick(60)  # 60프레임

    while settings.state == 'in_rank':        
        screen.fill(WHITE)
        for event in pygame.event.get():
            # 게임 종료
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(pygame.image.load(os.path.join(BASEDIR, "images/isolated_frames", "leaderboard.png")).convert(),(400-230,10))
        screen.blit(pygame.image.load(os.path.join(BASEDIR, "images/isolated_frames", "ranking_draw.png")).convert(),(400-222,240))
        screen.blit(rex.player.update_surface(), (375, 185))
        screen.blit(rex.player.update_surface(), (227, 231))
        screen.blit(rex.player.update_surface(), (523, 231))
        gui.display_rank('Aino', 5677, 375, 110)
        gui.display_rank('Bino', 1243, 227, 166)
        gui.display_rank('Cino', 14, 523, 166)
        pygame.display.update()
        clock.tick(60)  # 60프레임

    while settings.state == 'in_setting':        
        screen.fill(WHITE)
        for event in pygame.event.get():
            # 게임 종료
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(rex.player.update_surface(), (375, 172))
        BtnNormal = BtnClass(screen, btn_normal, 150, 75, 100, 50, act_normal, Mode_to_Normal)
        BtnStage = BtnClass(screen, btn_stage, 350, 75, 100, 50, act_stage, Mode_to_Stage)
        BtnRace = BtnClass(screen, btn_race, 550, 75, 100, 50, act_race, Mode_to_race)
        BtnRun = BtnClass(screen, btn_set_run, 275, 250, 250, 75, act_set_run, To_Run)
        BtnHome = BtnClass(screen,btn_home, 50, 310, 70, 40, act_home, To_main)
        pygame.display.update()
        clock.tick(60)  # 60프레임

    while settings.state == 'login':
        screen.fill(WHITE)
        screen.blit(btn_game , CENTER)
        pygame.display.update()
        clock.tick(60)  # 60프레임
        # 4-2. 각종 입력 감지
        for event in pygame.event.get():
            # 게임 종료
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    settings.state = 'in_game'
                    break


    # 메인 이벤트
    while settings.state == 'in_game':
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
                        if JumpTwice == True :
                            sounda.play()
                            time1 = time.time()
                            velocidade = -45  # 점프 높이 설정
                            rex.player.y = rex.player.y
                            gravity = 10
        t = time.time() - time1
        if velocidade < 100 and rex.player.y <= 250:
            if velocidade > 0:
                gravity = 5
            rex.player.y += (int(velocidade * t))
            velocidade += gravity * t
        if rex.player.y > 250:
            rex.player.y = 250

        # 4-4. 그리기
        player_rect = pygame.Rect(rex.player.x + 8, rex.player.y, 26, 60) # 이게 메인루프 안에 있어야지만 충돌을 감지함..
        surface = pygame.Surface(screen.get_size())
        surface = surface.convert()
        surface.fill(skycolor.getColor())
        screen.blit(surface, (0, 0))
        gui.display_score(scores)
        screen.blit(rex.player.update_surface(), (rex.player.x, rex.player.y))

        # 장애물, 배경, 구름을 움직이게 설정
        terrain_obj.move(screen, game_speed, terrain_game_speed_multi, terrain_x_limit, terrain_x_start, terrain_y_start)
        cloud_obj.move(screen, game_speed, cloud_game_speed_multi, cloud_x_limit, cloud_x_start , cloud_y_start)
        cactus_obj.move(screen, game_speed, cactus_game_speed_multi, cactus_x_limit , cactus_x_start, cactus_y_start)
        
        # 아이템을 움직이게 설정
        Shield_obj.move(screen, game_speed, Shield_game_speed_multi, Shield_x_limit , Shield_x_start, Shield_y_start)
        Dash_obj.move(screen, game_speed, Dash_game_speed_multi, Dash_x_limit , Dash_x_start, Dash_y_start)
        Mini_obj.move(screen, game_speed, Mini_game_speed_multi, Mini_x_limit , Mini_x_start, Mini_y_start)
        Middle_obj.move(screen, game_speed, Middle_game_speed_multi, Middle_x_limit , Middle_x_start, Middle_y_start)
        Big_obj.move(screen, game_speed, Big_game_speed_multi, Big_x_limit , Big_x_start, Big_y_start)
        Jump_obj.move(screen, game_speed, Jump_game_speed_multi, Jump_x_limit , Jump_x_start, Jump_y_start)
        # 게임 설정
        rex.player.run("run")
        
        #캐릭터와 장애물간 충돌 
        if rex.check_collision(player_rect, cactus_obj, obs_dx=10, obs_dy=15):
            cactus_obj.Crash(cactus_x_start,cactus_y_start)
            if Shield == False and Dash == False:
                game_over = True
                isRetry = True
            elif Shield == True:
                Shield = False
        if game_over:
            gui.display_game_over()
            game_speed = 0
        if not game_over:
            scores += 0.5  # 스코어
        
        # 아이템 획득 부분 및 해당 아이템 구동 부분
        #실드 아이템
        if rex.check_collision(player_rect, Shield_obj, obs_dx=5, obs_dy=10) :
            Shield = True
            Shield_obj.Crash(Shield_x_start,Shield_y_start)
        #대쉬 아이템
        if rex.check_collision(player_rect, Dash_obj, obs_dx=5, obs_dy=10):
            Dash = True
            Dash_Target_Score = scores+100
            game_speed += game_speed/20
        if Dash == True and Dash_Target_Score <= scores:
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
            scores += 100
            Big_obj.Crash(Big_x_start,Big_y_start)
        
        #2회 점프 아이템
        if rex.check_collision(player_rect, Jump_obj, obs_dx=5, obs_dy=10):
            JumpTwice = True
            Jump_Target_Score = scores + 100
        if Dash == True and Jump_Target_Score <= scores:
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

            #400점 기준 속력 상승
            if (scores % 400 == 1):
                game_speed+=0.1
                print(game_speed)

            
        # 4-5. 업데이트

        pygame.display.update()

        #재시작함수
        while isRetry:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_over = False
                        isRetry = False
                        Shield = False
                        Dash   = False
                        Dash_Target_Score = 0
                        JumpTwice = False
                        game_speed = 1.2
                        Restart()
                        break
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_n:
                        To_Setting
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit()

            if isRetry == False:
                main()

if __name__ == '__main__':
    main()