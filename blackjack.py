import random

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Player:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.ace_flag = False

    def compute_hand_value(self):
        for card in self.hand:
            if card.value in values[0:9]:
                self.hand_value += int(card.value)
            elif card.value in values[9:12]:
                self.hand_value += 10
            else:
                if self.ace_flag:
                    self.hand_value = 2
                else:
                    self.hand_value += 1
                self.ace_flag = True

    def blackjack(self):
        return player.ace_flag and player.compute_hand_value + 10 == 21

def shuffle():
    deck = [Card(value, suit) for value in values for suit in suits]
    random.shuffle(deck)
    return deck

deck = shuffle()
player = Player()
dealer = Player()
for i in range(2):
    player.hand.append(deck.pop(0))
    dealer.hand.append(deck.pop(0))

player.compute_hand_value()
dealer.compute_hand_value()
if player.blackjack():
    if dealer.blackjack():
        print("push")
    else:
        print("blackjack")

print("Player cards: " + player.hand[0].value + " " + player.hand[0].suit + ", " + player.hand[1].value + " " + player.hand[1].suit)
print("Dealer card: " + dealer.hand[0].value + " " + dealer.hand[0].suit + ", " + dealer.hand[1].value + " " + dealer.hand[1].suit)
play = input("Play: ")