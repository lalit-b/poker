import unittest
from poker_hands import PokerHands
from cards_and_suits import CardsAndSuits

class PokerHandsTest(unittest.TestCase):
    def test_check_royal_flush(self):
        p = PokerHands()
        test_cards, test_suits = ['T', 'J', 'Q', 'K', 'A'], ['H', 'H', 'H', 'H', 'H']
        test_cards_loser, test_suits_loser = ['T', 'J', 'Q', 'K', 'A'], ['H', 'H', 'H', 'C', 'H']
        self.assertTrue(p.check_royal_flush(test_cards, test_suits))
        self.assertFalse(p.check_royal_flush(test_cards_loser, test_suits_loser))

    def test_check_straight_flush(self):
        p = PokerHands()
        test_cards, test_suits = ['4', '5', '6', '7', '8'],['S', 'S', 'S', 'S', 'S']
        self.assertTrue(p.check_straight(test_cards, test_suits))
        self.assertTrue(p.check_flush(test_cards, test_suits))

    def test_check_four_of_a_kind(self):
        p = PokerHands()
        test_cards, test_suits = ['5','5','5','5','Q'], ['H', 'S', 'D', 'C', 'H']
        test_cards_losert, test_suits_loser = ['5', '5', '6', '5', 'Q'], ['H', 'S', 'D', 'C', 'H']
        self.assertTrue(p.check_four_of_a_kind(test_cards, test_suits))
        self.assertFalse(p.check_four_of_a_kind(test_suits_loser, test_suits_loser))

    def test_check_full_house(self):
        p = PokerHands()
        test_cards, test_suits = ['5', '5', '5', '6', '6'], ['H', 'S', 'D', 'C', 'H']
        self.assertTrue(p.check_three_of_a_kind(test_cards, test_suits))
        self.assertTrue(p.check_one_pair(test_cards, test_suits))

    def test_check_flush(self):
        p = PokerHands()
        test_cards, test_suits = ['4', '5', '6', '7', '8'], ['S', 'S', 'S', 'S', 'S']
        test_cards_loser, test_suits_loser = ['4', '5', '6', '7', '8'], ['S', 'S', 'H', 'S', 'S']
        self.assertTrue(p.check_flush(test_cards, test_suits))
        self.assertFalse(p.check_flush(test_cards_loser, test_suits_loser))

    def test_check_straight(self):
        p = PokerHands()
        test_cards, test_suits = ['4', '5', '6', '7', '8'],['S', 'S', 'C', 'S', 'H']
        test_cards_loser, test_suits_loser = ['4', '5', '6', '7', '9'],['S', 'S', 'C', 'S', 'H']
        self.assertTrue(p.check_straight(test_cards, test_suits))
        self.assertFalse(p.check_straight(test_cards_loser, test_suits_loser))

    def test_check_three_of_a_kind(self):
        p = PokerHands()
        test_cards, test_suits = ['5', '5', '5', '6', 'Q'], ['H', 'S', 'D', 'C', 'H']
        test_cards_losert, test_suits_loser = ['5', '5', '6', '7', 'Q'], ['H', 'S', 'D', 'C', 'H']
        self.assertTrue(p.check_three_of_a_kind(test_cards, test_suits))
        self.assertFalse(p.check_three_of_a_kind(test_suits_loser, test_suits_loser))

    def test_check_two_pairs(self):
        p = PokerHands()
        test_cards, test_suits = ['5', '5', 'A', '6', '6'], ['H', 'S', 'D', 'C', 'H']
        test_cards_loser, test_suits_loser = ['5', '2', 'A', 'J', '6'], ['H', 'S', 'D', 'C', 'H']
        self.assertTrue(p.check_two_pairs(test_cards, test_suits))
        self.assertFalse(p.check_two_pairs(test_cards_loser, test_suits_loser))

    def test_check_one_pair(self):
        p = PokerHands()
        test_cards, test_suits = ['5', '2', 'A', '6', '6'], ['H', 'S', 'D', 'C', 'H']
        test_cards_loser, test_suits_loser = ['5', '2', 'A', 'J', '6'], ['H', 'S', 'D', 'C', 'H']
        self.assertTrue(p.check_one_pair(test_cards, test_suits))
        self.assertFalse(p.check_one_pair(test_cards_loser, test_suits_loser))

    def test_get_high_card_value(self):
        p = PokerHands()
        test_cards, test_suits = ['K', 'Q', 'T', '2', '8'], ['H', 'S', 'D', 'C', 'H']
        self.assertEqual(13, p.get_high_card_value(test_cards, test_suits))

    def test_number_of_pairs(self):
        p = PokerHands()
        test_cards, test_suits = ['5','5','7','6','3'], ['H', 'S', 'D', 'C', 'H']
        self.assertEqual(1, p.number_of_pairs(test_cards, test_suits))
        test_cards, test_suits = ['5','5','6','6','7'], ['H', 'S', 'D', 'C', 'H']
        self.assertEqual(2, p.number_of_pairs(test_cards, test_suits))
        test_cards, test_suits = ['4','3','Q','K','T'], ['H', 'S', 'D', 'C', 'H']
        self.assertEqual(0, p.number_of_pairs(test_cards, test_suits))

    def test_determine_winner_for_a_tie(self):
        p = PokerHands()
        hand_one = CardsAndSuits(hand='8C TS KC 9H 4S')
        hand_two = CardsAndSuits(hand='7D 2S 5D 3S AC')

        self.assertEqual(hand_two, p.determine_winner_for_a_tie(hand_one, hand_two))

if __name__ == "__main__":
    unittest.main()