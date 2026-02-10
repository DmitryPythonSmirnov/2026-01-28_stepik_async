'''
https://stepik.org/lesson/2012891/step/8?unit=2041130

Задача 5: "Подготовка и работа"
Условие:
Напишите программу, которая докажет, что семафор ограничивает только определенную часть работы.
Создайте корутину worker(worker_id, semaphore).
Внутри нее должны быть две фазы: "Подготовка" (имитируется через await asyncio.sleep(0.1)) и "Работа" (имитируется через await asyncio.sleep(0.2)).
Только фаза "Работы" должна быть защищена семафором с лимитом 2.
Вам нужно подсчитать, сколько воркеров одновременно находилось в фазе "Подготовки", и сколько — в фазе "Работы".
Для этого:
Создайте глобальные счетчики и переменные для максимумов: preparing_count, max_preparing, working_count, max_working.
Используйте asyncio.Lock для безопасного изменения этих счетчиков.
Внутри worker увеличивайте/уменьшайте соответствующие счетчики до и после каждой фазы.
В main запустите 4 воркера.
После их завершения, выведите два числа на отдельных строках: сначала max_preparing, затем max_working.
Входные данные:
Нет.
Выходные данные:
Программа должна показать, что в фазе подготовки могли находиться все 4 воркера, а в фазе работы — не более 2.
Sample Input:
Sample Output:
4
2
'''

import asyncio

semaphore = asyncio.Semaphore(2)
lock = asyncio.Lock()

preparing_count = 0
max_preparing = 0
working_count = 0
max_working = 0

async def worker(worker_id, semaphore):
    global preparing_count
    global max_preparing
    global working_count
    global max_working

    # Подготовка
    async with lock:
        preparing_count += 1
        if preparing_count > max_preparing:
            max_preparing = preparing_count

    await asyncio.sleep(0.1)

    async with lock:
        preparing_count -= 1



    async with semaphore:
        async with lock:
            working_count += 1
            if working_count > max_working:
                max_working = working_count

        # Работа
        await asyncio.sleep(0.2)

        async with lock:
            working_count -= 1


async def main():
    tasks = [worker(i, semaphore) for i in range(4)]

    await asyncio.gather(*tasks)

    print(max_preparing)
    print(max_working)


asyncio.run(main())
