import typing
from dataclasses import dataclass


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