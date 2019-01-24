# Python3
# This code utilizes booleans, equality testing and binary search to find if a number is in an ordered list.

import random


a = random.sample(range(9999), 1000)
a = sorted(a)
b = random.randint(1,9999)


print(a)
print(b)


def binarySearchFunction(orderedList, userNumber):
	middle = float(len(orderedList)/2)
	
	if userNumber < orderedList[int(middle)]:
		if userNumber in orderedList[:int(middle)]:
			return True
		else:
			return False
	else:
		if userNumber in orderedList[int(middle):]:
			return True
		else:
			return False


x = binarySearchFunction(a, b)
print(x)
