import schedule
import time
import logging
import asyncio
from kasa import SmartPlug, SmartDeviceException


def switch_plug():
    p = SmartPlug("192.168.0.51")

    try:
        asyncio.run(p.update())
    except SmartDeviceException as e:
        logging.error("Could not reach smart plug...")
        sys.exit(e)

    if p.is_on:
        asyncio.run(p.turn_off())
    else:
        asyncio.run(p.turn_on())

    asyncio.run(p.update())
    print("The plug is on: ",  p.is_on)


schedule.every(2).minutes.do(switch_plug)

def main():
    switch_plug()

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()
