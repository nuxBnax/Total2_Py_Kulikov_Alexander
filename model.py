from copy import deepcopy

PATH = 'notes.txt'
book = {}
original_book = {}

def open_file():
    global book, original_book, PATH
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, note in enumerate(data, 1):
        note = note.strip().split(';')
        book[i] = note
    original_book = deepcopy(book)

def save_file():
    global book, PATH
    data = []
    for note in book.values():
        note = ';'.join(note)
        data.append(note)
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)

def add_note(new_note: list[str]):
    global book
    c_id = max(book) + 1
    book[c_id] = new_note


def find_note(word: str) -> dict[int, list[str]]:
    global book
    result = {}
    for c_id, note in book.items():
        for field in note:
            if word.lower() in field.lower():
                result[c_id] = note
                break
    return result

def edit_note(c_id: int, new_note: list[str]):
    global book
    current_note = book.get(c_id)
    note = []
    for i in range(len(new_note)):
        if new_note[i]:
            note.append(new_note[i])
        else:
            note.append(current_note[i])
    book[c_id] = note
    return note[0]

def delete_note(c_id: int) -> str:
    global book
    return book.pop(c_id)[0]



