class Demo:
    @classmethod
    def klassmeth(*args):
        return args
    @staticmethod
    def statmeth(*args):
        return args

def main():
    """
    classmethod gets the class as the first arg,
    this is useful for alternative constructors
    staticmethods isn't very useful, as a function in the module
    is probably more practical than tying it to a class..
    """

    print(Demo.klassmeth())
    print(Demo.klassmeth('spam'))

    print(Demo.statmeth())
    print(Demo.statmeth('spam'))

if __name__=="__main__":
    main()

