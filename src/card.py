from constants import *

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.ace = rank == CARD_RANKS[-1]
        self.calculate_value()

    def calculate_value(self):
        if self.rank in CARD_RANKS[:8]:
            self.value = int(self.rank)
        elif self.rank == CARD_RANKS[-1]:
            self.value = 11
        else:
            self.value = 10

    def is_ace(self):
        return self.ace
    
    def __str__(self):
        return "% s of % s" % (self.rank, self.suit)
    
    def __repr__(self):
        return "% s of % s" % (self.rank, self.suit)