class Hand:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards