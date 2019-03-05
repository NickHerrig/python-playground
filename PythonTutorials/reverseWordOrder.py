# Python3
# This reverse the order of words in a sentance

def reverse_sentance(sentance):
	result = sentance.split()
	result.reverse()
	newSentance = " ".join(result)
	return newSentance

usr_input = str(input("Please enter a senteance!  "))
print(reverse_sentance(usr_input))

