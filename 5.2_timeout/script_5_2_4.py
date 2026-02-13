'''
https://stepik.org/lesson/2012895/step/4?unit=2041134

Задача 1: "Успеть вовремя"
Условие:
Напишите программу, которая демонстрирует успешное выполнение операции до истечения тайм-аута.
Создайте корутину quick_task(), которая ждет 0.1 секунды и возвращает строку "Успех".
В main вызовите quick_task() с помощью asyncio.wait_for(), установив тайм-аут в 1 секунду.
Напечатайте результат, возвращенный asyncio.wait_for().
Входные данные:
Нет.
Выходные данные:
Программа должна успешно получить и вывести результат.
Sample Input:
Sample Output:
Успех
'''

import asyncio

async def quick_task():
    await asyncio.sleep(0.1)
    return 'Успех'

async def main():
    try:
        result = await asyncio.wait_for(quick_task(), timeout=1)
        print(result)
    except asyncio.TimeoutError:
        print('Таймаут истёк')
    
    # Даём время на отмену задачу
    await asyncio.sleep(0.1)


asyncio.run(main())
