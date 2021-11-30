from pygame import init
from pygame.time import delay
import main
from settings import *
import sys
import settings
import verOrigin
import verItem
import game

class GameOver:
    score = 0
    result_score = 0 
    rank = '???'
    timing = 0

    #temporary
    result_rank = 32
    high = 300
    time_delay = 50
    result_state = False

    def init():
        GameOver.score = 0
        GameOver.rank = "???"
        GameOver.timing = 0
        GameOver.time_delay = 10
        GameOver.result_state = False

    def saveScore(score):
        GameOver.result_score = score

    def over():
        dinosour.character.player.create_animation(64, 34, 50, 57, False, duration=120, rows=1, cols=1)
        surface.fill((255, 255, 255))
        screen.blit(surface, (0, 0))
        cactus_obj.drawAll(screen)
        terrain_obj.drawAll(screen)
        #screen.blit(dinosour.over, (rex.player.x, 245))
        screen.blit(dinosour.character.player.update_surface(), (dinosour.character.player.x, 245))
        gui.display_game_over()
        gui.display_game_retry()

    def overRun():
        GameOver.init()
        #sound_finish.play()
        dinosour.character.player.create_animation(64, 34, 50, 57, False, duration=120, rows=1, cols=1)
        with open("scores.txt", "a") as f:
            f.write(str(game.name) + " ")
            f.write(str(GameOver.result_score) + " ")
            f.write(str(1) + "\n")
            f.close()
        #sound_finish.play()
        while True:
            clock.tick(60)
            surface.fill((255, 255, 255))
            screen.blit(surface, (0, 0))
            over = pygame.Rect(280, 20, 230, 70)
            text = pygame.Rect(170, 40, 460, 280)
            pygame.draw.rect(screen, DKGRAY, text)
            pygame.draw.rect(screen, LTGRAY, over)
            GameOver.display_result()

            #exit = pygame.Rect(640, 270, 53, 40)
            #retry = pygame.Rect(110, 260, 45, 48)
            #pygame.draw.rect(screen, LTGRAY, exit)
            #pygame.draw.rect(screen, DKGRAY, retry)

            if GameOver.result_state == True:
                textsurface_retry = gui.font.render(f'Retry', False ,(0,0,0))
                gui.screen.blit(textsurface_retry, (90, 300))
                textsurface_retry = gui.font.render(f'Home', False ,(0,0,0))
                gui.screen.blit(textsurface_retry, (640, 300))
            terrain_obj.drawAll(screen)
            #screen.blit(dinosour.over, (dinosour.character.player.x, 245))
            screen.blit(dinosour.character.player.update_surface(), (dinosour.character.player.x, 245))
            screen.blit(cactus, (rex.player.x + 550, 268))
            gui.display_game_over()
            for event in pygame.event.get():
                if(GameOver.score == GameOver.result_score):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        location = pygame.mouse.get_pos()
                        if location[0] >= 110 and location[0] <= 155 and location[1] >= 260 and location[1]<=308:
                            settings.state = "gameRun"
                            return
                        if location[0] >= 650 and location[0] <= 703 and location[1] >= 270 and location[1]<=310:
                            settings.state = "gameSetting"
                            verOrigin.GameRun.init()
                            verItem.GameRun.init()
                            return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_x:
                        settings.state = "quit"
                        return
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    def display_result():
        temp = []
        scores = []
        with open("scores.txt", "r") as f:
            text = f.read()
            temp = text.split("\n")
            del temp[len(temp) - 1]

            for i in range(len(temp)):
                temp2 = temp[i].split(" ")
                scores.append(float(temp2[1]))
            f.close()

        for i in range(len(scores) - 1):
            for j in range(len(scores) - 1 - i):
                if scores[j] < scores[j+1]:
                    scores[j], scores[j+1] = scores[j+1], scores[j]

        for i in range(len(scores)):
            if scores[i] == GameOver.result_score:
                GameOver.rank = i + 1
        
        GameOver.high = scores[0]
        
        text_rank = gui.font.render(f'Your Rank : {GameOver.rank}', False, (0, 0, 0))
        gui.screen.blit(text_rank, (290, 110))
        text_score = gui.font.render(f'Your Score : {GameOver.score}' , False, (0, 0, 0))
        gui.screen.blit(text_score, (285, 180))
        text_score = gui.font.render(f'Your Highest Score : {GameOver.high}' , False, (0, 0, 0))
        gui.screen.blit(text_score, (220, 250))
        delay(GameOver.time_delay)
        if(GameOver.score < GameOver.result_score):
            if((GameOver.result_score - GameOver.score) / 100 > 1):
                #print((GameOver.result_score - GameOver.score) / 100)
                GameOver.score += 100
            elif((GameOver.result_score - GameOver.score) / 50 > 1):
                GameOver.score += 50
            else:
                GameOver.time_delay -= int(GameOver.time_delay * 3/2)
                GameOver.score += 0.5
        if(GameOver.score == GameOver.result_score):
            GameOver.timing += 1
            if(GameOver.timing == 3):
                delay(500)
                GameOver.rank = "{}".format(GameOver.result_rank)
                sound_jump.play()
            if(GameOver.score > GameOver.high and GameOver.timing == 5):
                delay(500) 
                GameOver.high = GameOver.score   
                sound_jump.play()
            if(GameOver.timing == 7):
                delay(500)
                GameOver.result_state = True
                sound_jump.play()