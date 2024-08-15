from player import Player
from constants import *

class Dealer(Player):
    def action(self, hand_value: int, is_soft_seventeen: bool):
        print("Dealer action.")
        if hand_value <= 16 or is_soft_seventeen:
            return HIT
        return STAND
            