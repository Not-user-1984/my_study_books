import collections

# collections.Counter - это класс в Python,
# который используется для подсчета элементов в итерируемом объекте.
# Он создает словарь, где ключами являются элементы итерируемого объекта,
# а значениями - количество каждого элемента в этом объекте.
ct = collections.Counter('acbaracadabra')

print(ct)
ct.update("aaaaa")
print(ct)
print(ct.most_common(2))
