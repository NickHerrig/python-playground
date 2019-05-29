class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.insert(0,value)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
