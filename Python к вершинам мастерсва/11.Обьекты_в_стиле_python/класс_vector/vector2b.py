import math
from array import array


class Vector2b:
    """
    Представляет двумерный вектор.

    Атрибуты:
        x (float): Координата x вектора.
        y (float): Координата y вектора.
    """
    __match_args__ = ('x', 'y')
    typecode = 'd'

    def __init__(self, x, y):
        """
        Инициализирует объект Vector2b с координатами x и y.

        Параметры:
            x (float): Координата x вектора.
            y (float): Координата y вектора.
        """
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        """
        float: Координата x вектора.
        """
        return self.__x

    @property
    def y(self):
        """
        float: Координата y вектора.
        """
        return self.__y

    def __iter__(self):
        """
        Возвращает итератор по координатам вектора.
        """
        return (i for i in (self.x, self.y))

    def __repr__(self):
        """
        Возвращает строковое представление вектора.
        """
        class_name = type(self).__name__
        return "{} {!r}, {!r}".format(class_name, *self)

    def __str__(self):
        """
        Возвращает строковое представление вектора в виде кортежа.
        """
        return str(tuple(self))

    def __bytes__(self):
        """
        Возвращает байтовое представление вектора.
        """
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        """
        Проверяет равенство векторов.
        """
        return tuple(self) == tuple(other)

    def __hash__(self):
        """
        Возвращает хэш вектора.
        """
        return hash((self.x, self.y))

    def __abs__(self):
        """
        Возвращает модуль вектора.
        """
        return math.hypot(self.x, self.y)

    def __bool__(self):
        """
        Проверяет истинность вектора.
        """
        return bool(abs(self))

    def angle(self):
        """
        Возвращает угол вектора в радианах.
        """
        return math.atan2(self.y, self.x)

    def __format__(self, format_spec=''):
        """
        Возвращает строковое представление вектора с определенным форматом.
        """
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)

    @classmethod
    def frombytes(cls, octets):
        """
        Создает объект Vector2b из байтового представления.

        Параметры:
            octets (bytes): Байтовое представление вектора.

        Возвращает:
            Vector2b: Объект Vector2b.
        """
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
