# Python3

import sys


def compareResponse(playerA, playerB):
	if playerA == playerB:
		print("it's a tie!")
	elif playerA == "Rock":
		if playerB == "Scissors":
			print("Player one Wins!")
		elif playerB == "Paper":
			print("Player two wins!")
	elif playerA == "Paper":
		if playerB == "Rock":
			print("Player one wins!")
		elif playerB == "Scissors":
			print("Player two wins!")
	elif playerA == "Scissors":
		if playerB == "Rock":
			print("Player two wins!")
		elif playerB == "Paper":
			print("Player one wins!")
	else:
		print("invalid input")
		sys.exit()

while True:
	usr_command = input("type quit to stop playing.")
	if usr_command == "quit":
		break
	else:
		a = str(input("Player One: Rock, Paper, or Scissors?"))
		b = str(input("Player Two: Rock, Paper, or Scissors?"))
		compareResponse(a, b)
