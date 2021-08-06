import asyncio
import functools


def callback(arg, *, kwarg='default'):
    print(arg, kwarg)


async def proc(loop):
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwarg='nope')
    loop.call_soon(wrapped, 2)
    await asyncio.sleep(0.1)


def main():
    el = asyncio.get_event_loop()
    try:
        el.run_until_complete(proc(el))
    finally:
        el.close()


if __name__ == '__main__':
    main()

