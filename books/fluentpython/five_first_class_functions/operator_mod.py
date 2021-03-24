from functools import reduce
import operator

def fact(n):
    return reduce(operator.mul, range(1, n+1))

def main():
    print(fact(4))

    data = [
        ('apple', 'dooope', 36.933, (35.689722, 139.691667)),
        ('bannana', 'angry', 21.935, (28.613889, 77.208889)),
        ('coo', 'dog', 20.142, (19.433333, -99.133333)),
        ('dilby', 'cat', 20.104, (40.808611, -74.020386)),
    ]

    # sorting based on the second record of the list of tuples
    from operator import itemgetter
    for rec in sorted(data, key=itemgetter(1)):
        print(rec)

    # printing the tuple based on itemmgetter
    cc_name = itemgetter(1,0)
    for rec in data:
        print(cc_name(rec))


    # list of functions defined in operator
    funcs = [name for name in dir(operator) if not name.startswith('_')]
    print(funcs)


if __name__=="__main__":
    main()

