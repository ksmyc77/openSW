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
    result_rank = 0
    high = 0
    time_delay = 50
    result_state = False

    def init():
        GameOver.score = 0
        GameOver.rank = "???"
        GameOver.timing = 0
        GameOver.time_delay = 50
        GameOver.result_state = False

    def saveScore(score):
        GameOver.result_score = score

    def over():
        surface.fill((255, 255, 255))
        screen.blit(surface, (0, 0))
        cactus_obj.drawAll(screen)
        terrain_obj.drawAll(screen)
        bird_obj.drawAll(screen)
        screen.blit(dinosour.character.player.update_surface(), (dinosour.character.player.x, dinosour.character.player.early_Y))
        gui.display_game_over()
        gui.display_game_retry()

    def overRun():
        GameOver.init()
        #sound_finish.play()
        dinosour.setDeath()
        GameOver.store_result()
        GameOver.calculate_result()
        while True:
            clock.tick(60)
            surface.fill((255, 255, 255))
            screen.blit(surface, (0, 0))
            over = pygame.Rect(280, 20, 230, 70)
            text = pygame.Rect(170, 40, 460, 280)
            pygame.draw.rect(screen, DKGRAY, text)
            pygame.draw.rect(screen, LTGRAY, over)
            GameOver.display_result()

            if GameOver.result_state == True:
                textsurface_retry = gui.font.render(f'Retry', False ,(0,0,0))
                gui.screen.blit(textsurface_retry, (90, 300))
                textsurface_retry = gui.font.render(f'Home', False ,(0,0,0))
                gui.screen.blit(textsurface_retry, (640, 300))
            terrain_obj.drawAll(screen)
            #screen.blit(dinosour.over, (dinosour.character.player.x, 245))
            screen.blit(dinosour.character.player.update_surface(), (dinosour.character.player.x, dinosour.character.player.early_Y))
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

    def store_result():
        context = ""
        context_r = ""
        with open(settings.game_mode + "Scores.txt", "r") as f:
            text = f.read().split("\n")
            del text[len(text) - 1]

            con = ""
            same = False
            for i in range(len(text)):
                print(text[i])
                text1 = text[i].split(" ")
                if(game.element.name == text1[0]):
                    con = game.element.name + " " + str(GameOver.result_score) + " " + str(1) + " " + dinosour.dino + "\n" 
                    same = True
                else:
                    con = text[i] + "\n"
                context += con
            f.close()
        if same == False:
            con = game.element.name + " " + str(GameOver.result_score) + " " + str(1) + " " + dinosour.dino + "\n" 
            context += con
        
        with open("record.txt", "r") as f:
            text = f.read().split("\n")
            del text[len(text) - 1]

            con = ""
            same_r = False
            for i in range(len(text)):
                print(text[i])
                text1 = text[i].split(" ")
                if(game.element.name == text1[0]):
                    con = game.element.name + " " + dinosour.dino + "\n" 
                    same_r = True
                else:
                    con = text[i] + "\n"
                context_r += con
            f.close()
        if same_r == False:
            con = game.element.name + " " + dinosour.dino + "\n" 
            context_r += con

        with open("record.txt", "w") as f:
            f.write(context_r)
            f.close()

        with open(settings.game_mode + "Scores.txt", "w") as f:
            f.write(context)
            f.close()


    def calculate_result():
        temp = []
        scores = []
        with open(settings.game_mode + "Scores.txt", "r") as f:
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
                GameOver.result_rank = i + 1

        if(GameOver.score != GameOver.result_score):
            if(scores[0] != GameOver.result_score):
                GameOver.high = scores[0]
            else:
                if(len(scores) > 1):
                    GameOver.high = scores[1]
                else:
                    GameOver.high = 0

    def display_result():       
        text_rank = gui.font.render(f'Your Rank : {GameOver.rank}', False, (0, 0, 0))
        gui.screen.blit(text_rank, (290, 110))
        text_score = gui.font.render(f'Your Score : {GameOver.score}' , False, (0, 0, 0))
        gui.screen.blit(text_score, (285, 180))
        text_score = gui.font.render(f'Your Highest Score : {GameOver.high}' , False, (0, 0, 0))
        gui.screen.blit(text_score, (220, 250))
        delay(GameOver.time_delay)
        if(GameOver.score < GameOver.result_score):
            if((GameOver.result_score - GameOver.score) / 100 > 1):
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
                GameOver.high = GameOver.result_score   
                sound_jump.play()
            if(GameOver.timing == 7):
                delay(500)
                GameOver.result_state = True
                sound_jump.play()