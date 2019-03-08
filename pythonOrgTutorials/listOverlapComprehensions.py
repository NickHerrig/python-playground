# Python3

import random

listOne = random.sample(range(1,30),12)
listTwo = random.sample(range(1,30),18)

newList = [a for a in listOne if a in listTwo]
