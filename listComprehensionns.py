# python3
# This was created by Nick Herrig
# This code utilizes list comprehension to find even numbers in a list of numbers

import random

a = []
list_length = random.randint(5,15)
while len(a) < list_length:
	a.append(random.randint(1,75))

b = []

b = [num for num in a if num % 2 == 0]

print(b)

