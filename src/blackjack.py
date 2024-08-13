from game import Game
from constants import *

if __name__ == '__main__':
    game = Game()
    game.deal_cards()
    
    game_state = game.check_blackjacks()
    if game_state != PLAYER_TURN:
        game.print_cards()
        print(game_state)
    else:
        game.player_action()
        game.dealer_action()