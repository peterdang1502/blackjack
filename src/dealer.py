from player import Player
from constants import *

class Dealer(Player):
    def print_cards(self, reveal = False):
        if reveal:
            self.hands[0].print_cards()
        else:
            self.hands[0].print_dealer_cards()

    def is_soft_seventeen(self):
        hand = self.hands[self.hand_index]
        return hand.return_num_cards() == 2 and hand.has_ace() and hand.get_hand_value() == 17

    def action(self):
        print("Dealer action.")
        hand_value = self.hands[self.hand_index].get_hand_value()
        if hand_value <= 16 or self.is_soft_seventeen():
            return HIT
        return STAND
    
    def get_hand_value(self):
        return self.hands[self.hand_index - 1].get_hand_value()
    
    def print_final_hand(self):
        hand = self.hands[self.hand_index - 1]
        hand.print_cards(True)
            