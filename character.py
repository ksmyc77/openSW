
import pygame
from pyanimation import Animation
import settings

class Player:
    def __init__(self, sprite_path, type, dino_t):
        self.player = Animation(sprite_path)
        self.type = dino_t
        if(type == "run"):
            if(dino_t == "rex"):
                self.player.y = 250
            else:
                self.player.y = 262
            if(dino_t == "rex"):
                self.player.create_animation(0,110,50,57, "run", duration=120, rows=1, cols=2)
            else:
                self.player.create_animation(0,75,49,57, "run", duration=120, rows=1, cols=2)
        if(type == "slide"):
            if(dino_t == "rex"):
                self.player.y = 250
            else:
                self.player.y = 258
            if(dino_t == "rex"):
                self.player.create_animation(10,167,60,70, "slide", duration=120, rows=1, cols=2)
            else:
                self.player.create_animation(0,129,61,50, "slide", duration=120, rows=1, cols=2)
        if(type == "death"):
            if(dino_t == "rex"):
                self.player.y = 250
            elif(dino_t == "terzi"):
                self.player.y = 263
            else:
                self.player.y = 266
            if(dino_t == "rex"):
                self.player.create_animation(64, 34, 50, 57, False, duration=120, rows=1, cols=1)
            elif(dino_t == "terzi"):
                self.player.create_animation(44, 0, 60, 60, False, duration=120, rows=1, cols=1)
            else:
                self.player.create_animation(64, 4, 50, 57, False, duration=120, rows=1, cols=1)
        self.player.x = 100
        self.player.early_Y = self.player.y
 
    def check_collision(self, player_rect, obstacle_obj, obs_dx=22, obs_dy=20):
        for coord in obstacle_obj.coord_list:
            obstacle_rect = pygame.Rect(coord[0] + obs_dx,
                                        coord[1] + obs_dy, 34, 33)
            #pygame.draw.rect(settings.screen, settings.LTGRAY, obstacle_rect)
            if player_rect.colliderect(obstacle_rect):
                return True

    def check_collision_bird(self, player_rect, obstacle_obj, obs_dx=5, obs_dy=10):
        for coord in obstacle_obj.coord_list:
            bird_rect = pygame.Rect(coord[0] + obs_dx,
                                        coord[1] + obs_dy, 44, 22)
            #pygame.draw.rect(settings.screen, settings.LTGRAY, bird_rect)
            if player_rect.colliderect(bird_rect):
                return True

    def check_collision_item(self, player_rect, item_obj, obs_dx=0, obs_dy=0):
        item_rect = pygame.Rect(item_obj.item_list[item_obj.index].x + obs_dx, item_obj.item_list[item_obj.index].y + obs_dy, 50, 40)
        if player_rect.colliderect(item_rect):
            return True

class Character:
    def setCharacter(self, c, s, d, name):
        self.character = c
        self.run = c
        self.slide = s
        self.death = d
        self.dino = name

    def setRun(self):
        self.character = self.run
        self.character.player.y = self.slide.player.y
        self.character.player.run("run")

    def setSlide(self):
        self.character = self.slide
        self.character.player.y = self.run.player.y
        self.character.player.run("slide")

    def setDeath(self):
        self.death.player.y = self.character.player.y
        self.character = self.death
        self.character.player.run(False)