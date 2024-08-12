from deck import Deck
from player import Player
from dealer import Dealer
from constants import *

class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.split = False

    def deal_cards(self):
        for i in range(2):
            self.deal_card_to_player(self.deck.draw_card())
            self.deal_card_to_dealer(self.deck.draw_card())

        if self.player.is_split():
            self.split = True

    def deal_card_to_player(self, card):
        self.player.receive_card(card)
    
    def deal_card_to_dealer(self, card):
        self.dealer.receive_card(card)

    def check_blackjacks(self):
        dealer_blackjack = self.dealer.is_blackjack()
        player_blackjack = self.player.is_blackjack()

        if dealer_blackjack and player_blackjack:
            return PUSH
        elif dealer_blackjack:
            return LOST
        elif player_blackjack:
            return WON
        else:
            return CONTINUE
        
    def print_player_prompt(self):
        split = " split," if self.split else ""
        print("Possible actions: stand, hit, double down," + split + " surrender")
        print("Player action?")
        return input()
        
    def print_cards(self):
        self.dealer.print_cards()
        self.player.print_cards()