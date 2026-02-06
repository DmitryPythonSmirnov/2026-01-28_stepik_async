'''
https://stepik.org/lesson/2012889/step/8?unit=2041127

Задача 5: "Симуляция банковского счета"
Условие:
Напишите программу, которая имитирует снятие денег со счета, защищенное от "гонки".
Создайте глобальную переменную balance = 100 и Lock.
Напишите корутину withdraw(amount), которая:
Захватывает лок.
Проверяет, достаточно ли средств (balance >= amount).
Если да, ждет 0.01 секунды, затем вычитает amount из balance и печатает Снятие успешно.
Если нет, печатает Недостаточно средств.
В main запустите две задачи withdraw(70) конкурентно.
После их завершения напечатайте итоговый баланс.
Входные данные:
Нет.
Выходные данные:
Первая задача должна успеть снять деньги, а вторая — получить отказ. Итоговый баланс должен быть 30. Порядок сообщений о снятии не важен для проверки, но итоговый баланс должен быть верным.
Sample Input:
Sample Output:
Снятие успешно
Недостаточно средств
30
'''

import asyncio

balance = 100
lock = asyncio.Lock()

async def withdraw(amount):
    global balance
    async with lock:
        if balance >= amount:
            await asyncio.sleep(0.1)
            balance -= amount
            print('Снятие успешно')
        else:
            print('Недостаточно средств')
            


async def main():
    tasks = [withdraw(70) for _ in range(2)]
    await asyncio.gather(*tasks)
    print(balance)

asyncio.run(main())