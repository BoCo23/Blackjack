cards_symbol = [['🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂽', '🂾',],
                ['🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', '🂫', '🂭', '🂮',],
                ['🃁', '🃂', '🃃', '🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃍', '🃎',],
                ['🃑', '🃒', '🃓', '🃔', '🃕', '🃖', '🃗', '🃘', '🃙', '🃚', '🃛', '🃝', '🃞']]

class Card:
    def __init__(self, card_code):
        if not isinstance(card_code, list):
            raise TypeError('card_code must be a list')
        else:
            self.suit = card_code[0]
            self.value = card_code[1]
            self.symbol = cards_symbol[card_code[0]][card_code[1]]

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def get_symbol(self):
        return self.symbol