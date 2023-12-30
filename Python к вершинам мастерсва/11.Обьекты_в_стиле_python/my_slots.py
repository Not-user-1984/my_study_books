import weakref


class Pixil:
    """Represents a pixel with x and y coordinates."""
    __slots__ = ('x', 'y')


p = Pixil()
# В классе Pixil используются __slots__, что означает, что у него нет атрибута __dict__.
# Это обеспечивает экономию памяти и быстрый доступ к атрибутам.

p.x = 10
p.y = 20
# Мы можем использовать атрибуты x и y, определенные в __slots__.

# p.color = 'red'
# Попытка добавить атрибут color вызовет ошибку, так как он не определен в __slots__.


class OpenPixel(Pixil):
    """Extends Pixil to include a color attribute."""
    __slots__ = ('color', )
# OpenPixel наследует от Pixil и добавляет новый слот color для атрибута цвета.

op = OpenPixel()
op.x = 8
op.color = "Red"
# OpenPixel может использовать атрибуты x и новый color, определенный в его __slots__.

# print(op.__dict__)
# Вызов __dict__ приведет к ошибке, так как OpenPixel также использует __slots__.


class MyClass:
    """Represents a class with a weakly referenced attribute."""
    __slots__ = ('some_attribute', '__weakref__')

    def __init__(self, value):
        self.some_attribute = value

obj = MyClass(10)

ref = weakref.ref(obj)
print(ref)
# Создается слабая ссылка на экземпляр MyClass с использованием модуля weakref.
