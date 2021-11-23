import game
from gameover import GameOver

game_state = 0

if __name__ == '__main__':
    while game_state != -1:
        if game_state == 0:
            game_state = game.GameRun.gameRun()
        elif game_state == 1:
            game_state = GameOver.overRun()