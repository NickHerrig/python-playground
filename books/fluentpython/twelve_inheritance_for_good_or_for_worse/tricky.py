class DoppleDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

import collections
class CorrectDict(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

def main():
    d = DoppleDict(one=1)
    print(d)
    d['two'] = 2
    d.update(three=3)
    print(d)

    print("Correct Dict")
    d = CorrectDict(one=1)
    print(d)
    d['two'] = 2
    d.update(three=3)
    print(d)

if __name__=='__main__':
    main()
