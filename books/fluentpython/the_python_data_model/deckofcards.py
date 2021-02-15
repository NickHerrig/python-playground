import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:

    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'heart club spade diamond'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__=="__main__":
    deck = FrenchDeck()
    # Iterating through a slice the FrenchDeck
    for card in deck[2:6]:
        print(card)

    # __getitem__ supports indexing
    print("The first card is", deck[0])

    print("reversing the slice...")
    for card in reversed(deck[2:6]):
        print(card)

    print("Selcing three random cards from the deck")
    from random import choice
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))

    exists = Card('Q', 'heart') in deck
    not_exists = Card('foo', 'beasts') in deck
    print("exists: ", exists)
    print("not_exists: ", not_exists)



