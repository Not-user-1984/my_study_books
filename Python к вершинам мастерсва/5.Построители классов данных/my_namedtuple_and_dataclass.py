import typing
from collections import namedtuple
from dataclasses import dataclass


class Coordinate:
    """
    класс Coordinate не имеет переопределенных методов
    __repr__, __eq__, __ne__,
    поэтому операции сравнения и вывода объекта будут использовать
    стандартные реализации для классов Python.
    Если вам нужно изменить это поведение,
    вы можете явно определить эти методы в классе Coordinate.
    """
    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon


moscow = Coordinate(21.21, 1212.121)
locals_my = Coordinate(21.21, 1212.121)

print(moscow == locals_my)
print(moscow.lat == locals_my.lat)


# Использование именованного кортежа позволяет создавать объекты,
# у которых доступ к полям осуществляется по их именам,
# а также получать преимущества кортежей,
# такие как неизменяемость и возможность использования
#  в качестве ключей в словарях и множествах.

Coordinate_my_namedtuple = namedtuple(
    'Coordinate_my_namedtuple',
    " lat lot"
    )
moscow = Coordinate_my_namedtuple(21.21, 1212.121)
moscow_1 = Coordinate_my_namedtuple(21.21, 1212.121)
print(moscow == moscow_1)


# Использование именованного кортежа с типированием (NamedTuple)
# позволяет явно указать типы полей
# и получить преимущества статической типизации
# при разработке кода, особенно при использовании инструментов
#  статической проверки типов, таких как Mypy
Coordinate_my_namedtuple_typing = typing.NamedTuple(
    'Coordinate_my_namedtuple',
    lat= float,
    lan = float
    )


moscow = Coordinate_my_namedtuple_typing(21.21, 1212.121)
print(moscow)
print(
    typing.get_type_hints(Coordinate_my_namedtuple_typing)
    )


class My_Coordinate(typing.NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


d = My_Coordinate(21.21, 212.121)

print(d)
# Преимущества использования dataclass :
# Автоматическое создание общих методов: Декоратор dataclass автоматически создает общие методы,
# такие как __init__, __repr__ и методы сравнения (__eq__, __ne__), на основе определенных атрибутов.
# Это уменьшает объем повторяющегося кода и делает реализацию класса более чистой и краткой.
# Неизменяемые экземпляры: Установка параметра frozen=True делает экземпляры класса неизменяемыми.
# Это гарантирует, что атрибуты не могут быть случайно изменены, обеспечивая целостность данных и предотвращая ошибки, связанные с непреднамеренными изменениями.
# Читаемость и поддержка кода: Использование dataclass улучшает читаемость и поддерживаемость кода,
# четко указывая намерение класса и его атрибутов. Он также предоставляет последовательный и стандартизированный способ определения классов с ориентацией на данные.
# В отличие от предыдущих реализаций класса Coordinate, использующих обычный класс, namedtuple и NamedTuple, требуется ручная реализация методов,
# и в них отсутствует неизменяемость, предоставляемая dataclass.

@dataclass(frozen=True)
class My_dataclass_Coordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


d = My_dataclass_Coordinate(21.21, 21211.121)
# d.lat = 2312.12
print(d)

# У классов, построенных с помощью typing.NamedTuple
# и @dataclass, имеется атрибут __annotations__,
# в котором хранятся аннотации типов полей.
# Однако читать __annotations__ напрямую не реко- мендуется.
# Лучше получать эту информацию от метода inspect. get_annotations(MyClass)

import inspect

print(inspect.get_annotations(My_dataclass_Coordinate))
print(typing.get_type_hints(My_dataclass_Coordinate))
