import random
from typing import List
from constants import *
from card import Card

class Deck:
    def __init__(self) -> None:
        '''Deck constructor'''
        self.deck = [Card(a, b) for a in CARD_RANKS for b in CARD_SUITS] * NUM_OF_DECKS
        self.shuffle()

    def shuffle(self) -> None:
        '''Shuffle the deck'''
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        '''Draw a card'''
        return self.deck.pop(0)
    
    def return_cards(self, pile: List[Card]) -> None:
        '''Return a pile of discards to the deck and shuffle'''
        self.deck.extend(pile)
        self.shuffle()
