from configparser import ConfigParser
import sys

def main():

    parser = ConfigParser()
    if not parser.read('doesnt_exist.ini'):
        sys.exit("Configuration file doesn't exist")


if __name__=="__main__":
    main()

