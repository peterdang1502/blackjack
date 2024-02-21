from player import Player

class Dealer(Player):
    def __init__(self):
        Player.__init__(self, "Dealer")

    def show_hand_at_deal(self):
        print(self.name + " hands: ")
        print(self.hand[1].value + " of " + self.hand[1].suit + " ")
        print("Hidden card")