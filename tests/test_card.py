import unittest
from src.card import Card

class TestCard(unittest.TestCase):
    def test_calculate_value_number(self):
        """Test to calculate card value of 2"""
        card = Card("2", "Clubs");
        self.assertEqual(card.value, 2)

    def test_calculate_value_special(self):
        """Test to calculate card value of Jack"""
        card = Card("Jack", "Diamonds");
        self.assertEqual(card.value, 10)

    def test_calculate_value_ace(self):
        """Test to calculate card value of Ace"""
        card = Card("Ace", "Hearts");
        self.assertEqual(card.value, 1)

    def test_is_ace(self):
        """Test to check card is Ace"""
        card = Card("Ace", "Spades");
        self.assertTrue(card.is_ace())

    def test_is_not_ace(self):
        """Test to check card is not Ace"""
        card = Card("3", "Clubs");
        self.assertFalse(card.is_ace())

if __name__ == "__main__":
    unittest.main()