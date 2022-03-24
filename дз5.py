def decorator(path):

    def logger(old_function):
        filename = 'new_file.txt'

        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            from datetime import datetime
            import os
            file_path = os.path.join(path, filename)
            if not os.path.exists(path):
                os.makedirs(path)
            with open(file_path, 'w', encoding='utf-8') as file:
                now = datetime.now()
                file.write(f'Дата: {now.day}-{now.month}-{now.year}, Время: {now.hour}:{now.minute}, '
                           f'Название вызванной функции: {old_function.__name__}, '
                           f'Аргументы функции: {args, kwargs}, '
                           f'Результат функции: {result} \n')
            print('декоратор работет')
            return result

        return new_function
    return logger


# Данные из домашнего задания №5 (Основы языка Python)
# Исходные данные и одна функция выборка
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


@decorator('\Новый путь\к новой папке')
def people():
    number = str(input('введите номер '))
    for id, value in enumerate(documents):
        if value["number"] == number:
            return (value["name"])
        elif id >= (len(documents)-1):
            return ('такого номера не существует')

print(people())

