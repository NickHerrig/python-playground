"""
    >>> from inspect import getgeneratorstate
    >>> avgr = averager()
    >>> getgeneratorstate(avgr)
    'GEN_SUSPENDED'
    >>> avgr.send(10)
    10.0
    >>> avgr.send(20)
    15.0
    >>> avgr.send(30)
    20.0
"""
from priming import coroutine

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield average
        total += term
        count += 1
        average = total / count
