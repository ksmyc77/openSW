from settings import *
import sys

class GameOver:
    def over(gui):
        surface.fill((255, 255, 255))
        screen.blit(surface, (0, 0))
        cactus_obj.drawAll(screen)
        terrain_obj.drawAll(screen)
        screen.blit(rex_over, (rex.player.x, 245))
        gui.display_game_over()
        gui.display_game_retry()

    def overRun():
        while True:
            surface.fill((255, 255, 255))
            screen.blit(surface, (0, 0))
            over = pygame.Rect(280, 20, 230, 70)
            text = pygame.Rect(160, 40, 460, 300)
            pygame.draw.rect(screen, DKGRAY, text)
            pygame.draw.rect(screen, LTGRAY, over)

            terrain_obj.drawAll(screen)
            screen.blit(rex_over, (rex.player.x, 245))
            gui.display_game_over()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return -1
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit()
            pygame.display.update()