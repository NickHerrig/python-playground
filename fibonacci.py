# Python3 
# asks a user how many numbers in the fibonacci sequence to generate

usr_input = int(input("How many numbers in the fibonacci sequence should be generate? "))

def generate_fibonacci(x):
	global fibonacciList
	
	if x == 0:
		fibonacciList = [0]
	elif x == 1:
		fibonacciList = [1]
	elif x == 2:
		fibonacciList = [1, 1]
	elif x > 2: 
		fibonacciList = [1, 1]
		while x-2 > 0:
			y = fibonacciList[-1] + fibonacciList[-2]
			fibonacciList.append(y)
			x -= 1
	return fibonacciList
generate_fibonacci(usr_input)
print(fibonacciList)
