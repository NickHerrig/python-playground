from deckofcards import FrenchDeckOfCards
from player import Player

deck = FrenchDeckOfCards()
deck.shuffle()

player1 = Player()
dealer = Player()
print(f'Hello, You have {player1.chips} chips!')

bet = input('How many chips would you like to bet? ')

while int(bet) > player1.chips:
    bet = input('you cannot bet more chips than you have. Try again: ')
    if int(bet) <= player1.chips:
        break

player1.addtohand(deck.deal())
dealer.addtohand(deck.deal())
player1.addtohand(deck.deal())
dealer.addtohand(deck.deal())

print(f'Your cards are: {player1.hand}.')
print(f'The dealer has a {dealer.hand[0]} showing.')

#TODO: Ask player if they want to hit or stand

#TODO: If no Bust, Ask if hit or stand

#TODO: Play Dealer Hand (Dealer will always hit until 17 or greater)

#TODO: Determin winner and add/subtract players chips

#TODO: Play Again?
