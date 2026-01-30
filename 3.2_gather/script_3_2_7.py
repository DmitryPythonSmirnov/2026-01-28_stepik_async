'''
https://stepik.org/lesson/2012886/step/7?unit=2041125
Задача 3: "Сбор разных типов"
Условие:
Напишите корутину fetch_data(data), которая возвращает (return) полученное значение data без каких-либо задержек.
В main с помощью asyncio.gather() одновременно "получите" три значения: строку "apple", число 100 и True. Сохраните результат работы gather в переменную и напечатайте этот результат (список).

Входные данные:
Нет.

Выходные данные:
Программа должна вывести на экран список, содержащий результаты в том же порядке, в котором корутины были переданы в gather.
'''


import asyncio

async def fetch_data(data):
    return data

async def main():
    results = await asyncio.gather(fetch_data('apple'), fetch_data(100), fetch_data(True))
    print(results)


asyncio.run(main())
