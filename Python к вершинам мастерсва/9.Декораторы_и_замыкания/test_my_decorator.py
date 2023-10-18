import time
# from  my_decorator import clock
from my_dacorator_class import clock


@clock()
def shooze(seconds):
    time.sleep(seconds)


@clock()
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


if __name__ == '__main__':
    shooze(.123)
    factorial(6)
