import pygame
import random
import os
import backgorund
import character
import display


WHITE = (255, 255, 255)

# 1. 게임 초기화
pygame.init()
pygame.mixer.init()

# 게임창 옵션 설정
pygame.display.set_caption("Dino Advanture")
SCREEN_WIDTH, SCREEN_HEIGHT = (800, 400)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# 3-2 요소
BASEDIR = os.path.dirname(os.path.abspath(__file__))

# 캐릭터 스프라이트 경로
rex_sprite_path = os.path.join(BASEDIR, "images/sprites", "rex_alfa.png")

sprite = pygame.image.load(rex_sprite_path).convert()

# 장애물, 배경, 구름 설정
cactus_posx = [600, 900]
cactus_list_coord = [[x, 258] for x in cactus_posx]  # [ [600,258] , [900,258] ]
cactus_rect = (148, 55, 60, 58)
cactus_obj = backgorund.ScenarioElement(sprite, cactus_rect, cactus_list_coord)
cactus_game_speed_multi = 4
cactus_x_limit = 100
cactus_x_start = random.randint(800, 1500)
cactus_y_start = cactus_obj.coord_list[0][1]

terrain_posx = [0, 480, 960]
terrain_list_coord = [[x, 300] for x in terrain_posx]  # [ [0,300] , [480,300] , [960,300] ]
terrain_rect = (20, 268, 540, 20)
terrain_obj = backgorund.ScenarioElement(sprite, terrain_rect, terrain_list_coord)
terrain_game_speed_multi = 3
terrain_x_limit = -500
terrain_x_start = 960
terrain_y_start = terrain_obj.coord_list[0][1]

cloud_list_coord = [[random.randint(400, 600), random.randint(20, 200)] for i in range(10)]
cloud_rect = (470, 5, 50, 25)
cloud_obj = backgorund.ScenarioElement(sprite, cloud_rect, cloud_list_coord)
cloud_game_speed_multi = 1
cloud_x_limit = 0
cloud_x_start = random.randint(800, 1200)
cloud_y_start = random.randint(20, 200)

sound_path = os.path.join(BASEDIR, "sound", "press.wav")
sounda = pygame.mixer.Sound(sound_path)