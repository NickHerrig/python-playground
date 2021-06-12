import logging
from configparser import ConfigParser, NoOptionError
import time


logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


def main():
    """Description of the function"""
    parser = ConfigParser()
    if not parser.read('logging.ini'):
        sys.exit("Configuration file doesn't exist")


    debug = parser.getboolean('application', 'debug')

    if debug:
        logging.getLogger().level = logging.DEBUG

    logging.info("Starting the program")

    for i in range(10):
        logging.debug(f"This is debug message {i}")

    logging.info("Finished the program")


if __name__=="__main__":
    main()

