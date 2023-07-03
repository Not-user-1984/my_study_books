a = '444444'
b = '999999'


# Добавление нулей в начало строк, чтобы их длины были одинаковыми
maxlen = max(len(a), len(b))
a = a.zfill(maxlen)
b = b.zfill(maxlen)

result = ''  # Результат будет сохранен здесь
carry = 0   # Переменная для переноса

for i in range(maxlen-1, -1, -1):
    r = carry
    r += int(a[i])
    r += int(b[i])
    carry = 1 if r > 9 else 0
    result = str(r % 10) + result


if carry > 0:
    result = str(carry) + result

print(result)

class BiGBoss:
    def __init__(self, my_list):
        self.my_list = my_list

    def genfloat(self):
        return [float(x) for x in self.my_list]

list_comp = [x for x in range(1000) if x % 2 == 0]

list_lamda = list(map(lambda x: str(x), list_comp))
big_boss = BiGBoss(list_lamda)
print(list_comp)
print(big_boss.my_list)
print(big_boss.genfloat())
my_set = set(list_lamda)

# for _ in range(len(my_set)):
#     print(my_set.pop())

my_tuple = tuple(list_comp)
print(my_tuple[2])