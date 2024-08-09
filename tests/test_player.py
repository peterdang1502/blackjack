import unittest
from src.player import Player
from src.card import Card

class TestPlayer(unittest.TestCase):
    def test_player_receive_card(self):
        """Test that a player receives a card correctly"""
        player = Player()
        card = Card("4", "Diamonds")
        player.receive_card(card)
        self.assertIn(card, player.hand)
        self.assertFalse(player.ace)
        self.assertEqual(player.hand_value, 4)

if __name__ == "__main__":
    unittest.main()