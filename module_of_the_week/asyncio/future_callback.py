import asyncio
import functools


def callback(future, n):
    print(future, n)


async def register_callbacks(future):
    future.add_done_callback(functools.partial(callback, n=1))
    future.add_done_callback(functools.partial(callback, n=3))


async def main(future):
    await register_callbacks(future)
    all_done.set_result('result')


if __name__ == '__main__':

    event_loop = asyncio.get_event_loop()
    try:
        all_done = asyncio.Future()
        event_loop.run_until_complete(main(all_done))
    finally:
        event_loop.close()
