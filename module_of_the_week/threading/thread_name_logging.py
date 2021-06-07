import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

def worker():
    logging.debug('starting')
    time.sleep(0.2)
    logging.debug('exiting')

def service():
    logging.debug('starting')
    time.sleep(0.2)
    logging.debug('exiting')

def main():
    t = threading.Thread(name='my_service', target=service)
    w = threading.Thread(name='my_worker', target=worker)
    w2 = threading.Thread(target=worker)

    w.start()
    w2.start()
    t.start()


if __name__=="__main__":
    main()
