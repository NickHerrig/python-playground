import asyncio

async def coroutine():
    print('inside coro')
    return 'result'

def main():
    event_loop = asyncio.get_event_loop()

    try:
        return_val = event_loop.run_until_complete(
            coroutine()
        )
        print('value returned: ', return_val)

    finally:
        event_loop.close()


if __name__ == '__main__':
    main()

