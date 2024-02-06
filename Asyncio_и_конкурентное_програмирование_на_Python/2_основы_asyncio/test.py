import asyncio
from util.delay import delay
from util.async_timed import async_timed


@async_timed
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))
    await task_one
    await task_two

asyncio.run(main())
