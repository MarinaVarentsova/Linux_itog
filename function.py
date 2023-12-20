import file
import Note_class


def show_note():
    path = file.path_file()
    data = file.read_file(path)
    print(data)


def add_note():
    file.path_file()
    info = Note_class.get_info()
    file.write_file(info)


def delete_note():
    path = file.path_file()
    contact = file.find_for_change_file(path)
    print(file.delete_file(path, contact))


def change_note():
    path = file.path_file()
    contact = file.find_for_change_file(path)
    print(file.change_file(path, contact))
