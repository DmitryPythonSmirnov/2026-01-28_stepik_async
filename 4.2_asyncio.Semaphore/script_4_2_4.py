'''
https://stepik.org/lesson/2012891/step/4?unit=2041130

Задача 1: "Счетчик активных задач"
Условие:
Напишите программу, которая докажет, что семафор действительно ограничивает количество активных задач.
Создайте глобальные переменные active_tasks = 0 и max_active_tasks = 0.
Создайте семафор с лимитом 3.
Напишите корутину worker(), которая:
Захватывает семафор.
Увеличивает active_tasks, обновляет max_active_tasks, если текущее значение больше.
Ждет 0.1 секунды.
Уменьшает active_tasks.
В main запустите 10 задач worker() конкурентно.
После их завершения напечатайте итоговое значение max_active_tasks.
Входные данные:
Нет.
Выходные данные:
Несмотря на запуск 10 задач, максимальное количество одновременно работающих не должно превышать лимит семафора.
Sample Input:
Sample Output:
3
'''

import asyncio


active_tasks = 0
max_active_tasks = 0

semaphore = asyncio.Semaphore(3)

async def worker():
    global active_tasks
    global max_active_tasks

    async with semaphore:
        active_tasks += 1
        if active_tasks > max_active_tasks:
            max_active_tasks += 1
        await asyncio.sleep(0.1)
        active_tasks -= 1

async def main():
    tasks = [worker() for _ in range(10)]
    await asyncio.gather(*tasks)
    print(max_active_tasks)

asyncio.run(main())
