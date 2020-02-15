import array
import timeit

symbols = '@#$%^%$'
my_tuple = tuple(ord(symbol) for symbol in symbols)

my_array = array.array("I", (ord(symbol) for symbol in symbols))

print(my_tuple)
print(my_array)

