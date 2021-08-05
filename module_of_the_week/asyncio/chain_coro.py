import asyncio

async def outer():
    print('inside outer')
    print('waiting on one')
    result1 = await phase1()
    print('waiting on two')
    result2 = await phase2(result1)
    return (result1, result2)


async def phase1():
    print('inside one')
    return 'result1'


async def phase2(arg):
    print('inside two')
    return arg + 'result2'


def main():
    event_loop = asyncio.get_event_loop()

    try:
        return_val = event_loop.run_until_complete(
            outer()
        )
        print('value returned: ', return_val)

    finally:
        event_loop.close()


if __name__ == '__main__':
    main()

