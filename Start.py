from Controller import Controller
from GameFrame import GameFrame

# Set up a controller object, and give it access to the graphical representation of the board
# Board is passed the click and startnewgame functions from the controller so that controller
# can decide what happens when buttons are clicked

if __name__ == '__main__':
    controller = Controller()
    game = GameFrame("title" ,controller.click, controller.restart_game, controller.start_game)
    controller.game = game
    game.start()
pass