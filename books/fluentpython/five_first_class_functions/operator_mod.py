from functools import reduce
import operator

def fact(n):
    return reduce(operator.mul, range(1, n+1))

def main():
    print(fact(4))

    metro_data = [
        ('apple', 'dilby', 36.933, (35.689722, 139.691667)),
        ('bannana NCR', 'apple', 21.935, (28.613889, 77.208889)),
        ('coo', 'dog', 20.142, (19.433333, -99.133333)),
        ('dilby', 'cat', 20.104, (40.808611, -74.020386)),
    ]

    from operator import itemgetter
    for data in sorted(metro_data, key=itemgetter(0)):
        print(data)


if __name__=="__main__":
    main()

