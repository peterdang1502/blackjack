import unittest
from src.deck import Deck
from src.card import Card
from src.constants import *

class TestDeck(unittest.TestCase):
    def test_deck_size(self):
        """Test that the deck has 312 cards and contains proper cards"""
        deck = Deck()
        self.assertEqual(len(deck.deck), 312);
    
    def test_deck_draw_card(self):
        """Test that deck can draw a card"""
        deck = Deck()
        card = deck.draw_card()
        #self.assertIsInstance(card, Card)
        self.assertIn(card.number, CARD_NUMBERS)
        self.assertIn(card.suit, CARD_SUITS)

if __name__ == "__main__":
    unittest.main()