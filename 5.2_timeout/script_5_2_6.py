'''
https://stepik.org/lesson/2012895/step/6?unit=2041134

Задача 3: "Гонка с тайм-аутом"
Условие:
Создайте программу, где две задачи соревнуются, и одна из них "отваливается" по тайм-ауту.
Создайте корутину worker(delay), которая ждет delay секунд и возвращает f"Завершено за {delay}с".
В main одновременно запустите две операции с помощью asyncio.gather(..., return_exceptions=True):
asyncio.wait_for(worker(0.1), timeout=0.2)
asyncio.wait_for(worker(0.3), timeout=0.2)
Результатом работы gather будет список. Напечатайте первый элемент списка (результат успешной задачи) и проверьте, является ли второй элемент исключением TimeoutError (isinstance(result[1], asyncio.TimeoutError)), выведя результат этой проверки (True или False).
Входные данные:
Нет.
Выходные данные:
Первая задача должна успеть, вторая — нет.
Sample Input:
Sample Output:
Завершено за 0.1с
True
'''

import asyncio

async def worker(delay):
    await asyncio.sleep(delay)
    return f'Завершено за {delay}с'

async def main():
    results = await asyncio.gather(
        asyncio.wait_for(worker(0.1), timeout=0.2),
        asyncio.wait_for(worker(0.3), timeout=0.2),
        return_exceptions=True
    )

    print(results[0])
    print(isinstance(results[1], asyncio.TimeoutError))

asyncio.run(main())
