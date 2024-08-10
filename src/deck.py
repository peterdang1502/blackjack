import random
from constants import *
from card import Card

class Deck:
    def __init__(self):
        self.deck = [Card(a, b) for a in CARD_NUMBERS for b in CARD_SUITS] * 6
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop(0)
    
    def return_cards(self, pile):
        random.shuffle(pile)
        self.deck.extend(pile)
