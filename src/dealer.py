from player import Player

class Dealer(Player):
    def print_cards(self):
        self.hands[0].print_dealer_cards()