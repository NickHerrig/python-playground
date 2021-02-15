from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__=="__main__":
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    v3 = v1 + v2
    v4 = v1 * 3
    v5 = Vector(0, 0)

    print("__mul__ dunder method: ", v4)
    print("__repr__ dunder method: ", v3)
    print("__abs__ dunder method: ", abs(v3))
    print("__bool__ dunder method: ", bool(v5))

