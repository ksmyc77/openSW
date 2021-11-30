from typing import Set
from settings import *
import settings
import sys

class SetGame:     
    set_stop = False
    set_state = "set_character"
    game_speed = 0.6

    def gameSet():
        SetGame.set_stop = False
        SetGame.set_state = "set_Mode"
        while True:
            if (SetGame.set_state == "set_Character"):
                SetGame.setCharacter()
            if (SetGame.set_state == "set_Mode"):
                SetGame.setMode()
            
            if(SetGame.set_stop == True):
                return

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        settings.state = "quit"
                        SetGame.set_stop = True
                if event.type == pygame.QUIT :
                    settings.state = "quit"
                    SetGame.set_stop = True

    def setMode():
        x = 140
        y = 60
        xm = x + 400
        while True:
            clock.tick(60)
            #dinosour.character.player.run("run")
            surface.fill(WHITE)
            screen.blit(surface, (0, 0))
            gui.display_title("Choose Game Mode")
            screen.blit(dinosour.character.player.update_surface(), (dinosour.character.player.x, dinosour.character.player.y))
            terrain_obj.move(screen, SetGame.game_speed, terrain_game_speed_multi, terrain_x_limit, terrain_x_start, terrain_y_start)

            rect_m = pygame.Rect(590, 326, 180, 60)
            pygame.draw.rect(screen, DDKGRAY, rect_m)
            goC_button = gui.font.render(f'[Character]', False, LTGRAY)
            gui.screen.blit(goC_button, (600, 330))

            rect_b = pygame.Rect(30, 326, 120, 60)
            pygame.draw.rect(screen, DDKGRAY, rect_b)
            goB_button = gui.font.render(f'[BACK]', False, LTGRAY)
            gui.screen.blit(goB_button, (40, 330))

            origin = pygame.Rect(x, y, 160, 120)
            origin2 = pygame.Rect(x+10, y+10, 140, 100)
            item = pygame.Rect(xm, y, 160, 120)           
            item2 = pygame.Rect(xm+10, y+10, 140, 100)           
              
            if(settings.game_mode == "origin"):
                pygame.draw.rect(screen, DKGRAY, origin)
                pygame.draw.rect(screen, DDKGRAY, origin2)
                origint = gui.font.render(f'Normal', False, LTGRAY)
                pygame.draw.rect(screen, DDKGRAY, item)
                pygame.draw.rect(screen, DKGRAY, item2)
                itemt = gui.font.render(f'Item', False, DDKGRAY)
            elif(settings.game_mode == "item"):
                pygame.draw.rect(screen, DDKGRAY, origin)
                pygame.draw.rect(screen, DKGRAY, origin2)
                origint = gui.font.render(f'Normal', False, DDKGRAY)
                pygame.draw.rect(screen, DKGRAY, item)
                pygame.draw.rect(screen, DDKGRAY, item2)
                itemt = gui.font.render(f'Item', False, LTGRAY)

            gui.screen.blit(origint, (x + 35, y + 36))
            gui.screen.blit(itemt, (xm + 44, y + 36)) 

            btn_run = pygame.image.load(btn_set_run_image_path)
            gui.screen.blit(btn_run, (300,330))
            #rect = pygame.Rect(320, 330, 182, 55)
            #pygame.draw.rect(screen, LTGRAY, rect)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    location = pygame.mouse.get_pos()
                    if location[0] >= x and location[0] <= x+160 and location[1] >= y and location[1]<=y+120:
                        settings.game_mode = "origin"
                    if location[0] >= xm and location[0] <= xm+160 and location[1] >= y and location[1]<=y+120:
                        settings.game_mode = "item"
                    if location[0] >= 300 and location[0] <= 482 and location[1] >= 330 and location[1]<=385:
                        settings.state = "loading"
                        SetGame.set_stop = True
                        return
                    if location[0] >= 590 and location[0] <= 770 and location[1] >= 326 and location[1]<=386:
                        SetGame.set_state = "set_Character"
                        return
                    if location[0] >= 30 and location[0] <= 150 and location[1] >= 326 and location[1]<=386:
                        #settings.state = "in_main"
                        settings.state = "quit"
                        SetGame.set_stop = True
                        return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        settings.state = "quit"
                        SetGame.set_stop = True
                        return
                if event.type == pygame.QUIT :
                    settings.state = "quit"
                    SetGame.set_stop = True
                    return
            pygame.display.update()

    def setCharacter():
        while True:
            clock.tick(60)
            surface.fill(WHITE)
            screen.blit(surface, (0, 0))
            gui.display_title("Choose your Dino")
            screen.blit(cactus, (220, 0))
            screen.blit(cactus, (560, 0))

            x = xm = 320
            y = ym = 80

            rex_r = pygame.Rect(x, y, 160, 200)
            paki_r = pygame.Rect(x - 220, y, 160, 200)
            terzi_r = pygame.Rect(x + 220, y, 160, 200)

            if(dinosour.character == rex):
                #rex choice
                pygame.draw.rect(screen, BLACK, rex_r)
                pygame.draw.rect(screen, DKGRAY, paki_r)
                pygame.draw.rect(screen, DKGRAY, terzi_r)
                rex_t = gui.font.render(f'Rex', False, WHITE)
                paki_t = gui.font.render(f'Paki', False, BLACK)
                terzi_t = gui.font.render(f'Terzi', False, BLACK)
            elif(dinosour.character == paki):
                #paki choice
                pygame.draw.rect(screen, DKGRAY, rex_r)
                pygame.draw.rect(screen, BLACK, paki_r)
                pygame.draw.rect(screen, DKGRAY, terzi_r)
                rex_t = gui.font.render(f'Rex', False, BLACK)
                paki_t = gui.font.render(f'Paki', False, WHITE)
                terzi_t = gui.font.render(f'Terzi', False, BLACK)
            else:
                #terzi choice
                pygame.draw.rect(screen, DKGRAY, rex_r)
                pygame.draw.rect(screen, DKGRAY, paki_r)
                pygame.draw.rect(screen, BLACK, terzi_r)
                rex_t = gui.font.render(f'Rex', False, BLACK)
                paki_t = gui.font.render(f'Paki', False, BLACK)
                terzi_t = gui.font.render(f'Terzi', False, WHITE)

            rex_r2 = pygame.Rect(x+10, y+20, 140, 100)
            pygame.draw.rect(screen, WHITE, rex_r2)
            paki_r2 = pygame.Rect(x - 210, y+20, 140, 100)
            pygame.draw.rect(screen, WHITE, paki_r2)
            terzi_r2 = pygame.Rect(x + 230, y+20, 140, 100)
            pygame.draw.rect(screen, WHITE, terzi_r2)

            if(dinosour.character == rex):
                #rex choice
                screen.blit(paki_p, (x - 160, y+77))
                screen.blit(terzi_p, (x + 280, y+77))
                xm = x + 50
                ym = y + 65
            elif(dinosour.character == paki):
                #paki choice
                screen.blit(rex_p, (x + 50, y+60))
                screen.blit(terzi_p, (x + 280, y+77))
                xm = x - 160
                ym = y + 77
            else:
                #terzi choice
                screen.blit(rex_p, (x + 50, y+60))
                screen.blit(paki_p, (x - 160, y+77))
                xm = x + 280
                ym = y + 77

            gui.screen.blit(rex_t, (x + 50, y + 140))      
            gui.screen.blit(paki_t, (x - 170, y + 140))  
            gui.screen.blit(terzi_t, (x + 260, y + 140))
            screen.blit(dinosour.character.player.update_surface(), (xm, ym))

            rect_m = pygame.Rect(590, 326, 180, 60)
            pygame.draw.rect(screen, DDKGRAY, rect_m)
            goMode_button = gui.font.render(f'[Set Mode]', False, LTGRAY)
            gui.screen.blit(goMode_button, (600, 330))

            rect_b = pygame.Rect(30, 326, 120, 60)
            pygame.draw.rect(screen, DDKGRAY, rect_b)
            goB_button = gui.font.render(f'[BACK]', False, LTGRAY)
            gui.screen.blit(goB_button, (40, 330))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    location = pygame.mouse.get_pos()
                    if location[0] >= x and location[0] <= x+160 and location[1] >= y and location[1]<=y+200:
                        dinosour.setCharacter(rex, rex_over)
                    if location[0] >= x - 220 and location[0] <= x - 60 and location[1] >= y and location[1]<=y+200:
                        dinosour.setCharacter(paki, paki_over)
                    if location[0] >= x + 220 and location[0] <= x + 380 and location[1] >= y and location[1]<=y+200:
                        dinosour.setCharacter(terzi, terzi_over)
                    if location[0] >= 590 and location[0] <= 770 and location[1] >= 326 and location[1]<=386:
                        SetGame.set_state = "set_Mode"
                        return
                    if location[0] >= 30 and location[0] <= 150 and location[1] >= 326 and location[1]<=386:
                        #settings.state = "in_main"
                        settings.state = "quit"
                        SetGame.set_stop = True
                        return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        settings.state = "quit"
                        SetGame.set_stop = True
                        return
                if event.type == pygame.QUIT :
                    settings.state = "quit"
                    SetGame.set_stop = True
                    return
            pygame.display.update()