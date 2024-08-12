import unittest
import random
from src.card import Card
from src.constants import *

class TestCard(unittest.TestCase):
    suit = random.choice(CARD_SUITS)
    ace = CARD_RANKS[-1]

    def test_calculate_value_number(self):
        """Test to calculate card value of 2"""
        number = random.choice(NUMBER_CARDS)
        card = Card(number, self.suit);
        self.assertEqual(card.value, int(number))

    def test_calculate_value_special(self):
        """Test to calculate card value of court cards"""
        card = Card(random.choice(COURT_CARDS), self.suit);
        self.assertEqual(card.value, 10)

    def test_calculate_value_ace(self):
        """Test to calculate card value of Ace"""
        card = Card(self.ace, self.suit);
        self.assertEqual(card.value, 11)

    def test_is_ace(self):
        """Test to check card is Ace"""
        card = Card(self.ace, self.suit);
        self.assertTrue(card.is_ace())

    def test_is_not_ace(self):
        """Test to check card is not Ace"""
        card = Card(random.choice(CARD_RANKS[:-1]), self.suit);
        self.assertFalse(card.is_ace())

if __name__ == "__main__":
    unittest.main()