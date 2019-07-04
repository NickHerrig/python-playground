
class Player():

    def __init__(self, name='default', hand=[], chips=0):
        self.name = name
        self.hand = hand
        self.chips = chips

    def addchips(self, winnings=0):
        self.chips += winnings

    def losechips(self, losses=0):
        self.chips -= losses

    def addtohand(self, card):
        self.hand.append(card)

