import unittest
import random
from src.game import Game
from src.card import Card
from src.constants import *

class TestGame(unittest.TestCase):
    suit = random.choice(CARD_SUITS)
    blackjack_hand = [Card(random.choice(COURT_CARDS), suit), Card(CARD_RANKS[-1], suit)]
    non_blackjack_hand = [Card(random.choice(CARD_RANKS[:-1]), suit), Card(random.choice(CARD_RANKS[:-1]), suit)]

    def deal_card_helper(self, game, dealer_cards, player_cards):
        for c in dealer_cards:
            game.deal_card_to_dealer(c)
        
        for c in player_cards:
            game.deal_card_to_player(c)


    def test_both_blackjack(self):
        """Test that both dealer and player have blackjacks"""
        game = Game()
        self.deal_card_helper(game, self.blackjack_hand, self.blackjack_hand)
        self.assertEqual(game.check_blackjacks(), PUSH)
    
    def test_dealer_blackjack(self):
        """Test that dealer has blackjacks"""
        game = Game()
        self.deal_card_helper(game, self.blackjack_hand, self.non_blackjack_hand)
        self.assertEqual(game.check_blackjacks(), LOST)

    def test_player_blackjack(self):
        """Test that player has blackjacks"""
        game = Game()
        self.deal_card_helper(game, self.non_blackjack_hand, self.blackjack_hand)
        self.assertEqual(game.check_blackjacks(), WON)

    def test_no_blackjacks(self):
        """Test that both dealer and player don't have blackjacks"""
        game = Game()
        self.deal_card_helper(game, self.non_blackjack_hand, self.non_blackjack_hand)
        self.assertNotIn(game.check_blackjacks(), [PUSH, LOST, WON])

if __name__ == "__main__":
    unittest.main()