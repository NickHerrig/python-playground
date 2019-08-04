from contextlib import contextmanager
from time import time

@contextmanager
def timerfunc():
    start = time()
    yield
    ellapsed_time = time() - start

    print(f'Program Took {ellapsed_time}')
        

