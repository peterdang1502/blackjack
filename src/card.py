from __future__ import annotations
import random
from constants import *

class Card:
    def __init__(self, rank, suit = random.choice(CARD_SUITS)):
        self.rank = rank
        self.suit = suit
        self.ace = rank == CARD_RANKS[-1]

    def get_value(self, soft: bool = True) -> int:
        """
        Returns the value of a card.
        The soft parameter only matters if the card is an Ace
        """
        if self.rank in CARD_RANKS[:8]:
            return int(self.rank)
        elif self.rank == CARD_RANKS[-1]:
            return 11 if soft else 1
        else:
            return 10
        
    def get_rank(self):
        return self.rank

    def is_ace(self):
        return self.ace
    
    def __str__(self):
        return "% s of % s" % (self.rank, self.suit)
    
    def __repr__(self):
        return "% s of % s" % (self.rank, self.suit)
    
    def __eq__(self, other: Card):
        return self.get_rank() == other.get_rank()