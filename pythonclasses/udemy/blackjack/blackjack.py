from deckofcards import FrenchDeckOfCards
from player import Player

playing = True
current_chips = 100

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
            elif bet_value <= 0:
                print('Your bet must be greater than 0.')
            else:
                break
    return bet_value


def show_cards():
    print("______________________\n")
    print('Dealer is showing an: ')
    print(f'{dealer.hand[0]} \n')
    print("Player's Cards: ", *player1.hand, sep='\n')
    print(f'Player1 HandValue: {player1.handvalue}')
    print("______________________\n")


def hit_or_stand():
    global playing

    while True:
        hitorstand = input('Would you like to hit(h) or stand(s)? ')

        if hitorstand[0].lower() == 'h':
            player1.addtohand(deck.deal())
            show_cards()
        elif hitorstand[0].lower() == 's':
            print("______________________\n")
            print('Player stands. Dealer is playing.')
            print("______________________\n")
            playing = False
        else:
            print('Please try again.')
            continue
        break

def dealer_wins(bet):
    player1.losechips(losses=bet)


def player_wins(bet):
    player1.addchips(winnings=bet)


def dealer_busts(bet):
    player1.addchips(winnings=bet)


def player_busts(bet):
    player1.losechips(losses=bet)


while True:
    print('Welcome to blackjack! Try and beat the dealer by getting to 21 without going over!')

    deck = FrenchDeckOfCards()
    deck.shuffle()

    player1 = Player()
    player1.addchips(winnings=current_chips)
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
            print("______________________\n")
            player_busts(bet)
            break
   
    if player1.handvalue <= 21:    
        
        while dealer.handvalue < 17:
            dealer.addtohand(deck.deal())
        
        if dealer.handvalue > 21:
            print(f'Dealer Busts with a {dealer.handvalue}, player hand value is {player1.handvalue}.')
            print(f'Dealer Hand: {dealer.hand}\n')
            dealer_busts(bet)

        elif dealer.handvalue > player1.handvalue:
            print(f'Dealer wins with a {dealer.handvalue}, player has {player1.handvalue}')
            print(f'Dealer Hand: {dealer.hand}\n')
            dealer_wins(bet)

        elif dealer.handvalue < player1.handvalue:
            print(f'Player wins with a {player1.handvalue}, dealer has {dealer.handvalue}.')
            print(f'Dealer Hand: {dealer.hand}\n')
            player_wins(bet)
        else:
            print(f"Push, dealer has {dealer.handvalue} and player has {player1.handvalue}.")
            print(f'Dealer Hand: {dealer.hand}\n')

    print("______________________\n")
    current_chips = player1.chips
    print(f'player has {player1.chips} chips left.')

    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
