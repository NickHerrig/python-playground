import time
from clockdeco_param import clock

@clock('{name}: {elapsed}s')
def snooze(seconds):
    time.sleep(seconds)

@clock('{name}({args}) dt={elapsed:0.3f}s')
def snoozed(seconds):
    time.sleep(seconds)

def main():
    for i in range(3):
        snooze(.123)

    for i in range(3):
        snoozed(.123)

if __name__=="__main__":
    main()

