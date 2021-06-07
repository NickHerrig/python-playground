import random
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

def worker():
    pause = random.randint(1, 5) / 10
    logging.debug('Sleeping %0.2f', pause)
    time.sleep(pause)
    logging.debug('ending')

def main():
    for i in range(3):
        t = threading.Thread(target=worker, daemon=True)
        t.start()

    main_thread = threading.main_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        logging.debug('joining %s', t.getName())
        t.join()

if __name__=="__main__":
    main()
