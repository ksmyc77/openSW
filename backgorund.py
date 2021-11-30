import random
from settings import *

class ScenarioElement:
    def __init__(self, sprite, crop_rect, coord_list):
        self.surface = sprite.subsurface(crop_rect)
        self.coord_list = coord_list

    def move(self, screen, game_speed, game_speed_multiplicator, x_limit, x_start, y_start):
        for i, coord in enumerate(self.coord_list):  # 인덱스 번호와 요소를 튜플형태로 돌려줌
            screen.blit(self.surface, coord)
            # coord x
            self.coord_list[i][0] -= game_speed_multiplicator * game_speed
            if coord[0] < x_limit:  # x값이 제한선을 만나면
                x_last = self.coord_list[i-1][0]
                if(x_start - x_last < 200 and x_start - x_last > 0):
                    x_start += random.randint(180, 300)
                elif(x_start - x_last <= 0):
                    x_start  = x_last + random.randint(180, 300)
            
                # 스타트 값으로 재설정
                self.coord_list[i][0] = x_start
                self.coord_list[i][1] = y_start

    def Crash(self, x_start, dino):
        for i, coord in enumerate(self.coord_list):
            if(self.coord_list[i][0] > dino.character.player.x-60 and self.coord_list[i][0] < dino.character.player.x + 60):
                x_last = self.coord_list[i-1][0]
                if(x_start - x_last < 200 and x_start - x_last > 0):
                    x_start += random.randint(180, 300)
                elif(x_start - x_last <= 0):
                    x_start  = x_last + random.randint(180, 300)
                self.coord_list[i][0] = x_start
    
    def Crash_dash(self, x_start, dino):
          for i, coord in enumerate(self.coord_list):
              if(self.coord_list[i][0] > dino.character.player.x-60 and self.coord_list[i][0] < dino.character.player.x + 250):
                    x_last = self.coord_list[i-1][0]
                    if(x_start - x_last < 200 and x_start - x_last > 0):
                        x_start += random.randint(180, 300)
                    elif(x_start - x_last <= 0):
                        x_start  = x_last + random.randint(180, 300)
                    self.coord_list[i][0] = x_start

    def drawAll(self, screen):
        for i, coord in enumerate(self.coord_list):
            screen.blit(self.surface, coord)

    def Yinit(self):
        for i, coord in enumerate(self.coord_list):
            if(coord[1] != 300):
                coord[1] = 300