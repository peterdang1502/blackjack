import unittest
import random
from src.game import Game
from src.card import Card
from src.deck import Deck
from src.constants import *
from unittest.mock import patch, PropertyMock, Mock, MagicMock

class TestGame(unittest.TestCase):
    blackjack_hands = [Card(random.choice(FACE_CARDS)), Card(random.choice(FACE_CARDS)), Card(ACE_RANK), Card(ACE_RANK)]
    dealer_blackjack_hand = [Card(random.choice(NUMBER_CARDS)), Card(random.choice(FACE_CARDS)), Card(random.choice(NUMBER_CARDS)), Card(ACE_RANK)]
    player_blackjack_hand = [Card(random.choice(FACE_CARDS)), Card(random.choice(NUMBER_CARDS)), Card(ACE_RANK), Card(random.choice(NUMBER_CARDS))]
    non_blackjack_hands = [Card(random.choice(NUMBER_CARDS)), Card(random.choice(NUMBER_CARDS)), Card(random.choice(NUMBER_CARDS)), Card(random.choice(NUMBER_CARDS))]

    def test_both_blackjack(self):
        """Test that both dealer and player have blackjacks"""
        game = Game()
        game.deck.draw_card = MagicMock(side_effect=self.blackjack_hands)
        game.deal_cards()
        self.assertEqual(game.get_state(), DEALER_BLACKJACK)
        self.assertEqual(game.hands[1].get_state(), PUSH)
    
    def test_dealer_blackjack(self):
        """Test that dealer has blackjacks"""
        game = Game()
        game.deck.draw_card = MagicMock(side_effect=self.dealer_blackjack_hand)
        game.deal_cards()
        self.assertEqual(game.get_state(), DEALER_BLACKJACK)
        self.assertEqual(game.hands[1].get_state(), LOST)

    def test_player_blackjack(self):
        """Test that player has blackjacks"""
        game = Game()
        game.deck.draw_card = MagicMock(side_effect=self.player_blackjack_hand)
        game.deal_cards()
        self.assertEqual(game.get_state(), PLAYER_BLACKJACK)
        self.assertEqual(game.hands[1].get_state(), WON)

    def test_no_blackjacks(self):
        """Test that both dealer and player don't have blackjacks"""
        game = Game()
        game.deck.draw_card = MagicMock(side_effect=self.non_blackjack_hands)
        game.deal_cards()
        self.assertEqual(game.get_state(), IN_PLAY)
        self.assertEqual(game.hands[1].get_state(), IN_PLAY)

if __name__ == "__main__":
    unittest.main()