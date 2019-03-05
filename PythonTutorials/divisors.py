
findDivisors = int(input('What number would you like to find divisors for? '))

divisorsList = []

for x in range(1,findDivisors+1):
	if findDivisors % x == 0:
		divisorsList.append(x)

print(divisorsList)

