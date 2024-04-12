import file
import registry


def show_animals():
    path = file.path_file()
    data = file.read_file(path)
    print(data)


def add_animals():
    file.path_file()
    infp0 = registry.Registry()
    info = infp0.get_info()
    file.write_file(info)


def delete_note():
    path = file.path_file()
    contact = file.find_for_change_file(path)
    print(file.delete_file(path, contact))


def change_note():
    path = file.path_file()
    contact = file.find_for_change_file(path)
    print(file.change_file(path, contact))

def print_available_types(self):
    print("Доступные типы животных:")
    print("- собака")
    print("- кошка")
    print("- хомяк")

def save_to_file(self):
    with open("animal_registry.txt", "w") as file:
        for animal in self.registry:
            file.write(f"Имя: {animal['name']}, Возраст: {animal['age']}, Тип: {animal['type']}\n")