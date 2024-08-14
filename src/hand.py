from constants import *

class Hand:
    def __init__(self, card = None):
        self.cards = [] if card is None else [card]
        self.blackjack = False
        self.split = False
        self.ace = False
        self.first_ace = -1
        self.hand_value = 0

    def return_num_cards(self):
        return len(self.cards)

    def receive_card(self, card):
        self.cards.append(card)
        soft = False
        if card.get_rank() == CARD_RANKS[-1] and self.ace == False:
            self.first_ace = len(self.cards) - 1
            soft = True
            self.ace = True
        
        card_value = card.get_value(soft)
        if self.hand_value + card_value > 21 and self.ace == True:
            self.hand_value -= self.cards[self.first_ace].get_value(True)
            self.hand_value += self.cards[self.first_ace].get_value(False)
        self.hand_value += card_value

        if self.hand_value > 21:
            return BUST
        if len(self.cards) == 2:
            if self.hand_value == 21:
                self.blackjack = True
            if self.cards[0].get_value() == self.cards[1].get_value():
                self.split = True
        elif len(self.cards) > 2:
            self.blackjack = False
            self.split = False
            self.ace = False
            self.first_ace = -1
        return ALIVE
    
    def is_blackjack(self):
        return self.blackjack

    def is_split(self):
        return self.split
    
    def has_ace(self):
        return self.ace
    
    def get_hand_value(self):
        return self.hand_value
    
    def remove_second_card(self):
        card = self.cards.pop(1)
        return card
    
    def reset_hand(self):
        discard = self.cards
        self.cards = []
        self.blackjack = False
        self.split = False
        self.ace = False
        self.first_ace = -1
        self.hand_value = 0
        return discard
    
    def print_cards(self, with_value = False, dealer_value = 0):
        print(self.cards)
        if with_value:
            print("Hand value: {0}, {1}".format(self.hand_value, WON if self.hand_value > dealer_value else LOST if self.hand_value < dealer_value else PUSH))

    def print_dealer_cards(self):
        print([" ", self.cards[1]])