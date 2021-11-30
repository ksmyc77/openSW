
import pygame
import random
import os
import backgorund
import character
import display
import item


WHITE = (255, 255, 255)
LTGRAY = (195, 195, 195)
DKGRAY = (127, 127, 127)
BLACK = (0,0,0)
DDKGRAY = (60, 60, 60)

CENTER = (325, 175)

# 1. 게임 초기화
pygame.init()
pygame.mixer.init()

# 게임창 옵션 설정
pygame.display.set_caption("Dino Adventure")
SCREEN_WIDTH, SCREEN_HEIGHT = (800, 400)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()

# 요소
myfont = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()  # 시계 객체 생성
gui = display.Display(screen,myfont)

# 3-2 요소
BASEDIR = os.path.dirname(os.path.abspath(__file__))

# 각종 스프라이트 및 이미지 경로
rex_sprite_path = os.path.join(BASEDIR, "images/sprites", "rex_alfa.png")
paki_sprite_path = os.path.join(BASEDIR, "images/sprites", "paki_alfa.png")
terzi_sprite_path = os.path.join(BASEDIR, "images/sprites", "terzi_alfa.png")

#초기 게임 화면 및 게임 모드 설정
state = 'in_main'
game_mode  = 'normal'

dino_path = os.path.join(BASEDIR, "images/img")
rex_over_path = os.path.join(BASEDIR, "images/img", "rex_over.png")
cactus_path = os.path.join(BASEDIR, "images/img", "cactus.png")
sprite = pygame.image.load(rex_sprite_path).convert()
rex = character.Player(rex_sprite_path)
paki = character.Player(paki_sprite_path)
terzi = character.Player(terzi_sprite_path)
rex_over = pygame.image.load(rex_over_path)
paki_over = pygame.image.load(os.path.join(dino_path, "paki_over.png"))
terzi_over = pygame.image.load(os.path.join(dino_path, "terzi_over.png"))
cactus = pygame.image.load(cactus_path)

dinosour = character.Character()
dinosour.setCharacter(rex, rex_over)
rex_p = pygame.image.load(os.path.join(dino_path, "rex.png"))
paki_p = pygame.image.load(os.path.join(dino_path, "paki.png"))
terzi_p = pygame.image.load(os.path.join(dino_path, "terzi.png"))

#통상 이미지 버튼
btn_setting_path = os.path.join(BASEDIR, "images/isolated_frames", "btn_setting.png")
btn_ranking_path = os.path.join(BASEDIR, "images/isolated_frames", "btn_rank.png")
btn_exit_path = os.path.join(BASEDIR, "images/isolated_frames", "btn_exit.png")
btn_game_image_path = os.path.join(BASEDIR, "images/isolated_frames", "button.png")
btn_normal_image_path = os.path.join(BASEDIR, "images/isolated_frames", "btn_normal.png")
btn_stage_image_path = os.path.join(BASEDIR, "images/isolated_frames", "btn_stage.png")
btn_race_image_path = os.path.join(BASEDIR, "images/isolated_frames", "btn_race.png")
btn_set_run_image_path = os.path.join(BASEDIR, "images/isolated_frames", "btn_set_run.png")
btn_home_image_path = os.path.join(BASEDIR, "images/isolated_frames", "btn_home.png")
#마우스 오버시 이미지 버튼
act_setting_path = os.path.join(BASEDIR, "images/isolated_frames", "act_setting.png")
act_ranking_path = os.path.join(BASEDIR, "images/isolated_frames", "act_rank.png")
act_exit_path = os.path.join(BASEDIR, "images/isolated_frames", "act_exit.png")
act_normal_image_path = os.path.join(BASEDIR, "images/isolated_frames", "act_normal.png")
act_stage_image_path = os.path.join(BASEDIR, "images/isolated_frames", "act_stage.png")
act_race_image_path = os.path.join(BASEDIR, "images/isolated_frames", "act_race.png")
act_set_run_image_path = os.path.join(BASEDIR, "images/isolated_frames", "act_set_run.png")
act_home_image_path = os.path.join(BASEDIR, "images/isolated_frames", "act_home.png")

sprite = pygame.image.load(rex_sprite_path).convert()
#통상 이미지 버튼
btn_setting = pygame.image.load(btn_setting_path).convert()
btn_rank = pygame.image.load(btn_ranking_path).convert()
btn_exit = pygame.image.load(btn_exit_path).convert()

btn_game = pygame.image.load(btn_game_image_path).convert()
btn_normal = pygame.image.load(btn_normal_image_path).convert()
btn_stage = pygame.image.load(btn_stage_image_path).convert()
btn_race = pygame.image.load(btn_race_image_path).convert()
btn_set_run = pygame.image.load(btn_set_run_image_path).convert()
btn_home = pygame.image.load(btn_home_image_path).convert()
#마우스 오버시 이미지 버튼
act_setting = pygame.image.load(act_setting_path).convert()
act_rank = pygame.image.load(act_ranking_path).convert()
act_exit = pygame.image.load(act_exit_path).convert()

act_normal = pygame.image.load(act_normal_image_path).convert()
act_stage = pygame.image.load(act_stage_image_path).convert()
act_race = pygame.image.load(act_race_image_path).convert()
act_set_run = pygame.image.load(act_set_run_image_path).convert()
act_home = pygame.image.load(act_home_image_path).convert()

# 장애물, 배경, 구름 설정
cactus_posx = [600, 900, 1100, 1500]
cactus_list_coord = [[x, 258] for x in cactus_posx]  # [ [600,258] , [900,258] ]
cactus_rect = (148, 55, 60, 58)
cactus_obj = backgorund.ScenarioElement(sprite, cactus_rect, cactus_list_coord)
cactus_game_speed_multi = 4
cactus_x_limit = 0
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

Shield_posx = [600]
Shield_list_coord = [[x, 200] for x in Shield_posx]  # [ [700,350] , [1000,350] ]
Shield_rect = (645, 75, 32, 32)
Shield_obj = item.ItemElement(sprite, Shield_rect, Shield_list_coord)
Shield_game_speed_multi = 6
Shield_x_limit = 100
Shield_x_start = random.randint(800, 5000)
Shield_y_start = Shield_obj.coord_list[0][1]

Dash_posx = [3500]
Dash_list_coord = [[x, 258] for x in Dash_posx]  # [ [700,350] , [1000,350] ]
Dash_rect = (645, 107, 32, 32)
Dash_obj = item.ItemElement(sprite, Dash_rect, Dash_list_coord)
Dash_game_speed_multi = 6
Dash_x_limit = 100
Dash_x_start = random.randint(700, 6000)
Dash_y_start = Dash_obj.coord_list[0][1]

Mini_posx = [1500]
Mini_list_coord = [[x, 258] for x in Mini_posx]  # [ [700,350] , [1000,350] ]
Mini_rect = (645, 139, 32, 32)
Mini_obj = item.ItemElement(sprite, Mini_rect, Mini_list_coord)
Mini_game_speed_multi = 6
Mini_x_limit = 100
Mini_x_start = random.randint(700, 3000)
Mini_y_start = Mini_obj.coord_list[0][1]

Middle_posx = [4000]
Middle_list_coord = [[x, 258] for x in Middle_posx]  # [ [700,350] , [1000,350] ]
Middle_rect = (645, 171, 32, 32)
Middle_obj = item.ItemElement(sprite, Middle_rect, Middle_list_coord)
Middle_game_speed_multi = 6
Middle_x_limit = 100
Middle_x_start = random.randint(3000, 6000)
Middle_y_start = Middle_obj.coord_list[0][1]

Big_posx = [6500]
Big_list_coord = [[x, 258] for x in Big_posx]  # [ [700,350] , [1000,350] ]
Big_rect = (645, 203, 32, 32)
Big_obj = item.ItemElement(sprite, Big_rect, Big_list_coord)
Big_game_speed_multi = 6
Big_x_limit = 100
Big_x_start = random.randint(6000, 9000)
Big_y_start = Big_obj.coord_list[0][1]

Jump_posx = [4000]
Jump_list_coord = [[x, 258] for x in Jump_posx]  # [ [700,350] , [1000,350] ]
Jump_rect = (645, 235, 32, 32)
Jump_obj = item.ItemElement(sprite, Jump_rect, Jump_list_coord)
Jump_game_speed_multi = 6
Jump_x_limit = 100
Jump_x_start = random.randint(4000, 9000)
Jump_y_start = Jump_obj.coord_list[0][1]

# 게임 모드 설정 함수
def Mode_to_Normal() : # 무한 모드 설정
  global mode
  mode = 'normal'
def Mode_to_Stage() : #스테이지 모드 설정
  global mode
  mode = 'stage'
def Mode_to_race() : # 경쟁 모드 설정
  global mode
  mode = 'race'

#화면 전환 함수
def To_main():
  global state
  state = 'in_main'

def To_EXIT():
  pygame.quit()

def To_Ranking():
  global state
  state = 'in_rank'

def To_Setting():
  global state
  state = 'in_setting'

def To_Run():
  global state, mode
  if mode == 'normal':
    state ='in_game'
  elif mode == 'stage':
    print("미구현")
  elif mode == 'race':
    print("미구현")


sound_jump_path = os.path.join(BASEDIR, "sound", "press.wav")
sound_hit_path = os.path.join(BASEDIR, "sound", "hit.wav")
sound_finish_path = os.path.join(BASEDIR, "sound", "finish.wav")
sound_jump = pygame.mixer.Sound(sound_jump_path)
sound_hit = pygame.mixer.Sound(sound_hit_path)
sound_finish = pygame.mixer.Sound(sound_finish_path)