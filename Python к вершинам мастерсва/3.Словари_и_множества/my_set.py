my_set = {'sdsdf', 'sdsdf', 'sddf'}
print(my_set)
my_typle = ('jiojij', 445,)
print(my_typle)

set1 = {1, 2, 3}
set2 = {3, 4, 5, 6, 7}

# пересечение множеств
print(set1.union(set2))
print(set1 | set2)

# разность множеств
print(set1.difference(set2))
print(set1 - set2)


# выводит пересечение 
print(set1.intersection(set2))
print(set1 & set2)

alphabet = "abcdefghijklmnopqrstuvwxyz"  # строка с алфавитом
my_dict = {alphabet[i]: i+1 for i in range(len(alphabet))}
s = {'a','b','c'}

print(my_dict)
print(my_dict.keys() | s) # можно работать с ключами так они подреживают хеш
