import asyncio
import logging
import threading

from kasa import SmartPlug
from kasa.exceptions import SmartDeviceException


pump = SmartPlug('192.168.0.51')

def update_pump_status():
    threading.Timer(5, update_pump_status).start()
    try:
        asyncio.run(pump.update())
    except SmartDeviceException as e:
        logging.error("Unable to update pump... trying again in 5 seconds")
        logging.error(f"exception: {e}")

    print(pump.is_on)


if __name__ == "__main__":
    update_pump_status()
