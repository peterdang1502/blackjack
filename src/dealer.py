from player import Player

class Dealer(Player):
    def print_cards(self, reveal = False):
        if reveal:
            self.hands[0].print_cards()
        else:
            self.hands[0].print_dealer_cards()

    def action(self):
        print("Dealer action.")