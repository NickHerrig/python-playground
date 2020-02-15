
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.color!r}, {self.mileage!r})'

    def __str__(self):
        return f'The Car color is {self.color} and mileage is {self.mileage}'

myBlueCar = Car('blue', 10000)
myGreenCar = Car('green', 100)

# The result of __str__ should be human readable.
print(repr(myBlueCar))
print(repr(myGreenCar))

# The result of __repr__ should be unabiguous and helpful to developers.
print(str(myBlueCar))
print(str(myGreenCar))
