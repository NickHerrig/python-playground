def simple_coro2(a):
    print("-> Started: a =", a)
    b = yield a
    print("-> Received: b =", b)
    c = yield a + b
    print("-> Received: c =", c)

def main():
    '''Description of the function'''
    from inspect import getgeneratorstate
    x = my_coro2 = simple_coro2(14)
    print(x)
    print(getgeneratorstate(my_coro2))
    x = my_coro2.send(None)
    print(x)
    print(getgeneratorstate(my_coro2))
    x = my_coro2.send(28)
    print(x)
    print(getgeneratorstate(my_coro2))
    x = my_coro2.send(99)
    print(x)
    print(getgeneratorstate(my_coro2))


if __name__=='__main__':
    main()

