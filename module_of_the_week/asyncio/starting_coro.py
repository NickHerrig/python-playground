import asyncio

async def coroutine():
    print('inside coro')

def main():
    event_loop = asyncio.get_event_loop()

    try:
        print('starting coro')
        coro = coroutine()
        print('entering event loop')
        event_loop.run_until_complete(coro)

    finally:
        print('closing event loop')
        event_loop.close()


if __name__ == '__main__':
    main()

