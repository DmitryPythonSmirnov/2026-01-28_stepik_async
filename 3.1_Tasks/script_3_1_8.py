'''
https://stepik.org/lesson/2012885/step/8?unit=2041124
Задача 5: "Асинхронный таймер"

Условие:
Напишите корутину alarm(seconds, name), которая ждет seconds секунд и затем печатает "{name} ALARM!".
В main:
1. Напечатайте "Таймеры запущены".
2. Одновременно запустите два "будильника" с помощью create_task: один на 0.2 секунды и c name Первый, другой на 0.1 секунды и name = Второй.
3. Дождитесь завершения обеих задач.

Входные данные:
Нет.

Выходные данные:
Поскольку задачи выполняются конкурентно, сообщение "ALARM!" должно появиться дважды, но программа завершится примерно через 0.2 секунды (время самой долгой задачи).
Таймеры запущены
Второй ALARM!
Первый ALARM!
'''


import asyncio

async def alarm(seconds, name):
    await asyncio.sleep(seconds)
    print(f'{name} ALARM!')


async def main():
    print('Таймеры запущены')
    tasks = []
    task1 = asyncio.create_task(alarm(0.2, 'Первый'))
    task2 = asyncio.create_task(alarm(0.1, 'Второй'))

    await task1
    await task2


asyncio.run(main())
