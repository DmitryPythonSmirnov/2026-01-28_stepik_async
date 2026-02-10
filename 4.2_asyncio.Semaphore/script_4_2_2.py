'''
https://stepik.org/lesson/2012891/step/2?unit=2041130

100 одновременных запросов
'''

import asyncio
import time

# Количество "запросов", которые мы хотим сделать
TOTAL_REQUESTS = 100

async def make_request(request_num):
    """Имитирует выполнение сетевого запроса."""
    print(f"[{time.time():.2f}] Начинаю запрос #{request_num}...")
    # Имитация ожидания ответа от сети
    await asyncio.sleep(1)
    print(f"[{time.time():.2f}] Запрос #{request_num} завершен.")

async def main():
    print(f"Запускаем {TOTAL_REQUESTS} запросов одновременно...")
    start_time = time.time()

    # Создаем и запускаем все 100 задач сразу
    tasks = [make_request(i) for i in range(TOTAL_REQUESTS)]
    await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"\nВсе {TOTAL_REQUESTS} запросов выполнены за {end_time - start_time:.2f} сек.")


asyncio.run(main())