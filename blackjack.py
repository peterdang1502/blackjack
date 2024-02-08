import random
from player import Player
from dealer import Dealer
from game import Game
from constants import CARD_VALUES, CARD_SUITS

def play():
    game = Game()
    player = Player()
    dealer = Dealer()
    game.add_players([player, dealer])
    game.deal()
    game.blackjack_check()
    
    if player.blackjack():
        if dealer.blackjack():
            print("push")
        else:
            print("blackjack")
    elif dealer.blackjack():
        print("lost")
    else:
        player.show_hand()
        dealer.show_hand_at_deal()

if __name__ == "__main__":
    play()