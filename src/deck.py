import random
from constants import *
from card import Card

class Deck:
    def __init__(self):
        self.deck = [Card(a, b) for a in CARD_RANKS for b in CARD_SUITS] * NUM_OF_DECKS
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop(0)
    
    def return_cards(self, pile):
        self.deck.extend(pile)
        self.shuffle()
