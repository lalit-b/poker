from cards_and_suits import CardsAndSuits
from poker_hands import PokerHands


def main():
    try:
        with open('poker.txt') as f:
            all_data = f.readlines()
            player_one_win_count = 0
            poker_hand = PokerHands()

            for item in all_data:
                hands = item.strip()
                player_one_hand, player_two_hand = hands[:14], hands[15:]

                player_one_cards_and_suits = CardsAndSuits(player_one_hand)
                player_two_cards_and_suits = CardsAndSuits(player_two_hand)

                player_one_hand_rank = poker_hand.get_hand_rank(player_one_cards_and_suits)
                player_two_hand_rank = poker_hand.get_hand_rank(player_two_cards_and_suits)

                if player_one_hand_rank > player_two_hand_rank:
                    player_one_win_count += 1
                elif player_one_hand_rank == player_two_hand_rank:
                    winning_hand = poker_hand.determine_winner_for_a_tie(player_one_cards_and_suits, player_two_cards_and_suits)
                    if winning_hand == player_one_cards_and_suits:
                        player_one_win_count += 1

        print player_one_win_count
    except Exception, e:
        print e.__str__()

if __name__ == '__main__':
    main()