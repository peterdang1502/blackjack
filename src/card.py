from constants import *

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.ace = number == CARD_NUMBERS[-1]
        self.calculate_value()

    def calculate_value(self):
        if self.number in CARD_NUMBERS[:8]:
            self.value = int(self.number)
        elif self.number == CARD_NUMBERS[-1]:
            self.value = 1
        else:
            self.value = 10

    def is_ace(self):
        return self.ace
    
    def __str__(self):
        return "% s of % s" % (self.number, self.suit)
    
    def __repr__(self):
        return "% s of % s" % (self.number, self.suit)