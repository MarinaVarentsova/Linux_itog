import uuid
import datetime
from datetime import datetime


def get_info():
    info = []
    note_id = str(uuid.uuid1())[0:2]
    info.append(note_id)
    title = input("Введите заголовок заметки: ")
    info.append(title.lower())
    body = input("Введите содержание заметки: ")
    info.append(body.lower())
    date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    info.append(date)
    print('\n')
    return info
