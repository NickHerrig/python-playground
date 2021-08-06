import asyncio
import functools


def callback(n):
    print("callback ", n)


async def proc(loop):
    loop.call_later(2, callback, 1)
    loop.call_later(0.1, callback, 2)
    loop.call_soon(callback, 3)
    await asyncio.sleep(3)


def main():
    el = asyncio.get_event_loop()
    try:
        el.run_until_complete(proc(el))
    finally:
        el.close()


if __name__ == '__main__':
    main()

