import registry
import function


def list_program():
    print('\n Выберите команду по работе с заметками: '
          '\n 1 - осмотреть реестр животых'
          '\n 2 - добавление животного'
          '\n 3 - удаление животного'
          '\n 4 - редактирование животного'
          '\n 5 - посмотреть список команд животного'
          '\n 6 - обучить новым командам животного'
          '\n 7 - выход')


def run():
    while True:
        list_program()
        command = input('Введите команду: ')
        if command == '1':
            function.show_animals()
        elif command == '2':
            function.add_animals()
        elif command == '3':
            function.delete_note()
        elif command == '4':
            function.change_note()
        elif command == '5':
            break
        else:
            print('Ошибка ввода команды')
