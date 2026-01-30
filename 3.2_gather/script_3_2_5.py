'''
Задача 1: "Сбор и сумма"
Условие:
Напишите программу, которая использует asyncio.gather() для конкурентного получения двух чисел. Создайте две корутины:
- get_five(): возвращает (return) число 5.
- get_ten(): возвращает (return) число 10.

В main с помощью gather получите результаты этих двух корутин, сложите их и выведите на экран итоговую сумму.
Цель: Продемонстрировать, что gather может не только выполнять действия, но и собирать результаты для дальнейшей обработки.
'''

import asyncio

async def get_five():
    return 5

async def get_ten():
    return 10

async def main():
    results = await asyncio.gather(get_five(), get_ten())
    print(sum(results))


asyncio.run(main())