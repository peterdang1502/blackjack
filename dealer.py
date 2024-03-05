from player import Player

class Dealer(Player):
    def __init__(self):
        Player.__init__(self, "Dealer", 1000)

    def show_hand_at_deal(self):
        print(self.name + " hands: ")
        self.hands[0].show_dealer_hand()