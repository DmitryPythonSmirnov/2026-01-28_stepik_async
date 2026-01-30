'''
https://stepik.org/lesson/2012885/step/5?unit=2041124
Задача 2: "Правильное ожидание"

Условие:
Исправьте проблему из предыдущей задачи. Напишите программу с той же корутиной print_message (ждет 0.1 сек и печатает "Задача выполнена!"). В main запустите ее с помощью asyncio.create_task и сохраните возвращенный объект Task в переменную. После этого main должна напечатать "Задача запущена, ждем...", а затем дождаться (await) завершения сохраненной задачи.
'''


import asyncio

async def print_message():
    print('Задача запущена, ждем...')
    await asyncio.sleep(0.1)
    print('Задача выполнена!')

async def main():
    await asyncio.create_task(print_message())


asyncio.run(main())
