
from utilits import timer


def fibonacci(nubmer: int):

    def fib(n):
        if n <= 0:
            return "Неверный ввод, число должно быть больше 0"
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f'номер {nubmer} = {fib(nubmer)}')


@timer
def fibs_no_theading():
    fibonacci(40)
    fibonacci(42)


fibs_no_theading()
