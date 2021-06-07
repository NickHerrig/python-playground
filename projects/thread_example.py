import time
import threading


serial_lock = threading.Lock()

def collect_data():
    while True:
        serial_lock.acquire()
        print("collecting serial data for one second....")
        time.sleep(1)
        serial_lock.release()
        time.sleep(5)


def main():

    print("starting prog....")

    data_thread = threading.Thread(target=collect_data)
    data_thread.start()

    while True:
        serial_lock.acquire()
        print("Doing work for ten seconds...")
        time.sleep(10)
        serial_lock.release()
        time.sleep(60)


if __name__=="__main__":
    main()

