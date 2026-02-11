'''
https://stepik.org/lesson/2012893/step/8?unit=2041132

Задача 4: "Запрос на отмену"
Условие:
Напишите программу, которая отменяет долго выполняющуюся задачу.
Создайте корутину long_runner(), которая внутри блока try...except asyncio.CancelledError ждет 10 секунд. В блоке except она должна напечатать "Задача отменена!".
В main:
Запустите long_runner() с помощью create_task.
Подождите 0.1 секунды, чтобы задача успела запуститься.
Отмените задачу с помощью метода .cancel().
Дождитесь завершения задачи с помощью gather (с return_exceptions=True), чтобы "собрать" CancelledError и дать задаче время на обработку отмены.
Входные данные:
Нет.
Выходные данные:
Сообщение должно быть напечатано изнутри самой отменяемой задачи.
Sample Input:
Sample Output:
Задача отменена!
'''

import asyncio

async def long_runner():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print('Задача отменена!')
        raise  # Переподнимаем исключение, чтобы оно прошло дальше и попало в gather

async def main():
    task = asyncio.create_task(long_runner())
    await asyncio.sleep(0.1)
    task.cancel()
    await asyncio.gather(task, return_exceptions=True)
    # results = await asyncio.gather(task, return_exceptions=True)  # Можем собрать результаты


asyncio.run(main())
