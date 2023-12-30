registry = []


def my_decorate_registry(func):
    print(f'регистрация функции: {func}')
    registry.append(func)
    return func


@my_decorate_registry
def my_func_1():
    print('вызов функции: 1')


def my_func_2():
    print('вызов функции: 2')


def my_func_3():
    print('вызов функции: 3')


def main():
    print("*" * 46)
    print("запуск модуля")
    print("зарег. ->", registry)
    my_func_1()
    my_func_2()
    my_func_3()
    print("*" * 46)


if __name__ == '__main__':
    main()
