class Player:
    def __init__(self):
        self.hand = []
        self.blackjack = False

    def receive_card(self, card):
        self.hand.append(card)

    def print_cards(self):
        print(self.hand)