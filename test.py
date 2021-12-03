from cardlib.deck import *
from cardlib.hand import *

# create the deck. False here means to not shuffle the deck upon init
deck = Deck(False)

print("All of the cards:")
for c in deck.cards:
    print(f"card: {str(c)}")
print(f"card count: {deck.size()}")
print("\n")

# shuffle the deck
deck.shuffle()

# create 2 hands
hand1 = Hand()
hand2 = Hand()

# deal each hand 5 cards
for x in range(0, 5):
    hand1.add_card(deck.draw())
    hand2.add_card(deck.draw())

# show the hands
print(hand1)
print(hand2)

print(f"cards left in deck: {deck.size()}")
