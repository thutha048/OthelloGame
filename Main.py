from Controller import Controller
from RandomTest import RandomTest
from GameFrame import GameFrame


if __name__ == '__main__':
    controller = Controller()
    game = GameFrame("title" ,controller.click, controller.restart_game, controller.start_game)
    controller.game = game
    game.start()
pass
