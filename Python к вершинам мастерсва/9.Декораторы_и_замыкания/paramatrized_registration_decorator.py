# Создаем пустое множество для хранения функций, которые мы регистрируем.
registry = set()

# Создаем декоратор `register`, который может принимать параметр `active`.
# Этот декоратор позволяет регистрировать функции в `registry`.

def register(active=True):
    def decorate(func):
        """
        Декоратор `register`, который позволяет регистрировать функции в `registry`.

        Args:
            active (bool): Опциональный параметр, указывающий, активна ли регистрация функции.

        Returns:
            func: Возвращает функцию без изменений.

        Декоратор проверяет параметр `active`:
        - Если `active` равно True, функция `func` будет добавлена в `registry`.
        - Если `active` равно False, функция `func` будет удалена из `registry`.
        """
        print('Происходит регистрация', f'active={active} -> decorate({func})')
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func

    return decorate


# Регистрируем функции, используя декоратор `register`.
# Функция `f1` будет добавлена в `registry`, так как мы передали `active=False`.
@register(active=False)
def f1():
    print('вызов функции 1')


# Функция `f2` будет добавлена в `registry`, так как мы не указали параметр `active`.
@register()
def f2():
    print('вызов функции 2')