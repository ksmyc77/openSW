import pygame
import game
import gameover
with open("scores.txt", "a") as f:
    f.close
if __name__ == '__main__':
    state = "main"
    while state != "quit":
        if(state == "main"):
            state = game.MainMenu.mainMenu()
        if(state == "ranking"):
            state = game.Ranking.ranking()
        if(state == "input"):
            state = game.inputName.inputing()
        if(state == "gameover"):
            state = gameover.GameOver.overRun()
        if(state == "gamerun"):
            state = game.GameRun.gameRun()