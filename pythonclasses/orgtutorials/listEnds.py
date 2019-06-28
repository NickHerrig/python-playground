# Python3
# this python code takes a list of number and returns a new list of the first and last element

def listEnd(x):
	global newList
	newList = [x[0], x[-1]]
	return newList

a = [5, 10, 15, 20, 25]
listEnd(a)
print(newList)

