import asyncio
from .async_timed import async_timed


@async_timed()
async def delay(delay_second: int) -> int:
    print(f'зысыпаю на {delay_second} c')
    await asyncio.sleep(delay_second)
    print(f'сон в течение {delay_second} с')
    return delay_second
