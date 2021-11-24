import game
import gameover

if __name__ == '__main__':
    state = "gamerun"
    while state != "quit":
        if(state == "gamerun"):
            state = game.GameRun.gameRun()
        if(state == "gameover"):
            state = gameover.GameOver.overRun()