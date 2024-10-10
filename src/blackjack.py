from game import Game
from constants import *

if __name__ == '__main__':
    game = Game()
    while True:
        game.deal_cards()
        game_state = game.get_state()
        if game_state == DEALER_BLACKJACK or game_state == PLAYER_BLACKJACK:
            game.print_cards(True)
        else:
            game.player_action()
            game_state = game.get_state()
            if game_state == PLAYER_BUSTED:
                game.player_bust()
            else:
                game.dealer_action()
                print("\n")
                game_state = game.get_state()
                if game_state == DEALER_BUSTED:
                    game.dealer_bust()
                else:
                    game.compare_hands()
        
        game.return_discard()
        print("\n")
