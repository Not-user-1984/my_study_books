import unittest


# Этот код определяет функцию get_creators, 
# которая принимает словарь record в качестве аргумента и возвращает список имен создателей (авторов или режиссеров)
# для записи, используя новый синтаксис матчинга (Python 3.10+).
# Блок match включает несколько ветвей (case) с различными шаблонами для соответствующих записей record.
# Если запись соответствует одному из шаблонов,
# то выполняется соответствующий блок кода, и результат возвращается из функции.
# Если тип записи - "book", значение api равно 1, 
# и ключ автор содержит список имен, то функция возвращает этот список.
# Если тип записи - "book", значение api равно 1,
# и ключ автор содержит одно имя, то функция возвращает список, содержащий это имя.
# Если тип записи - "book", но нет ключа автор, возникает ошибка ValueError.
# Если тип записи - "movie" и есть ключ directors, то функция возвращает список, содержащий это имя.
# Иначе функция генерирует ошибку ValueError.
def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 1, 'author': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book'  record: {record!r}")
        case {'type': 'movie', 'directors': name}:
            return [name]
        case _ :
            raise ValueError(f"Invalid record: {record!r}")


class TestGetCreators(unittest.TestCase):
    def test_valid_book_with_multiple_authors(self):
        record = {'type': 'book', 'api': 1, 'author': ['John Doe', 'Jane Smith']}
        expected = ['John Doe', 'Jane Smith']
        self.assertEqual(get_creators(record), expected)

    def test_valid_book_with_single_author(self):
        record = {'type': 'book', 'api': 1, 'author': 'Jane Smith'}
        expected = ['Jane Smith']
        self.assertEqual(get_creators(record), expected)

    def test_invalid_book_record_missing_author(self):
        record = {'type': 'book', 'api': 1}
        with self.assertRaises(ValueError):
            get_creators(record)

    def test_invalid_book_record_wrong_api_version(self):
        record = {'type': 'book', 'api': 2, 'author': 'Jane Smith'}
        with self.assertRaises(ValueError):
            get_creators(record)

    def test_valid_movie_record_with_director(self):
        record = {'type': 'movie', 'directors': 'Steven Spielberg'}
        expected = ['Steven Spielberg']
        self.assertEqual(get_creators(record), expected)

    def test_invalid_record(self):
        record = {'type': 'music', 'artist': 'Bob Dylan'}
        with self.assertRaises(ValueError):
            get_creators(record)


if __name__ == '__main__':
    unittest.main()

food = dict(category='ice creat', flavor='vanilla', cost=199)

match food:
    case {'category': 'ice creat', **datails}:
        print(f'Ice cream details: {datails}')
