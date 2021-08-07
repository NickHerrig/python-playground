import asyncio


def mark_done(future, result):
    future.set_result(result)


def main():
    event_loop = asyncio.get_event_loop()

    try:
        all_done = asyncio.Future()
        event_loop.call_soon(mark_done, all_done, 'result')
        result = event_loop.run_until_complete(all_done)
    finally:
        event_loop.close()

    print('future result', result)



if __name__ == '__main__':
    main()

