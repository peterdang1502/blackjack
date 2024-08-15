import unittest
import random
from src.game import Game
from src.card import Card
from src.deck import Deck
from src.constants import *
from unittest.mock import patch, PropertyMock, Mock, MagicMock

class TestGame(unittest.TestCase):
    suit = random.choice(CARD_SUITS)
    blackjack_hands = [Card(random.choice(COURT_CARDS), suit), Card(random.choice(COURT_CARDS), suit), Card(ACE_RANK, suit), Card(ACE_RANK, suit)]
    dealer_blackjack_hand = [Card(random.choice(NUMBER_CARDS), suit), Card(random.choice(COURT_CARDS), suit), Card(random.choice(NUMBER_CARDS), suit), Card(ACE_RANK, suit)]
    player_blackjack_hand = [Card(random.choice(COURT_CARDS), suit), Card(random.choice(NUMBER_CARDS), suit), Card(ACE_RANK, suit), Card(random.choice(NUMBER_CARDS), suit)]
    non_blackjack_hands = [Card(random.choice(NUMBER_CARDS), suit), Card(random.choice(NUMBER_CARDS), suit), Card(random.choice(NUMBER_CARDS), suit), Card(random.choice(NUMBER_CARDS), suit)]

    def test_both_blackjack(self):
        """Test that both dealer and player have blackjacks"""
        game = Game()
        game.deck.draw_card = MagicMock(side_effect=self.blackjack_hands)
        self.assertEqual(game.deal_cards(), DEALER_BLACKJACK)
        self.assertEqual(game.hands[1].get_state(), PUSH)
    
    def test_dealer_blackjack(self):
        """Test that dealer has blackjacks"""
        game = Game()
        game.deck.draw_card = MagicMock(side_effect=self.dealer_blackjack_hand)
        self.assertEqual(game.deal_cards(), DEALER_BLACKJACK)
        self.assertEqual(game.hands[1].get_state(), LOST)

    def test_player_blackjack(self):
        """Test that player has blackjacks"""
        game = Game()
        game.deck.draw_card = MagicMock(side_effect=self.player_blackjack_hand)
        self.assertEqual(game.deal_cards(), PLAYER_BLACKJACK)
        self.assertEqual(game.hands[1].get_state(), WON)

    def test_no_blackjacks(self):
        """Test that both dealer and player don't have blackjacks"""
        game = Game()
        game.deck.draw_card = MagicMock(side_effect=self.non_blackjack_hands)
        self.assertEqual(game.deal_cards(), IN_PLAY)
        self.assertEqual(game.hands[1].get_state(), IN_PLAY)

if __name__ == "__main__":
    unittest.main()