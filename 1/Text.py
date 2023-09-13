﻿main_menu = ['Главное меню',
             'Открыть файл c заметками',
             'Сохранить файл с заметками',
             'Показать все заметки',
             'Добавить заметки',
             'Найти заметку',
             'Изменить заметку',
             'Удалить заметку',
             'Выход']

select_menu = 'Выберите пункт меню: '

input_error = f'Ошибка ввода. Введите число от 1 до {len(main_menu) - 1}'

new_note = {'header': 'Введите заголовок заметки: ', 
               'body': 'Введите текст заметки: ', 
               'comment': 'Введите комментарий: '}

empty_book = 'Файл заметок пуст или не существует!'

load_succesful = 'Заметки успешно загружены!'
save_succesful = 'Заметки успешно сохранены!'
error_load = 'Ошибка загрузки файла заметок!'
error_save = 'Ошибка сохранения файла заметок!'
print_errors= 'Ошибка изменения файла заметок!'
def add_succesful(header: str) -> str:
    return f'Заметка {header} успешно добавлена в файл!'


search_word = 'Введите строку для поиска: '

def empty_search(word: str) -> str:
    return f'Заметки, содержащие {word} не найдены!'



def del_mess(word: str) -> str:
    return f'Заметка,{word} была удалена!'