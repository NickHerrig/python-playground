

name = input('What is your name? ')
age = input('What is your age? ')
repeateFactor = input('how much should i repeat the statement? ')



yearsUntilHundred = 100 - int(age)
year = 2019 + yearsUntilHundred

for x in range(int(repeateFactor)):
	print( name + " you will turn 100 in the year " + str(year))

