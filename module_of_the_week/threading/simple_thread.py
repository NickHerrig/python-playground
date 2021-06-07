import threading

def worker():
    print("worker")

def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker)
        threads.append(t)

    for thread in threads:
        thread.start()

if __name__=="__main__":
    main()

