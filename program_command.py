import function


def list_program():
    print('\n Выберите команду по работе с заметками: '
          '\n 1 - чтение всех заметок'
          '\n 2 - добавление заметки'
          '\n 3 - удаление заметки'
          '\n 4 - редактирование заметки'
          '\n 5 - выход')


def run():
    while True:
        list_program()
        command = input('Введите команду: ')
        if command == '1':
            function.show_note()
        elif command == '2':
            function.add_note()
        elif command == '3':
            function.delete_note()
        elif command == '4':
            function.change_note()
        elif command == '5':
            break
        else:
            print('Ошибка ввода команды')
