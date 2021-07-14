from concurrent import futures
import os
import time
import sys
import requests
import string

import tqdm

CC = set()
A_Z = string.ascii_uppercase
CC.update(a+b for a in A_Z for b in A_Z)

BASE_URL = 'https://flagcdn.com/256x192/'

DEST_DIR = 'downloads/'

MAX_WORKERS = 40

def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def get_flag(cc):
    url = '{}/{cc}.png'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    if resp.status_code != 200:
        resp.raise_for_status()
    return resp.content

def download_one(cc):
    try:
        image = get_flag(cc)
    except requests.exceptions.HTTPError as exc:
        return

    save_flag(image, cc.lower() + '.png')
    return cc

def download_many(cc_list):
    with futures.ThreadPoolExecutor(max_workers=3) as ex:
        to_do = []
        for cc in sorted(cc_list):
            future = ex.submit(download_one, cc)
            to_do.append(future)

        results = []
        future_iter = futures.as_completed(to_do)
        future_iter = tqdm.tqdm(future_iter, total=len(cc_list))
        for future in future_iter:
            res = future.result()
            results.append(res)

    return len(results)


def main(download_many):
    t0 = time.time()
    count = download_many(CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)
