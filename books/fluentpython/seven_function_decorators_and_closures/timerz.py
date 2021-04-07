import time


def clock(func):
    def clocked(*args):
        t0 =  time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if  n < 2 else n*factorial(n-1)


def main():
    snooze(2)
    factorial(3)

if __name__=="__main__":
    main()
