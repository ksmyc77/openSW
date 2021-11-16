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
pygame.display.set_caption("Dino Adventure")
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
<<<<<<< Updated upstream
=======

# 재시작시 구동을 위한 함수
def Restart():
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
  cactus_x_start = random.randint(800, 1100)
  cactus_y_start = cactus_obj.coord_list[0][1]

  terrain_posx = [0, 480, 960]
  terrain_list_coord = [[x, 300] for x in terrain_posx]  # [ [0,300] , [480,300] , [960,300] ]
  terrain_rect = (20, 268, 540, 20)
  terrain_obj = backgorund.ScenarioElement(sprite, terrain_rect, terrain_list_coord)
  terrain_game_speed_multi = 4
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

  Shield_posx = [600]
  Shield_list_coord = [[x, 200] for x in Shield_posx]  # [ [700,350] , [1000,350] ]
  Shield_rect = (645, 75, 32, 32)
  Shield_obj = item.ItemElement(sprite, Shield_rect, Shield_list_coord)
  Shield_game_speed_multi = 4
  Shield_x_limit = 100
  Shield_x_start = random.randint(800, 5000)
  Shield_y_start = Shield_obj.coord_list[0][1]

  Dash_posx = [3500]
  Dash_list_coord = [[x, 258] for x in Dash_posx]  # [ [700,350] , [1000,350] ]
  Dash_rect = (645, 107, 32, 32)
  Dash_obj = item.ItemElement(sprite, Dash_rect, Dash_list_coord)
  Dash_game_speed_multi = 4
  Dash_x_limit = 100
  Dash_x_start = random.randint(700, 10000)
  Dash_y_start = Dash_obj.coord_list[0][1]

  Mini_posx = [1500]
  Mini_list_coord = [[x, 258] for x in Mini_posx]  # [ [700,350] , [1000,350] ]
  Mini_rect = (645, 139, 32, 32)
  Mini_obj = item.ItemElement(sprite, Mini_rect, Mini_list_coord)
  Mini_game_speed_multi = 4
  Mini_x_limit = 100
  Mini_x_start = random.randint(700, 3000)
  Mini_y_start = Mini_obj.coord_list[0][1]

  Middle_posx = [4000]
  Middle_list_coord = [[x, 258] for x in Middle_posx]  # [ [700,350] , [1000,350] ]
  Middle_rect = (645, 171, 32, 32)
  Middle_obj = item.ItemElement(sprite, Middle_rect, Middle_list_coord)
  Middle_game_speed_multi = 4
  Middle_x_limit = 100
  Middle_x_start = random.randint(3000, 6000)
  Middle_y_start = Middle_obj.coord_list[0][1]

  Big_posx = [6500]
  Big_list_coord = [[x, 258] for x in Big_posx]  # [ [700,350] , [1000,350] ]
  Big_rect = (645, 203, 32, 32)
  Big_obj = item.ItemElement(sprite, Big_rect, Big_list_coord)
  Big_game_speed_multi = 4
  Big_x_limit = 100
  Big_x_start = random.randint(6000, 9000)
  Big_y_start = Big_obj.coord_list[0][1]

  Jump_posx = [4000]
  Jump_list_coord = [[x, 258] for x in Jump_posx]  # [ [700,350] , [1000,350] ]
  Jump_rect = (645, 235, 32, 32)
  Jump_obj = item.ItemElement(sprite, Jump_rect, Jump_list_coord)
  Jump_game_speed_multi = 4
  Jump_x_limit = 100
  Jump_x_start = random.randint(4000, 9000)
  Jump_y_start = Jump_obj.coord_list[0][1]

  sound_path = os.path.join(BASEDIR, "sound", "press.wav")
  sounda = pygame.mixer.Sound(sound_path)
>>>>>>> Stashed changes
