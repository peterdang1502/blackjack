class Player:
    def __init__(self):
        self.hand = []
        self.ace = False
        self.blackjack = False
        self.hand_value = 0

    def receive_card(self, card):
        if card.ace:
            self.ace = True
        self.hand_value += card.value
        self.hand.append(card)
        
    def print_cards(self):
        print(self.hand)