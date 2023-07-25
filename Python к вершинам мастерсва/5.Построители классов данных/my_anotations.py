from Democlass import DemoClass, DemoDataClass, DemoNtClass


print(DemoClass.__annotations__)
# print(DemoClass.a)
print(DemoClass.b)
print(DemoClass.c)


# тут а как атрибут
# Атрибуты класса a и b являются дескрипторами;
# этот продвинутый механизм рассматривается Пока считайте,
# что это некий аналог методов чтения свойств (getter),
# который не нуждается в явном операторе вызова (),
# чтобы получить атрибут экземпляр
print(DemoNtClass.__annotations__)
print(DemoNtClass.a)
print(DemoNtClass.b)
print(DemoNtClass.c)

# Атрибуты __annotations__ и __doc__ не таят никаких сюрпризов.
#  Но атрибута с именем a в классе DemoDataClass нет – в отличие от DemoNTClass 
# из примера , в котором имеется дескриптор для получения a из экземпляров в виде атрибутов,
#  допускающих только чтение (таинственный атрибут <_collections._ tuplegetter>).
#  Все объясняется тем, что атрибут a существует лишь в экземплярах DemoDataClass.
#  Это будет открытый атрибут, который можно читать и записывать, если только класс не заморожен.
#  который не будет связан с экземплярами.
print(DemoDataClass.__annotations__)
# print(DemoDataClass.a)
print(DemoDataClass.b)
print(DemoDataClass.c)
print(DemoDataClass.__doc__)
