class Stack:
    def __init__(self): 
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            raise Exception("Nothing in stack")

    def size(self):
        return len(self.items)
