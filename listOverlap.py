
import random

randomListA = []
for i in range(0,16):
	x = random.randint(1,12)
	randomListA.append(x)

randomListB = []
for i in range(0,12):
	x = random.randint(1,16)
	randomListB.append(x)

print(randomListA)
print(randomListB)

overlapList = []

for num in randomListB:
	if num in randomListA and not num in overlapList:
		overlapList.append(num)

print(overlapList)



