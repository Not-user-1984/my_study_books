import typing


class City(typing.NamedTuple):
    continent: str
    name: str
    country: str


cities = [
    City('Asia', 'Tokyo', 'JP'),
    City('Asia', 'Delhi', 'IN'),
    City('North America', 'Mexico City', 'MX'),
    City('North America', 'New York', 'US'),
    City('South America', 'São Paulo', 'BR'),
]


def math_asian_cities():
    """
    Функция выполняет сопоставление с образцом для выборки всех городов,
    которые находятся в Азии (континент 'Asia').

    :return: Список городов, находящихся в Азии.
    :rtype: list[City]
    """
    results = []
    for city in cities:
        match city:
            case City(continent='Asia'):
                results.append(city)
    return results


def math_asian_cities_coutry():
    """
    Функция выполняет сопоставление с образцом для выборки стран всех городов,
    находящихся в Азии (континент 'Asia').

    :return: Список стран, в которых находятся города Азии.
    :rtype: list[str]
    """
    results = []
    for city in cities:
        match city:
            case City(continent='Asia', country=cc):
                results.append(cc)
    return results


def match_asian_countries_pos():
    """
    Функция выполняет сопоставление с образцом
    для выборки стран всех городов Азии,
    используя синтаксис с подчеркиваниями для неиспользуемых переменных.

    :return: Список стран, в которых находятся города Азии.
    :rtype: list[str]
    """
    results = []
    for city in cities:
        match city:
            case City('Asia', _, country):
                results.append(country)
    return results


print("Города Азии:", math_asian_cities())
print("Страны городов Азии:", math_asian_cities_coutry())
print("Страны всех городов Азии:", match_asian_countries_pos())
print("Аргументы сопоставления для класса City:", City.__match_args__)
