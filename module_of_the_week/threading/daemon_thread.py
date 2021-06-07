import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

def main():
    d = threading.Thread(name='daemon', target=daemon, daemon=True)
    t = threading.Thread(name='non-daemon', target=non_daemon)

    d.start()
    t.start()


if __name__=="__main__":
    main()
