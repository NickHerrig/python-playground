import asyncio


def mark_done(future, result):
    future.set_result(result)


async def main(loop):

    all_done = asyncio.Future()
    loop.call_soon(mark_done, all_done, 'result')
    result = await all_done
    print('future result', result)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop))
    finally:
        event_loop.close()
