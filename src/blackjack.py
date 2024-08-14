import time
from game import Game
from constants import *

if __name__ == '__main__':
    game = Game()
    cont = True
    while cont:
        game.deal_cards()

        game_state = game.check_blackjacks()
        if game_state != PLAYER_TURN:
            game.print_cards(True)
            print(game_state)
        else:
            player_state = game.player_action()
            if player_state == BUST:
                game.print_cards()
                print(PLAYER_BUSTED)
            else:
                dealer_state = game.dealer_action()
                time.sleep(1)
                if dealer_state == BUST:
                    game.print_cards(True)
                    print(DEALER_BUSTED)
                else:
                    game.compare_hands()
        
        game.return_discard()
        again = input("again?")
        cont = again == "y"