import time
from typing import List
from deck import Deck
from hand import Hand
from player import Player
from dealer import Dealer
from constants import *

class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()

        # an array of hand, starting with the dealer hand
        # in case the player splits, more hands get added on
        self.hands = []
        self.make_default_hands()

    def make_default_hands(self) -> None:
        for i in range(2):
            self.hands.append(Hand())

    def deal_cards(self) -> str:
        # deal 2 cards each in order of player hands first, then dealer
        for i in range(2):
            hand: Hand
            for hand in reversed(self.hands):
                hand.receive_card(self.deck.draw_card())

        return self.check_blackjacks()

    def check_blackjacks(self) -> str:
        dealer_hand: Hand = self.hands[0]
        dealer_state = dealer_hand.get_state()
        if dealer_state == BLACKJACK:
            hand: Hand
            for hand in self.hands[1:]:
                if hand.get_state() != BLACKJACK:
                    hand.set_state(LOST)
                else:
                    hand.set_state(PUSH)
            return DEALER_BLACKJACK
        else:
            hand: Hand
            for hand in self.hands[1:]:
                if hand.get_state() != BLACKJACK:
                    return IN_PLAY
            dealer_hand.set_state(LOST)
            for hand in self.hands[1:]:
                hand.set_state(WON)
            return PLAYER_BLACKJACK
        
    def player_action(self, action = "") -> List[str]:
        hand_states = []
        hand: Hand = self.hands[1]

        # this first if part is for the machine learning only
        if action != "":
            if action == STAND:
                hand.stand()
            elif action == HIT:
                hand.receive_card(self.deck.draw_card())
            elif action == DOUBLE_DOWN:
                hand.double_down(self.deck.draw_card())
            elif action == SPLIT:
                # new_hand = Hand()
                # self.hands.append(new_hand)
                second_card = hand.split()
                self.deck.return_cards([second_card])
                hand.receive_card(self.deck.draw_card())
                # new_hand.receive_cards([second_card, self.deck.draw_card()])
            else:
                hand.surrender()
        # this second part is for player gameplay
        else:
            i = 1
            while i < len(self.hands):
                hand: Hand = self.hands[i]
                while hand.get_state() not in [BLACKJACK, BUST, STAND, LOST]:
                    action = self.player.action(hand.get_can_split(), hand.return_num_cards() == 2)
                    if action == STAND:
                        hand.stand()
                    elif action == HIT:
                        hand.receive_card(self.deck.draw_card())
                    elif action == DOUBLE_DOWN:
                        hand.double_down(self.deck.draw_card())
                    elif action == SPLIT:
                        new_hand = Hand()
                        self.hands.append(new_hand)
                        second_card = hand.split()
                        hand.receive_card(self.deck.draw_card())
                        new_hand.receive_cards([second_card, self.deck.draw_card()])
                    else:
                        hand.surrender()
                i += 1
                        
        hand_states.append(hand.get_state())
        return hand_states

    def dealer_action(self) -> str:
        hand: Hand = self.hands[0]
        self.print_cards(True)
        while hand.get_state() not in [BUST, STAND]:
            time.sleep(1)
            action = self.dealer.action(hand.get_hand_value(), hand.is_soft_seventeen())
            if action == STAND:
                hand.stand()
            else:
                hand.receive_card(self.deck.draw_card())
            self.print_cards(True)
        return hand.get_state()
    
    def player_bust(self) -> None:
        self.hands[0].set_state(WON)
        self.print_cards(True)

    def dealer_bust(self) -> None:
        time.sleep(1)
        hand: Hand
        for hand in self.hands[1:]:
            hand.set_state(WON if hand.get_state() in [BLACKJACK, STAND] else LOST)
        self.print_cards(True)

    def compare_hands(self) -> None:
        time.sleep(1)
        dealer_hand_value = self.hands[0].get_hand_value()
        hand: Hand
        for hand in self.hands[1:]:
            hand_state = hand.get_state()
            if hand_state in [BUST, SURRENDER]:
                hand.set_state(LOST)
            elif hand_state == BLACKJACK:
                hand.set_state(WON)
            else:
                hand_value = hand.get_hand_value()
                hand.set_state(WON if hand_value > dealer_hand_value else PUSH if hand_value == dealer_hand_value else LOST)
        self.print_cards(True)

    def return_discard(self) -> None:
        discard = []
        hand: Hand
        for hand in self.hands:
            discard.extend(hand.get_cards())
        self.deck.return_cards(discard)
        self.hands = []
        self.make_default_hands()
        
    def print_cards(self, reveal = False):
        self.hands[0].print_cards(True, reveal)
        for i in range(1, len(self.hands)):
            self.hands[i].print_cards(False, False, i)

    # for ml
    def get_player_hand(self, index) -> Hand:
        return self.hands[index]