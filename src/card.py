from __future__ import annotations
import random
from constants import *

class Card:
    def __init__(self, rank, suit = random.choice(CARD_SUITS)):
        '''Constructor for a card'''
        self.rank = rank
        self.suit = suit

        if self.rank in CARD_RANKS[:8]:  # number card
            self.value = int(self.rank)
        elif self.rank == CARD_RANKS[-1]:  # ace
            self.value = 1
        else:  # face card
            self.value = 10

    def get_value(self) -> int:
        '''Get a card's value'''
        return self.value
        
    def get_rank(self):
        '''Get a card's rank'''
        return self.rank

    def is_ace(self):
        '''Return whether a card is an ace or not'''
        return self.rank == CARD_RANKS[-1]
    
    def __str__(self):
        return "% s of % s" % (self.rank, self.suit)
    
    def __repr__(self):
        return "% s of % s" % (self.rank, self.suit)
    
    def __eq__(self, other: Card):
        return self.get_rank() == other.get_rank()