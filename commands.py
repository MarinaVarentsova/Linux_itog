class Commands:
    def __init__(self):
        self.commands = []

    def __init__(self):
        self.registry = {}

    def add_command(self, name, age, animal_type, command):
        if name in self.registry:
            self.registry[name].append((age, command))
        else:
            self.registry[name] = [(age, command)]

    def get_info(self):
        info = []
        name = input("Введите имя животного: ")
        info.append(name)
        age = input("Введите возраст животного: ")
        info.append(age)

        return (info)

