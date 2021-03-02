import collections

class StrKeyDict(collections.UserDict):
    """ A user friendly dictionary with out type checking """

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

if __name__=="__main__":
    test_class = StrKeyDict([('2', 'two'), ('4', 'four')])
    print(test_class[2])
    print(test_class['2'])
    print(test_class.get(1, 'NOPE'))
    print(2 in test_class)
    print(1 in test_class)
