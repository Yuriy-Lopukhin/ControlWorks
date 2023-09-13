import Text


def menu() -> int:
    print(Text.main_menu[0])
    for i in range(1, len(Text.main_menu)):
        print(f'\t{i}. {Text.main_menu[i]}')

    while True:
        select = input(Text.select_menu)
        if select.isdigit() and 0 < int (select) < int(len(Text.main_menu)):
            return int(select)
        print(Text.input_error)


def show_contacts(book: dict[int: dict[str, str]], message):
    if book:
        max_header = []
        max_body = []
        max_comment = []
        for note in book.values():
            max_header.append(len(note.get('header')))
            max_body.append(len(note.get('body')))
            max_comment.append(len(note.get('comment')))

        size_name = max(max_header)
        size_body = max(max_body)
        size_comment = max(max_comment)
        print('\n' + '=' * (size_name + size_body + size_comment + 7))
        for index, note in book.items():
            print(f'{index:>3}. {note.get("header"):<{size_name}} {note.get("phone"):<{size_body}} {note.get("comment"):<{size_comment}}')
        print('=' * (size_name + size_body + size_comment + 7) + '\n')
    else:
        print_message(message)
def show_del(book: dict[int: dict[str, str]], message):
    if book:
        max_header = []
        max_body = []
        max_comment = []
        for note in book.values():
            max_header.append(len(note.get('header')))
            max_body.append(len(note.get('body')))
            max_comment.append(len(note.get('comment')))

        size_name = max(max_header)
        size_body = max(max_body)
        size_comment = max(max_comment)
        print('\n' + '=' * (size_name + size_body + size_comment + 7))
        for index, note in book.items():
            print(f'Заметка {index:>3}. {note.get("name"):<{size_name}} {note.get("body"):<{size_body}} {note.get("comment"):<{size_comment}} была удалена!')
        print( '=' * (size_name + size_body + size_comment + 7) + '\n')
    else:
        print_message(message)
def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')
             
def add_note():
    new = {}
    for key, value in Text.new_note.items():
        new[key] = input(value)
    return new


def search_word() -> str:
    return input(Text.search_word)
