from paramatrized_registration_decorator import registry, register, f2

# Определяем функцию `f3`, которую мы позже попробуем зарегистрировать.
def f3():
    print('вызов функции 3')

# Выводим текущее состояние `registry` до и после попытки регистрации `f3`.
print(registry)
print(register()(f3))
print(registry)

# Попытка зарегистрировать `f2` с параметром `active=False`, что приведет к удалению из `registry`.
print(register(active=False)(f2))
print(registry)