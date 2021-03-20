def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)

def main():
    print(factorial.__doc__)
    fact = factorial
    print(fact(5))

    my_list = list(map(fact, range(11)))
    print(my_list)

if __name__=="__main__":
    main()

