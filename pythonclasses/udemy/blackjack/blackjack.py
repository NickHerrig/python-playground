from deckofcards import FrenchDeckOfCards
from player import Player

deck = FrenchDeckOfCards()
deck.shuffle()

player1 = Player(chips=100)
dealer = Player()

#TODO: Ask Player for their bet(Cannot be more than current chips)

#TODO: Deal cards to player and dealer (Does the order matter in real blackjack?... Not sure)

#TODO: Ensure one of dealers cards is face up, and show both players cards

#TODO: Ask player if they want to hit or stand

#TODO: If no Bust, Ask if hit or stand

#TODO: Play Dealer Hand (Dealer will always hit until 17 or greater)

#TODO: Determin winner and add/subtract players chips

#TODO: Play Again?
