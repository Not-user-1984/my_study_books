from types import MappingProxyType

# MappingProxyType - это класс, который позволяет создавать обертки (proxy) над существующими словарями,
# предоставляя только чтение для исходного словаря.
# Это означает, что любые изменения, внесенные в обернутый словарь,
# будут отображаться в нем же, но сама обертка будет неизменяемой.
original_dict = {1: 'a', 2: '5'}
# Создаем proxy-объект для original_dict
read_only_dict = MappingProxyType(original_dict)

try:
    read_only_dict['a'] = 3
except TypeError as e:
    print(e)
# Изменения в original_dict будут отражаться в read_only_dict:
original_dict['d'] = 3
print(read_only_dict)
