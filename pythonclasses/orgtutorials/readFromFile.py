# Python3
# Read a file and returns how many of each name there is

counter_dict = {}
with open('namesList.txt', 'r') as open_file:
	line = open_file.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = open_file.readline()


print(counter_dict)

