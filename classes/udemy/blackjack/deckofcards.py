import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeckOfCards:
    """
    Purpose: creates a deck of 52 playing cards.
    Input: None
    Returns: a list of 52 named tuples Card(rank, suit)
            rank = 2-11, J, Q, K, A
            suit = heart, club, spade, or diamond
    """

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'heart club spade diamond'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
    def shuffle(self):
        """
        Purpose: The shuffle method shuffles existing object list of cards.
        Input: None
        Returns: None
        """
        random.shuffle(self._cards)

    def deal(self):
        """
        Purpose: the deal method deals a card from the deck
        Input: None
        Returns: returns  one card from the top of the deck
                 a named tuple Card(rank, suit)
        """
        single_card = self._cards.pop()
        return single_card
