from card import Card
from deck import Deck

class Hand:
    def __init__(self, deck, length=0):
        self.hand = []
        self.deck = deck
        if length != 0:
            self.draw_x_cards(length)

    def __str__(self):
        string_output = ''
        for card in self.hand:
            string_output += str(card.get_symbol()) + ' '
        return string_output

    def draw_card(self):
        self.add_card(self.deck.next_card())

    def draw_x_cards(self, x):
        for i in range(x):
            self.draw_card()

    def add_card(self, card):
        if not isinstance(card, Card):
            raise TypeError('card must be of type Card')
        else:
            self.hand.append(card)