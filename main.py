import verOrigin
import gameover
import verItem
import setGame
import settings
import loading

if __name__ == '__main__':
    settings.state = "gameSetting"
    ver = "origin"
    while settings.state != "quit":
        if(settings.state == "gameSetting"):
            setGame.SetGame.gameSet()
        if(settings.state == "gameRun"):
            if(ver == "origin"):
                verOrigin.GameRun.gameRun()
            if(ver == "item"):
                verItem.GameRun.gameRun()
        if(settings.state == "gameover"):
            gameover.GameOver.overRun()
        if(settings.state == "loading"):
            loading.Loading.loadingGame()