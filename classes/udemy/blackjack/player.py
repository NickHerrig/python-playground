
class Player():

    def __init__(self):
        self.chips = 0
        self.hand = []
        self.handvalue = 0

    def addchips(self, winnings=0):
        self.chips += winnings

    def losechips(self, losses=0):
        self.chips -= losses

    def addtohand(self, card):
        self.hand.append(card)
        self.addhandvalue()

    def addhandvalue(self):
        self.handvalue = 0
        values = {'2':2,
              '3':3,
              '4':4,
              '5':5,
              '6':6,
              '7':7,
              '8':8,
              '9':9,
              '10':10,
              'J':10,
              'Q':10,
              'K':10,
              'A':11}
        cards = [self.hand[i].rank for i in range(len(self.hand))]
        for card in cards:
            self.handvalue += values[card]
