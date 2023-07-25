
from dataclasses import dataclass
from typing import ClassVar

from Democlass import ClubMemder


@dataclass
class HackerClubMember(ClubMemder):
    """
    Представляет участника клуба "Hacker Club",
    является подклассом класса ClubMember.
    Атрибуты:
        all_handles (ClassVar[set[str]]):
        Множество на уровне класса, которое хранит все имена (handle),
        используемые участниками HackerClubMember.
        handle (str):
        Имя (handle) участника. Если не предоставлено при создании объекта,
        оно будет автоматически инициализировано
        на основе первой части имени участника.
    """

    all_handles: ClassVar[set[str]] = set()
    handle: str = ""

    def __post_init__(self):
        """
        Метод, вызываемый после инициализации объекта.
        Автоматически инициализирует атрибут 'handle',
        если он не предоставлен при создании объекта.
        Также проверяет,
        уникален ли handle среди всех участников HackerClubMember.

        Исключения:
            ValueError: Если handle не уникален
            и уже используется другим участником HackerClubMember.
        """
        cls = self.__class__

        # Инициализация атрибута handle,
        #  если он не был предоставлен при создании объекта.
        if self.handle == '':
            self.handle = self.name.split()[0]

        # Проверка,
        # не используется ли handle другим участником HackerClubMember.
        if self.handle in cls.all_handles:
            msg = f"Имя '{self.handle}' уже используется."
            raise ValueError(msg)

        # Добавление handle в множество всех имен,
        #  используемых участниками HackerClubMember.
        cls.all_handles.add(self.handle)


anna = HackerClubMember('Anna Ravenscroft', handle='AnnaRaven')
# leo = HackerClubMember('Leo Rochael')
leo2 = HackerClubMember('Leo Rochael')
print(anna)
print(leo2)
