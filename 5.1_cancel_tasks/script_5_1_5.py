'''
https://stepik.org/lesson/2012893/step/5?unit=2041132

Задача 1: "Простой перехват ошибки"
Условие:
Напишите программу, которая демонстрирует базовую обработку исключений в асинхронном коде.
Создайте корутину raiser(), которая вызывает исключение ValueError с сообщением "Произошла ошибка!".
В главной корутине main вызовите raiser() внутри блока try...except.
В блоке except поймайте ValueError и напечатайте его сообщение.
Входные данные:
Нет.
Выходные данные:
Программа должна напечатать сообщение из пойманного исключения.
Sample Input:
Sample Output:
Произошла ошибка!
'''

import asyncio


async def raiser():
    raise ValueError('Произошла ошибка!')

async def main():
    try:
        await asyncio.gather(raiser())
    except ValueError as e:
        print(e)


asyncio.run(main())
