from enum import Enum
from collections import Counter

class PokerHandsRank(Enum):
    ROYAL_FLUSH = 10
    STRAIGHT_FLUSH = 9
    FOUR_OF_A_KIND = 8
    FULL_HOUSE = 7
    FLUSH = 6
    STRAIGHT = 5
    THREE_OF_A_KIND = 4
    TWO_PAIRS = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

class PokerHands:

    def get_hand_rank(self, hand):
        # Function to determine the rank of a poker hand
        cards, suits = hand.cards, hand.suits

        if self.check_royal_flush(cards, suits):
            return PokerHandsRank.ROYAL_FLUSH
        elif self.check_straight_flush(cards, suits):
            return PokerHandsRank.STRAIGHT_FLUSH
        elif self.check_four_of_a_kind(cards, suits):
            return PokerHandsRank.FOUR_OF_A_KIND
        elif self.check_full_house(cards, suits):
            return PokerHandsRank.FULL_HOUSE
        elif self.check_flush(cards, suits):
            return PokerHandsRank.FLUSH
        elif self.check_straight(cards, suits):
            return PokerHandsRank.STRAIGHT
        elif self.check_three_of_a_kind(cards, suits):
            return PokerHandsRank.THREE_OF_A_KIND
        elif self.check_two_pairs(cards, suits):
            return PokerHandsRank.TWO_PAIRS
        elif self.check_one_pair(cards, suits):
            return PokerHandsRank.ONE_PAIR
        else:
            return PokerHandsRank.HIGH_CARD

    def check_royal_flush(self, cards, suits):
        # Function to return True if a given hand is a royal flush
        # Royal flush Example:
        # ['T', 'J', 'Q', 'K', 'A']['H', 'H', 'H', 'H', 'H'] = > True
        # ['3', 'T', '9', '8', 'A']['S', 'D', 'H', 'S', 'S'] = > False
        if set(['T', 'J', 'Q', 'K', 'A']) == set(cards):
            if len(set(suits)) == 1:
                return True
        return False

    def check_straight_flush(self, cards, suits):
        # Function to return True if a given hand is a straight flush
        # Straight Flush Example:
        # ['4', '5', '6', '7', '8']['S', 'S', 'S', 'S', 'S'] = > True
        # ['3', '9', 'Q', 'T', '2']['C', 'D', 'H', 'S', 'S'] = > False
        if self.check_straight(cards, suits) and self.check_flush(cards, suits):
            return True
        return False

    def check_flush(self, cards, suits):
        # Function to return True if a given hand is a flush
        # Flush Example:
        # ['S', 'S', 'S', 'S', 'S'] = > True
        # ['C', 'C', 'S', 'S', 'D'] = > False
        if len(set(suits)) == 1:
            return True
        return False

    def check_full_house(self, cards, suits):
        # Function to return True if a given hand is a full house
        # Full House Example:
        # ['T', 'T', 'T', 'A', 'A'] = > True
        # ['A', '9', '8', 'Q', 'T'] = > False
        if self.check_three_of_a_kind(cards, suits) and self.check_one_pair(cards, suits):
            return True
        return False

    def check_straight(self, cards, suits):
        # Function to return True if a given hand is a straight
        # Straight Example:
        # ['K', 'Q', 'J', 'T', '9'] => True
        # ['Q', 'T', '3', '2', '1'] => False
        card_ranks = {14: 'A', 13: 'K', 12: 'Q', 11: 'J', 10: 'T', 9: '9',
                      8: '8', 7: '7', 6: '6', 5: '5', 4: '4', 3: '3', 2: '2', 1: '1'}

        high_card = self.get_high_card_value(cards, suits)
        if card_ranks[high_card - 1] in cards and \
                card_ranks[high_card - 2] in cards and \
                card_ranks[high_card - 3] in cards and \
                card_ranks[high_card - 4] in cards:
            return True
        return False

    def check_four_of_a_kind(self, cards, suits):
        # Function to return True if a given hand is a four of a kind
        # Four of a Kind Example:
        # ['5','5','5','5','Q'] => True
        # ['5', '7', 'Q', 'T', 'K'] => False
        count_of_all_cards = Counter(cards)
        if 4 in count_of_all_cards.values():
            return True
        return False

    def check_three_of_a_kind(self, cards, suits):
        # Function to return True if a given hand is a three of a kind
        # Three of a Kind Example:
        # ['5','5','5','T','Q'] => True
        # ['5', '7', 'Q', 'T', 'K'] => False
        count_of_all_cards = Counter(cards)
        if 3 in count_of_all_cards.values():
            return True
        return False

    def check_two_pairs(self, cards, suits):
        # Function to return True if a given hand has two pairs
        # Two pairs Example:
        # ['5','5','2','Q','Q'] => True
        # ['5', '7', 'Q', 'T', 'K'] => False
        if self.number_of_pairs(cards, suits) == 2:
            return True
        return False

    def check_one_pair(self, cards, suits):
        # Function to return True if a given hand has one pair
        # One pair Example:
        # ['5','6','2','Q','Q'] => True
        # ['5', '7', 'Q', 'T', 'K'] => False
        if self.number_of_pairs(cards, suits) == 1:
            return True
        return False

    def get_high_card_value(self, cards, suits):
        # Function to return the highest card value in a hand
        # Example:
        # ['K', 'Q', 'T', '2', '8'] = > 13
        highest = 0
        for card in cards:
            if card == 'A':
                return 14
            elif card == 'K':
                if 13 >= highest:
                    highest = 13
            elif card == 'Q':
                if 12 >= highest:
                    highest = 12
            elif card == 'J':
                if 11 >= highest:
                    highest = 11
            elif card == 'T':
                if 10 >= highest:
                    highest = 10
            elif int(card) > highest:
                highest = int(card)

        return highest

    def determine_winner_for_a_tie(self, hand_one, hand_two):
        cards_one, suits_one = hand_one.cards, hand_two.suits
        cards_two, suits_two = hand_two.cards, hand_two.suits

        if self.get_highest_paired_card_value(cards_one, suits_one) > self.get_highest_paired_card_value(cards_two, suits_two):
            return hand_one
        elif self.get_highest_paired_card_value(cards_one, suits_one) == self.get_highest_paired_card_value(cards_two, suits_two):
            if self.get_high_card_value(cards_one, suits_one) > self.get_high_card_value(cards_two, suits_two):
                return hand_one
            else:
                return hand_two
        else:
            return hand_two

    def number_of_pairs(self, cards, suits):
        # Function to return the number of paired cards in a hand
        # Example:
        # ['5', '5', '7', '6', '3'] = > 1
        # ['5', '5', '6', '6', '7'] = > 2
        # ['4', '3', 'Q', 'K', 'T'] = > 0
        count = {}
        pairs = 0
        for card in cards:
            if card in count:
                count[card] += 1
            else:
                count[card] = 1

        for key, value in count.items():
            if value == 2:
                pairs += 1

        return pairs

    def get_highest_paired_card_value(self, cards, suits):
        # Function to return the highest paired card value in a hand
        # Example:
        # ['5', '5', '6', '7', 'K'] = > 5
        # ['K', 'K', 'T', 'T', '8'] = > 13
        card_ranks = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
                      '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '1': 1}
        highest = 0
        count = Counter(cards)
        for card, value in count.items():
            if value == 2 and card_ranks[card] > highest:
                highest = card_ranks[card]
        return highest
