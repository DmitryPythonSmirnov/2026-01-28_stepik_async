'''
https://stepik.org/lesson/2012891/step/3?unit=2041130

100 запросов пачками по 10.
'''

import asyncio
import time

# Количество "запросов", которые мы хотим сделать
TOTAL_REQUESTS = 100


# Создаем семафор, который пропустит не более 10 задач одновременно
semaphore = asyncio.Semaphore(10)

async def make_request(request_num):
    async with semaphore:
        # --- НАЧАЛО ОГРАНИЧЕННОЙ ЗОНЫ ---
        # Этот код будет выполняться одновременно
        # не более чем для 10 задач.
        print(f"[{time.time():.2f}] Запрос #{request_num} 'заехал на парковку'")
        await asyncio.sleep(1) # Имитация работы
        # --- КОНЕЦ ОГРАНИЧЕННОЙ ЗОНЫ ---
    print(f"[{time.time():.2f}] Запрос #{request_num} 'выехал с парковки'")

async def main():
    print(f"Запускаем {TOTAL_REQUESTS} запросов одновременно...")
    start_time = time.time()

    # Создаем и запускаем все 100 задач сразу
    tasks = [make_request(i) for i in range(TOTAL_REQUESTS)]
    await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"\nВсе {TOTAL_REQUESTS} запросов выполнены за {end_time - start_time:.2f} сек.")


asyncio.run(main())