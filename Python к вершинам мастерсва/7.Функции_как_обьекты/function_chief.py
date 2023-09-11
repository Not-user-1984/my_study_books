# Функции высшего порядка - это концепция в функциональном программировании,
# которая означает, что функции могут принимать другие функции в качестве аргументов и/или возвращать функции как результат
# Важным аспектом функций высшего порядка является то,
# что они рассматривают функции как "первоклассные объекты" (или "первоклассные функции"),
# что означает, что они могут быть созданы,
# переданы и сохранены так же,
# как и другие значения данных,
# такие как числа и строки.
def factorial(n):
    return 1 if n < 2 else n * factorial(n -1)


fruits = ['stawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

def reverce(word):
    return word[::-1]


print(sorted(fruits, key=reverce))

print(list(map(factorial, range(6)))) 

print(
    [factorial(n) for n in range(6)] # списковые включения лучше
)
print(
    list(map(factorial, filter(lambda n: n % 2, range(6))))
)
print(
    [factorial(n) for n in range(6) if  n % 2]
)