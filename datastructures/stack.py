class Stack:
    def __init__(self): 
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
