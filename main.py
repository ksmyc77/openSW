import verOrigin
import gameover
import verItem
import setGame
import settings
import loading

if __name__ == '__main__':
    settings.state = "gameSetting"
    settings.game_mode = "origin"
    while settings.state != "quit":
        if(settings.state == "gameSetting"):
            print("state : set")
            setGame.SetGame.gameSet()
        if(settings.state == "gameRun"):
            print("state : run")
            if(settings.game_mode == "origin"):
                verOrigin.GameRun.gameRun()
            if(settings.game_mode == "item"):
                verItem.GameRun.gameRun()
        if(settings.state == "gameover"):
            print("state : over")
            gameover.GameOver.overRun()
        if(settings.state == "loading"):
            print("state : loading")
            loading.Loading.loadingGame()