from card import Card

class Hand:
    def __init__(self, deck, length=0):
        self.hand = []
        self.deck = deck
        if length != 0: # if a length was specified, draw those cards
            self.draw_x_cards(length)

    def __str__(self):
        string_output = ''
        for card in self.hand:
            string_output += str(card.get_symbol()) + ' '
        return string_output

    def draw_card(self):
        try:
            self.add_card(self.deck.next_card())
        except Exception:
            pass
        # what happens when no cards left

    def draw_x_cards(self, x): # used to draw multiple cards
        for i in range(x):
            self.draw_card()

    def add_card(self, card):
        if not isinstance(card, Card):
            raise TypeError('card must be of type Card')
        else:
            self.hand.append(card)