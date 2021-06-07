import threading
import time

def worker():
    print(threading.current_thread().getName(), 'starting')
    time.sleep(0.2)
    print(threading.current_thread().getName(), 'exiting')

def service():
    print(threading.current_thread().getName(), 'starting')
    time.sleep(0.2)
    print(threading.current_thread().getName(), 'exiting')

def main():
    t = threading.Thread(name='my_service', target=service)
    w = threading.Thread(name='my_worker', target=worker)
    w2 = threading.Thread(target=worker)

    w.start()
    w2.start()
    t.start()


if __name__=="__main__":
    main()
