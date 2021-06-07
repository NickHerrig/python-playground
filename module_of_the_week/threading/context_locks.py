import threading
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

def collect_data_forever(lock):
    while True:
        with lock:
            logging.debug('collecting data...')
            time.sleep(1)
            logging.debug('finished collecting data...')
        time.sleep(5)


def main():
    lock = threading.Lock()
    w = threading.Thread(target=collect_data_forever, args=(lock,))
    w.start()

    while True:
        with lock:
            logging.debug('doing other work...')
            time.sleep(10)
            logging.debug('finished other work...')

        time.sleep(10)


if __name__=="__main__":
    main()

