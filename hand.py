from constants import CARD_VALUES, CARD_SUITS

class Hand:
    def __init__(self, hand_owner="player"):
        self.hand_owner = hand_owner
        self.cards = []
        self.hand_value = 0
        self.ace_flag = False
        self.blackjack = False

    def receive_card(self, card):
        self.cards.append(card)

        if card.value in CARD_VALUES[0:9]:
            self.hand_value += int(card.value)
        elif card.value in CARD_VALUES[9:12]:
            self.hand_value += 10
        else:
            if len(self.cards) == 2 and self.ace_flag:
                self.hand_value = 2
            else:
                self.hand_value += 1
            self.ace_flag = True

        self.blackjack = len(self.cards) == 2 and self.ace_flag and self.hand_value + 10 == 21
    
    def show_hand(self):
        for card in self.cards:
            print(card.value + " of " + card.suit + " ")
        if self.blackjack:
            print("BLACKJACK!")
        elif self.ace_flag and self.hand_value != 2:
            print("Hand value: " + str(self.hand_value) + " or " + str(self.hand_value + 10))
        else:
            print("Hand value: " + str(self.hand_value))
        print("\n")

    def show_dealer_hand(self):
        if self.blackjack:
            print(self.cards[0].value + " of " + self.cards[0].suit + " ")
        else:
            print("Hidden card")
        print(self.cards[1].value + " of " + self.cards[1].suit + " ")
        if self.blackjack:
            print("BLACKJACK!")
        print("\n")

    def action(self):
        split = "split, " if len(self.cards) == 2 and self.cards[0].value == self.cards[1].value else ""
        action = input("Hand action: stand, hit, double down, " + split + "or surrender")
        return action