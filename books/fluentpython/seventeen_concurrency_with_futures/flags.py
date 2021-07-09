import os
import time
import sys

import requests

CC = ['cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'de', 'dj',
      'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'eh', 'er',
      'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr',
      'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', ]

BASE_URL = 'https://flagcdn.com/256x192/'

DEST_DIR = 'downloads/'

def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def get_flag(cc):
    url = '{}/{cc}.png'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content

def show(text):
    print(text, end=' ')
    sys.stdout.flush()

def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.png')

    return len(cc_list)

def main(download_many):
    t0 = time.time()
    count = download_many(CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))

if __name__ == '__main__':
    main(download_many)

