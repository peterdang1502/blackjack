import unittest
import random
from src.hand import Hand
from src.card import Card
from src.constants import *

class TestHand(unittest.TestCase):
    suit = random.choice(CARD_SUITS)
    number_rank_one = random.choice(NUMBER_CARDS)
    number_rank_two = random.choice(NUMBER_CARDS)
    number_card_one = Card(number_rank_one, suit)
    number_card_two = Card(number_rank_two, suit)
    court_card_one = Card(random.choice(COURT_CARDS), suit)
    court_card_two = Card(random.choice(COURT_CARDS), suit)
    ace_card = Card(CARD_RANKS[-1], suit)

    only_numbers_hand = [number_card_one, number_card_two]
    number_and_court_hand = [number_card_one, court_card_one]
    number_and_ace_hand = [number_card_two, ace_card]
    only_courts_hand = [court_card_one, court_card_two]
    court_and_ace_hand = [court_card_two, ace_card]
    only_aces_hand = [ace_card, ace_card]

    def hand_receive_cards(self, hand, cards):
        for c in cards:
            hand.receive_card(c)

    def test_hand_receive_cards(self):
        """Test that a hand's value is calculated correctly through various hand arrangements"""
        hand = Hand()
        self.hand_receive_cards(hand, self.only_numbers_hand)
        self.assertFalse(hand.blackjack)
        self.assertEqual(hand.hand_value, int(self.number_rank_one) + int(self.number_rank_two))
        
        hand.reset_hand()
        self.hand_receive_cards(hand, self.number_and_court_hand)
        self.assertFalse(hand.blackjack)
        self.assertEqual(hand.hand_value, int(self.number_rank_one) + 10)

        hand.reset_hand()
        self.hand_receive_cards(hand, self.number_and_ace_hand)
        self.assertFalse(hand.blackjack)
        self.assertEqual(hand.hand_value, int(self.number_rank_two) + 11)

        hand.reset_hand()
        self.hand_receive_cards(hand, self.only_courts_hand)
        self.assertFalse(hand.blackjack)
        self.assertEqual(hand.hand_value, 20)

        hand.reset_hand()
        self.hand_receive_cards(hand, self.court_and_ace_hand)
        self.assertTrue(hand.blackjack)
        self.assertEqual(hand.hand_value, 21)

        hand.reset_hand()
        self.hand_receive_cards(hand, self.only_aces_hand)
        self.assertFalse(hand.blackjack)
        self.assertEqual(hand.hand_value, 22)


if __name__ == "__main__":
    unittest.main()