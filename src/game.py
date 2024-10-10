import time
from typing import List
from deck import Deck
from hand import Hand
from player import Player
from dealer import Dealer
from constants import *

class Game:
    def __init__(self) -> None:
        '''Constructor for a game of Blackjack'''
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.game_state = IN_PLAY

        # array of hands starting with the dealer hand
        self.hands = [Hand(), Hand()]

    def get_state(self) -> str:
        '''Get the game state'''
        return self.game_state
    
    def set_state(self, state: str) -> None:
        '''Set the game state'''
        self.game_state = state 

    def deal_cards(self) -> None:
        '''Deal 2 cards each in order of player hands first, then dealer'''
        for i in range(2):
            for hand in reversed(self.hands):
                hand.receive_card(self.deck.draw_card())

        # check for any blackjacks after dealing
        self.check_blackjacks()

    def check_blackjacks(self) -> None:
        '''Check for dealer blackjack and player blackjacks'''
        dealer_state = self.hands[0].get_state()
        if dealer_state == BLACKJACK:
            self.set_state(DEALER_BLACKJACK)
            for hand in self.hands[1:]:
                if hand.get_state() != BLACKJACK:
                    hand.set_state(LOST)
                else:
                    hand.set_state(PUSH)
        else:
            # dealer didn't get blackjack
            for hand in self.hands[1:]:
                if hand.get_state() != BLACKJACK:
                    # if there's a playable player hand
                    self.set_state(IN_PLAY)
                    return
            # player got all blackjacks
            self.hands[0].set_state(LOST)
            for hand in self.hands[1:]:
                hand.set_state(WON)
            self.set_state(PLAYER_BLACKJACK)
        
    def player_action(self, action = "") -> None:
        '''Player action'''
        # this first if part is for the machine learning only
        if action != "":
            hand: Hand = self.hands[1]
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
            # for every hand player has, can add more hands in an iteration if player splits
            while i < len(self.hands):
                hand = self.hands[i]
                while hand.get_state() not in [BLACKJACK, BUST, STAND, LOST]:
                    self.print_cards()
                    action = self.player.action(hand.get_can_split(), hand.get_num_cards() == 2)
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
                        new_hand.receive_card(second_card)
                        new_hand.receive_card(self.deck.draw_card())
                    else:
                        hand.surrender()
                i += 1
                        
        for hand in self.hands[1:]:
            if hand.get_state() == STAND or hand.get_state() == BLACKJACK:
                # if there's a comparable player hand
                self.set_state(IN_PLAY)
                return
        
        # all hands are busted or surrendered
        self.set_state(PLAYER_BUSTED)

    def dealer_action(self, learn = False) -> None:
        '''Dealer action'''
        hand = self.hands[0]
        if not learn: self.print_cards(True)  # reveal card
        while hand.get_state() not in [BUST, STAND]:
            if not learn: time.sleep(1)
            action = self.dealer.action(hand.get_hand_value(), hand.is_soft_seventeen(), learn)
            if action == STAND:
                hand.stand()
            else:
                hand.receive_card(self.deck.draw_card())
            if not learn: self.print_cards(True)

        # only two possible states after while loop
        self.set_state(STAND if hand.get_state() == STAND else DEALER_BUSTED)
    
    def player_bust(self) -> None:
        '''Player busted, dealer won and reveal their card'''
        self.hands[0].set_state(WON)
        self.print_cards(True)

    def dealer_bust(self) -> None:
        '''Dealer busted, if a player hand is not busted then they won'''
        time.sleep(1)
        for hand in self.hands[1:]:
            hand.set_state(WON if hand.get_state() in [BLACKJACK, STAND] else LOST)
        self.print_cards(True)

    def compare_hands(self, learn = False) -> None:
        '''Neither dealer busted or player busted all of their hands, so compare hand values with hands that haven't lost or won'''
        if not learn: time.sleep(1)
        for hand in self.hands[1:]:
            hand_state = hand.get_state()
            if hand_state in [BUST, SURRENDER]:
                hand.set_state(LOST)
            elif hand_state == BLACKJACK:
                hand.set_state(WON)
            else:
                dealer_hand_value = self.hands[0].get_hand_value()
                hand_value = hand.get_hand_value()
                hand.set_state(WON if hand_value > dealer_hand_value else PUSH if hand_value == dealer_hand_value else LOST)
        if not learn: self.print_cards(True)

    def return_discard(self) -> None:
        '''Return the discarded cards to deck and reset the game to just dealer hand and one player hand'''
        discard = []
        for hand in self.hands:
            discard.extend(hand.get_cards())
        self.deck.return_cards(discard)
        self.set_state(IN_PLAY)
        self.hands = self.hands[:2]
        for hand in self.hands:
            hand.reset()
        
    def print_cards(self, reveal = False):
        self.hands[0].print_cards(True, reveal)
        for i in range(1, len(self.hands)):
            self.hands[i].print_cards(False, False, i)

    # for ml
    def get_player_hand(self, index) -> Hand:
        return self.hands[index]