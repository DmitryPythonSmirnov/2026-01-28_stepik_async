'''
https://stepik.org/lesson/2012886/step/9?unit=2041125
Задача 5: "Пакетная обработка"
Условие:
Напишите корутину square(n), которая принимает число n и возвращает его квадрат (n * n).
В main дан список чисел numbers = [1, 2, 3, 4, 5]. Вам нужно:
Создать список корутин, применив square() к каждому числу из numbers.
Выполнить этот список корутин конкурентно с помощью asyncio.gather().
Напечатать итоговый список с результатами (квадратами чисел).
Входные данные:
Нет.
Выходные данные:
Программа должна вывести список квадратов исходных чисел.
'''


import asyncio

async def square(n):
    return n * n

async def main():
    numbers = [1, 2, 3, 4, 5]
    coro_list = [square(n) for n in numbers]
    results = await asyncio.gather(*coro_list)
    print(results)


asyncio.run(main())
