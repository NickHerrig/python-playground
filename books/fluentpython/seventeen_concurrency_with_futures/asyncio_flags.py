import os
import time
import sys
import asyncio

import aiohttp


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

def show(text):
    print(text, end=' ')
    sys.stdout.flush()

async def get_flag(cc):
    url = '{}/{cc}.png'.format(BASE_URL, cc=cc.lower())
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url)
        image = await resp.read()
    return image

async def download_one(cc):
    image = await get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.png')
    return cc

def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [ download_one(cc) for cc in sorted(cc_list) ]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()


def main(download_many):
    t0 = time.time()
    count = download_many(CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))

if __name__ == '__main__':
    main(download_many)

