# Python3 
# This program will generate passwords using the random module


import random


def weak_pass(passlength):
	char = 'abcdefghijklmnopqrstuvwxyz'
	p = ''.join(random.sample(char, passlength))
	return p


def strong_pass(passlength):
	char = '!@#$%^&*()><?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	p = ''.join(random.sample(char, passlength))
	return p


usr_input = input("Would you like your password to have special characters? ")
length = int(input("How long do you want your password to be? "))

if usr_input == "yes":
	password = strong_pass(length)
	print("Your password is " + password)
else:
	password = weak_pass(length)
	print("Your password is " + password)




