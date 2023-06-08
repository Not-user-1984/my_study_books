from unicodedata import name

# генератор множества(set comprehension),
# который перебирает все числа от 32 до 255 и добавляет в множество символы,
# у которых в названии символа есть строка "SIGN".

print(
    {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
    )