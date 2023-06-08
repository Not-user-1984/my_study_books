# Конструкция list comprehension позволяет создавать
# новый список на основе уже существующего
# списка или другого итерируемого объекта.
# Вот несколько примеров его использования:

# Создание списка квадратов чисел от 1 до 10:
squares = [x**2 for x in range(1,11)]
print(squares)


# Создание списка только четных чисел из другого списка:
my_list = list(range(13))
evens = [x for x in my_list if x % 2 == 0]
print(evens)

# Создание списка строк в верхнем регистре:
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
print(upper_words)

# Создание списка кортежей (число, квадрат числа):
squares = [(x,x**2) for x in range(1,6)]
print(squares)

# Создание списка всех возможных комбинаций букв в строке:
string = "abc"
combinations = [a + b + c for a in string for b in string for c in string]
print(combinations)


list1 = [1, 2, 3]
list2 = [2, 3, 4]
unique = list(set([x for x in list1 + list2 if (list1 + list2).count(x) == 1]))
print(unique)