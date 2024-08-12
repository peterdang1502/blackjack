from constants import *

class Hand:
    def __init__(self):
        self.cards = []
        self.blackjack = False
        self.hand_value = 0

    def receive_card(self, card):
        self.hand_value += card.value
        self.cards.append(card)
        if len(self.cards) == 2 and self.hand_value == 21:
            self.blackjack = True
    
    def is_blackjack(self):
        return self.blackjack
    
    def reset_hand(self):
        self.cards = []
        self.ace_index = -1
        self.blackjack = False
        self.hand_value = 0
    
    def print_cards(self):
        print(self.cards)

    def print_dealer_cards(self):
        print([" ", self.cards[1]])