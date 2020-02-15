from collections import namedtuple

# variables with _ in front are meant for internal use.

_species = "walleye"
print(_species)


# variables with trailing _ are used to avoid naming conficts with python keywords

print_ = "hello world"
print(print_)


# "__var" triggers name mangling in a class context
# also, not the dunder, or special/magic init method

class Fishweight: 
    def __init__(self):
        self.__species = "walleye"

fish = Fishweight()
print(fish._Fishweight__species)


# _ can be used as a 'throw away' variable.
Fish = namedtuple('Fish', 'species color')
my_fish = Fish('walleye', 'blue')
spec, _ = my_fish
print(spec)
print(_)
