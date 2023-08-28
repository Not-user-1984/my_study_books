import copy


class Bus:
    def __init__(self, passangers=None):
        if passangers is None:
            self.passangers = []
        else:
            self.passangers = list(passangers)

            #  если будет self.passangers = passangers измениться список оригинальный
            #  Если вам не требуется изменять оригинальный список пассажиров при вызове методов класса Bus,
            #  то вам следует создать копию списка и работать с ней внутри класса.
            #  Это обеспечит независимость между списками и избежит нежелательных изменений

    def pick(self, name):
        self.passangers.append(name)

    def drop(self, name):
        self.passangers.remove(name)


bus1 = Bus(["дима", "света", "настя"])
bus2 = copy.copy(bus1)  # поверхностная копия
bus3 = copy.deepcopy(bus1)  # глубокая копия

print(id(bus1), id(bus2), id(bus3))

bus1.drop("дима")
print(bus1.passangers, bus2.passangers, bus3.passangers)
print(id(bus1.passangers), id(bus2.passangers), id(bus3.passangers))

# циклическое копирование
a = [10, 30]
b = [a, 30]
a.append(b)
print(a)
c = copy.deepcopy(a)
print(c)
