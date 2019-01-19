# python3
# This was created by Nick Herrig
# This code utilizes list comprehension to find even numbers in a list of numbers

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []

b = [num for num in a if num % 2 == 0]

print(b)

