# items
class ItemElement:

    def __init__(self, sprite, crop_rect, coord_list):
        self.surface = sprite.subsurface(crop_rect)
        self.coord_list = coord_list

    def move(self, screen, game_speed, game_speed_multiplicator, x_limit, x_start, y_start):
        for i, coord in enumerate(self.coord_list):  # 인덱스 번호와 요소를 튜플형태로 돌려줌
            screen.blit(self.surface, coord)
            # coord x
            self.coord_list[i][0] -= game_speed_multiplicator * game_speed
            if coord[0] < x_limit:  # x값이 제한선을 만나면
                # 스타트 값으로 재설정
                self.coord_list[i][0] = x_start
                self.coord_list[i][1] = y_start
    def Crash(self, x_start, y_start):
          for i, coord in enumerate(self.coord_list):
              self.coord_list[i][0] = x_start
              self.coord_list[i][1] = y_start