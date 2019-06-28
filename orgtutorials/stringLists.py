
word = str(input("Enter a word to check if it's a palindrome. "))
flipWord = word[-1::-1]

if word == flipWord:
	print("The world " + word + " is a palindrome!")
else:
	print("The world " + word + " is not a palindrome.")
