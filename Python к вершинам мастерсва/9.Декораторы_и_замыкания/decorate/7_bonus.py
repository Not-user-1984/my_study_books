import time

# Эмуляция базы данных (словарь для хранения данных)
database = {
    1: 'запись 1',
    2: 'запись 2',
    3: 'запись 3'
}

# Декоратор для эмуляции кэширования запросов к базе данных
def cache_database_queries(func):
    cache = {}

    def wrapper(query_id):
        if query_id not in cache:
            # Предположим, это имитация запроса к базе данных
            print(f"Выполняется запрос к базе данных для записи с id={query_id}")
            time.sleep(3)
            cache[query_id] = func(query_id)
        else:
            print(f"Информация о записи с id={query_id} взята из кэша")
        return cache[query_id]

    return wrapper

# Функция для эмуляции запроса к базе данных
@cache_database_queries
def get_record_from_database(record_id):
    return database.get(record_id, 'Запись не найдена')

# Имитация запросов к базе данных
print(get_record_from_database(1))  # Выполнит запрос к базе данных
print(get_record_from_database(2))  # Выполнит запрос к базе данных
print(get_record_from_database(1))
print(get_record_from_database(4))   # Возьмет информацию из кэша
