from collections import defaultdict , OrderedDict


# defaultdict - это подкласс словаря в Python,
# который предоставляет значение по умолчанию для ключей,
# которые не существуют в словаре. Это означает,
# что если вы попытаетесь получить доступ к ключу, который еще не был добавлен в словарь,
# defaultdict автоматически создаст этот ключ и назначит ему значение,
# которое вы определите при создании словаря.
# Одним из главных преимуществ defaultdict является то,
# что он позволяет упростить код, связанный со словарями,
# поскольку вы можете избежать проверок наличия ключей перед их использованием.
# Вместо этого вы можете просто обращаться к ключам и использовать значения по умолчанию,
# если эти ключи еще не существуют.


dd = defaultdict(str)


# OrderedDict - это подкласс словаря в Python,
# который запоминает порядок вставки пар ключ-значение.
# В обычном словаре порядок элементов зависит от хэш-функции
# ключей и может меняться при изменении размера словаря или при повторной вставке элементов.
# В OrderedDict порядок элементов фиксирован и сохраняется в том же порядке,
# в котором они были добавлены. Таким образом, если вы переберете ключи или значения словаря OrderedDict,
# они будут в том же порядке, что и при добавлении в словарь.

od = OrderedDict()
d = {}

dd["spam"] = 'ff'
dd["eggs"] = 'dd'
print(dd["bacon"])
print(dd)

d['c'] = 3
d['b'] = 2
d['a'] = 1


for key in d.keys():
    print(key)
print(hash(d))
