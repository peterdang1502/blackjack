from __future__ import annotations
from typing import List
from card import Card
from constants import *

class Hand:
    def __init__(self, cards: List[Card] = []):
        self.cards: List[Card] = []
        self.hand_value = 0
        self.ace = False
        self.soft_ace_index = -1
        self.can_split = False
        self.state = IN_PLAY
        if len(cards) > 0:
            self.receive_cards(cards)

    def return_num_cards(self):
        return len(self.cards)

    def receive_card(self, card: Card) -> None:
        self.cards.append(card)

        card_value = card.get_value()
        # if card is an ace and there exists an ace already, the new ace value is automatically hard, otherwise its value stays soft and record its index
        if card.is_ace():
            if self.ace:
                card_value = card.get_value(False)
            else:
                self.ace = True
                self.soft_ace_index = self.cards.index(card)

        self.hand_value += card_value
        # if new hand value over 21, check if there are any soft aces (including the card just received) and turn it hard
        if self.hand_value > 21 and self.soft_ace_index != - 1:
            self.hand_value -= self.cards[self.soft_ace_index].get_value()
            self.hand_value += self.cards[self.soft_ace_index].get_value(False)
            self.soft_ace_index = -1

        # check hand status
        if self.hand_value > 21:
            self.state = BUST
            return
        
        if len(self.cards) == 2:
            if self.hand_value == 21:
                self.state = BLACKJACK
                return
            if self.cards[0].get_value() == self.cards[1].get_value():
                self.can_split = True
        elif len(self.cards) > 2:
            self.can_split = False

        self.state = IN_PLAY

    def receive_cards(self, cards: List[Card]) -> None:
        for card in cards:
            self.receive_card(card)

    def get_cards(self) -> List[Card]:
        return self.cards
    
    def get_hand_value(self) -> int:
        return self.hand_value
    
    def has_soft_ace(self):
        return self.soft_ace_index != -1
    
    def get_can_split(self) -> bool:
        return self.can_split
    
    def get_state(self) -> str:
        return self.state
    
    def set_state(self, state: str) -> None:
        self.state = state
    
    def stand(self) -> None:
        self.state = STAND

    def double_down(self, card: Card) -> None:
        self.receive_card(card)
        if self.state == IN_PLAY:
            self.state = STAND

    def split(self) -> Card:
        card = self.cards.pop(1)
        # when splitting a pair of aces and removing the second one, it's always gonna be hard ace
        self.hand_value -= card.get_value(False)
        self.can_split = False
        return card
    
    def surrender(self) -> None:
        self.state = LOST

    def is_soft_seventeen(self) -> bool:
        return len(self.cards) == 2 and self.ace and self.hand_value == 17
    
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
    
    def __eq__(self, other: Hand):
        other_cards = other.get_cards()
        same = True
        for i in range(len(self.cards)):
            if self.cards[i] != other_cards[i]:
                same = False
        return same