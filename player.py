from constants import CARD_VALUES, CARD_SUITS
from hand import Hand
import re

class Player:
    def __init__(self, name="Player", balance=100):
        self.name = name
        self.hands = []
        self.balance = balance

    def new_hand(self, hand):
        self.hands.append(hand)

    def show_hands(self):
        print(self.name + " hands: ")
        for hand in self.hands:
            print("Hand 1:")
            hand.show_hand()