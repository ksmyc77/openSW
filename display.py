from pygame import color
import settings
import pygame
#test


class Display:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    def display_game_over(self):
        textsurface_over = self.font.render(f'Game Over', False, (0, 0, 0))
        self.screen.blit(textsurface_over, (320, 30))

    def display_game_retry(self):
        textsurface_retry = self.font.render(f'Retry?(Y/N)', False ,(0,0,0))
        self.screen.blit(textsurface_retry, (316, 90))

    def display_score(self, SCORES):
        textsurface = self.font.render(f'{SCORES:.0f}', False, (0, 0, 0))
        self.screen.blit(textsurface, (385, 0))
    
    def display_Shiled(self):
        textsurface = self.font.render(f'Shiled', False ,(0,0,0))
        self.screen.blit(textsurface, (100, 0))

    def undisplay_Shiled(self):
        textsurface = self.font.render(f'Shiled', False ,(255,255,255))
        self.screen.blit(textsurface, (100, 0))

    def display_rank(self, name, score, x, y):
        charName = self.font.render(name, False, (0, 0, 0))
        charScore = self.font.render(f'{score:.0f}', False, (0, 0, 0))
        self.screen.blit(charName, (x, y)) 
        self.screen.blit(charScore, (x, y + 32))

    def display_title(self, title_u):
        title = self.font.render(title_u, False, (0, 0, 0))
        self.screen.blit(title, (300, 0))

    def display_count(self, count):
        pygame.draw.circle(self.screen, settings.DDKGRAY, [170, 210], 35)
        pygame.draw.circle(self.screen, settings.DKGRAY, [170, 210], 30)
        count_t = self.font.render(str(count), False, settings.WHITE)
        if(count == "GO"):
            self.screen.blit(count_t, (150, 188))
        else:
            self.screen.blit(count_t, (160, 190))

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
#
# class Page :
#     def __init__(self, screen):
#         self.screen = screen
#
#     def show_page(self) :
#         pass
#
#
# class LoginPage(Page) :
#     def __init__(self, button):
#         self.button = button
#
#     def show_page(self):
#         self.screen.fill(settings.WHITE)
#         self.screen.blit(self.button , (0 , 0))
#
