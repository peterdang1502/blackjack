import time
from deck import Deck
from player import Player
from dealer import Dealer
from constants import *

class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.split = False

    def deal_cards(self):
        for i in range(2):
            self.deal_card_to_player(self.deck.draw_card())
            self.deal_card_to_dealer(self.deck.draw_card())

        if self.player.is_split():
            self.split = True

    def return_discard(self):
        discard = self.player.reset_hands() + self.dealer.reset_hands()
        self.deck.return_cards(discard)

    def deal_card_to_player(self, card):
        return self.player.receive_card(card)
    
    def deal_card_to_dealer(self, card):
        return self.dealer.receive_card(card)

    def check_blackjacks(self):
        dealer_blackjack = self.dealer.is_blackjack()
        player_blackjack = self.player.is_blackjack()

        if dealer_blackjack and player_blackjack:
            return PUSH
        elif dealer_blackjack:
            return LOST
        elif player_blackjack:
            return WON
        else:
            return PLAYER_TURN
        
    def player_action(self):
        while self.player.is_alive():
            self.print_cards()
            action = self.player.action()
            if action == STAND:
                self.player.stand()
            elif action == HIT:
                curr_hand_state = self.deal_card_to_player(self.deck.draw_card())
                if curr_hand_state == BUST:
                    return BUST
            elif action == DOUBLE_DOWN:
                curr_hand_state = self.deal_card_to_player(self.deck.draw_card())
                if curr_hand_state == BUST:
                    return BUST
                else:
                    self.player.stand()
            elif action == SPLIT:
                two_new_cards = [self.deck.draw_card(), self.deck.draw_card()]
                self.player.split(two_new_cards)
            else:
                self.player.surrender()
        return ALIVE

    def dealer_action(self):
        while self.dealer.is_alive():
            time.sleep(1)
            action = self.dealer.action()
            self.print_cards(True)
            if action == STAND:
                self.dealer.stand()
            else:
                curr_hand_state = self.deal_card_to_dealer(self.deck.draw_card())
                if curr_hand_state == BUST:
                    return BUST
        return ALIVE
    
    def compare_hands(self):
        print("COMPARING HANDS")
        self.dealer.print_final_hand()
        dealer_hand_value = self.dealer.get_hand_value()
        self.player.print_final_hand(dealer_hand_value)

        
    def print_cards(self, reveal = False):
        self.dealer.print_cards(reveal)
        self.player.print_cards()