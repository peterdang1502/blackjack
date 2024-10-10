import unittest
import random
from src.card import Card
from src.constants import *

class TestCard(unittest.TestCase):
    ace = CARD_RANKS[-1]

    def test_calculate_value_number(self):
        """Test to calculate a numbered card value"""
        number = random.choice(NUMBER_CARDS)
        card = Card(number);
        self.assertEqual(card.get_value(), int(number))

    def test_calculate_value_special(self):
        """Test to calculate card value of face cards"""
        card = Card(random.choice(FACE_CARDS));
        self.assertEqual(card.get_value(), 10)

    def test_calculate_value_ace(self):
        """Test to calculate card value of Ace"""
        card = Card(self.ace);
        self.assertEqual(card.get_value(), 1)

    def test_is_ace(self):
        """Test to check card is Ace"""
        card = Card(self.ace);
        self.assertTrue(card.is_ace())

    def test_is_not_ace(self):
        """Test to check card is not Ace"""
        card = Card(random.choice(CARD_RANKS[:-1]));
        self.assertFalse(card.is_ace())

if __name__ == "__main__":
    unittest.main()