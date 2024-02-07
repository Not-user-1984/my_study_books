import asyncio
from utilit import delay


async def main():

    delay_task = asyncio.create_task(delay(5))

    try:
        result = await asyncio.wait_for(asyncio.shield(delay_task), timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Время вышло программа скоро завершиться')
        result = await delay_task


asyncio.run(main())
