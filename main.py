from deck import Deck
from hand import Hand
from card import Card
import random


# this is a deck of cards encoded in numbers in the form [suit, rank]
# suit 0 = Heart, 1 = Spade, 2 = Diamond, 3 = Club
# Rank = A23456789JQK -> (0 -> 12)
cards_code = [
 [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12],
 [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12],
 [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [2, 12],
 [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12]
]

def initialise_deck():
    cards_shuffled = cards_code # copy card codes list
    random.shuffle(cards_code) # shuffle the copy
    # loop through the shuffled list adding them to the deck object
    for card_code in cards_shuffled:
        deck.add_card(Card(card_code))

deck = Deck() # declaring a deck
initialise_deck()
players_hand = Hand(deck, 3) # declaring a hand of cards using the deck declared above with a length of 3
print(players_hand)