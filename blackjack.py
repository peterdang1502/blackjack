import random
from constants import CARD_VALUES, CARD_SUITS
from hand import Hand
from player import Player
from dealer import Dealer

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Blackjack:
    def __init__(self):
        self.deck = [Card(value, suit) for value in CARD_VALUES for suit in CARD_SUITS]
        random.shuffle(self.deck)
        self.player = Player()
        self.dealer = Dealer()
        self.hands = []
    
    def draw_card(self):
        return self.deck.pop(0)
    
    def deal(self):
        new_player_hand = Hand()
        new_dealer_hand = Hand("dealer")
        self.player.new_hand(new_player_hand)
        self.dealer.new_hand(new_dealer_hand)
        self.hands.append(new_player_hand)
        self.hands.append(new_dealer_hand)

        for i in range(2):
            new_player_hand.receive_card(self.draw_card())
            new_dealer_hand.receive_card(self.draw_card())

        self.dealer.show_hand_at_deal()
        self.player.show_hands()

        if self.hands[0].blackjack:
            if self.hands[1].blackjack:
                print("PUSH")
            else:
                print("WON")
        elif self.hands[1].blackjack:
            print("BUSTED")


if __name__ == "__main__":
    game = Blackjack()
    game.deal()