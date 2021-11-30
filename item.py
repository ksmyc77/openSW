import random

# items
class ItemElement:
    def __init__(self, sprite, crop_rect, x1, y1):
        self.surface = sprite.subsurface(crop_rect)
        self.x = x1
        self.y = y1
        self.isIN = False

    def move(self, screen, game_speed, game_speed_multiplicator, x_limit, x_start, y_start):
        for i, coord in enumerate(self.coord_list):  # 인덱스 번호와 요소를 튜플형태로 돌려줌
            screen.blit(self.surface, coord)
            # coord x
            self.coord_list[i][0] -= game_speed_multiplicator * game_speed
            if coord[0] < x_limit:  # x값이 제한선을 만나면
                # 스타트 값으로 재설정
                self.coord_list[i][0] = x_start
                self.coord_list[i][1] = y_start

    def move(self, screen, game_speed, game_speed_multiplicator):
        screen.blit(self.surface, (self.x, self.y))
        # coord x
        self.x -= game_speed_multiplicator * game_speed

    def Crash(self, x_start, y_start):
        for i, coord in enumerate(self.coord_list):
            self.coord_list[i][0] = x_start
            self.coord_list[i][1] = y_start

    def get(self):
        self.isIN = True

    def use(self):
        self.isIN = False

class Items:
    def __init__(self):
        self.item_list = []
        self.x_limit = 0

    def addItem(self, item):
        self.item_list.append(item)

    def selectItem(self):
        self.index = random.randint(0, len(self.item_list)-1)
        self.item_list[self.index].x = random.randint(1500, 2000)
        self.item_list[self.index].y = random.randint(150, 280)

    def init(self):
        self.selectItem()
        for i, coord in enumerate(self.item_list):
            self.item_list[i].x = random.randint(900, 1000)
            self.item_list[i].y = random.randint(150, 280)
            self.item_list[i].use()

    def move(self, screen, game_speed, game_speed_multiplicator):
        if(self.item_list[self.index].isIN == True):
            screen.blit(self.item_list[self.index].surface, (100,320))
            return
        self.item_list[self.index].move(screen, game_speed, game_speed_multiplicator)
        if self.item_list[self.index].x < self.x_limit:
            self.selectItem()

    def getItem(self):
        self.item_list[self.index].get()

    def useItem(self):
        self.item_list[self.index].use()
        self.selectItem()

    def getIndex(self):
        return self.index