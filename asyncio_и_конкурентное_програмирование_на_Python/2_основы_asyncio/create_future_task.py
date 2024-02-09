import asyncio
from asyncio import Future


def create_future() -> Future:
    future = asyncio.Future()
    asyncio.create_task(set_task_value(future))
    return future


# Функция для установки значения для таска
async def set_task_value(my_future) -> None:
    await asyncio.sleep(1)
    my_future.set_result(42)


# Главная функция, которая запускает процесс
async def main():
    future = create_future()
    print(f'Готов ли мой future? {future.done()}')
    value = await future
    print(f'Готов ли мой future? {future.done()}')
    print(f'Какое значение хранится в моем future? - {value}')

asyncio.run(main())
