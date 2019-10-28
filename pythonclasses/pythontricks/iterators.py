
class Repeater:
    def __init__(self, value, maxRepetitions):
        self.value = value
        self.maxRepetitions = maxRepetitions
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.maxRepetitions:
            raise StopIteration 
        self.count += 1
        return self.value

repeater = Repeater("hello", 23)
for word in repeater:
    print(word)
