from deckofcards import FrenchDeckOfCards
from player import Player

def make_bet(player_chips):

    while True:
        print(f'you have {player_chips} chips.')
        try:
            bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print('Please enter an integer.')
        else:
            if bet > player_chips:
                print('You cannot bet more than', player_chips, 'chips.')
            else:
                break
        
while True:
    print('Welcome to blackjack! Try and beat the dealer by getting to 21 without going over!')

    deck = FrenchDeckOfCards()
    deck.shuffle()

    player1 = Player()
    dealer = Player()
    player1.addtohand(deck.deal())
    dealer.addtohand(deck.deal())
    player1.addtohand(deck.deal())
    dealer.addtohand(deck.deal())

    make_bet(player1.chips)
    break
