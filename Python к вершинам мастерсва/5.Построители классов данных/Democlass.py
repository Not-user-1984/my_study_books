import typing
from dataclasses import dataclass, field


class DemoClass:
    a: int
    b: float = 1.1
    c = 'spam'


class DemoNtClass(typing.NamedTuple):
    a: int
    b: float = 1.1
    c = 'spam'


@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = 'spam'


@dataclass
class ClubMemder:
    name: str
    guests: list[str] = field(default_factory=list)
    # Новый синтаксис list[str] – это параметризованный обобщенный тип: начиная с версии Python 3.9
    # встроенный тип list допускает задание типа элементов списка в квадратных скобках
    athlete: bool = field(default=False, repr=False)