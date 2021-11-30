
import pygame
from pyanimation import Animation

class Player:
    def __init__(self, sprite_path):
        self.player = Animation(sprite_path)
        self.player.create_animation(0,110,50,57, "run", duration=120, rows=1, cols=2)
        self.player.x = 100
        self.player.y = 250
 
    def check_collision(self, player_rect, obstacle_obj, obs_dx=0, obs_dy=0):
        for coord in obstacle_obj.coord_list:
            obstacle_rect = pygame.Rect(coord[0] + obs_dx,
                                        coord[1] + obs_dy, 50, 40)
            if player_rect.colliderect(obstacle_rect):
                self.player.create_animation(64, 34, 50, 57, False, duration=120, rows=1, cols=1)
                return True

class Character:
    def setCharacter(self, c, overimg):
        self.character = c
        self.over = overimg