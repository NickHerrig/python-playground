from deckofcards import FrenchDeckOfCards
from player import Player

deck = FrenchDeckOfCards()
deck.shuffle()

player1 = Player(name = 'player1', chips=100)
dealer = Player(name = 'dealer')
print(f'Hello {player1.name}, You have {player1.chips} chips!')

bet = input('How many chips would you like to bet? ')

while int(bet) > player1.chips:
    bet = input('you cannot bet more chips than you have. Try again: ')
    if int(bet) <= player1.chips:
        break


#TODO: Deal cards to player and dealer (Does the order matter in real blackjack?... Not sure)

#TODO: Ensure one of dealers cards is face up, and show both players cards

#TODO: Ask player if they want to hit or stand

#TODO: If no Bust, Ask if hit or stand

#TODO: Play Dealer Hand (Dealer will always hit until 17 or greater)

#TODO: Determin winner and add/subtract players chips

#TODO: Play Again?
