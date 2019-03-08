# python3

import random
import sys 

ranNum = random.randint(1, 9)
counter = 0

def countTries():
	global counter
	counter = counter + 1
	return counter


while True:
	usr_command = input("type exit to stop playing. ")
	if usr_command == "exit":
		break
	else:
		numberGuess = int(input("Guess a number between 1 and 9! "))
		if numberGuess < ranNum:
			print("The random number is greater than " + str(numberGuess))
			countTries()
		elif numberGuess > ranNum:
			print("The random number is less than " + str(numberGuess))
			countTries()
		else:
			countTries()
			print("Correct, your guess " + str(numberGuess) + " is equal to " + str(ranNum))
			print("you guessed in " + str(counter) + " tries!")
			sys.exit()
