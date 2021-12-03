

class Hand():
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        ret = "Hand:\n"
        for c in self.cards:
            ret += f"\t{str(c)}\n"
        return ret
