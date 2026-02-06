'''
https://stepik.org/lesson/2012889/step/6?unit=2041127

Задача 3: "Защита критической секции"
Условие:
Напишите программу, которая имитирует небезопасную операцию "прочитай-измени-запиши" и исправляет ее с помощью Lock.
Создайте глобальную переменную SHARED_RESOURCE = 0.
Напишите корутину unsafe_worker(), которая:
Читает SHARED_RESOURCE в локальную переменную.
Ждет 0.01 секунды (await asyncio.sleep(0.01)).
Записывает локальная_переменная + 1 обратно в SHARED_RESOURCE.
В main запустите 10 таких воркеров конкурентно. Без блокировки результат будет неверным! Ваша задача — добавить в main объект Lock и передать его в unsafe_worker, чтобы защитить "критическую секцию" (все три шага) и получить корректный результат.
Напечатайте итоговое значение SHARED_RESOURCE.
'''

import asyncio

SHARED_RESOURCE = 0
TASKS_QTY = 10

async def unsafe_worker(lock):
    global SHARED_RESOURCE

    async with lock:
        temp_counter = SHARED_RESOURCE
        await asyncio.sleep(0.01)
        SHARED_RESOURCE = temp_counter + 1


async def main():
    lock = asyncio.Lock()

    tasks = [unsafe_worker(lock) for _ in range(TASKS_QTY)]
    await asyncio.gather(*tasks)
    print(SHARED_RESOURCE)

asyncio.run(main())