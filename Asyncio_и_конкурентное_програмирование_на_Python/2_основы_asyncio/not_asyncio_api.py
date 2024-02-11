import requests
import asyncio
from utilit import async_timed


@async_timed()
async def read_headers_status_url(url: str) -> str:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Oтвет сервера:{response.status_code}')
        else:
            print(f"Ошибка: Невозможно получить доступ к {url}. "
                  f"Код состояния: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполения запроса{e}")


@async_timed()
async def main():
    task_1 = asyncio.create_task(read_headers_status_url('https://mail.ru/'))
    task_2 = asyncio.create_task(read_headers_status_url('https://mail.ru/'))
    task_3 = asyncio.create_task(read_headers_status_url('https://mail.ru/'))
    await task_1
    await task_2
    await task_3


asyncio.run(main())
