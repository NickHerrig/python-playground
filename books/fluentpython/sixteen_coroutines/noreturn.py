"""
  >>> a = returnaverager()
  >>> a.send(10)
  >>> a.send(None)
  Traceback (most recent call last):
  ...
  StopIteration: Result(count=1, result=10.0)
"""

from priming import coroutine
from collections import namedtuple

Result = namedtuple('Result', 'count result')

@coroutine
def returnaverager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)

def main():

  a = returnaverager()
  a.send(None)
  a.send(10)
  a.send(10)
  try:
      a.send(None)
  except StopIteration as exc:
      result = exc.value
  print(result)

if __name__ == '__main__':
    main()
