from concurrent import futures

from flags import get_flag, save_flag, show, main

MAX_WORKERS = 40

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.png')
    return cc

def download_many(cc_list):
    cc_list = cc_list[:5]
    with futures.ProcessPoolExecutor() as ex:
        to_do = []
        for cc in sorted(cc_list):
            future = ex.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


if __name__ == '__main__':
    main(download_many)

