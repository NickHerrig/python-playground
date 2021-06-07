import threading

def worker(num):
    print("worker: %s" % num)

def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)

    for thread in threads:
        thread.start()

if __name__=="__main__":
    main()

