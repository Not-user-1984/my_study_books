import threading

from utilits import URLS, timer, read_headers_url
from synchronous_execution_get_url import read_headers_url


def get_asynch_url(url_name):
    # print(f"Запуск потока для URL: {URLS[url_name]}")
    # time.sleep(2)  # Добавляем задержку для наглядности
    read_headers_url(URLS[url_name])
    # print(f"Поток для URL {URLS[url_name]} завершен")


@timer
def async_readers_url():
    thread_1 = threading.Thread(target=get_asynch_url, args=('Google',))
    thread_2 = threading.Thread(target=get_asynch_url, args=('Google',))
    thread_1.start()
    thread_2.start()
    print("Главный поток продолжает выполнение...")
    thread_1.join()
    thread_2.join()


if __name__ == "__main__":
    async_readers_url()
