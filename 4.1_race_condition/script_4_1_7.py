'''
https://stepik.org/lesson/2012889/step/7?unit=2041127

Задача 4: "Единственный экземпляр"
Условие:
Напишите программу, которая гарантирует, что "тяжелая" инициализация ресурса произойдет только один раз.
Создайте глобальный Lock и флаг RESOURCE_INITIALIZED = False.
Напишите корутину initialize_resource(), которая:
Захватывает лок.
Проверяет, если RESOURCE_INITIALIZED равен False, то печатает "Инициализация ресурса...", ждет 0.1 секунды, и устанавливает флаг в True.
Если флаг уже True, корутина ничего не делает.
Блок async with должен использоваться в любом случае.
В main запустите 5 задач initialize_resource() конкурентно.
Входные данные:
Нет.
Выходные данные:
Несмотря на 5 одновременных запусков, сообщение об инициализации должно появиться только один раз.
'''

import asyncio

RESOURCE_INITIALIZED = False
TASKS_QTY = 5

async def initialize_resource(lock):
    global RESOURCE_INITIALIZED

    async with lock:
        if RESOURCE_INITIALIZED == False:
            print('Инициализация ресурса...')
            await asyncio.sleep(0.1)
            RESOURCE_INITIALIZED = True


async def main():
    lock = asyncio.Lock()

    tasks = [initialize_resource(lock) for _ in range(TASKS_QTY)]
    await asyncio.gather(*tasks)

asyncio.run(main())