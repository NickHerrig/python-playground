from configparser import ConfigParser, NoOptionError

def main():
    """Description of the function"""
    parser = ConfigParser()
    if not parser.read('simple.ini'):
        sys.exit("Configuration file doesn't exist")

    print(parser.sections())

    try:
        name = parser['default']['name']
    except KeyError:
        print("could not find name in config file")

    try:
        name = parser.get('default', 'nope')
    except NoOptionError:
        print("could not find name in config file")

    name = parser.get('default', 'url')
    print(name)




if __name__=="__main__":
    main()

