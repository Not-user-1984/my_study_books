from dataclasses import dataclass, field, fields
from datetime import date
from enum import Enum, auto
from typing import Optional


class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()


@dataclass
class Resource:
    """Описание мультимедийного ресурса.

    Атрибуты:
        identifier (str): Уникальный идентификатор мультимедийного ресурса.
        title (str, optional): Название ресурса. По умолчанию '<untitled>'.
        creators (list[str], optional): Список авторов или создателей ресурса. По умолчанию [].
        date (Optional[date], optional): Дата создания ресурса. По умолчанию None.
        type (ResourceType, optional): Тип ресурса из перечисления ResourceType. По умолчанию ResourceType.BOOK.
        description (str, optional): Описание ресурса. По умолчанию ''.
        language (str, optional): Язык ресурса. По умолчанию ''.
        subjects (list[str], optional): Список тем или предметов, связанных с ресурсом. По умолчанию [].

    Методы:
        __repr__(self): Возвращает строковое представление объекта в формате, который позволяет воссоздать объект.
    """
    identifier: str
    title: str = '<untitled>'
    creators: list[str] = field(default_factory=list)
    date: Optional[date] = None
    type: ResourceType = ResourceType.BOOK
    description: str = ''
    language: str = ''
    subjects: list[str] = field(default_factory=list)

    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        indent = ' ' * 4
        res = [f'{cls_name}(']
        for f in fields(cls):
            value = getattr(self, f.name)
            res.append(f'{indent}{f.name} = {value!r},')
        res.append(')')
        return '\n'.join(res)


resource1 = Resource(
    identifier='12345',
    title='Python Programming',
    creators=['John Doe'],
    description='An introduction to Python programming.')


resource2 = Resource(
    identifier='67890',
    title='Deep Learning',
    creators=['Jane Smith', 'Bob Johnson'],
    date=date(2023, 7, 31),
    type=ResourceType.VIDEO,
    description='An in-depth course on deep learning techniques.',
    language='English',
    subjects=['Machine Learning', 'Neural Networks']
)

# Изменение значений атрибутов после создания экземпляра
resource1.title = 'Introduction to Programming'
resource1.subjects.append('Computer Science')

resource3 = Resource(13131)




# Вывод информации об экземплярах
print(repr(resource1))
print(repr(resource2))

print(type(resource3.identifier))
