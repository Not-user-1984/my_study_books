from collections import namedtuple
import json

Person = namedtuple(
    "Person",
    "name age job pay",
    defaults=["non"]
    )
Pay = namedtuple("Pay", "month day")
Valera = Person('Valera', '25', 'gamedev')
data = ("vera",
        "18",
        "insta-bloger",
        Pay(1000, 100000))
Vera = Person._make(data)

print(Valera)
print(Valera.age)
print(Valera.name)
print(Valera.pay)
print(Valera._fields)
print(json.dumps(Vera._asdict()))
