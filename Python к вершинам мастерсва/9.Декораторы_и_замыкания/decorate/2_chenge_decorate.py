

def my_deco(func):
    def inner():
        print("замена функции")


@my_deco
def my_func():
    print('вызов функции')

my_func()
