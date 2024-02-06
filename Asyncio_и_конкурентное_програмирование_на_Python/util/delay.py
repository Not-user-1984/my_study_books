import asyncio
from async_timed import async_timed


@async_timed()
async def delay(delay_second: int) -> int:
    print(f'зысыпаю на {delay_second} c')
    await asyncio.sleep(delay_second)
    print(f'сон в течение {delay_second} с')
    return delay_second


# async def main():
#     task_one = asyncio.create_task(delay(2))
#     task_two = asyncio.create_task(delay(3))
#     await task_one
#     await task_two

# asyncio.run(main())
