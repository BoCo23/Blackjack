from card import Card

class Deck:
    def __init__(self):
        self.deck = [] # initialise an enpty list

    def add_card(self, card):
        if not isinstance(card, Card): # check card is an instance of Card
            raise TypeError('card must be of type Card')
        else:
            self.deck.append(card) # add it to the deck list

    def __str__(self):
        # loop through the list of cards and add them to a string
        string_output = ''
        for card in self.deck:
            string_output += str(card.get_symbol()) + ' '
        return string_output

    def next_card(self):
        if len(self.deck) == 0: # check if the deck is empty
            return None # returning none if it is
        else:
            return self.deck.pop(0) # else popping the next card