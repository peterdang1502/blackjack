from game import Game
from constants import *

if __name__ == '__main__':
    game = Game()
    game.deal_cards()
    game.print_cards()

    game_state = game.check_blackjacks()
    if game_state != CONTINUE:
        print(game_state)
    else:
        action = game.print_player_prompt()

