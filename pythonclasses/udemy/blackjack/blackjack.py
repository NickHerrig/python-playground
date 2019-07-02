from deckofcards import FrenchDeckOfCards
from random import randint

deck = FrenchDeckOfCards()

card = deck[randint(1,53)]

print(card)

