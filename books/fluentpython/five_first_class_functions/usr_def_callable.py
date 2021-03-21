import random

class BingoCage:
    """A class representing a Bingo Cage"""

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty bing cage.")

    def __call__(self):
        return self.pick()


def main():
    cage = BingoCage(range(10))
    print(cage)
    print(cage())
    print(cage.pick())
    print(callable(cage))


if __name__=="__main__":
    main()

