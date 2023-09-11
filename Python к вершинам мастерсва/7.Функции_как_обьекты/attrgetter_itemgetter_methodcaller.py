from collections import namedtuple
from operator import attrgetter, itemgetter, methodcaller

"""
Этот код представляет собой пример использования именованных кортежей и функций библиотеки collections и operator.
Он также демонстрирует, как сортировать и выбирать данные из списка городов.

1. Импортируем необходимые модули:
   - `namedtuple` из `collections`: для создания именованных кортежей.
   - `attrgetter` и `itemgetter` из `operator`: для выбора атрибутов и элементов из структур данных.

2. Определяем список `meta_data`, содержащий информацию о городах в виде кортежей с данными:
   - Название города.
   - Код страны.
   - Население.
   - Координаты (широта и долгота).

3. Сортируем список `meta_data` по названию города и выводим отсортированный список.

4. Создаем именованный кортеж `latLon` для представления координат (широта и долгота).

5. Создаем именованный кортеж `Metropolis` для представления данных о метрополисах, включая название, код страны, население и координаты.

6. Создаем список `merto_areas`, где каждый элемент - это экземпляр `Metropolis`, созданный из данных в `meta_data`.

7. Выводим название первого метрополиса из списка `merto_areas`.

8. Создаем `name_lat` для выбора названия города и координаты (широты) из `Metropolis`.

9. Сортируем список `merto_areas` по названию города и выводим отсортированный список, включая название и координаты (широту).

Этот код полезен для представления и управления данными о городах и метрополисах, а также для сортировки и выбора определенных атрибутов из этих данных.
"""

meta_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691677)),
    ('Ass', 'JP', 36.933, (35.689722, 139.691677)),
    ('New York', 'US', 33.939, (40.712776, -74.005974)),
    ('London', 'GB', 36.383, (51.507351, -0.127758)),
    ('Paris', 'FR', 33.967, (48.856613, 2.352222)),
    ('Beijing', 'CN', 39.613, (39.904202, 116.407394)),
    ('Sydney', 'AU', 30.17, (-33.865143, 151.209900)),
    ('Rio de Janeiro', 'BR', 26.794, (-22.906847, -43.172896)),
    ('Cairo', 'EG', 30.044, (30.044420, 31.235712)),
    ('Moscow', 'RU', 35.907, (55.755825, 37.617600)),
    ('Dubai', 'AE', 35.071, (25.276987, 55.296249))
]

for city in sorted(
    meta_data,
    key=itemgetter(0)
):
    print(city)

cc_name = itemgetter(1, 2)


for city in meta_data:
    print(cc_name(city))

latLon = namedtuple('LetLop', " lat lop")

Metropolis = namedtuple(
    'Metropolis', 'name cc pop coord'
    )

merto_areas = [Metropolis(name, cc, pop, latLon(lat, lop))
               for name, cc, pop, (lat, lop) in meta_data]

print(merto_areas[0].name)
name_lat = attrgetter('name', 'coord.lat')

for city in sorted(merto_areas, key=attrgetter('name')):
    print(name_lat(city))


s = 'The time has come'
upcase = methodcaller('upper')
hyphanate = methodcaller('replace', ' ', '-')


print(upcase(s))
print(hyphanate(s))