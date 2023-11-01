import text
from datetime import datetime

def main_menu():
    """ Метод выводит в консоль меню и возможными операциями """
    for i, item in enumerate(text.menu):
        if i == 0:
            print(item)
        else:
            print(f'\t{i}. {item}')
    while True:
        choice = input(text.input_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.menu):
            return int(choice)
        else:
            print(text.input_menu_error)


def print_message(msg: str):
    """ Метод выводит в консоль сообщение """
    print(msg)
    

def show_notes(book: dict[int, list[str]], msg:str):
    """ Метод выводит в консоль данные по всем заметкам """
    if book:
        print('\n' + '= ' * 67)
        for i, note in book.items():
            print(f'{i:>3}. {note[2]:<20} {note[0]:<20} {note[1]:<20}')
        print('= ' * 67 + '\n')
    else:
        print_message(msg)

def show_notes_id(book: dict[int, list[str]], msg:str):
    """ Метод выводит в консоль данные по всем заметкам """
    if book:
        print('\n' + '= ' * 67)
        for i, note in book.items():
            print(f'{i:>3}. {note[0]:<20} {note[1]:<20}')
        print('= ' * 67 + '\n')
    else:
        print_message(msg)


def input_note(msg: str) -> list[str]:
    """ Метод содержит заготовок заметки и ее текст """
    note = []
    today = datetime.today()
    for input_text in msg:
        note.append(input(input_text))
    note.append(today.strftime("%d.%m.%y-%H:%M"))
    return note

def input_request(msg: str) -> str:
    """ Метод принимает из консоли искомое слово """
    return input(msg)

