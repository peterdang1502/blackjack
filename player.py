from constants import CARD_VALUES, CARD_SUITS

class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.hand = []
        self.hand_value = 0
        self.ace_flag = False

    def compute_hand_value(self):
        for card in self.hand:
            if card.value in CARD_VALUES[0:9]:
                self.hand_value += int(card.value)
            elif card.value in CARD_VALUES[9:12]:
                self.hand_value += 10
            else:
                if self.ace_flag:
                    self.hand_value = 2
                else:
                    self.hand_value += 1
                self.ace_flag = True

    def blackjack(self):
        return self.ace_flag and self.hand_value + 10 == 21
    
    def show_hand(self):
        self.compute_hand_value()
        print(self.name + " hands: ")
        for card in self.hand:
            print(card.value + " of " + card.suit + " ")
        if self.ace_flag and self.hand_value != 2:
            print("Hand value: " + str(self.hand_value) + " or " + str(self.hand_value + 10))
        else:
            print("Hand value: " + str(self.hand_value))
        print("\n")