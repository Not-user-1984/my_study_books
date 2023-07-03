from collections import namedtuple
import typing
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


@dataclass(frozen=True)
class My_dataclass_Coordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


d = My_dataclass_Coordinate(21.21, 21211.121)
d.lat = 2312.12
print(d)

