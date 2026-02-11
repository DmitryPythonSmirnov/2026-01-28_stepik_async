'''
https://stepik.org/lesson/2012893/step/7?unit=2041132

Задача 3: "Сбор ошибок"
Условие:
Используйте параметр return_exceptions=True у gather, чтобы собрать результаты всех задач, даже "упавших".
Создайте две корутины:
success_task(): возвращает строку "Успех".
failure_task(): вызывает исключение ValueError.
В main запустите обе корутины с помощью gather, установив return_exceptions=True.
Результатом будет список. Напечатайте первый элемент списка (результат успешной задачи) и проверьте, является ли второй элемент исключением ValueError (isinstance(result[1], ValueError)), выведя результат этой проверки (True или False).
Входные данные:
Нет.
Выходные данные:
Программа должна вывести результат успешной задачи и True на новой строке.
Sample Input:
Sample Output:
Успех
True
'''

import asyncio

async def success_task():
    return 'Успех'

async def failure_task():
    raise ValueError

async def main():
    results = await asyncio.gather(success_task(), failure_task(), return_exceptions=True)
    print(results[0])
    print(isinstance(results[1], ValueError))

asyncio.run(main())
