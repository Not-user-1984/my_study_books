

l1 = [
    3,
    [66, 55, 44],  # копия ссылки на этот список
    (7, 8, 9)
]
l2 = list(l1)
print(l1 == l2)  # проверка на содержимое
print(l1 is l2)  # проверка на id в памяти

l1.append(100)
l1[1].remove(55)

print('l1', l1)
print('l2', l2)


l2[1] += [33, 22]
l2[2] += (10, 11)
print('l1', l1)
print('l2', l2)

# l1 [3, [66, 44], (7, 8, 9), 100]
# l2 [3, [66, 44], (7, 8, 9)]
# l1 [3, [66, 44, 33, 22], (7, 8, 9), 100]
# l2 [3, [66, 44, 33, 22], (7, 8, 9, 10, 11)]
