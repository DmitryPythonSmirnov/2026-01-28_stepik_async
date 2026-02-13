'''
https://stepik.org/lesson/2012895/step/7?unit=2041134

Задача 4: "Тайм-аут со значением по умолчанию"
Условие:
Напишите функцию-обертку run_with_timeout(coro, timeout), которая запускает корутину coro с тайм-аутом timeout. В случае успеха она возвращает результат корутины, а в случае TimeoutError возвращает строку "Тайм-аут!".
Создайте корутину long_fetch(), которая ждет 1 секунду и возвращает "Данные получены".
Создайте корутину-обертку run_with_timeout.
В main вызовите run_with_timeout(long_fetch(), timeout=0.1) и напечатайте результат.
Входные данные:
Нет.
Sample Input:
Sample Output:
Тайм-аут!
'''


import asyncio

async def long_fetch():
    await asyncio.sleep(1)
    return 'Данные получены'

async def run_with_timeout(coro, timeout):
    try:
        # result = asyncio.gather(await asyncio.wait_for(coro, timeout=timeout))
        result = await asyncio.wait_for(coro, timeout=timeout)
        return result
    except asyncio.TimeoutError:
        return 'Тайм-аут!'


async def main():
    result = await run_with_timeout(long_fetch(), 0.1)
    print(result)


asyncio.run(main())
