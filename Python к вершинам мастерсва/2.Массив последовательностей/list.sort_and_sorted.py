# list.sort() и sorted(list) - это два разных метода для сортировки списков в Python.
# list.sort() - это метод, применяемый к самому объекту списка.
# Он изменяет список, сортируя его элементы в порядке возрастания (по умолчанию)
# или в соответствии с другой функцией сравнения. Возвращает None.
fruits = [
    'grape', 'respberry', 'apple', 'banana',
    'orange', 'pear', 'mango', 'pineapple',
    'pomegranate', 'watermelon', 'kiwi',
    'apricot', 'nectarine', 'lemon', 'lime',
    'peach', 'plum', 'cherries', 'strawberry',
    'blueberry', 'blackberry'
    ]


def monitor_print(arr):
    print("\n")
    print(f"id в памяти- {id(arr)}")
    for i, fruit in enumerate(arr):
        end = " " if (i+1) % 4 else "\n"
        print(fruit, end=end)


print(monitor_print(fruits))
# sorted(list) - это встроенная функция Python, которая создает новый отсортированный список
# на основе существующего списка. Она не изменяет исходный список,
# а возвращает новый отсортированный список. Пример:
print(monitor_print(sorted(fruits)))
print(monitor_print(sorted(fruits, reverse=True)))
fruits.sort()
print(monitor_print(fruits))
# Также следует отметить, что sorted(list) можно использовать с любым итерируемым объектом
# (не только с списками), в то время как list.sort() является методом класса list и может
# быть использован только с объектами класса list.