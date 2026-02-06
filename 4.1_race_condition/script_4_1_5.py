'''
https://stepik.org/lesson/2012889/step/5?unit=2041127

Задача 2: "Безопасный счетчик"
Условие:
Напишите программу, которая безопасно инкрементирует общий счетчик.
Создайте глобальную переменную COUNTER = 0.
Создайте глобальный asyncio.Lock().
Напишите корутину increment(), которая захватывает лок и увеличивает COUNTER на 1.
В main запустите 100 задач increment() конкурентно с помощью asyncio.gather().
После завершения всех задач напечатайте итоговое значение COUNTER.
Цель: Доказать, что при использовании Lock ни одно из приращений не "теряется".
'''

import asyncio

counter = 0
TASKS_QTY = 100

lock = asyncio.Lock()

async def increment():
    global counter

    async with lock:
        temp_counter = counter
        await asyncio.sleep(0)
        counter = temp_counter + 1


async def main():
    tasks = [increment() for _ in range(TASKS_QTY)]
    await asyncio.gather(*tasks)
    print(counter)

asyncio.run(main())
