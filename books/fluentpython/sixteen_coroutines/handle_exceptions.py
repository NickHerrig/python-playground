class DemoException(Exception):
   """An exception type for demos"""

def demo_exc_handling():
    print('-> starting the coroutine')
    while True:
        try:
            x = yield
        except DemoException:
            print("*** DemoException handled. Continuing.")
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('this line should never run.')


def main():
    from inspect import getgeneratorstate
    coro = demo_exc_handling()
    print(getgeneratorstate(coro))
    next(coro)
    print(getgeneratorstate(coro))
    coro.send(1000)
    print(getgeneratorstate(coro))
    coro.throw(DemoException)
    print(getgeneratorstate(coro))
    coro.close()
    print(getgeneratorstate(coro))


if __name__=='__main__':
    main()

