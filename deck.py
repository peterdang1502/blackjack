import random
card_numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["C", "D", "H", "S"]

class Deck:
    def __init__(self):
        self.deck = [(a + b) for a in card_numbers for b in suits] * 6
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop(0)
    
    def return_cards(self, pile):
        random.shuffle(pile)
        self.deck.extend(pile)
