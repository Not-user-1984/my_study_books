import asyncio
from utilit import delay, async_timed


@async_timed()
async def cpu_bound_work() -> int:
    couter = 0
    for i in range(10000000):
        couter = couter + 1
    return couter


@async_timed()
async def main():
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    task_delay = asyncio.create_task(delay(2))
    await task_one
    await task_two
    await task_delay

asyncio.run(main())