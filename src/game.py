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
            self.hands.append(self.make_hand())

    def make_hand(self) -> Hand:
        return Hand()

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

    def return_discard(self):
        discard = self.player.reset_hands() + self.dealer.reset_hands()
        self.deck.return_cards(discard)

    def deal_card_to_player(self, card):
        return self.player.receive_card(card)
    
    def deal_card_to_dealer(self, card):
        return self.dealer.receive_card(card)
        
    def player_action(self) -> List[str]:
        hand_states = []
        i = 1
        while i < len(self.hands):
            hand: Hand = self.hands[i]
            while hand.get_state() not in [BLACKJACK, BUST, STAND, SURRENDER]:
                self.print_cards(False)
                action = self.player.action(hand.get_can_split(), hand.return_num_cards() == 2)
                if action == STAND:
                    hand.stand()
                elif action == HIT:
                    hand.receive_card(self.deck.draw_card())
                elif action == DOUBLE_DOWN:
                    hand.double_down(self.deck.draw_card())
                elif action == SPLIT:
                    new_hand = self.make_hand()
                    self.hands.append(new_hand)
                    second_card = hand.split()
                    hand.receive_card(self.deck.draw_card())
                    new_hand.receive_cards([second_card, self.deck.draw_card()])
                else:
                    hand.surrender()
            hand_states.append(hand.get_state())
            i += 1
        return hand_states

    def dealer_action(self) -> str:
        hand: Hand = self.hands[0]
        while hand.get_state() not in [BUST, STAND]:
            action = self.dealer.action(hand.get_hand_value(), hand.is_soft_seventeen())
            if action == STAND:
                hand.stand()
            else:
                hand.receive_card(self.deck.draw_card())
            self.print_cards(True)
            time.sleep(1)
        return hand.get_state()

    def dealer_bust(self) -> None:
        hand: Hand
        for hand in self.hands[1:]:
            hand.set_state(WON if hand.get_state() in [BLACKJACK, STAND] else LOST)
        self.print_cards(True)

    def compare_hands(self) -> None:
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
            discard.extend(hand.remove_cards())
        self.deck.return_cards(discard)
        self.hands = []
        self.make_default_hands()
        
    def print_cards(self, reveal = False):
        self.hands[0].print_cards(True, reveal)
        for i in range(1, len(self.hands)):
            self.hands[i].print_cards(False, False, i)

