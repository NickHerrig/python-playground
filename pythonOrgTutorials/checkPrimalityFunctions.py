# Python3

def findDivisors(findDivisorsNum):
	global divisorsList
	divisorsList = [x for x in range(1,findDivisorsNum) if findDivisorsNum % x == 0]
	return divisorsList	


usr_input = int(input("What number would you like to check primality for? "))


findDivisors(usr_input)


print(divisorsList)

if usr_input == 1:
	print(str(usr_input) + " is not a prime number!")
elif len(divisorsList) > 1:
	print(str(usr_input) + " is not a prime number!")
else:
	print(str(usr_input) + " is a prime number!")

