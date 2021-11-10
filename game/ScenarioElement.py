class ScenarioElement():
    def __init__(self, sprite, crop_rect, coord_list):
        self.surface = sprite.subsurface(crop_rect)
        self.coord_list = coord_list