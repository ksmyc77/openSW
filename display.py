from pygame import color
import settings


class Display:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    def display_game_over(self):
        textsurface_over = self.font.render(f'Game Over', False, (0, 0, 0))
        self.screen.blit(textsurface_over, (315, 175))

    def display_score(self, SCORES):
        textsurface = self.font.render(f'{SCORES:.0f}', False, (0, 0, 0))
        self.screen.blit(textsurface, (385, 0))

class RGB:
    def __init__(self, r, g, b, a):
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a
        self.rgb = (r, g, b, a)

    def getColor(self):
        return self.rgb

    def setColor(self, r, g, b, a):
        self.rgb = (r, g, b, a)