'''
https://stepik.org/lesson/2012889/step/1?unit=2041127
'''

import asyncio

COUNTER = 0

async def increment():
    global COUNTER
    
    # Шаг 1: Читаем текущее значение
    # (как будто сделали SELECT из базы данных)
    temp_value = COUNTER 
    
    # Шаг 2: Имитируем бурную деятельность или ожидание сети.
    # ВНИМАНИЕ: Именно здесь управление передается другим задачам!
    await asyncio.sleep(0.1) 
    
    # Шаг 3: Увеличиваем и записываем обратно
    COUNTER = temp_value + 1

async def main():
    # Запускаем 10 задач конкурентно
    await asyncio.gather(*(increment() for _ in range(10)))

asyncio.run(main())
print(f"Итоговый счетчик: {COUNTER}")