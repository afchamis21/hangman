from GameController import GameController
from Hangman import Hangman

if __name__ == '__main__':
    gameController = GameController(Hangman())
    gameController.start()
