from game import Game
from constants import *

if __name__ == '__main__':
    game = Game()
    cont = True
    while cont:
        game_state = game.deal_cards()
        if game_state == DEALER_BLACKJACK or game_state == PLAYER_BLACKJACK:
            game.print_cards(True)
        else:
            player_hand_states = game.player_action()
            dealer_hand_state = game.dealer_action()
            if dealer_hand_state == BUST:
                game.dealer_bust()
            else:
                game.compare_hands()
        
        game.return_discard()
        again = input("again?")
        cont = again == "y"