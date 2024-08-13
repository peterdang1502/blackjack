from constants import *

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.ace = rank == CARD_RANKS[-1]

    def get_value(self, soft = True):
        if self.rank in CARD_RANKS[:8]:
            return int(self.rank)
        elif self.rank == CARD_RANKS[-1]:
            return 11 if soft else 1
        else:
            return 10

    def is_ace(self):
        return self.ace
    
    def __str__(self):
        return "% s of % s" % (self.rank, self.suit)
    
    def __repr__(self):
        return "% s of % s" % (self.rank, self.suit)