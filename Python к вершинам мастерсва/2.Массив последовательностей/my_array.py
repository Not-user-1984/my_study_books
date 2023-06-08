# В этом примере показано, как использовать модуль array для создания массива 
# из 10 миллионов псевдослучайных чисел с плавающей запятой и записи его в файл floats.bin. 
# Затем содержимое файла считывается обратно в новый массив floats_2, который выводится в консоль. 
# Пример также демонстрирует операции сортировки массива
# и вставки нового элемента в отсортированный список с помощью модуля bisect.

from array import array
from random import random
import bisect

# Создание массива из 10 миллионов псевдослучайных чисел с плавающей запятой.
floats = array('d', (random() for i in range(10**7)))

# Вывод последнего элемента массива floats.
print(floats[-1])

# Запись массива в файл 'floats.bin'.
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

# Чтение содержимого файла 'floats.bin' и запись его в новый массив floats_2.
floats_2 = array('d')
fp = open('floats.bin', 'rb')
floats_2.fromfile(fp, 10**7)
fp.close()

# Вывод последнего элемента массива floats_2.
print(floats_2[-1])

# Проверка на равенство массивов floats и floats_2.
print(floats == floats_2)

# Сортировка массива floats_2 в обратном порядке.
a = array(floats_2.typecode, sorted(floats_2, reverse=True))

# Вывод последнего элемента массива a.
print(a[-1])

# Вставка нового элемента в отсортированный список a с помощью модуля bisect.
new_obj = 0.2763565004000001
if not new_obj in a:
    bisect.insort(a, new_obj)
inx_new_obj=a.index(new_obj)

# Вывод индекса и значения нового элемента.
print(inx_new_obj)
print(a[inx_new_obj])

# Вместо использования списков Python для хранения большого объема данных,
# Mодуль array в данном случае является более эффективным способом управления памятью
# и выполнения операций над массивами.
# Также использование модуля bisect для вставки нового элемента в отсортированный
# список позволяет получить более быстрый алгоритм, чем простой поиск и вставка в список Python
