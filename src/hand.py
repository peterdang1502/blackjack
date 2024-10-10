from __future__ import annotations
from typing import List
from card import Card
from constants import *

class Hand:
    def __init__(self, cards: List[Card] = []):
        '''Constructor for a hand of cards'''
        self.cards: List[Card] = []
        self.hand_value = 0
        self.soft_ace_index = -1
        self.can_split = False
        self.state = IN_PLAY

        if len(cards) > 0:
            for card in cards:
                self.receive_card(card)

    def get_cards(self) -> List[Card]:
        '''Return the cards in hand'''
        return self.cards

    def get_num_cards(self) -> int:
        '''Return the number of cards'''
        return len(self.cards)
    
    def get_hand_value(self) -> int:
        '''Return the total value of cards in hand'''
        return self.hand_value
    
    def has_soft_ace(self) -> bool:
        '''Return whether there's a soft ace in this hand'''
        return self.soft_ace_index != -1
    
    def get_can_split(self) -> bool:
        '''Return whether this hand can split'''
        return self.can_split
    
    def get_state(self) -> str:
        '''Return the state of this hand'''
        return self.state
    
    def set_state(self, state: str) -> None:
        '''Set the state of this hand'''
        self.state = state

    def receive_card(self, card: Card) -> None:
        '''Add a card to this hand'''
        self.cards.append(card)

        self.hand_value += card.get_value()
        if card.is_ace() and self.hand_value + 10 <= 21:
            # dealt a soft ace
            self.hand_value += 10
            self.soft_ace_index = len(self.cards) - 1;
        
        # if our total is over 21 and we have a soft ace, make it hard
        if self.hand_value > 21 and self.soft_ace_index != -1:
            self.hand_value -= 10
            self.soft_ace_index = -1

        # check hand status
        if self.hand_value > 21:
            self.can_split = False
            self.state = BUST
            return
        elif self.hand_value == 21:
            self.can_split = False
            self.state = BLACKJACK if self.get_num_cards() == 2 else STAND
            return
        elif len(self.cards) == 2 and self.cards[0].get_value() == self.cards[1].get_value():
            # can only split when there are 2 equal cards
            self.can_split = True
        else:
            self.can_split = False

        self.state = IN_PLAY
    
    def stand(self) -> None:
        self.set_state(STAND)

    def double_down(self, card: Card) -> None:
        self.receive_card(card)
        if self.get_state() == IN_PLAY:
            self.set_state(STAND)

    def reset(self) -> None:
        self.cards = []
        self.hand_value = 0
        self.soft_ace_index = -1
        self.can_split = False
        self.state = IN_PLAY

    def split(self) -> Card:
        cards = self.cards
        self.reset()
        self.receive_card(cards[0])
        return cards[1]
    
    def surrender(self) -> None:
        self.set_state(LOST)

    def is_soft_seventeen(self) -> bool:
        return self.soft_ace_index != -1 and self.hand_value == 17
    
    def print_cards(self, is_dealer: bool = False, reveal: bool = False, hand_index: int = 0):
        prefix = "Dealer: " if is_dealer else "Player hand {0}: ".format(hand_index)
        if is_dealer and not reveal:
            print(prefix + str([" ", self.cards[1]]) + " " + self.state)
        else:
            print(prefix + str(self.cards) + " " + self.state)

    def __str__(self):
        return str(self.cards)
    
    def __repr__(self):
        return str(self.cards)