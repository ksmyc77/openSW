import pygame
from pygame import mouse
import time

class BtnClass :
  def __init__(self, screen,img_in, x, y, width, height, act, action = None) :
    Mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > Mouse[0] > x and y+height > Mouse[1] > y:
      screen.blit(act,(x,y))
      if click[0] and action != None:
        time.sleep(1)
        action()
    else :
      screen.blit(img_in,(x,y))##