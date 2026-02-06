'''
https://stepik.org/lesson/2012889/step/4?unit=2041127

Задача 1: "Упорядоченный вывод"
Условие:
Напишите программу, которая демонстрирует, как Lock заставляет задачи ждать своей очереди. Создайте две корутины:
worker_a(lock): Захватывает lock, печатает "Работа A: Начало", ждет 0.1 секунды, печатает "Работа A: Конец".
worker_b(lock): Захватывает lock, печатает "Работа B: Начало", ждет 0.1 секунды, печатает "Работа B: Конец".
В main создайте один объект Lock и запустите обе корутины конкурентно с помощью asyncio.gather(), передав им один и тот же lock.
Цель: Убедиться, что worker_b не сможет начать работу, пока worker_a не завершится полностью.
Входные данные:
Нет.
Выходные данные:
Вывод должен быть строго последовательным, блок за блоком: (Буквы англ A B)
'''

import asyncio


async def worker_a(lock):

    async with lock:
        print('Работа A: Начало')
        await asyncio.sleep(0.1)
        print('Работа A: Конец')


async def worker_b(lock):

    async with lock:
        print('Работа B: Начало')
        await asyncio.sleep(0.1)
        print('Работа B: Конец')


async def main():
    lock = asyncio.Lock()

    await asyncio.gather(worker_a(lock), worker_b(lock))


asyncio.run(main())
