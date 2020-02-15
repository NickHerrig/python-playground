from time import time


class TimerClass:
    def __init__(self):
        self.description = "Sample Code Timer"

    def __enter__(self):
        self.timestart = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.timestop = time()
        print(f'{self.description}: {self.timestop - self.timestart}')

