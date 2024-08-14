from hand import Hand
from constants import *

class Player:
    def __init__(self):
        self.hands = [Hand()]
        self.hand_index = 0

    def receive_card(self, card):
        curr_hand_state = self.hands[self.hand_index].receive_card(card)
        if curr_hand_state == BUST:
            self.hand_index += 1
            return BUST
        return ALIVE

    def is_blackjack(self):
        return self.hands[self.hand_index].is_blackjack()
    
    def is_split(self):
        return self.hands[self.hand_index].is_split()
    
    def is_alive(self):
        return self.hand_index < len(self.hands)
    
    def action(self):
        split = " split," if self.hands[self.hand_index].is_split() else ""
        print("Possible actions: stand, hit, double down," + split + " surrender")
        print("Player action?")
        return input()
    
    def stand(self):
        self.hand_index += 1

    def split(self, new_cards):
        second_card = self.hands[self.hand_index].remove_second_card()
        new_hand = Hand(second_card)
        self.hands.append(new_hand)
        curr_index = self.hand_index
        for i in range(2):
            self.hand_index += i
            self.receive_card(new_cards[i])
        self.hand_index = curr_index

    def surrender(self):
        self.hand_index += 1

    def reset_hands(self):
        discard = []
        for h in self.hands:
            discard.extend(h.reset_hand())
        self.hands = [Hand()]
        self.hand_index = 0
        return discard
    
    def print_cards(self):
        for h in self.hands:
            h.print_cards()

    def print_final_hand(self, dealer_value):
        for h in self.hands:
            h.print_cards(True, dealer_value)