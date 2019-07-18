from deckofcards import FrenchDeckOfCards
from player import Player

playing = True

def make_bet(player_chips):

    while True:
        print(f'you have {player_chips} chips.')
        try:
            bet_value = int(input("How many chips would you like to bet? "))
        except ValueError:
            print('Please enter an integer.')
        else:
            if bet_value > player_chips:
                print('You cannot bet more than', player_chips, 'chips.')
            else:
                break
    return bet_value


def show_cards():
    print('____\n')
    print('Dealer is showing an: ')
    print(f'{dealer.hand[0]} \n')
    print("Player's Cards: ", *player1.hand, sep='\n')
    print(f'Player1 HandValue: {player1.handvalue}')
    print('____\n')


def hit_or_stand():
    global playing

    while True:
        hitorstand = input('Would you like to hit(h) or stand(s)? ')

        if hitorstand[0].lower() == 'h':
            player1.addtohand(deck.deal())
            show_cards()
        elif hitorstand[0].lower() == 's':
            print('____\n')
            print('Player stands. Dealer is playing.')
            print('____\n')
            playing = False
        else:
            print('Please try again.')
            continue
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
    
    bet = make_bet(player1.chips)
    show_cards()

    while playing:
        hit_or_stand()

        if player1.handvalue > 21:
            print(f'player busts with a {player1.handvalue}')
            print('____\n')
            break
   
    if player1.handvalue <= 21:    
        
        while dealer.handvalue < 17:
            dealer.addtohand(deck.deal())
        
        if dealer.handvalue > 21:
            print(f'Dealer Busts with a {dealer.handvalue}')

        elif dealer.handvalue > player1.handvalue:
            print(f'Dealer wins with a {dealer.handvalue}')

        elif dealer.handvalue < player1.handvalue:
            print(f'Player wins with a {player1.handvalue}')

        else:
            print("Push")

