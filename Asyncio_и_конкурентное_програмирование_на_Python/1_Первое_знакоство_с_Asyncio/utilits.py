import time
import requests


URLS = {
    'Wikipedia': 'https://www.wikipedia.org/',
    'Google': 'https://www.google.com/',
    'Ya.ru': 'https://ya.ru/'
}

def timer(func):

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(
        f"Функция '{func.__name__}' выполнялась {execution_time:.4f} секунд."
            )
        return result
    return wrapper


@timer
def read_headers_url(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Oтвет сервера:{response.status_code}')
        else:
            print(f"Ошибка: Невозможно получить доступ к {url}. Код состояния: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполения запроса{e}")
