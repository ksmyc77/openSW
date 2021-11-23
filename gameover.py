from pygame.time import delay
from settings import *
import sys
import game

class GameOver:
    score = 0
    result_score = 0 
    rank = '???'
    timing = 0

    #temporary
    result_rank = 32
    high = 300
    time_delay = 10

    def saveScore(score):
        GameOver.result_score = score
        print(GameOver.result_score)

    def over(gui):
        surface.fill((255, 255, 255))
        screen.blit(surface, (0, 0))
        cactus_obj.drawAll(screen)
        terrain_obj.drawAll(screen)
        screen.blit(rex_over, (rex.player.x, 245))
        gui.display_game_over()
        gui.display_game_retry()

    def overRun():
        GameOver.score = 0
        #sound_finish.play()
        while True:
            surface.fill((255, 255, 255))
            screen.blit(surface, (0, 0))
            over = pygame.Rect(280, 20, 230, 70)
            text = pygame.Rect(160, 40, 460, 300)
            pygame.draw.rect(screen, DKGRAY, text)
            pygame.draw.rect(screen, LTGRAY, over)
            GameOver.display_result(gui)
            terrain_obj.drawAll(screen)
            screen.blit(rex_over, (rex.player.x, 245))
            screen.blit(cactus, (rex.player.x + 525, 268))
            gui.display_game_over()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return -1
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
                            
    def display_result(gui):
        text_rank = gui.font.render(f'Your Rank : {GameOver.rank}', False, (0, 0, 0))
        gui.screen.blit(text_rank, (280, 110))
        text_score = gui.font.render(f'Your Score : {GameOver.score}' , False, (0, 0, 0))
        gui.screen.blit(text_score, (265, 180))
        text_score = gui.font.render(f'Your Highest Score : {GameOver.high}' , False, (0, 0, 0))
        gui.screen.blit(text_score, (220, 250))
        delay(GameOver.time_delay)
        if(GameOver.score < GameOver.result_score):
            GameOver.time_delay -= int(GameOver.time_delay * 2/5)
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
                