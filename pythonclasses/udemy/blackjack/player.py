
class Player():

    def __init__(self):
        self.chips = 100
        self.hand = []

    def addchips(self, winnings=0):
        self.chips += winnings

    def losechips(self, losses=0):
        self.chips -= losses

    def addtohand(self, card):
        self.hand.append(card)

