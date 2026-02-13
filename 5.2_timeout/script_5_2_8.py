'''
https://stepik.org/lesson/2012895/step/8?unit=2041134

'''

import asyncio

async def inner():
    await asyncio.sleep(10)


async def middle():
    try:
        await asyncio.wait_for(inner(), timeout=2)
    except asyncio.TimeoutError:
        print('Сработал тайм-аут в middle')


async def main():
    try:
        await asyncio.wait_for(middle(), timeout=1)
    except asyncio.TimeoutError:
        print('Сработал внешний тайм-аут')

asyncio.run(main())
