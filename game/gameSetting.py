import pygame
import sys
from pyanimation import Animation
import random
import time
import os
from ScenarioElement import ScenarioElement

#pygame setting
pygame.init()
pygame.mixer.init()

BASEDIR = os.path.dirname(os.path.abspath(__file__))
SCREEN_WIDTH, SCREEN_HEIGHT = (800, 400)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((255, 255, 255))
clock = pygame.time.Clock()
screen.blit(surface, (0, 0))

# Rex Animation
rex_sprite_path = os.path.join(BASEDIR, "images/sprites", "rex_alfa.png")
rex = Animation(rex_sprite_path)
rex.create_animation(0, 110, 50, 57, "run", duration=120, rows=1, cols=2)
rex.x = 150
rex.y = 250

rex_over_path = os.path.join(BASEDIR, "images/sprites", "rex_over.png")
rex_over = pygame.image.load(rex_over_path)

sprite = pygame.image.load(rex_sprite_path).convert()

#obstacle setting
cactus_posx = [600, 900]
cactus_list_coord = [[x, 258] for x in cactus_posx]
cactus_obj = ScenarioElement(sprite, (148, 55, 60, 58), cactus_list_coord)
terrain_posx = [0, 480, 960]
terrain_list_coord = [[x, 300] for x in terrain_posx]
terrain_obj = ScenarioElement(sprite, (20, 268, 540, 20), terrain_list_coord)
coord_list = [[random.randint(400, 600), random.randint(20, 200)] for i in range(10)]
cloud_obj = ScenarioElement(sprite, (470, 5, 50, 25), coord_list)

#sound setting
sound_jump_path = os.path.join(BASEDIR, "sound", "press.wav")
sound_jump = pygame.mixer.Sound(sound_jump_path)
sound_hit_path = os.path.join(BASEDIR, "sound", "hit.wav")
sound_hit = pygame.mixer.Sound(sound_hit_path)

myfont = pygame.font.SysFont('Comic Sans MS', 30)