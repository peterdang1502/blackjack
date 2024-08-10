from deck import Deck
from player import Player
from dealer import Dealer
from constants import *

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def deal_cards(self):
        for i in range(2):
            self.deal_card_to_player(self.deck.draw_card())
            self.deal_card_to_dealer(self.deck.draw_card())

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