from abc import ABC, abstractmethod


# Абстрактный класс команды
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Конкретная команда для включения света
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


# Конкретная команда для выключения света
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# Класс-получатель, который выполняет действия
class Light:
    def turn_on(self):
        print("Свет включен")

    def turn_off(self):
        print("Свет выключен")


# Класс-инвокер
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()


# Клиентский код
if __name__ == '__main__':
    # Создаем объект-получатель
    light = Light()

    # Создаем команды для включения и выключения света
    Light_on = LightOnCommand(light)
    Light_off = LightOffCommand(light)

    # Создаем объект-инвокер (пульт управления)
    remote = RemoteControl()

    # Устанавливаем команду для включения света и выполняем ее
    remote.set_command(Light_on)
    remote.press_button()  # Включение света

    # Устанавливаем команду для выключения света и выполняем ее
    remote.set_command(Light_off)
    remote.press_button()  # Выключение света
