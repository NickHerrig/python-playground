class stack:
    def __init__(self): 
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop (self):
        return self.items.pop()


