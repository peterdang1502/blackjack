from game import Game
from constants import *

if __name__ == '__main__':
    game = Game()
    game.deal_cards()
    game.print_cards()

    game.check_blackjacks()
