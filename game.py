import random
from constants import CARD_VALUES, CARD_SUITS

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Game:
    def __init__(self):
        self.deck = [Card(value, suit) for value in CARD_VALUES for suit in CARD_SUITS]
        random.shuffle(self.deck)
        self.players = []  #dealer at last
        self.pot = 0

    def add_player(self, player):
        self.players.append(player)

    def add_players(self, players):
        self.players.extend(players)

    def total_pot(self):
        return self.pot
    
    def increase_pot(self, bet):
        self.pot += bet
        return self.pot
    
    def deal(self):
        for i in range(2):
            for p in self.players:
                p.hand.append(self.deck.pop(0))

    def blackjack_check(self):
        blackjack_players = []
        for p in self.players[:-1]:
            if p.blackjack():
                blackjack_players.append(p)
        if self.players[-1].blackjack():
            for p in self.players:
                if p in blackjack_players:
                    print("PUSH")
                else:
                    print("LOST")
        else:
            for p in blackjack_players:
                print("WON")
