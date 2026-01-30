'''
https://stepik.org/lesson/2012886/step/8?unit=2041125
Задача 4: "Порядок имеет значение"
Условие:
Эта задача доказывает, что gather сохраняет порядок результатов независимо от времени выполнения задач. Создайте две корутины:
slow_worker(): ждет 0.2 секунды и возвращает строку "Медленная работа завершена".
fast_worker(): ждет 0.1 секунды и возвращает строку "Быстрая работа завершена".
В main вызовите gather, передав ему сначала slow_worker(), а затем fast_worker(). Напечатайте итоговый список результатов.

Входные данные:
Нет.
Выходные данные:
Несмотря на то, что fast_worker завершится раньше, результат slow_worker должен стоять в списке первым, так как он был передан в gather первым.
Sample Input:
Sample Output:
['Медленная работа завершена', 'Быстрая работа завершена']
'''


import asyncio

async def slow_worker():
    await asyncio.sleep(0.2)
    return "Медленная работа завершена"

async def fast_worker():
    await asyncio.sleep(0.1)
    return "Быстрая работа завершена"

async def main():
    results = await asyncio.gather(slow_worker(), fast_worker())
    print(results)


asyncio.run(main())
