import unittest
import random
from typing import List
from src.hand import Hand
from src.card import Card
from src.constants import *

class TestHand(unittest.TestCase):
    number_rank_one = random.choice(NUMBER_CARDS[:-1])
    number_rank_two = random.choice(NUMBER_CARDS)
    number_card_one = Card(number_rank_one)
    number_card_two = Card(number_rank_two)
    face_card_one = Card(random.choice(FACE_CARDS))
    face_card_two = Card(random.choice(FACE_CARDS))
    ace_card = Card(CARD_RANKS[-1])

    only_numbers_hand = [number_card_one, number_card_two]
    number_and_face_hand = [number_card_one, face_card_one]
    number_and_ace_hand = [number_card_one, ace_card]
    only_faces_hand = [face_card_one, face_card_two]
    face_and_ace_hand = [face_card_two, ace_card]
    only_aces_hand = [ace_card, ace_card]
    soft_hand = [Card(NUMBER_CARDS[0]), Card(NUMBER_CARDS[0]), ace_card]
    hard_hand = [ace_card, ace_card, face_card_one]
    bust_hand = [face_card_one, face_card_two, ace_card, ace_card]

    split_rank = random.choice(CARD_RANKS)
    split_hand = [Card(split_rank), Card(split_rank)]

    def hand_receive_cards(self, hand: Hand, cards: List[Card]):
        for c in cards:
            hand.receive_card(c)

    def test_hand_receive_cards(self):
        """Test that a hand's value is calculated correctly through various hand arrangements"""
        hand = Hand()
        self.hand_receive_cards(hand, self.only_numbers_hand)
        self.assertFalse(hand.get_can_split())
        self.assertEqual(hand.get_state(), IN_PLAY)
        self.assertEqual(hand.get_hand_value(), int(self.number_rank_one) + int(self.number_rank_two))
        
        hand.reset()
        self.hand_receive_cards(hand, self.number_and_face_hand)
        self.assertFalse(hand.get_can_split())
        self.assertEqual(hand.get_state(), IN_PLAY)
        self.assertEqual(hand.get_hand_value(), int(self.number_rank_one) + 10)

        hand.reset()
        self.hand_receive_cards(hand, self.number_and_ace_hand)
        self.assertFalse(hand.get_can_split())
        self.assertEqual(hand.get_state(), IN_PLAY)
        self.assertEqual(hand.get_hand_value(), int(self.number_rank_one) + 11)

        hand.reset()
        self.hand_receive_cards(hand, self.only_faces_hand)
        self.assertTrue(hand.get_can_split())
        self.assertEqual(hand.get_state(), IN_PLAY)
        self.assertEqual(hand.get_hand_value(), 20)

        hand.reset()
        self.hand_receive_cards(hand, self.face_and_ace_hand)
        self.assertFalse(hand.get_can_split())
        self.assertEqual(hand.get_state(), BLACKJACK)
        self.assertEqual(hand.get_hand_value(), 21)

        hand.reset()
        self.hand_receive_cards(hand, self.only_aces_hand)
        self.assertTrue(hand.get_can_split())
        self.assertEqual(hand.get_state(), IN_PLAY)
        self.assertEqual(hand.get_hand_value(), 12)

        hand.receive_card(Card(ACE_RANK))
        self.assertEqual(hand.get_hand_value(), 13)

        hand.reset()
        self.hand_receive_cards(hand, self.soft_hand)
        self.assertFalse(hand.get_can_split())
        self.assertEqual(hand.get_state(), IN_PLAY)
        self.assertEqual(hand.get_hand_value(), 15)

        hand.reset()
        self.hand_receive_cards(hand, self.hard_hand)
        self.assertFalse(hand.get_can_split())
        self.assertEqual(hand.get_state(), IN_PLAY)
        self.assertEqual(hand.get_hand_value(), 12)

        hand.reset()
        self.hand_receive_cards(hand, self.bust_hand)
        self.assertEqual(hand.get_state(), BUST)
        self.assertEqual(hand.get_hand_value(), 22)

if __name__ == "__main__":
    unittest.main()