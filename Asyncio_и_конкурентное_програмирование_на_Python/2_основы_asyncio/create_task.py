import asyncio
from utilit import async_timed, delay


@async_timed()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))


asyncio.run(main())