from sys import settrace
from settings import *
import settings

class Loading:
    game_speed = 0.8
    next_step = "gameRun"

    def setNext(next):
        Loading.next_step = next

    def loadingGame():
        star = "."
        for i in range(200):
            clock.tick(60)
            surface.fill(WHITE)
            screen.blit(surface, (0, 0))
            if(i%30==0):
                star += "."
                if(star == "....."):
                    star = "."
            if( i < 150):
                gui.display_count(3-(int)(i/50))
            elif(i>=150):
                gui.display_count("GO")
            title = gui.font.render("Loading" + star, False, (0, 0, 0))
            gui.screen.blit(title, (300, 0))
            screen.blit(dinosour.character.player.update_surface(), (dinosour.character.player.x, dinosour.character.player.y))
            terrain_obj.drawAll(screen)
            cloud_obj.drawAll(screen)
            cactus_obj.drawAll(screen)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    location = pygame.mouse.get_pos()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        settings.state = "quit"
                        return
                if event.type == pygame.QUIT :
                    settings.state = "quit"
                    return
        settings.state = Loading.next_step