class CardsAndSuits:
    def __init__(self, hand):
        self.hand = hand
        self.cards = []
        self.suits = []
        self.get_card_value_and_suit()

    def get_card_value_and_suit(self):
        # function to return a list of card value and suit from a given hand

        for cs in self.hand.split(' '):
            self.cards.append(cs[0])
            self.suits.append(cs[1])