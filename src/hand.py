from constants import *

class Hand:
    def __init__(self, card = None):
        self.cards = [] if card is None else [card]
        self.blackjack = False
        self.split = False
        self.hand_value = 0

    def receive_card(self, card, soft = True):
        self.hand_value += card.get_value(soft)
        if self.hand_value > 21:
            return BUST
        self.cards.append(card)
        if len(self.cards) == 2:
            if self.hand_value == 21:
                self.blackjack = True
            if self.cards[0].get_value() == self.cards[1].get_value():
                self.split = True
        else:
            self.blackjack = False
            self.split = False
        return ALIVE
    
    def is_blackjack(self):
        return self.blackjack

    def is_split(self):
        return self.split
    
    def remove_second_card(self):
        card = self.cards.pop(1)
        return card
    
    def reset_hand(self):
        self.cards = []
        self.blackjack = False
        self.split = False
        self.hand_value = 0
    
    def print_cards(self):
        print(self.cards)

    def print_dealer_cards(self):
        print([" ", self.cards[1]])