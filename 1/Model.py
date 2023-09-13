import json

notes = {}
path = 'Notes.json'


def open_file():
    global notes
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            notes = json.load(file)
        return True
    except:
        return False


def save_file():
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(notes, file, ensure_ascii=False)
        return True
    except:
        return False


def search(word: str) -> dict[int: dict[str, str]]:
    result = {}
    for index, contact in notes.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[index] = contact
    return result


def chek_id():
    if notes:
        return max(list(map(int, notes))) + 1
    return 1


def add_note(new: {int: dict[str, str]}):
    note = {chek_id(): new}
    notes.update(note)


def delete(word) -> dict[int: dict[str, str]]:
    save_file()

    notes.pop(str(list(dict(word).keys())[0]))

    save_file()


def change(word,temp) -> dict[int: dict[str, str]]:

    note = {list(word.keys())[0]: temp}
    notes.update(note)