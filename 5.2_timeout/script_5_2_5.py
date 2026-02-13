'''
https://stepik.org/lesson/2012895/step/5?unit=2041134

Задача 2: "Провал по тайм-ауту"
Условие:
Напишите программу, которая ловит исключение asyncio.TimeoutError.
Создайте корутину slow_task(), которая ждет 1 секунду.
В main вызовите slow_task() с помощью asyncio.wait_for(), установив тайм-аут в 0.1 секунды.
Оберните вызов в блок try...except и в случае asyncio.TimeoutError напечатайте "Операция не уложилась в срок!".
Входные данные:
Нет.
Выходные данные:
Программа должна перехватить исключение и вывести сообщение.
Sample Input:
Sample Output:
Операция не уложилась в срок!
'''

import asyncio

async def slow_task():
    await asyncio.sleep(1)

async def main():
    try:
        result = await asyncio.wait_for(slow_task(), timeout=0.1)
    except asyncio.TimeoutError:
        print('Операция не уложилась в срок!')
    
    # Даём время на отмену задачу
    await asyncio.sleep(0.1)


asyncio.run(main())
