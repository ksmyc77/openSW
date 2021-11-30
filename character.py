
import pygame
from pyanimation import Animation

class Player:
    def __init__(self, sprite_path, type):
        self.player = Animation(sprite_path)
        if(type == "run"):
            self.player.create_animation(0,110,50,57, "run", duration=120, rows=1, cols=2)
        if(type == "slide"):
            self.player.create_animation(10,167,60,70, "slide", duration=120, rows=1, cols=2)
        self.player.x = 100
        self.player.y = 250
 
    def check_collision(self, player_rect, obstacle_obj, obs_dx=0, obs_dy=0):
        for coord in obstacle_obj.coord_list:
            obstacle_rect = pygame.Rect(coord[0] + obs_dx,
                                        coord[1] + obs_dy, 50, 40)
            if player_rect.colliderect(obstacle_rect):
                self.player.create_animation(64, 34, 50, 57, False, duration=120, rows=1, cols=1)
                return True

    def check_collision_item(self, player_rect, item_obj, obs_dx=0, obs_dy=0):
        item_rect = pygame.Rect(item_obj.item_list[item_obj.index].x + obs_dx, item_obj.item_list[item_obj.index].y + obs_dy, 50, 40)
        if player_rect.colliderect(item_rect):
            return True

class Character:
    def setCharacter(self, c, s):
        self.character = c
        self.another = s
        self.run = c
        self.slide = s

    def switch(self):
        temp = self.character
        self.character = self.another
        self.another = temp

    def setRun(self):
        self.character = self.run

    def setSlide(self):
        self.character = self.slide