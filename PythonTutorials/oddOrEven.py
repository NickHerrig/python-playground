
number = int(input("Please enter a number. "))
divideByNumber =  int(input("What would you like to divide it by? "))


modValue = number % divideByNumber

if modValue == 0:
	print(str(number) + " divides evenly into " + str(divideByNumber))
else:
	print("those numbers do not divide evenly")

