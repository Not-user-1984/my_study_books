# Функции для выполнения команд
def turn_light_on():
    print("Свет включен")


def turn_light_off():
    print("Свет выключен")


# Здесь конкретно create_command - это замыкание,
# которое берет функцию function в качестве аргумента и возвращает
# вложенную функцию execute.
# В результате вложенная функция execute сохраняет доступ к function,
# даже после завершения выполнения внешней функции create_command.
# Это позволяет нам создавать объекты-команд,
# которые могут быть вызваны,
# но при этом они все еще имеют доступ к функциональности,
# определенной внутри function.

def create_command(function):
    def execute():
        function()

    return execute


# Создание команд
light_on_command = create_command(turn_light_on)
light_off_command = create_command(turn_light_off)


# Класс-инвокер
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command()


# Класс для выполнения списка команд
class MacroCommand:
    def __init__(self, commands):
        self.commands = commands

    def __call__(self):
        for command in self.commands:
            command()


# Клиентский код
if __name__ == "__main__":
    remote = RemoteControl()

    remote.set_command(light_on_command)
    remote.press_button()

    remote.set_command(light_off_command)
    remote.press_button()

    macro_command = MacroCommand([light_on_command, light_off_command])

    remote.set_command(macro_command)
    remote.press_button()
