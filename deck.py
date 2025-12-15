from card import Card

class Deck:
    def __init__(self):
        self.deck = []

    def add_card(self, card):
        if not isinstance(card, Card):
            raise TypeError('card must be of type Card')
        else:
            self.deck.append(card)

    def __str__(self):
        string_output = ''
        for card in self.deck:
            string_output += str(card.get_symbol()) + ' '
        return string_output

