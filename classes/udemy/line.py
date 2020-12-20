from math import sqrt
from math import pow

class Line:
    
    def __init__(self, coordinate1, coordinate2):
        self.x1, self.y1 = coordinate1
        self.x2, self.y2 = coordinate2

    def distance(self):
        return sqrt(pow((self.x2 - self.x1),2) + pow((self.y2 - self.y1),2))           

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)
