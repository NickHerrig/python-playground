
userNumber = int(input("please enter a number: "))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = []

for num in a:
	if num < userNumber:
		b.append(num)

print(b)


