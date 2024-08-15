from constants import *

class Player:
    def action(self, can_split: bool, can_double: bool):
        split = " split," if can_split else ""
        double = " double down," if can_double else ""
        print("Possible actions: stand, hit," + double + split + " surrender")
        print("Player action?")
        return input().upper()