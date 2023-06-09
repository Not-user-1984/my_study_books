# coding: cp1252
cafe = bytes('cafe', encoding= 'utf_8')
print(cafe[::1])

cafe_arr = bytearray(cafe)
print(cafe_arr)
print('Olá, Mundo!')