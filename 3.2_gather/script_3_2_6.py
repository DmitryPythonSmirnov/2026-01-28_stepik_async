'''
https://stepik.org/lesson/2012886/step/6?unit=2041125
Задача 2: "Гонка со временем"
Условие:
Напишите программу, чтобы продемонстрировать эффективность gather. Создайте корутину timer(delay, value), которая ждет delay секунд и затем возвращает значение value.
В main с помощью gather одновременно запустите два таймера:
timer(0.2, "A")
timer(0.1, "B")

После завершения работы gather напечатайте полученный список результатов.
Цель: Убедиться, что общее время выполнения равно времени самого долгого таймера, а порядок результатов в списке соответствует порядку вызова.
'''

import asyncio

async def timer(delay, value):
    await asyncio.sleep(delay)
    return value

async def main():
    results = await asyncio.gather(timer(0.2, 'A'), timer(0.1, 'B'))
    print(results)

asyncio.run(main())