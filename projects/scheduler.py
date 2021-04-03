import schedule
import time

def job():
    print("Some sort of scheduled task...")

schedule.every().day.at("19:35").do(job)

def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()
