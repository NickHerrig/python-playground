# Python3
# this code takes in a list and returns another list without duplicates

def remove_duplicates(x):
	return list(set(x))

myList = [1, 1, 2, 2, 3, 6]
print(myList)
print(remove_duplicates(myList))


