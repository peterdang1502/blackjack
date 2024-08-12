from hand import Hand
from constants import *

class Player:
    def __init__(self):
        hand = Hand()
        self.hands = [hand]
        self.hand_index = 0

    def receive_card(self, card):
        self.hands[self.hand_index].receive_card(card)

    def is_blackjack(self):
        return self.hands[self.hand_index].is_blackjack()
    
    def is_split(self):
        return self.hands[self.hand_index].is_split()
    
    def print_cards(self):
        for h in self.hands:
            h.print_cards()