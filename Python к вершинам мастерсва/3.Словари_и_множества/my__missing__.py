class StrKeyDict0(dict):

#  __missing__ метод вызывается, когда в словаре происходит попытка получить значение по ключу,
#  которого в словаре нет (т.е. этот ключ отсутствует в словаре).
#  Вместо возбуждения исключения KeyError, как это происходит по умолчанию,
#  метод __missing__() позволяет определить свой собственный способ обработки отсутствующего ключа.
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

# get делегирует свою работу методу __getitem__ благодаря нотации
#   self[key]; это приводит в действие наш метод __missing
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

# __contains__(self, key) - это метод пользовательского класса,
# который возвращает True, если ключ key присутствует в словаре,
# и False, если ключа нет в словаре.
# Этот метод вызывается при использовании оператора in для проверки наличия ключа в словаре
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([('2','two'),('4','four')])

print(d[2])
print(d.get(4))
print(2 in d)