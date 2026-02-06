'''
https://stepik.org/lesson/2012889/step/2?unit=2041127
'''

import asyncio

# Наш общий ресурс, который будут изменять все задачи
COUNTER = 0
# Сколько задач мы хотим запустить
TASKS_COUNT = 10_000

async def increment():
    """
    Корутина, которая инкрементирует общий счетчик
    небезопасным (неатомарным) способом.
    """
    global COUNTER
    
    # 1. Читаем текущее значение
    temp_counter = COUNTER
    
    # В этой точке мы добровольно отдаем управление.
    # Другая задача может начать выполняться и тоже прочитать СТАРОЕ значение COUNTER.
    await asyncio.sleep(0)
    
    # 2. Увеличиваем локальное значение
    temp_counter += 1
    
    # 3. Записываем новое значение обратно
    COUNTER = temp_counter


async def main():
    print(f"Ожидаемое значение счетчика: {TASKS_COUNT}")

    # Запускаем 10 000 задач конкурентно
    tasks = [increment() for _ in range(TASKS_COUNT)]
    await asyncio.gather(*tasks)

    print(f"Итоговое значение счетчика: {COUNTER}")


# Запускаем программу
asyncio.run(main())