import time

from clockdeco import clock


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
