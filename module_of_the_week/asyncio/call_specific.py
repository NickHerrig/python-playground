import asyncio
import time


def callback(n, loop):
    print("callback ", n, loop.time())


async def proc(loop):
    now = loop.time()
    print("clock ", time.time())
    print("loop ", now)
    loop.call_at(now + 1, callback, 1, loop)
    loop.call_at(now + 2, callback, 1, loop)
    loop.call_soon(callback, 3, loop)
    await asyncio.sleep(5)


def main():
    el = asyncio.get_event_loop()
    try:
        el.run_until_complete(proc(el))
    finally:
        el.close()


if __name__ == '__main__':
    main()

