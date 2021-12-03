import random
from cardlib.card import *

class Deck():
    def __init__(self, do_shuffle=True):
        self.reset(do_shuffle)

    # resets the deck with 52 cards
    def reset(self, do_shuffle=True):
        self.cards = []

        for s in Suit:
            for r in Rank:
                new_card = Card(r, s)
                self.cards.append(new_card)

        if do_shuffle:
            self.shuffle()


    # shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # draws a card from the deck, and returns it
    # if the list is empty it will return None
    def draw(self):
        if not self.cards:
            return None

        return self.cards.pop(0)

    # returns the number of cards in the deck
    def size(self):
        return len(self.cards)
