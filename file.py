import csv
from os.path import exists
from datetime import datetime


path = "note.cvs"


def path_file():
    if not exists(path):
        create_file()
        return path
    return path


def create_file():
    with open('note.cvs', 'w', encoding='utf-8') as data:
        data.write("note_id,title,body,date\n")
        data.close()


def read_file(path):
    with open(path, 'r', encoding='utf-8') as data:
        note_book = data.readlines()
        data.close()
    return note_book


def write_file(info):
    with open(path, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]},{info[1]},{info[2]},{info[3]}\n')
    data.close()


def find_for_change_file(path):
    note = input("введите текст для поиска заметки\nпо заголовку либо по содержанию: ")
    with open(path, 'r', encoding='utf-8') as data:
        note_book = data.readlines()
        for i, line in enumerate(note_book):
            if note in line.strip():
                if i == 0:
                    print(f"fieldnames: ", line.strip())
                else:
                    print(f"Number №{i}: ", line.strip())
        flag = False
        while not flag:
            try:
                number = int(input("выберите номер заметки для изменения: "))
                if number < 0:
                    print('wrong note')
                    flag = False
                if number == 0:
                    number = 0
                    flag = True
                if number > 0:
                    number = number - 1
                    flag = True
                else:
                    flag = True
            except ValueError:
                print('not valid note')
        return number


def change_file(path, number):
    with open(path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        note_book = []
        for row in csv_reader:
            print(row)
            note_book.append(row)
    print('\n')
    to_update = note_book[number].values()
    print(f"Number №{number+1} будет изменен, текущие данные: ", to_update)
    title = input("Введите новое название заметки: ")
    new_title = f'{title}'
    body = input("Введите новый текст заметки: ")
    new_body = f'{body}'
    with open(path, 'w', newline='') as csv_file:
        fieldnames = note_book[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in note_book:
            if set(to_update).issubset(set(row.values())):
                row['title'] = new_title
            if set(to_update).issubset(set(row.values())):
                row['body'] = new_body
            if set(to_update).issubset(set(row.values())):
                row['date'] = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
            writer.writerow(row)


def delete_file(path, number):
    with open(path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        note_book = []
        for row in csv_reader:
            print(row)
            note_book.append(row)
    print('\n')
    to_update = note_book[number].values()
    number_1 = number + 1
    print(f"Number №{number_1} будет удален, текущие данные: ", to_update)
    valid = input("подтвердите удаление Y/N: ")
    if valid == 'Y':
        with open(path, 'w', newline='') as csv_file:
            fieldnames = note_book[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            note_book.pop(number)
            for row in note_book:
                writer.writerow(row)
                print(row)
    else:
        print('Номер заметки для удаления не выбран')
