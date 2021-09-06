from urllib.request import urlopen
import warnings
import os
import json
from pprint import pprint

from explore import FrozenJSON


URL = 'https://random-data-api.com/api/beer/random_beer?size=5'
JSON = 'data/beer.json'


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)


def main():
    '''Description of the function'''
    raw_json = load()
    feed = FrozenJSON(raw_json)
    print(feed)



if __name__ == '__main__':
    main()

