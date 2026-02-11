'''
https://stepik.org/lesson/2012893/step/6?unit=2041132

Задача 2: "Сбой в gather"
Условие:
Продемонстрируйте поведение asyncio.gather() по умолчанию при возникновении ошибки.
Создайте две корутины:
good_worker(): ждет 1 секунду.
bad_worker(): ждет 0.1 секунды и вызывает RuntimeError.
В main запустите обе корутины с помощью asyncio.gather().
Оберните вызов gather в try...except и поймайте RuntimeError.
В блоке except напечатайте "Поймал ошибку от gather!".
Входные данные:
Нет.
Выходные данные:
Программа должна доказать, что gather прервал работу и "пробросил" исключение.
Sample Input:
Sample Output:
Поймал ошибку от gather!
'''


import asyncio


async def good_worker():
    await asyncio.sleep(1)

async def bad_worker():
    await asyncio.sleep(0.1)
    raise RuntimeError


async def main():
    try:
        await asyncio.gather(good_worker(), bad_worker())
    except RuntimeError:
        print('Поймал ошибку от gather!')


asyncio.run(main())
