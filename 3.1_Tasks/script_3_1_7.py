'''
https://stepik.org/lesson/2012885/step/7?unit=2041124
Задача 4: "Список задач"

Условие:
Напишите программу для управления несколькими однотипными задачами. Создайте корутину worker(n), которая печатает Задача {n} выполнена..
В main:
1. Создайте пустой список для хранения задач.
2. В цикле for i in range(3):
- Создайте задачу для корутины worker(i) с помощью create_task.
- Добавьте созданную задачу в список.
3. Напечатайте "Все задачи запущены.".
4. В другом цикле for пройдитесь по списку задач и дождитесь (await) завершения каждой.
'''


import asyncio

async def worker(n):
    print(f'Задача {n} выполнена.')


async def main():
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(i))
        tasks.append(task)
    print('Все задачи запущены.')

    for task in tasks:
        await task


asyncio.run(main())
