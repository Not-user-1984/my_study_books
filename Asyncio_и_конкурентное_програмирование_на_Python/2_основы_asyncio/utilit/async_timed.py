import functools
import time
from typing import Callable, Any
import asyncio


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'выполняется{func} c аргуметами {args},{kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func} завершилась за {total:.4f} c')
        return wrapped
    return wrapper


@async_timed()
async def delay(delay_second: int) -> int:
    print(f'зысыпаю на {delay_second} c')
    await asyncio.sleep(delay_second)
    print(f'сон в течение {delay_second} с')
    return delay_second
