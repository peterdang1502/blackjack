from player import Player

class Dealer(Player):
    def print_cards(self):
        print(['  '] + self.hand[1:])